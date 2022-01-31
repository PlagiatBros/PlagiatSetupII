from mentat import Module

class MicroTonality(Module):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.autotunes = ['AutotuneNano', 'AutotuneNanoUp', 'AutotuneNanoDown', 'AutotuneKesch', 'AutotuneKeschUp', 'AutotuneKeschDown']
        self.zynsynth = 'ZHiSynths'
        self.calfpitcher = 'Pitcher'

    def enable(self):

        modules = self.engine.modules

        for zyn in self.zynsynths:
            modules[zyn].set('microtonality', True)


    def disable(self):

        modules = self.engine.modules

        self.set_tuning(*[0.0 for i in range(12)])

        modules[self.zynsynth].set('microtonality', False)


    def set_tuning(self, *tuning):
        """
        *tuning: 12 semi-tones tuning between -1 and 1
        """

        modules = self.engine.modules

        # zyn
        zyntuning = tuning[10:] + tuning[:10] # zyn commence au Si bémol
        modules[self.zynsynth].set('tuning', "\n".join([str(100.0 + i * 100 + zyntuning[i] * 100) for i in range(12)]).replace('1200.0', '2/1'))

        # calf
        modules[self.calfpitcher].set('tuning', tuning)

        # autotuner
        for at in self.autotunes:
            modules[at].set('tuning', tuning)
