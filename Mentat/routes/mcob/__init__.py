from ..global_route import GlobalRoute
from .audio import Audio
from .video import Video
from .light import Light

from modules import *

class Mcob(Light, Video, Audio, GlobalRoute):

    def __init__(self):

        super().__init__(name='Mcob')


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
        transport.set_tempo(120)
        transport.set_cycle(8)

        # Setups, banks...
        seq192.set_screenset(self.name)
        prodSampler.set_kit(self.name)

        # Microtonality
        microtonality.enable()
        microtonality.set_tuning(0, 0, 0, 0, 0, 0.35, 0, 0, 0.35, 0, 0.35, 0)

        # Controllers
        mk2Control.set_lights({
            1:'blue',
            2:'purple',
            3:'purple',
            4:'purple',
            5:'purple',
            6:'yellow',
            7:'yellow',
            8:'yellow',
        })

    def route(self, protocol, port, address, args):
        """
        Call parent class method first
        so that the order of routing is
        GlobalRoute -> MCOB
        """
        super().route(protocol, port, address, args)

        if address == '/pedalboard/button':

            if args[0] == 1:
                self.part("stop")
            if args[0] == 2:
                self.part("intro")
            if args[0] == 3:
                self.part("couplet1-1")
            if args[0] == 4:
                self.part("couplet1-2", modifier=True)

        if address == '/mk2/button':

            if args[0] == 2:
                self.part("refrain")
            if args[0] == 3:
                self.part("couplet1-3")


            if args[0] == 5:
                self.part("look", modifier=True)
