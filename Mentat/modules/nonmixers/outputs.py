from ..nonmixer import NonMixer

class Outputs(NonMixer):

    def create_meta_parameters(self):
        """
        Link cut/pitch/filter from between Samples / Synths and LeadSamples / LeadSynths
        """
        self.submodules['Samples'].add_event_callback('parameter_changed', self.linkleads)
        self.submodules['Synths'].add_event_callback('parameter_changed', self.linkleads)


    def linkleads(self, module, name, value):
        if module.name in ['Pitchshifter', 'Lowpass', 'Aux-A', 'Aux-B']:
            self.submodules['Lead' + module.parent_module.name].set(module.name, name, value)
        elif name == 'Mute':
            self.submodules['Lead' + module.name].set('Mute', value)


    def get_state(self, *args, **kwargs):
        """
        Exclude some plugins/params from saved states to avoid remote mix save from breaking things
        """
        state = []
        for s in super().get_state():
            if s[1] in ['Pitchshifter', 'Lowpass', 'Aux-A', 'Aux-B', 'Level'] or 'dsp/bypass' in s:
                continue

            p = self.get_parameter(*s[:-1])
            if hasattr(p, 'is_alias'):
                continue

            state.append(s)

        return state

    def load_fx_state(self, state_name, fx_name):
        if state_name in self.states:
            state = [s for s in self.states[state_name] if s[0] == fx_name]
            self.set_state(state)
