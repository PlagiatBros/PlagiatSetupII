from mentat import Module
import fnmatch


class PostProcess(Module):
    """
    Post processing effects managers for main mix outputs (bass, synths, samples, vocals)
    """


    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)


    def set_pitch(self, strip_name, pitch):
        """
        Set pitch shifting parameter for one or multiple strips.
        For vocals this is handled at the autotuner's level, for the others with AM Pitchshifter

        **Parameters**

        - `strip_name`: name of strip (with unix filename pattern matching support)
        - `pitch`: pitch multiplier (0.5 = -1 octave, 2 = +1 octave)
        """

        self.no_AMpitch = ['VocalsNano', 'VocalsKesch']
        mod = self.engine.modules['Outputs']
        for n in fnmatch.filter(mod.submodules.keys(), strip_name):
            if n not in self.no_AMpitch:
                mod.set(n, 'Pitchshifter', 'Pitch', pitch)
            else:
                pre = n[6:]
                for name in [pre+'Meuf', pre+'Normo', pre+'Gars']:
                    self.engine.modules[name].set('Pitch', pitch)

    def animate_pitch(self, strip_name, start, end, duration, mode='beats', easing='linear'):
        """
        Animate pitch shifting for one or multiple strips

        **Parameters**

        - `strip_name`: name of strip (with unix filename pattern matching support)
        - `start`: pitch multiplier start value (0.5 = -1 octave, 2 = +1 octave)
        - `end`: pitch multiplier end value (0.5 = -1 octave, 2 = +1 octave)
        - `duration`: animation duration
        - `mode`: beats or seconds
        - `easing`: interpolation curve (see mentat's documentation)
        """
        self.no_AMpitch = ['VocalsNano', 'VocalsKesch']
        mod = self.engine.modules['Outputs']
        for n in fnmatch.filter(mod.submodules.keys(), strip_name):
            if n not in self.no_AMpitch:
                mod.animate(n, 'Pitchshifter', 'Pitch', start, end, duration, mode, easing)
            else:
                pre = n[6:]
                for name in [pre+'Meuf', pre+'Normo', pre+'Gars']:
                    self.engine.modules[name].animate(n, 'Pitch', start, end, duration, mode, easing)


    def set_filter(self, strip_name, freq):
        """
        Set lowpass filter cutoff parameter for one or multiple strips

        **Parameters**

        - `strip_name`: name of strip (with unix filename pattern matching support)
        - `freq`: cutoff frequency in Hz
        """
        mod = self.engine.modules['Outputs']
        for n in fnmatch.filter(mod.submodules.keys(), strip_name):
            mod.set(n, 'Lowpass', 'Cutoff', freq)

    def animate_filter(self, strip_name, start, end, duration, mode='beats', easing='linear'):
        """
        Animate lowpass filter cutoff for one or multiple strips

        **Parameters**

        - `strip_name`: name of strip (with unix filename pattern matching support)
        - `start`: cutoff frequency start value in Hz
        - `end`: cutoff frequency end value in Hz
        - `duration`: animation duration
        - `mode`: beats or seconds
        - `easing`: interpolation curve (see mentat's documentation)
        """
        mod = self.engine.modules['Outputs']
        for n in fnmatch.filter(mod.submodules.keys(), strip_name):
            mod.animate(n, 'Lowpass', 'Cutoff', start, end, duration, mode, easing)


    def slice(self):
        pass

    def animate_slice(self):
        pass
