from ..base import RouteBase, mk2_button, pedalboard_button
from .video import Video
from .light import Light

from modules import *

class ViktorHuguau(Video, Light, RouteBase):
    """
    Viktor Huguau En France Afrique
    """

    def activate(self):
        """
        Called when the engine switches to this route.
        """

        super().activate()

        transport.set_tempo(75)
        transport.set_cycle('4/4')
        transport.set_pattern('xxxx')

        # Setups, banks...
        seq192.set_screenset(self.name)
        prodSampler.set_kit(self.name)

        # Microtonality
        microtonality.disable()


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

        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('meuf_exclu', 'on')

        # Keyboard
        jmjKeyboard.set_sound('ZDupieux')

        # Bass
        bassFX.set('basscape','on')

    @mk2_button(2)
    def stopsampmles(self):
        """
        STOP BLAST 'N' SAX
        """
        self.pause_loopers()
        self.reset()

        # Samples
        prodSampler.send('/tap192/stop', 's:Plagiat/ViktorHuguau/blast')
        prodSampler.send('/tap192/stop', 's:Plagiat/ViktorHuguau/Sax')

    @mk2_button(3)
    def blast(self):
        """
        BLAST
        """
        self.pause_loopers()
        self.reset()

        # Samples
        samples.set('Samples1', 'Gain', 'Mute', 0.0)
        prodSampler.send('/tap192/play', 's:Plagiat/ViktorHuguau/blast')

    @mk2_button(4)
    def sax(self):
        """
        SAX
        """
        self.pause_loopers()
        self.reset()

        # Samples
        samples.set('Samples1', 'Gain', 'Mute', 0.0)
        prodSampler.send('/tap192/play', 's:Plagiat/ViktorHuguau/Sax')
