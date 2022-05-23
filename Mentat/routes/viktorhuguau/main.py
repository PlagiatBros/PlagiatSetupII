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
        transport.set_cycle('2/4', 'xx')

        # Setups, banks...
        seq192.set_screenset(self.name)
        prodSampler.set_kit(self.name)

        # Microtonality
        microtonality.disable()

        # Autotuner Notes
        #    ]@           c     d     e  f     g     a     b
        notes.set_notes(1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1)


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
        seq192.select('solo', 'dummy')

        # Transport
        transport.start()

        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('meuf_exclu', 'on')

        # Keyboard
        jmjKeyboard.set_sound('ZDupieux', boost=True)

        # Bass
        bassFX.set('scape','on')

    @mk2_button(2, 'blue')
    def stopsampmles(self):
        """
        STOP BLAST 'N' SAX
        """

        # Samples
        prodSampler.send('/instrument/stop', 's:Plagiat/ViktorHuguau/blast')
        prodSampler.send('/instrument/stop', 's:Plagiat/ViktorHuguau/Sax')

    @mk2_button(3, 'purple')
    def blast(self):
        """
        BLAST
        """

        # Samples
        samples.set('Samples1', 'Mute', 0.0)
        prodSampler.send('/instrument/play', 's:Plagiat/ViktorHuguau/blast')

    @mk2_button(4, 'purple')
    def sax(self):
        """
        SAX
        """

        # Samples
        samples.set('Samples1', 'Mute', 0.0)
        prodSampler.send('/instrument/play', 's:Plagiat/ViktorHuguau/Sax')
