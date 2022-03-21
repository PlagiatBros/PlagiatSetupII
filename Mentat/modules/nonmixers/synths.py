from ..nonmixer import NonMixer

class Synths(NonMixer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        pre_add = 'Non-Mixer.Synths/strip/'
        self.add_parameter('scape_bpm', pre_add + 'BassScape/C%2A%20Scape%20-%20Stereo%20delay%20with%20chromatic%20resonances/bpm', 'f', default=120.0)
