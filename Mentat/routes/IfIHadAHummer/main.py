
from ..base import RouteBase, mk2_button, pedalboard_button
from .video import Video
from .light import Light

from modules import *

class IfIHadAHummer(Video, Light, RouteBase):

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
        microtonality.enable()
        microtonality.set_tuning(0, 0.35, 0, -0.35, 0, 0.35, 0, 0, 0, 0, 0.35, 0)

        # Autotuner Notes
        #               c     d     e  f     g     a     b
        notes.set_notes(0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1)


    @pedalboard_button(1)
    @mk2_button(1, 'blue')
    def stop(self):
        """
        STOP
        """
        self.pause_loopers()
        transport.stop()
