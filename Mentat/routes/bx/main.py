from ..base import *
from .video import Video
from .light import Light

from modules import *

class BX(Video, Light, RouteBase):
    """
    BX Millesime aka Lamborghini Vroom Vroom II
    """

    def activate(self):
        """
        Called when the engine switches to this route.
        """

        super().activate()

        transport.set_tempo(120)
        transport.set_cycle('4/4')

        # Setups, banks...
        seq192.set_screenset(self.name)
        prodSampler.set_kit(self.name)

        # Microtonality
        microtonality.disable()
        # microtonality.enable()
        # microtonality.set_tuning(0.35, 0, 0, 0, 0, 0.35, 0, 0, 0.35, 0, 0, 0)

        # Autotuner Notes
        notes.set_notes(1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1)

        # Mk2
        mk2Control.set_mode('cut_samples', 'cut_synths')

    @pedalboard_button(1)
    @mk2_button(1, 'blue')
    def stop(self):
        """
        STOP
        """
        self.pause_loopers()
        transport.stop()


    @pedalboard_button(2)
    def intro(self):
        """
        INTRO
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'intro_*')

        # Transport
        transport.start()

        # Samples
        # samples.set('Samples2', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('meuf_exclu', 'on')
        vocalsKesch.set('meuf_exclu', 'on')

        # Keyboard
        jmjKeyboard.set_sound('ZTrumpets', boost=True)

        synthsFX2Delay.set('Trap', 'Gain', -14.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)


    @pedalboard_button(2)
    def couplet(self):
        """
        COUPLET
        """
        pass

    @pedalboard_button(2)
    def refrain(self):
        """
        REFRAIN
        """
        pass
