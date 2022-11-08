from ..base import RouteBase, mk2_button, pedalboard_button
from .video import Video
from .light import Light

from modules import *

class ClashDesCoaches(Video, Light, RouteBase):

    klick_pattern = 'Xxxx'

    def activate(self):
        """
        Called when the engine switches to this route.
        """

        super().activate()

        transport.set_tempo(110)
        transport.set_cycle('4/4', pattern=self.klick_pattern)

        # Setups, banks...
        seq192.set_screenset(self.name)
        prodSampler.set_kit(self.name)

        # Microtonality
        microtonality.enable()
        microtonality.set_tuning(0, 0, 0, 0, 0, 0.35, 0, 0, 0.35, 0, 0.35, 0)

        # Autotuner Notes
        #               c     d     e  f     g     a     b
        notes.set_notes(1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0)

        # Mk2
        mk2Control.set_mode('wobble')

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

        # Transport
        transport.start()

        # Sequencer
        seq192.select('solo', 'Sape_*')

        # Samples
        samples.set('Samples1', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')

        # jmjKeyboard
        jmjKeyboard.set_sound('Z8bits')

        # Bass
        bassfx.set('zynwah', 'on')

    @pedalboard_button(3)
    def key(self):
        """
        Bouclage Clavier
        """
        seq192.select('on', 'SapeUp_ZHi_Trumpets')

        # Samples
        samples.set('Samples1', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')

        # jmjKeyboard
        jmjKeyboard.set_sound('Z8bits')

        # Bass
        bassfx.set('zynwah', 'on')
