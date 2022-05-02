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
            },
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
                    seq192.select('solo', 'couplet1-2_*'),

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
                    seq192.select('solo', 'couplet1-2_*'),

                    # Vocals
                    vocalsKeschFX2Delay.set('KeschMeuf', 'Gain', 'Gain', 0.0),

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

    @pedalboard_button(2) # A l'origine bouton 6
    def quintolet(self):
        """
        QUINTOLET
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'quintolet_*')

        # Transport
        transport.start()

        # Samples
        samples.set('Samples1', 'Gain', 'Mute', 0.0)
        samples.set('Samples2', 'Gain', 'Mute', 0.0)
        samplesFX6Scape.set('Samples1', 'Gain', 'Gain', -4.5)
        samplesFX6Scape.set('SamplesFX6Scape', 'Gain', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('meuf_exclu', 'on')
        vocalsNano.set('normo', 'on')
        vocalsNano.set('gars', 'on')
        vocalsKesch.set('meuf_exclu', 'on')
        vocalsKeschFX2Delay.set('KeschMeuf', 'Gain', 'Gain', 0.0)
        vocalsKeschFX2Delay.set('VocalsKeschFX2Delay', 'Gain', 'Mute', 0.0)

        # Bass
        bassFX.set('distohi', 'on')

    @pedalboard_button(3) # A l'origine bouton 7
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

        # Samples
        samples.set('Samples1', 'Gain', 'Mute', 0.0)
        samples.set('Samples2', 'Gain', 'Mute', 0.0)
        samplesFX6Scape.set('Samples1', 'Gain', 'Gain', -4.5)
        samplesFX6Scape.set('SamplesFX6Scape', 'Gain', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('meuf_exclu', 'on')
        vocalsNanoFX2Delay.set('NanoMeuf', 'Gain', 'Gain', 0.0)
        vocalsNanoFX2Delay.set('VocalsNanoFX2Delay', 'Gain', 'Mute', 0.0)
        vocalsNanoFX4Disint.set('NanoMeuf', 'Gain', 'Gain', 0.0)
        vocalsNanoFX4Disint.set('vocalsNanoFX4Disint', 'Gain', 'Mute', 0.0)

        vocalsKesch.set('meuf_exclu', 'on')
        vocalsKeschFX2Delay.set('KeschMeuf', 'Gain', 'Gain', 0.0)
        vocalsKeschFX2Delay.set('VocalsKeschFX2Delay', 'Gain', 'Mute', 0.0)
        vocalsKeschFX4Disint.set('KeschMeuf', 'Gain', 'Gain', 0.0)
        vocalsKeschFX4Disint.set('vocalsKeschFX4Disint', 'Gain', 'Mute', 0.0)

        # Bass
        bassFX.set('distohi', 'on')

    @pedalboard_button(4) # A l'origine bouton 8
    def couplet2(self):
        """
        COUPLET 2
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'couplet2-1_*')

        # Transport
        transport.start()

        # Samples
        samples.set('Samples1', 'Gain', 'Mute', 0.0)
        samples.set('Samples2', 'Gain', 'Mute', 0.0)
        samplesFX6Scape.set('Samples1', 'Gain', 'Gain', -4.5)
        samplesFX7Degrade.set('SamplesFX7Degrade', 'Gain', 'Mute', 0.0),
        samplesFX6Scape.set('SamplesDegrade', 'Gain', 'Gain', -18.0),
        samplesFX6Scape.set('SamplesFX6Scape', 'Gain', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('meuf_exclu', 'on')
        vocalsKesch.set('meuf_exclu', 'on')

        # Sequences (Mentat)
        self.start_sequence('couplet2', [
            {}, # bar 1
            { # bar 2
                4 + 1/2.: lambda: [
                    seq192.select('solo', 'couplet2*'),
                    vocalsNano.set('gars_exclu', 'on')
                    ]
            }
        ], loop=False)

    @pedalboard_button(5) # à l'origine bouton 9
    def drumnbass(self):
        """
        DRUM 'N' BASS
        """
        #### TODO vérifier s'il faut self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'dnb_*')

        # Transport
        transport.start()

        # Samples
        samples.set('Samples1', 'Gain', 'Mute', 0.0)
        samples.set('Samples2', 'Gain', 'Mute', 0.0)
        samplesFX6Scape.set('Samples1', 'Gain', 'Gain', -4.5)
        samplesFX7Degrade.set('SamplesFX7Degrade', 'Gain', 'Mute', 0.0),
        samplesFX6Scape.set('SamplesDegrade', 'Gain', 'Gain', -18.0),
        samplesFX6Scape.set('SamplesFX6Scape', 'Gain', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('meuf_exclu', 'on')
        vocalsNanoFX2Delay.set('NanoMeuf', 'Gain', 'Gain', 0.0)
        vocalsNanoFX4Disint.set('NanoMeuf', 'Gain', 'Gain', 0.0)
        vocalsKesch.set('meuf_exclu', 'on')

    @mk2_button(3, 'purple')
    def vanhalen(self):
        """
        VAN HALEN BRIDGE
        """
        self.pause_loopers()
        self.reset()

        # Transport
        transport.stop()

        # keyboards
        jmjKeyboard.set_sound('ZTrumpets')

    @pedalboard_button(6)
    def lambotrap(self):
        """
        LAMBO TRAP
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'lambo_*')

        # Transport
        transport.start()

        # Samples
        samples.set('Samples1', 'Gain', 'Mute', 0.0)
        samples.set('Samples2', 'Gain', 'Mute', 0.0)
        samplesFX6Scape.set('Samples1', 'Gain', 'Gain', -6.0)
        samplesFX6Scape.set('SamplesFX6Scape', 'Gain', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')

        # keyboards
        jmjKeyboard.set_sound('LowCTrap1')

    @mk2_button(4, 'purple')
    def lambotrapout(self):
        """
        LAMBO TRAP OUT
        """

        # Sequences
        seq192.select('on', 'lambout')

    @pedalboard_button(5)
    def drumnbass2(self):
        """
        DRUM 'N' BASS 2 (cf. DRUM 'N' BASS)
        """
        pass

    @mk2_button(5, 'purple')
    def gettheshit(self):
        """
        GET THE SHIT GOING
        """
        self.pause_loopers()
        self.reset()

        # Transport
        transport.stop()

        # Samples
        samples.set('Samples1', 'Gain', 'Mute', 0.0)
        samples.set('Samples2', 'Gain', 'Mute', 0.0)
        samplesFX6Scape.set('Samples1', 'Gain', 'Gain', -4.5)
        samplesFX7Degrade.set('SamplesFX7Degrade', 'Gain', 'Mute', 0.0),
        samplesFX6Scape.set('SamplesDegrade', 'Gain', 'Gain', -18.0),
        samplesFX6Scape.set('SamplesFX6Scape', 'Gain', 'Mute', 0.0)


    @pedalboard_button(3)
    def refrain2(self):
        """
        REFRAIN 2 (cf. REFRAIN)
        """
        pass
