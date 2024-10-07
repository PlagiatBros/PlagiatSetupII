from mentat import Module

class FluidSynth(Module):


    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)


    def set_portamento(self, time, mono=False):
        """
        Set synth's portamento time
        See page 25 @ https://raw.githubusercontent.com/FluidSynth/fluidsynth/master/doc/polymono/FluidPolyMono-0004.pdf

        **Parameters**

        - `time`: time in ms between 0 and 16383
        """
        time = max(0, min(time, 16383))
        if time > 0:
            # enable portamento mode
            self.send('/control_change', 0, 65, 127)
            # set portamento time
            self.send('/control_change', 0, 5, time >> 7) # MSB
            self.send('/control_change', 0, 37, time & 127) # LSB
            # set legato mode
            self.send('/control_change', 0, 68, 127 if mono else 0)

        else:
            # disable portamento mode
            self.send('/control_change', 0, 65, 0)
            # disable legato mode
            self.send('/control_change', 0, 68, 0)
