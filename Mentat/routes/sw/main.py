from ..base import *
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
        microtonality.enable()
        microtonality.set_tuning(0.35, 0, 0, 0, 0, 0.35, 0, 0, 0.35, 0, 0, 0)

        # Autotuner Notes
        autotunes = ['NanoMeuf', 'NanoNormo', 'NanoGars', 'KeschMeuf', 'KeschNormo', 'KeschGars']
        notes.set_notes(1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1)

        # Mk2
        mk2Control.set_mode('cut_samples', 'cut_synths')

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
        transport.set_cycle('4/4', 'Xxxx')
        transport.start()

        # Samples
        samples.set('Samples2', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('meuf_exclu', 'on')
        vocalsKesch.set('meuf_exclu', 'on')

        # Keyboard
        jmjKeyboard.set_sound('ZTrumpets', boost=True)



    @mk2_button(2, 'purple')
    def couplet1(self):
        """
        COUPLET 1
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'intro_*')

        # Transport
        transport.set_cycle('4/4', 'XxXx')
        transport.start()

        # Samples
        samples.set('Samples2', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('meuf_exclu', 'on')
        vocalsKesch.set('meuf_exclu', 'on')

        # Keyboard
        jmjKeyboard.set_sound('ZNotSoRhodes')

        # Séquences (Mentat)
        self.start_sequence('couplet1', [
            {}, # bar 1
            { # bar 2
                4 + 1/2. : lambda: samples.set('Samples2', 'Mute', 1.0)
            },
            { # bar 3 ("Once")
                1 : lambda: [
                    # Sequences
                    seq192.select('solo', 'couplet1-1_*'),

                    # Transport
                    transport.set_cycle('4/4', 'Xxxx'),

                    # Samples
                    samples.set('Samples2', 'Mute', 0.0),
                    samples.set('Samples3', 'Mute', 0.0),
                    samplesFX7Degrade.set('Samples2', 'Gain', -3.0),
                    samplesFX7Degrade.set('SamplesFX7Degrade', 'Mute', 0.0),
                    samplesFX6Scape.set('SamplesFX7Degrade', 'Gain', -18.0),
                    samplesFX6Scape.set('SamplesFX6Scape', 'Mute', 0.0),
                    samplesFX3Reverb.set('Samples3', 'Gain', -15.0),
                    samplesFX3Reverb.set('SamplesFX3Reverb', 'Mute', 0.0)


                ]
            },
            {},{},{},{}, # bars 2 - 5
            { # bar 6 ("Moroness")
                4.5: lambda: vocalsKeschFX2Delay.set('active', 'on')
            },
            { # bar 7 Pont
                1: lambda: seq192.select('solo', 'couplet1-2_*'),
                3: lambda: vocalsKeschFX2Delay.set('pre', 'off'),
            },
            {}, # bar 8
            { # bar 9 ("Two two two two")
                1: lambda: seq192.select('on', 'couplet1-1_*')
            },
            {},{},{},{},{},{},{},{},{},{}, # bar 10 - 19
            { # bar 20 ("Alone")
                4.5: lambda: vocalsKeschFX2Delay.set('active', 'on')
            },
            { # bar 21 Pont
                1: lambda: [
                    # Sequences
                    seq192.select('solo', 'couplet1-2_*'),

                    # Samples
                    samplesFX7Degrade.set('Samples2', 'Gain', -70.0),
                    prodSampler.send('/instrument/play', 's:Plagiat/SW/BregoLong', 100)
                ],
                3: lambda: vocalsKeschFX2Delay.set('pre', 'off'),
                4: lambda: vocalsKesch.set('normo_exclu', 'on')
            },
            {}, # bar 22
            { # bar 23 ("Despite")
                1: lambda: seq192.select('solo', 'couplet1*')
            }

        ], loop=False)

    @pedalboard_button(3) # A l'origine bouton 6
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
        samples.set('Samples1', 'Mute', 0.0)
        samples.set('Samples2', 'Mute', 0.0)
        samplesFX7Degrade.set('Samples2', 'Gain', -3.0)
        samplesFX7Degrade.set('SamplesFX7Degrade', 'Mute', 0.0)
        samplesFX6Scape.set('Samples1', 'Gain', -4.5)
        samplesFX6Scape.set('SamplesFX7Degrade', 'Gain', 0.0)
        samplesFX6Scape.set('SamplesFX6Scape', 'Mute', 0.0)


        # Vocals
        vocalsNano.set('meuf_exclu', 'on')
        vocalsNano.set('normo', 'on')
        vocalsNano.set('gars', 'on')
        vocalsKesch.set('meuf_exclu', 'on')
        #vocalsKeschFX2Delay.set('KeschMeuf', 'Gain', 0.0)
        vocalsKeschFX2Delay.set('VocalsKeschFX2Delay', 'Mute', 0.0)

        # Bass
        bassFX.set('distohi', 'on')

        # Keyboards
        jmjKeyboard.set_sound('LowZDancestep')

    @pedalboard_button(4) # A l'origine bouton 7
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
        samples.set('Samples1', 'Mute', 0.0)
        samples.set('Samples4', 'Mute', 0.0)
        samplesFX6Scape.set('Samples1', 'Gain', -4.5)
        samplesFX6Scape.set('SamplesFX6Scape', 'Mute', 0.0)
        samplesFX2Delay.set('Samples4', 'Gain', -4.5)
        samplesFX2Delay.set('SamplesFX2Delay', 'Mute', 0.0)

        # Keyboards
        synthsFX2Delay.set('ZDiploLikeWide', 'Gain', -6.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)


        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        #vocalsNano.set('gars', 'on')
        #vocalsNano.set('normo', 'on')
        vocalsNanoFX2Delay.set('active', 'on')
        vocalsNanoFX4Disint.set('active', 'on')

        vocalsKesch.set('normo_exclu', 'on')
        #vocalsKesch.set('gars', 'on')
        #vocalsKesch.set('normo', 'on')
        vocalsKeschFX2Delay.set('active', 'on')
        vocalsKeschFX4Disint.set('active', 'on')

        # Bass
        bassFX.set('distohi', 'on')

    @pedalboard_button(5) # A l'origine bouton 8
    def couplet2(self):
        """
        COUPLET 2
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'dummy')

        # Transport
        transport.start()

        # Samples
        samples.set('Samples1', 'Mute', 0.0)
        samples.set('Samples2', 'Mute', 0.0)
        samples.set('Samples3', 'Mute', 0.0)
        samplesFX6Scape.set('Samples1', 'Gain', -4.5)
        samplesFX7Degrade.set('Samples2', 'Gain', -3.0)
        samplesFX7Degrade.set('SamplesFX7Degrade', 'Mute', 0.0)
        samplesFX6Scape.set('SamplesFX7Degrade', 'Gain', -18.0)
        samplesFX6Scape.set('SamplesFX6Scape', 'Mute', 0.0)
        samplesFX3Reverb.set('Samples3', 'Gain', -15.0)
        samplesFX3Reverb.set('SamplesFX3Reverb', 'Mute', 0.0)

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

    @pedalboard_button(6) # à l'origine bouton 9
    def drumnbass(self):
        """
        DRUM 'N' BASS
        """
        #### TODO vérifier s'il faut self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'drumnbass_*')

        # Transport
        transport.start()

        # Samples
        samples.set('Samples2', 'Mute', 0.0)
        samplesFX7Degrade.set('Samples2', 'Gain', -3.0),
        samplesFX7Degrade.set('SamplesFX7Degrade', 'Mute', 0.0),
        samplesFX6Scape.set('SamplesFX7Degrade', 'Gain', -18.0),
        samplesFX6Scape.set('SamplesFX6Scape', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('meuf_exclu', 'on')
        #vocalsNanoFX2Delay.set('NanoMeuf', 'Gain', 0.0)
        vocalsNanoFX4Disint.set('NanoMeuf', 'Gain', 0.0)
        vocalsKesch.set('meuf_exclu', 'on')

        # Keyboards
        jmjKeyboard.set_sound('ZTrumpets', boost=True)

    @gui_button()
    def salsabass(self):
        """
        SALSA BASS
        """
        seq192.select('on', 'couplet1-3_cLowTrap*')

    @gui_button()
    def salsahigh(self):
        """
        SALSA High
        """
        seq192.select('on', 'couplet1-3_*')
        seq192.select('on', 'couplet1-2_*')


    @pedalboard_button(7)
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
        samples.set('Samples1', 'Mute', 0.0)
        samples.set('Samples2', 'Mute', 0.0)
        samplesFX2Delay.set('Samples1', 'Gain', -9.0)
        samplesFX2Delay.set('SamplesFX2Delay', 'Mute', 0.0)
        samplesFX6Scape.set('Samples1', 'Gain', -6.0)
        samplesFX6Scape.set('SamplesFX6Scape', 'Mute', 0.0)

        # Synths
        synthsFX1Reverb.set('EasyClassical', 'Gain', -12.0)
        synthsFX1Reverb.set('SynthsFX1Reverb', 'Mute', 0.0)
        synthsFX2Delay.set('EasyClassical', 'Gain', -9.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)
        synths.set('EasyClassical', 'Pan', -0.5)
        synths.set('Trap', 'Pan', 0.5)

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')

        # keyboards
        jmjKeyboard.set_sound('LowCTrap1')

    @mk2_button(3, 'purple')
    def lambotrapout(self):
        """
        LAMBO TRAP OUT
        """

        # Sequences
        seq192.select('on', 'lambout')

    @mk2_button(4, 'blue')
    def vanhalen(self):
        """
        VAN HALEN BRIDGE
        """
        self.pause_loopers()
        self.reset()

        # Transport
        transport.start()
        seq192.select('solo', 'dummy')

        # keyboards
        jmjKeyboard.set_sound('ZTrumpets', boost=True)


    @pedalboard_button(8)
    def drumnbass2(self):
        """
        DRUM 'N' BASS 2 (cf. DRUM 'N' BASS)
        """
        self.drumnbass()
        seq192.select('on', 'drumnbassTOTAL*')

    @mk2_button(5, 'purple')
    def gettheshit(self):
        """
        GET THE SHIT GOING
        """
        self.pause_loopers()
        self.reset()

        # Transport
        transport.start()

        # Sequence
        seq192.select('solo', 'dummy')

        # Samples
        samples.set('Samples1', 'Mute', 0.0)
        samples.set('Samples2', 'Mute', 0.0)
        samplesFX6Scape.set('Samples1', 'Gain', -4.5)
        samplesFX7Degrade.set('SamplesFX7Degrade', 'Mute', 0.0),
        samplesFX6Scape.set('SamplesFX7Degrade', 'Gain', -18.0),
        samplesFX6Scape.set('SamplesFX6Scape', 'Mute', 0.0)

        # Vocals
        vocalsKeschFX2Delay.set('active', 'on')
        vocalsNanoFX2Delay.set('active', 'on')

    @pedalboard_button(4)
    def refrain2(self):
        """
        REFRAIN 2 (cf. REFRAIN)
        """
        pass
