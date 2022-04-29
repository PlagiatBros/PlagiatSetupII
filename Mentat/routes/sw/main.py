from ..base import RouteBase, mk2_button, pedalboard_button
from .video import Video
from .light import Light

from modules import *

class SW(Video, Light, RouteBase):
    """
    SW
    """

    def activate(self):
        """
        Called when the engine switches to this route.
        """

        super().activate()

        transport.set_tempo(178.5)
        transport.set_cycle('4/4')

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

        # Sequences
        seq192.select('solo', 'intro_*')

        # Transport
        transport.start()

        # Samples
        samples.set('Samples2', 'Gain', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('meuf_exclu', 'on')
        vocalsKesch.set('meuf_exclu', 'on')

        # Keyboard
        jmjKeyboard.set_sound('ZNotSoRhodes')

    @mk2_button(2)
    def couplet1(self):
        """
        COUPLET 1
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'intro_*')

        # Transport
        transport.set_pattern('XxXx')
        transport.start()

        # Samples
        samples.set('Samples2', 'Gain', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('meuf_exclu', 'on')
        vocalsKesch.set('meuf_exclu', 'on')

        # Keyboard
        jmjKeyboard.set_sound('ZNotSoRhodes')

        # Séquences (Mentat)
        self.start_sequence('couplet1', [
            {}, # bar 1
            { # bar 2
                4 + 1/2. : lambda: samples.set('Samples2', 'Gain', 'Mute', 1.0)
            }
            { # bar 3 ("Once")
                1 : lambda: [
                    # Sequences
                    seq192.set('solo', 'couplet1-1_*'),

                    # Transport
                    transport.set_pattern('Xxxx'),

                    # Samples
                    samples.set('Samples2', 'Gain', 'Mute', 0.0),
                    samplesFX7Degrade.set('Samples2', 'Gain', 'Gain', -3.0),
                    samplesFX7Degrade.set('SamplesFX7Degrade', 'Gain', 'Mute', 0.0),
                    samplesFX6Scape.set('SamplesDegrade', 'Gain', 'Gain', -18.0),
                    samplesFX6Scape.set('SamplesFX6Scape', 'Gain', 'Mute', 0.0),

                    # Vocals
                    vocalsKeschFX2Delay.set('VocalsKeschFX2Delay', 'Gain', 'Mute', 0.0),
                ]
            },
            {},{},{},{},{}, # bars 2 - 6
            { # bar 7 ("Moroness")
                1: lambda: [
                    # Sequences
                    seq192.select('solo', 'couplet1-2_*')

                    # Vocals
                    vocalsKeschFX2Delay.set('KeschMeuf', 'Gain', 'Gain', 0.0)
                ],
                3: lambda: vocalsKeschFX2Delay.set('KeschMeuf', 'Gain', 'Gain', -70.0),
            },
            {}, # bar 8
            { # bar 9 ("Two two two two")
                1: lambda: seq192.select('on', 'couplet1-1_*')
            },
            {},{},{},{},{},{},{},{},{},{},{}, # bars 10 - 20
        { # bar 21 ("Alone")
                1: lambda: [
                    # Sequences
                    seq192.select('solo', 'couplet1-2_*')

                    # Vocals
                    vocalsKeschFX2Delay.set('KeschMeuf', 'Gain', 'Gain', 0.0)

                    # Samples
                    tap192.send('/tap192/play', 's:Plagiat/SW/BregoLong')
                ],
                3: lambda: vocalsKeschFX2Delay.set('KeschMeuf', 'Gain', 'Gain', -70.0),
                4: lambda: vocalsKesch.set('normo_exclu', 'on')
            },
            {}, # bar 22
            { # bar 23 ("Despite")
                1: lambda: seq192.select('solo', 'couplet1*')
            }

        ], loop=False)
