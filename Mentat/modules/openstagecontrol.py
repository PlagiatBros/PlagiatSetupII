from mentat import Module

class OpenStageControl(Module):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.add_event_callback('parameter_changed', self.parameter_changed)

        self.osc_state = {}

    def parameter_changed(self, module, name, value):

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

    def send_state(self):

        super().send_state()

        # send custom state
        for address in self.osc_state:
            for name in self.osc_state[address]:
                self.send(address, name, *self.osc_state[address][name])

    def route(self, address, args):

        # send OSC controls to modules
        # /module_name param_name value
        module_path = address.split('/')
        module_name = module_path[1]
        if module_name in self.engine.modules:
            self.engine.modules[module_name].set(*module_path[2:], name, *args)
            return False
