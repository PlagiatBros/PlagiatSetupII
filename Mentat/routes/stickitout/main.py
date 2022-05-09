from ..base import RouteBase, mk2_button, pedalboard_button
from .video import Video
from .light import Light

from modules import *

class StickItOut(Video, Light, RouteBase):

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
        autotunes = ['NanoMeuf', 'NanoNormo', 'NanoGars', 'KeschMeuf', 'KeschNormo', 'KeschGars']
        for at in autotunes:
            #            c     d     e  f     g     a     b
            at.set_notes(0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1)


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
        INTRO (BASSE)
        """
        self.pause_loopers()
        self.reset()

        # Transport
        transport.start()

        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('meuf_exclu', 'on')

    @pedalboard_button(3)
    def couplet1(self):
        """
        COUPLET 1 (HERE WE GO)
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'couplet1-1_*')

        # Transport
        transport.start()



        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('meuf_exclu', 'on')

        # Synths
        synthsFX2Delay.set('Rhodes', 'Gain', 'Gain', -9.0)
        synthsFX2Delay.set('EasyClassical', 'Gain', 'Gain', -9.0)
        synthsFX2Delay.set('TrapFifth', 'Gain', 'Gain', -9.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Gain', 'Mute', 0.0)

        self.start_sequence('couplet1-1', [
            *[{} for i in range(12)], # bars 1 - 12
            { # bar 13
                1: lambda: [
                    vocalsKesch.set('normo_exclu', 'on'),
                    seq192.select('solo', 'allo_zLow_ragstep')
                    ]
            },
            { # bar 14
                2: lambda: seq192.select('on', 'allo_cHi_trapfifth')
            },
            { # bar 15
                1: lambda: seq192.select('off', 'allo_zLow_ragstep'),
                2: lambda: seq192.select('off', 'allo_cHi_trapfifth'),
                3 + 3/4. : lambda: seq192.select('on', 'couplet1-2_cHi_dubstephorn')
            },
            {
                # bar 16
                1: lambda: seq192.select('solo', 'couplet1-2_*')

            }


        ], loop=False)

    @pedalboard_button(4)
    def refrain(self):
        """
        REFRAIN
        """
        self.pause_loopers()
        self.reset()


        # Sequences
        seq192.select('solo', 'refrain_*')

        # Transport
        transport.start()


        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('meuf_exclu', 'on')

        # Synths
        synthsFX2Delay.set('Rhodes', 'Gain', 'Gain', -9.0)
        synthsFX2Delay.set('EasyClassical', 'Gain', 'Gain', -9.0)
        synthsFX2Delay.set('TrapFifth', 'Gain', 'Gain', -9.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Gain', 'Mute', 0.0)
