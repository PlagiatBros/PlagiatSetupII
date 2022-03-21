from ..global_route import GlobalRoute
from .audio import Audio
from .video import Video
from .light import Light

from modules import *

class Snapshat(Light, Video, Audio, GlobalRoute):

    def __init__(self):

        super().__init__(name='Snapshat')


    def part(self, *args, **kwargs):
        """
        Custom method to handle the different parts in the track
        in a semantic way
        """
        Audio.part(self, *args, **kwargs)
        Video.part(self, *args, **kwargs)
        Light.part(self, *args, **kwargs)

    def activate(self):
        """
        Called when the engine switches to this route.
        """

        seq192.set_screenset(self.name)
        prodSampler.set_kit(self.name)

    def route(self, protocol, port, address, args):
        """
        Call parent class method first
        so that the order of routing is
        GlobalRoute -> Snapshat
        """
        super().route(protocol, port, address, args)

        if address =='/pedalboard/button':
            if args[0] == 1:
                self.engine.modules['Transport'].stop()
            if args[0] == 2:
                self.part("pont")
            if args[0] == 3:
                self.part("couplet")
            if args[0] == 4:
                self.part("refrain")
