from mentat import Module
from .nonmixer import NonMixer

import os
import json
import urllib.parse
from inspect import getmembers, getdoc

from .plugins import osc_plugin

class OpenStageControl(Module):
    """
    Open Stage Control touch interface.
    """

    osc_version = '1.27.6'

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.session_dir = os.path.dirname(__file__) + '/../../OpenStageControl'

        self.osc_state = {}

        self.plugin_modals = {}

        self.add_parameter('active_non_mixer', None, types='s', default='')

        self.add_parameter('signature', '/signature', types='s', default='4/4')
        self.add_parameter('tempo', '/tempo', types='f', default=120)
        self.add_parameter('cursor', '/cursor', types='f', default=0)
        self.add_parameter('routes', '/routes', types='s', default='Loading')
        self.add_parameter('active_route', '/active_route', types='s', default='')
        self.add_parameter('active_route_name', '/active_route_name', types='s', default='')
        self.add_parameter('route_methods', '/route_methods', types='s', default='')
        self.add_parameter('miniroute_methods', '/miniroute_methods', types='s', default='')
        self.add_parameter('rolling', '/rolling', types='i', default=0)

        self.engine.add_event_callback('parameter_changed', self.parameter_changed)
        self.engine.add_event_callback('client_started', self.client_started)
        self.engine.add_event_callback('started', lambda: self.set('routes', ','.join(self.engine.routes.keys())) )
        self.engine.add_event_callback('route_changed', self.engine_route_changed)
        self.engine.add_event_callback('nonmixer_ready', lambda name: self.start_scene('populate_gui', self.populate_gui))


        self.start_scene('cycle_watch', self.cycle_watch)

    def cycle_watch(self):
        """
        Watch time to display global metric / cycle position
        """
        self.wait(0.04)
        engine = self.engine
        transport = self.engine.modules['Transport']
        while True:

            cursor = 0.0
            if self.get('rolling'):
                cycle_duration = 1000000000 * engine.cycle_length * 60 / engine.tempo
                cursor = ((engine.current_time - engine.cycle_start_time) % cycle_duration) / cycle_duration

            self.set('cursor', cursor)

            self.wait(0.04)

    def parameter_changed(self, module, name, value):
        """
        Whenever a parameter changes, send it to the interface:
            /module_name/submodule_name parameter_name *value

        and store that state locally.
        """
        # send state changes to OSC
        # /module_name param_name value
        address = '/' + '/'.join(module.module_path)

        if module == self.engine:
            address = '/Mentat'
        else:
            address = '/' + '/'.join(module.module_path[1:])

        if type(value) is not list:
            value = [value]

        self.send(address, name, *value)

        # store custom state
        if address not in self.osc_state:
            self.osc_state[address] = {}
        self.osc_state[address][name] = value

    def engine_route_changed(self, route):

        self.set('active_route', route.name)
        methods = [x for n,x in getmembers(route) if callable(x) and (hasattr(x, 'mk2_buttons') or hasattr(x, 'pedalboard_buttons') or hasattr(x, 'gui_button'))]
        methods = sorted(methods, key=lambda m: m.index)

        data = []
        subroute_data = []
        for m in methods:
            if route.name in m.__qualname__:
                if hasattr(m, 'gui_button'):
                    subroute_data.append({
                        'type': 'button',
                        'mode': 'momentary',
                        'method': m.__name__,
                        'label': getdoc(m).split('\n')[0] if getdoc(m) else m.__name__,
                        **m.gui_data
                    })
                else:
                    btns = ''
                    if hasattr(m, 'mk2_buttons'):
                        btns += ''.join(['<div class="mk2">%s</div>' % x for x in m.mk2_buttons])
                    if hasattr(m, 'pedalboard_buttons'):
                        btns += ''.join(['<div class="pb">%s</div>' % x for x in m.pedalboard_buttons])

                    data.append({
                        'method': m.__name__,
                        'label': getdoc(m).split('\n')[0] if getdoc(m) else m.__name__,
                        'html': '%s' % btns
                    })


        self.set('route_methods', json.dumps(data))
        self.set('miniroute_methods', json.dumps(subroute_data))


    def client_started(self, name):

        self.send_state()


    def send_state(self):
        """
        Send local state (because it's not part of this module's actual state)
        """

        super().send_state()

        # send custom state
        for address in self.osc_state:
            for name in self.osc_state[address]:
                self.send(address, name, *self.osc_state[address][name])

    def resolve_path(self, path):
        """
        Resolve module path (see route())
        """
        module_name = path[0]

        if module_name == 'Mentat':
            return self.engine
        elif module_name in self.engine.modules:
            mod = self.engine.modules[module_name]
            for n in path[1:]:
                if n in mod.submodules:
                    mod = mod.submodules[n]
            return mod
        return None

    def route(self, address, args):
        """
        Allow controlling any module parameter from the interface using the same syntax:
            /module_name/submodule_name parameter_name *value
        or calling a module method:
            /module_name/submodule_name/call method_name *args
        """

        if address == '/keyboard':
            self.engine.modules['OpenStageControlKeyboardOut'].send(*args)
            return False

        # send OSC controls to modules
        # /module_name param_name value
        module_path = address.split('/')[1:]
        module_name = module_path[0]

        call = False
        if module_path[-1] == 'call':
            module_path = module_path[:-1]
            call = True

        mod = self.resolve_path(module_path)

        if mod is not None:

            if call:
                if len(args) > 0 and type(args[0] == str) and hasattr(mod, args[0]):
                    method = getattr(mod, args[0])
                    if callable(method):
                        method(*args[1:])
            else:

                if type(args[0]) == str:
                    mod.set(*args)

            return False


    def populate_gui(self):
        """
        Generates a gui for:
            - non mixers instances
            - ray session
        """
        if not self.engine.restarted:

            self.wait(2, 's')


            """
            Non mixer gui
            """
            panel = {'id': 'non-mixer-gui-tabs', 'type': 'panel', 'default': 6, 'tabs': [], 'verticalTabs': True, 'bypass': True, 'onValue': 'var name = getProp(this, "variables").names[value]; if (name) send("/OpenStageControl/call", "set_active_non_mixer", name)'}
            tab_names = []
            for name, mod in self.engine.modules.items():
                if isinstance(mod, NonMixer):
                    tab = {
                        'type': 'tab',
                        'id': name,
                        'label': name,
                        'layout': 'horizontal',
                        'innerPadding': False,
                        'widgets': [],
                        'padding': 1,
                        'contain': False
                    }
                    tab_names.append(name)
                    panel['tabs'].append(tab)
                    for sname, smod in mod.submodules.items():
                        id = '%s/%s' % (name, sname)
                        strip = {
                            'id': id,
                            'type': 'panel',
                            'layout': 'vertical',
                            'width': 120,
                            'widgets': [],
                            'innerPadding': True,
                            'lineWidth': 0,
                            'css': 'class: strip;',
                            'html': '<div class="label center">%s</div>' % urllib.parse.unquote(sname),
                            'scroll': False
                        }
                        tab['widgets'].append(strip)
                        plugins = {
                            'type': 'panel',
                            'layout': 'vertical',
                            'height': 120,
                            'widgets': [],
                            'innerPadding': True,
                            'padding': 4,
                            'css': 'class: carved;',
                            'scroll': True,
                            'contain': False
                        }
                        strip['widgets'].append(plugins)

                        for plugname, plugmod in smod.submodules.items():
                            oscplug = osc_plugin(plugmod)
                            plugins['widgets'].append(oscplug.modal)
                            self.plugin_modals[oscplug.id] = oscplug

                        strip['widgets'].append({
                            'type': 'button',
                            'label': 'Mute',
                            'colorWidget': 'var(--yellow)',
                            'css': 'class: discrete;',
                            'value': smod.get('Mute'),
                            'address': '/%s/%s' % (name, sname),
                            'preArgs': 'Mute'
                        })

                        strip['widgets'].append({
                            'type': 'panel',
                            'height': 50,
                            'layout': 'horizontal',
                            'innerPadding': False,
                            'padding': 10,
                            'widgets': [
                                {
                                    'type': 'knob',
                                    'range': {'min': -1, 'max': 1},
                                    'design': 'solid',
                                    'horizontal': True,
                                    'origin': 0,
                                    'css': 'class: locked;' if not 'Pan' in smod.parameters else '',
                                    'doubleTap': True,
                                    'value': smod.get('Pan') if 'Pan' in smod.parameters else 0,
                                    'address': '/%s/%s' % (name, sname),
                                    'preArgs': 'Pan',
                                    'linkId': '/%s/%s/Pan' % (name, sname),
                                    'sensitivity': 0.25
                                },
                                {
                                    'type': 'input',
                                    'css': ('class: locked;' if not 'Pan' in smod.parameters else '') + ';\nmargin: 7rem 0 8rem!important',
                                    'width': 120,
                                    'decimals': 2,
                                    'linkId': '/%s/%s/Pan' % (name, sname),
                                    'bypass': True
                                }
                            ]
                        })

                        strip['widgets'].append({
                            'type': 'panel',
                            'expand': True,
                            'scroll': False,
                            'widgets': [
                                {
                                    'type': 'fader',
                                    'range': {'min': -70, '6%': -60, '12%': -50, '20%': -40, '30%': -30, '42%': -20, '60%': -10, '80%': 0, 'max': 6 },
                                    'width': '100%',
                                    'height': '100%',
                                    'doubleTap': True,
                                    'pips': True,
                                    'design': 'round',
                                    'value': smod.get('Gain'),
                                    'default': smod.get('Gain'),
                                    'address': '/%s/%s' % (name, sname),
                                    'linkId': '/%s/%s/Gain' % (name, sname),
                                    'preArgs': 'Gain'
                                },
                                {
                                    'type': 'fader',
                                    'css': 'class: meter',
                                    'range': {'min': -70, '6%': -60, '12%': -50, '20%': -40, '30%': -30, '42%': -20, '60%': -10, '80%': 0, 'max': 6 },
                                    'interaction': False,
                                    'pips': False,
                                    'design': 'compact',
                                    'dashed': [2,2],
                                    'default': -70,
                                    'address': '/%s/%s' % (name, sname),
                                    'preArgs': 'Level'
                                }
                            ]
                        })
                        strip['widgets'].append({
                            'type': 'input',
                            'width': 120,
                            'decimals': 5,
                            'linkId': '/%s/%s/Gain' % (name, sname),
                            'bypass': True
                        })

            panel['variables'] = {'names': tab_names}
            frag = {
                'type': 'fragment',
                'version': self.osc_version,
                'content': panel
            }
            file = open(self.session_dir + '/non-mixers.json', 'w+')
            data = json.dumps(frag)
            if data != file.read():
                file.write(data)
            file.close()

        """
        Ray session gui
        """

        ray = self.engine.modules['RaySession']
        panel = {'type': 'panel', 'widgets': [], 'layout': 'vertical', 'padding': 1, 'innerPadding': False, 'contain': False, 'id': 'raysession_status_panel'}
        for p in ray.parameters:
            if 'status_' in p:
                name = p[7:]
                strip = {'type': 'panel', 'layout': 'horizontal', 'css': 'class: strip;', 'height': 50, 'padding': 4,'widgets' : [
                    {
                        'type': 'button',
                        'label': '^play',
                        'mode': 'momentary',
                        'colorWidget': 'var(--green)',
                        'css': '#{@{status_%s} ? \'class: on;\': \'\'}' % name,
                        'address': '/RaySession/call',
                        'preArgs': ['send', '/ray/client/start', name]
                    },
                    {
                        'type': 'variable',
                        'id': 'status_%s' % name,
                        'address': '/RaySession',
                        'preArgs': ['status_%s' % name]
                    },
                    {
                        'type': 'button',
                        'label': '^stop',
                        'mode': 'momentary',
                        'colorWidget': 'var(--red)',
                        'address': '/RaySession/call',
                        'preArgs': ['send', '/ray/client/stop', name]
                    },
                    {
                        'type': 'button',
                        'label': '^save',
                        'mode': 'momentary',
                        'colorWidget': 'var(--blue-green)',
                        'address': '/RaySession/call',
                        'preArgs': ['send', '/ray/client/save', name]
                    },
                    {
                        'type': 'button',
                        'label': '^eye',
                        'mode': 'momentary',
                        'colorWidget': 'white',
                        'address': '/RaySession/call',
                        'preArgs': ['send', '/ray/client/show_optional_gui', name]
                    },
                    {
                        'type': 'text',
                        'align': 'left',
                        'address': '/RaySession',
                        'preArgs': 'label_%s' % name,
                        'expand': True
                    }
                ]}
                panel['widgets'].append(strip)


        if not self.engine.restarted:
            frag = {
                'type': 'fragment',
                'version': self.osc_version,
                'content': panel
            }
            file = open(self.session_dir + '/ray-session.json', 'w+')
            data = json.dumps(frag)
            if data != file.read():
                file.write(data)
            file.close()

        """
        Misc
        """

        self.wait(2, 's')
        self.send_state()

    def edit_gui(self, widget, data):
        """
        Send data to interface, split it into small chunks that udp can handle.
        """
        blob = json.dumps(data)

        self.send('/EDIT_QUEUE/START', widget)
        size = 1024 * 16
        i = 0

        while True:
            bits = blob[i:i+size]
            self.send('/EDIT_QUEUE/APPEND', widget, bits)
            if i >= len(blob):
                break
            i += size

        self.send('/EDIT_QUEUE/END', widget)


    def transport_start(self):
        """
        Start transport and trigger rolling loops
        """
        self.engine.modules['Transport'].trigger()

    def transport_stop(self):
        """
        Stop transport and loops
        """
        self.engine.modules['Transport'].stop()
        self.engine.active_route.pause_loopers()

    def route_method(self, name, *args):
        """
        Call method in active route that's linked to a pedalboard or mk2 button
        """
        if hasattr(self.engine.active_route, name):
            m = getattr(self.engine.active_route, name)
            if callable(m):
                if hasattr(m, 'mk2_buttons'):
                    self.engine.active_route.route('osc', None, '/mk2/button', list(m.mk2_buttons.keys())[:1])
                elif hasattr(m, 'pedalboard_buttons'):
                    self.engine.active_route.route('osc', None, '/pedalBoard/button', list(m.pedalboard_buttons.keys())[:1])
                elif hasattr(m, 'gui_button'):
                    m(*args)

    def set_active_non_mixer(self, name):
        """
        Switch on-demand non-mixer meter levels
        """
        prev_name = self.get('active_non_mixer')
        if prev_name != '' and prev_name in self.engine.modules:
            self.engine.modules[prev_name].disable_meters()

        if name != '' and name in self.engine.modules:
            self.engine.modules[name].enable_meters()

        self.set('active_non_mixer', name)


    def display_modal(self, id, state):
        if id in self.plugin_modals:
            if state == 1:
                self.send('/EDIT/MERGE', id, json.dumps({'widgets': self.plugin_modals[id].widgets}), '{"noWarning": true}')
                self.start_scene('plugmodal',lambda: [
			self.wait(0.1,'s'),
			self.send_state()
		])
                # self.plugin_modals[id].plugin.enable_feedback()
            else:
                # self.plugin_modals[id].plugin.disable_feedback()
                pass
