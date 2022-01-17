from mentat import Module

class Strip(Module):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

class NonMixer(Module):

    def __init__(self, *args, **kwargs):

        Module.__init__(self, *args, **kwargs)

        self.signals = {}

        # get submodules
        self.send('/non/hello', self.engine.osc_server.get_url(), '', '', self.engine.name)
        self.send('/signal/list')

        self.create_meta_parameters()


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
                        parameter_address = '/' + '/'.join(path[1:-1])
                        self.submodules[strip_name].add_parameter(parameter_name, parameter_address, 'f', default=args[5])
            else:

                # only 1 arg: list end
                self.logger.info('strip list retreived')

            return False


    def create_meta_parameters(self):

        if name == 'VocalsKesch':

            pass
