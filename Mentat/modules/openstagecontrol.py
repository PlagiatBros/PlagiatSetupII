from mentat import Module

class OpenStageControl(Module):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.add_event_callback('parameter_changed', self.parameter_changed)

    def parameter_changed(self, module_path, name, values):

        # send state changes to OSC
        # /module_name param_name value
        address = '/' + '/'.join(module_path)
        self.send(address, name, *values)

    def route(self, address, args):

        # send OSC controls to modules
        # /module_name param_name value
        module_path = address.split('/')
        module_name = module_path[1]
        if module_name in self.engine.modules:
            self.engine.modules[module_name].set(*module_path[2:], name, *args)
            return False
