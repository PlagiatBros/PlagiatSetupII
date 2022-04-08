from mentat import Module
from .nonmixer import NonMixer

import json
import urllib.parse

class OpenStageControl(Module):
    """
    Open Stage Control touch interface.
    """

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.add_event_callback('parameter_changed', self.parameter_changed)
        self.add_event_callback('client_restarted', self.client_restarted)

        self.start_scene('populate_gui', self.populate_gui)

        self.osc_state = {}

    def parameter_changed(self, module, name, value):
        """
        Whenever a parameter changes, send it to the interface:
            /submodule_name/module_name parameter_name *value

        and store that state locally.
        """

        # send state changes to OSC
        # /module_name param_name value
        address = '/' + '/'.join(module.module_path)
        if type(value) is not list:
            value = [value]

        self.send(address, name, *value)

        # store custom state
        if address not in self.osc_state:
            self.osc_state[address] = {}
        self.osc_state[address][name] = value

    def client_restarted(self, name):
        if name == self.name:
            self.start_scene('populate_gui', self.populate_gui)


    def send_state(self):
        """
        Send local state (because it's not part of this module's actual state)
        """

        super().send_state()

        # send custom state
        for address in self.osc_state:
            for name in self.osc_state[address]:
                self.send(address, name, *self.osc_state[address][name])

    def route(self, address, args):
        """
        Allow controlling any module from the interface using the same syntax:
            /submodule_name/module_name parameter_name *value
        """

        # send OSC controls to modules
        # /module_name param_name value
        module_path = address.split('/')
        module_name = module_path[1]

        if module_name in self.engine.modules:
            self.engine.modules[module_name].set(*module_path[2:], *args)
            return False


    def populate_gui(self):
        """
        Here be dragons.

        Generates a gui for all non mixers instance.

        Maybe this could be extended to all modules.
        Maybe this is overkill.
        """

        self.wait(2, 's') # wait until everyone is here (bad, should rely on events)

        panel = {'tabs': []}

        for name, mod in self.engine.modules.items():
            if isinstance(mod, NonMixer):
                tab = {
                    'type': 'tab',
                    'label': name,
                    'layout': 'horizontal',
                    'innerPadding': False,
                    'widgets': [],
                    'contain': False
                }
                panel['tabs'].append(tab)
                for sname, smod in mod.submodules.items():
                    strip = {
                        'type': 'panel',
                        'layout': 'vertical',
                        'width': 120,
                        'widgets': [],
                        'innerPadding': False,
                        'lineWidth': 0
                    }
                    tab['widgets'].append(strip)
                    strip['widgets'].append({
                        'type': 'text',
                        'value':  urllib.parse.unquote(sname)
                    })
                    plugs = {}
                    for plugname, plugmod in smod.submodules.items():
                        if plugname != 'Gain':
                            if plugname not in plugs:
                                modal = {
                                    'type': 'modal',
                                    'label': urllib.parse.unquote(plugname),
                                    'layout': 'vertical',
                                    'height': 30,
                                    'widgets': []
                                }
                                plugs[plugname] = modal
                                strip['widgets'].append(modal)

                            for pname in plugmod.parameters:

                                param = plugmod.parameters[pname]
                                modal['widgets'].append({
                                    'type': 'panel',
                                    'layout': 'horizontal',
                                    'innerPadding': False,
                                    'lineWidth': 0,
                                    'height': 80,
                                    'widgets': [
                                        {
                                            'type': 'text',
                                            'value': urllib.parse.unquote(pname),
                                            'width': 120,
                                            'wrap': True
                                        },
                                        {
                                            'type': 'fader',
                                            'horizontal': True,
                                            'pips': True,
                                            'range': {'min': {'%.1f' % param.range[0]: param.range[0]}, 'max': {'%.1f' % param.range[1]: param.range[1]}},
                                            'value': param.args[0],
                                            'linkId': param.address,
                                            'address': '/%s/%s/%s/%s' % (name, sname, plugname, pname),
                                            'expand': True
                                        },
                                        {
                                            'type': 'input',
                                            'width': 120,
                                            'address': '/%s/%s/%s/%s' % (name, sname, plugname, pname),
                                            'linkId': param.address
                                        }
                                    ]
                                })

                    strip['widgets'].append({
                        'type': 'text',
                        'label': False,
                        'expand': True,
                    })
                    strip['widgets'].append({
                        'type': 'fader',
                        'range': {'min': -70, '6%': -60, '12%': -50, '20%': -40, '30%': -30, '42%': -20, '60%': -10, '80%': 0, 'max': 6 },
                        'height': '50%',
                        'default': 0,
                        'doubleTap': True,
                        'pips': True,
                        'value': smod.get('Gain', 'Gain'),
                        'address': '/%s/%s/Gain/Gain' % (name, sname)
                    })
                    strip['widgets'].append({
                        'type': 'button',
                        'label': 'Mute',
                        'value': smod.get('Gain', 'Mute'),
                        'address': '/%s/%s/Gain/Mute' % (name, sname)
                    })

        self.edit_gui('non-mixers', panel)

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
