from mentat import Module

NMPREFIX = 'Non-Mixer-XT.'

class Strip(Module):
    """
    NonMixer Strip
    """

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

class Plugin(Module):
    """
    NonMixer Plugin
    """
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.feedback_parameters = []

    def add_parameter(self, *args, direction='in', **kwargs):

        super().add_parameter(*args, **kwargs)

        p = self.parameters[args[0]]

        p.feedback_only = False
        if direction == 'out' and p not in self.feedback_parameters and p.name not in ['latency']:
            self.feedback_parameters.append(p)
            p.feedback_only = True

    def query_feedback(self):
        while True:
            self.wait(1/5, 'sec')
            for p in self.feedback_parameters:
                # print('query %s' % p.address)
                self.send(p.address)

    def enable_feedback(self, foh=False):
        self.start_scene('feedback_levels', self.query_feedback)

    def disable_feedback(self):
        self.stop_scene('feedback_levels')



class NonMixer(Module):
    """
    Base module for NonMixer instances.
    Retrieves all controllable parameters with their values automatically at init, structured as follows:
    NonMixer > Strips > Plugins > Parameters
    """

    def __init__(self, *args, **kwargs):

        Module.__init__(self, *args, **kwargs)

        self.init_params = []
        self.pending_params_labels = 0

        self.init_done = False

        self.pending_set_calls = []

        self.engine.add_event_callback('client_started', self.client_started)

    def client_started(self, name):

        if name == self.name:
            # self.send('/non/hello', 'osc.udp://127.0.0.1:%i' % self.engine.port, '', '', self.engine.name)

            if not self.init_done:
                self.send('/signal/list')

            if self.name == 'Outputs':
                self.enable_meters()

    def update_meters(self):
        while True:
            self.wait(1/30, 'sec')
            for strip in self.submodules:
                self.send(NMPREFIX + self.name + '/strip/'+strip+'/Meter/Level%20(dB)/unscaled')


    def enable_meters(self):
        self.start_scene('meter_levels', self.update_meters)

    def disable_meters(self):
        if self.name == 'Outputs':
            # never disable output meters
            return
        self.stop_scene('meter_levels')


    def set(self, *args, **kwargs):
        if not self.init_done:
            self.pending_set_calls.append((args, kwargs))
        else:
            super().set(*args, **kwargs)

    def route(self, address, args):
        """
        Populate submodules and parameters from non's response
        """
        # print(self.name, len(self.init_params))

        if address == '/reply' and args[0] == '/signal/list':

            if len(args) > 1:
                """
                Populating
                """
                path = args[1].split('/')

                if path[1] == 'strip':

                    strip_name = path[2]

                    if strip_name not in self.submodules:

                        self.add_submodule(Strip(strip_name, parent=self))


                    strip_mod = self.submodules[strip_name]

                    if path[-1] == 'unscaled':

                        parameter_name = '/'.join(path[3:-1])
                        parameter_address = ('%s%s' % (NMPREFIX, self.name)) + '/' + '/'.join(path[1:])

                        plugin_name, _, param_shortname = parameter_name.partition('/')

                        if plugin_name in NonMixer.plugin_aliases:
                            plugin_name = NonMixer.plugin_aliases[plugin_name]
                        if param_shortname in NonMixer.parameter_aliases:
                            param_shortname = NonMixer.parameter_aliases[param_shortname]

                        if plugin_name in ['Gain', 'Pan', 'Meter']:
                            # add gain / pan / level params directly to the strip module
                            strip_mod.add_parameter(param_shortname, parameter_address if plugin_name != 'Meter' else None, 'f', default=None)
                            strip_mod.parameters[param_shortname].range = args[3:5]

                        else:

                            if plugin_name not in strip_mod.submodules:
                                strip_mod.add_submodule(Plugin(plugin_name, parent=strip_mod))

                            plugin_mod = strip_mod.submodules[plugin_name]

                            plugin_mod.add_parameter(param_shortname, parameter_address, 'f', default=None, direction=args[2])
                            plugin_mod.parameters[param_shortname].range = args[3:5]

                            self.send('/signal/infos', parameter_address)
                            self.pending_params_labels += 1


                        self.init_params.append(parameter_address)


            else: # only 1 arg: list end
                """
                All received, query current values and create meta parameters
                """
                for parameter_address in self.init_params:
                    self.send(parameter_address)
                self.check_init_done()

        elif address == '/reply' and args[0] == '/signal/infos':
            # print(self.name, args)

            if len(args) > 2:
                path = args[1].split('/')
                parameter_name = '/'.join(path[3:-1])
                parameter_address = ('%s%s' % (NMPREFIX, self.name)) + '/' + '/'.join(path[1:])
                plugin_name, _, param_shortname = parameter_name.partition('/')
                if plugin_name in NonMixer.plugin_aliases:
                    plugin_name = NonMixer.plugin_aliases[plugin_name]
                strip_name = path[2]
                strip_mod = self.submodules[strip_name]

                plugin_mod = strip_mod.submodules[plugin_name]
                args[3] = args[3].replace(' ', '%20')
                if args[3] != param_shortname and '[' not in args[3] and args[3] not in plugin_mod.parameters:
                    if args[3] in NonMixer.parameter_aliases:
                        args[3] = NonMixer.parameter_aliases[args[3]]

                    plugin_mod.add_alias_parameter(args[3], param_shortname)
                    plugin_mod.parameters[args[3]].range = plugin_mod.parameters[param_shortname].range
                    plugin_mod.parameters[args[3]].feedback_only = plugin_mod.parameters[param_shortname].feedback_only

                self.pending_params_labels -= 1
                self.check_init_done()

        elif address == '/reply':
            path = args[0].partition('/strip/')[2]
            strip, _, pname = args[0].partition('/strip/')[2].partition('/')
            if 'unscaled' in pname:
                pname = pname[:-9]
            plugin_name, _, param_shortname = pname.partition('/')
            if plugin_name in NonMixer.plugin_aliases:
                plugin_name = NonMixer.plugin_aliases[plugin_name]
            if param_shortname in NonMixer.parameter_aliases:
                param_shortname = NonMixer.parameter_aliases[param_shortname]

            if args[0] in self.init_params:
                self.init_params.remove(args[0])
                self.check_init_done()


            if plugin_name in ['Pan', 'Gain', 'Meter']:
                self.set(strip, param_shortname, args[1])
            else:
                self.set(strip, plugin_name, param_shortname, args[1])

        return False

    def create_meta_parameters(self):
        """
        For specific instances we'll create meta parameters
        """


        for strip_name in self.submodules:
            if 'Delay' in strip_name:
                for plugin_name in self.submodules[strip_name].submodules:
                    plug = self.submodules[strip_name].submodules[plugin_name]
                    if plugin_name == 'GxMultiBandDelay':
                        plug.add_parameter('bpm', None, types='f', default=120)
                        plug.add_parameter('multiplier', None, types='f', default=1)
                        plug.add_mapping(['bpm', 'multiplier'], ['DELAY1', 'DELAY2', 'DELAY3', 'DELAY4', 'DELAY5'],
                            transform=lambda bpm, mult: [bpm * mult] * 5
                        )
                        plug.add_parameter('feedback', None, types='f', default=0.5)
                        plug.add_mapping('feedback', ['FEEDBACK1', 'FEEDBACK2', 'FEEDBACK3', 'FEEDBACK4', 'FEEDBACK5'],
                            transform=lambda feed: [feed * 100] * 5,
                            inverse=lambda f1, f2, f3, f4, f5: -1 if f1 != f2 or f2 != f3 or f3 != f4 or f4 != f5 else f1 / 100
                        )

    def check_init_done(self):

        if not self.init_done and self.pending_params_labels == 0 and not self.init_params:
            self.init_done = True

            pending_meta_set_calls = []
            for args, kwargs in self.pending_set_calls:
                if self.get_parameter(*args[:-1]) is not None:
                    self.set(*args, **kwargs)
                else:
                    pending_meta_set_calls.append([args, kwargs])
            self.create_meta_parameters()
            for args, kwargs in pending_meta_set_calls:
                self.set(*args, **kwargs)

            self.logger.info(' is ready')
            self.engine.dispatch_event('nonmixer_ready', self.name)


    plugin_aliases = {
        'C%2A%20Scape%20-%20Stereo%20delay%20with%20chromatic%20resonances': 'Scape',
        'Reverse%20Delay%20(5s%20max)': 'ReverseDelay',
        'Glame%20Lowpass%20Filter': 'Lowpass',
        'AM%20pitchshifter': 'Pitchshifter',
        'Mono%20Pan': 'Pan',
        'Aux%20(A)': 'Aux-A',
        'Aux%20(B)': 'Aux-B',
        'Aux%20(C)': 'Aux-C',
        'Aux%20(D)': 'Aux-D',
        'Amplifier%20(Mono)': 'Amp',
        'C%2A%20AutoFilter%20-%20Self-modulating%20resonant%20filter': 'AutoFilter'
    }

    parameter_aliases = {
        'Gain%20(dB)': 'Gain',
        'Level%20(dB)': 'Level',
        'Wet%20Level%20(dB)': 'Wet',

        'Cutoff%20Frequency': 'Cutoff',
        'Pitch%20shift': 'Pitch',
    }
