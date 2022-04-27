from ..base import RouteBase, mk2_button, pedalboard_button
from .video import Video
from .light import Light

from modules import *

class AgneauGastrik(Video, Light, RouteBase):

    def activate(self):
        """
        Called when the engine switches to this route.
        """

        super().activate()

        # Transport
        transport.set_tempo(150)
        transport.set_cycle('3/4', pattern="Xxx")

        # Setups, banks...
        seq192.set_screenset(self.name)
        prodSampler.set_kit(self.name)

        # Microtonality
        microtonality.enable()
        microtonality.set_tuning(0, 0, 0, 0, 0, 0.35, 0, 0, 0.35, 0, 0.35, 0)

    @pedalboard_button(1)
    @mk2_button(1, 'blue')
    def stop(self):
        """
        STOP
        """
        self.pause_loopers()
        transport.stop()

    @pedalboard_button(2) # bouton 5 à l'origine
    def ethiotrap(self):
        """
        EthioTrap
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'ethiotrap_*')

        # Transport
        transport.start()

        # Samples
        samples.set('Samples4', 'Gain', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')

        # Keyboards
        jmjKeyboard.set_sound('CTrap')
        #### TODO mk2Keyboard ?

    @pedalboard_button(3) # bouton 6 à l'origine
    def mandelaaa(self):
        """
        Mandela A A A
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'mandelaaa_*')

        # Transport
        transport.set_cycle('4/4', pattern="Xxxx")
        transport.start()

        # Samples
        samples.set('Samples4', 'Gain', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('meuf_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')

        # Keyboards
        jmjKeyboard.set_sound('LowCTrap1')

    @pedalboard_button(4) # bouton 7 à l'origine
    def couplet_m1(self):
        """
        Couplet M 1
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'couplet_m1_*')

        # Transport
        transport.set_cycle('3/4', pattern="Xxx")
        transport.start()

        # Samples
        samples.set('Samples4', 'Gain', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('meuf_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')

        # Keyboards
        jmjKeyboard.set_sound('CLowBoomTrapline')
