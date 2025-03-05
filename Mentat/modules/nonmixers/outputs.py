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
        return [s for s in super().get_state() if s[1] not in ['Pitchshifter', 'Lowpass', 'Aux-A', 'Aux-B', 'Level'] and 'dsp/bypass' not in s]
