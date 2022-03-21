from mentat import Module

class Strip(Module):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

class NonMixer(Module):

    def __init__(self, *args, **kwargs):

        Module.__init__(self, *args, **kwargs)

        self.signals = {}
        self.init_params = []

        # get submodules
        self.send('/non/hello', 'osc.udp://127.0.0.1:%i' % self.engine.port, '', '', self.engine.name)
        self.send('/signal/list')

    def route(self, address, args):

        if address == '/reply' and args[0] == '/signal/list':

            if len(args) > 1:

                path = args[1].split('/')

                if path[1] == 'strip':

                    strip_name = path[2]

                    if strip_name not in self.submodules:

                        self.add_submodule(Strip(strip_name, parent=self))

                    if path[-1] == 'unscaled':

                        parameter_name = '/'.join(path[3:-1])
                        parameter_address = ('Non-Mixer.%s' % self.name) + '/' + '/'.join(path[1:])
                        self.submodules[strip_name].add_parameter(parameter_name, parameter_address, 'f', default=None)
                        self.submodules[strip_name].parameters[parameter_name].range = args[3:5]
                        self.init_params.append(parameter_address)

            else:

                for parameter_address in self.init_params:
                    self.send(parameter_address)

                # only 1 arg: list end
                # self.logger.info('strip list retreived')
                self.create_meta_parameters()

        elif address == '/reply' and args[0] in self.init_params:
            path = args[0].partition('/strip/')[2]
            strip, _, pname = args[0].partition('/strip/')[2].partition('/')
            if 'unscaled' in pname:
                pname = pname[:-9]
            self.set(strip, pname, args[1])
            self.init_params.remove(args[0])
            # self.logger.info('init parameter %s %s to value %s ' % (strip, pname, args[1]))

        return False




    def create_meta_parameters(self):

        pass
