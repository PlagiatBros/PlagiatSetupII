from mentat import Module
import fnmatch


class PostProcess(Module):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)


    def pitch(self, strip_name, pitch):

        self.no_AMpitch = ['VocalsNano', 'VocalsKesch']
        mod = engine.modules['Outputs']
        for n in fnmatch.filter(mod.submodules.keys(), strip_name):
            if n not in no_AMpitch:
                mod.set(n, 'Pitchshifter', 'Pitch', pitch)
            else:
                pre = n[6:]
                for name in [pre+'Meuf', pre+'Normo', pre+'Gars']:
                    engine.modules[name].set('Pitch', pitch)

    def animate_pitch(self, strip_name, start, end, duration, mode='beats', easing='linear'):

        self.no_AMpitch = ['VocalsNano', 'VocalsKesch']
        mod = engine.modules['Outputs']
        for n in fnmatch.filter(mod.submodules.keys(), strip_name):
            if n not in no_AMpitch:
                mod.animate(n, 'Pitchshifter', 'Pitch', start, end, duration, mode, easing)
            else:
                pre = n[6:]
                for name in [pre+'Meuf', pre+'Normo', pre+'Gars']:
                    engine.modules[name].animate(n, 'Pitch', start, end, duration, mode, easing)


    def filter(self, strip_name, freq):

        mod = engine.modules['Outputs']
        for n in fnmatch.filter(mod.submodules.keys(), strip_name):
            mod.set(n, 'Lowpass', 'Cutoff', freq)

    def animate_filter(self, strip_name, start, end, duration, mode='beats', easing='linear'):

        mod = engine.modules['Outputs']
        for n in fnmatch.filter(mod.submodules.keys(), strip_name):
            mod.animate(n, 'Lowpass', 'Cutoff', start, end, duration, mode, easing)


    def slice(self):
        pass

    def animate_slice(self):
        pass
