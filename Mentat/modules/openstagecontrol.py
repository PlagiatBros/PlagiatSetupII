from mentat import Module

class OpenStageControl(Module):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.watch_module('zyntest', '*')

    def initialize(self, *args, **kwargs):

        super().initialize(*args, **kwargs)

        self.start_scene('init', self.delayed_init, *args, **kwargs)

    def delayed_init(self, *args, **kwargs):
        # re initialze because watched modules may have new parameters
        # defined during their init routine
        self.wait(1, 's')
        Module.initialize(self, *args, **kwargs)

    def watched_module_changed(self, module_path, name, args):

        # send state changes to OSC
        # /module_name param_name value
        address = '/' + '/'.join(module_path)
        self.send(address, name, *args)

    def route(self, address, args):

        # send OSC controls to modules
        # /module_name param_name value
        module_path = address.split('/')
        module_name = module_path[1]
        if module_name in self.engine.modules:
            self.engine.modules[module_name].set(*module_path[2:], name, *args)
            return False
