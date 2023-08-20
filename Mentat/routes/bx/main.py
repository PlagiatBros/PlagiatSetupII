from ..base import *
from .video import Video
from .light import Light

from modules import *

class BX(Video, Light, RouteBase):
    """
    BX Millesime aka Lamborghini Vroom Vroom II
    """

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
        # microtonality.disable()
        microtonality.enable()
        microtonality.set_tuning(0.35, 0, 0, 0, 0, 0.35, 0, 0, 0.35, 0, 0, 0)

        # Autotuner Notes
        notes.set_notes(1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1)

        # Mk2
        mk2Control.set_mode('cut_samples', 'cut_synths')

        # Sample
        self.set_samples_aliases({
            'GuitarCrunch': 'Samples1',
            'GuitarNatural': 'Samples2',
            'GuitarChorus': 'Samples3',
            'Trumpets': 'Samples4',
            'ZurnaTheme': 'Samples5',
            'ZurnaLongue': 'Samples3',
            'Sitar': 'Samples4'
        })

    def open_samples(self):
        samples.set('GuitarCrunch', 'Mute', 0.0)
        samples.set('GuitarNatural', 'Mute', 0.0)
        samples.set('GuitarChorus', 'Mute', 0.0)
        samples.set('Trumpets', 'Mute', 0.0)
        samplesFX3Reverb.set('Trumpets', 'Gain', -10.0)
        samplesFX3Reverb.set('SamplesFX3Reverb', 'Mute', 0.0)

    def open_samples_lickme(self):
        samples.set('Sitar', 'Mute', 0.0)
        samples.set('ZurnaLongue', 'Mute', 0.0)
        samples.set('ZurnaTheme', 'Mute', 0.0)


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
        self.open_samples()

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('meuf_exclu', 'on')

        # Keyboard
        jmjKeyboard.set_sound('ZTrumpets', boost=True)


        # Synths
        synths.set('Trap', 'Pan', -0.7)
        synths.set('ZStambul', 'Pan', 0.5)
        synths.set('EasyClassical', 'Pan', 0.3)

        synths.set('Trap', 'Amp', 'Gain', 0.35)

        synthsFX2Delay.set('Trap', 'Gain', -14.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)



    @pedalboard_button(3)
    def couplet(self):
        """
        COUPLET
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'couplet_*')
        seq192.select('off', 'couplet_*guitar*')
        # seq192.select('off', 'couplet_*cHi_easyClassical')


        # Transport
        transport.start()

        # Samples
        self.open_samples()

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
#        vocalsKesch.set('meuf_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')


        # Keyboard
        jmjKeyboard.set_sound('ZTrumpets', boost=True)

        # Synths
        synths.set('Trap', 'Pan', -0.7)
        synths.set('ZStambul', 'Pan', 0.5)
        synths.set('EasyClassical', 'Pan', 0.3)


        synths.set('Trap', 'Amp', 'Gain', 0.35)
        # synthsFX2Delay.set('Trap', 'Gain', -14.0)
        # synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)

        # self.start_sequence('couplet_1_p1', [
        #     {},
        #     {},
        #     {},
        #     {
        #         3.5: lambda: self.couplet_1_p2()
        #     }
        # ], loop=False)
        # Séquences

        # self.start_sequence('transitiondegenre', [
        # {}, # bar 1
        # {}, # bar 2
        # {}, # bar 3
        # {
        #     4.5: lambda: vocalsKesch.set('normo_exclu', 'on')
        # } # bar 4
        # ])



    @mk2_button(2)
    def couplet_keeping(self):
        # Séquence
        # seq192.select('off', 'couplet_*'),

        seq192.select('solo', 'triou*'),

        # transport
        transport.start()

        # Samples
        self.open_samples()
        samplesFX2Delay.set('ConstantSampler', 'Gain', -18.0)
        samplesFX2Delay.set('SamplesFX2Delay', 'Mute', 0.0)
        samplesFX3Reverb.set('GuitarCrunch', 'Gain', -42.0)
        samplesFX3Reverb.set('SamplesFX3Reverb', 'Mute', 0.0)
        samplesFX6Scape.set('GuitarCrunch', 'Gain', -26.67)
        samplesFX6Scape.set('SamplesFX6Scape', 'Mute', 0.0)
        prodSampler.send('/instrument/play', 's:Bx_Car')

        # Séquences
        self.start_scene('keeping', lambda: [
        #     seq192.select('on', 'couplet_*'),
        #     self.wait(1, 'b'),
        #     seq192.select('off', 'couplet_*'),
        #     self.wait(3, 'b'),
        #     transport.start(),
        #     seq192.select('on', 'couplet_*'),
        #     self.wait(1, 'b'),
        #     seq192.select('off', 'couplet_*'),
        #     self.wait(2, 'b'),
            self.wait(1,'b'),
            postprocess.animate_pitch('Synths', 1,0.2, 2.5, 'b'),
            self.wait(2.5, 'b'),
            postprocess.animate_pitch('Synths', None,1, .5, 'b'),
            self.wait(0.5, 'b'),
            self.wait(1,'b'),
            postprocess.animate_pitch('Synths', 1,0.2, 1.5, 'b'),
            self.wait(1.5, 'b'),
            postprocess.animate_pitch('Synths', None,1, .5, 'b'),
            self.wait(0.5, 'b'),
            constantSampler.send('/instrument/play', 's:TimboYeah'),
            # vocalsKesch.set('normo_exclu', 'on'),
            self.wait(1,'b'),
            self.couplet()
        ])

        # Vocals
        # vocalsKesch.set('normo_exclu', 'on')
        # vocalsKesch.set('gars', 'on')
        vocalsNano.set('normo_exclu', 'on')
        vocalsFeat.set('gars_exclu', 'on')


    # @mk2_button(3)
    # def couplet_1_p3(self):
    #     # Séquences
    #     seq192.select('on', 'couplet_*Hi*')

    @mk2_button(3)
    def stop_basses(self):
        """
        STOP BASSES
        """
        # Séquences
        seq192.select('off', 'couplet_*Low*')
        seq192.select('off', 'couplet_*samples*')


        # Séquences (Mentat)
        self.start_scene('bx_heeee', lambda: [
            self.wait(3.6, 'beat'),
            prodSampler.send('/instrument/play', 's:Bx_Heee'),
            self.wait(0.4, 'b'),
            # self.wait(3.4, 'beat'),
            self.pretrap()
        ])

        # Keyboards
        jmjKeyboard.set_sound('ZDupieux')

    # @mk2_button(3)
    def pretrap(self):
        """
        PRE-TRAP
        """
        # Séquences
        # seq192.select('solo', 'pretrap_cHi_trap')
        seq192.select('solo', 'pretrap_cLow_trap1')

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        # vocalsKesch.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        # self.start_scene('bestplace', lambda: [
        #     self.wait(16, 'beat'),
        #     seq192.select('on', 'pretrap_*')
        # ])

        # Keyboards
        # jmjKeyboard.set_sound('ZDupieux')

        synthsFX2Delay.set('Trap', 'Gain', -14.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)


    @mk2_button(4, 'purple')
    def trap(self):
        """
        TRAP
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'trap_*')

        # Transport
        transport.start()

        # Samples
        self.open_samples()

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')
        vocalsKesch.set('gars', 'on')
        self.start_sequence('sequence/bad_kiddybitch', [
            {
                1: lambda: vocalsFeat.set('normo_exclu', 'on')
            }, {},
            {
                1: lambda: [
                    vocalsFeat.set('normo_exclu', 'on'),
                    vocalsFeat.set('meuf', 'on')
                    ]
            }, {}
        ], loop=True)


        # Keyboard
        jmjKeyboard.set_sound('ZTrumpets', boost=True)

        synthsFX2Delay.set('Trap', 'Gain', -14.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)

        # Séquences
        self.start_sequence('sequence/trap', [
            {},
            {
                3: lambda: self.engine.animate('pitch_samples', 1, 0.6, 1.95, 'b', easing='cubic-in'),
                4.95: lambda: self.engine.animate('pitch_samples', None, 1, 0.05, 'b', easing='cubic-in')
            },
            {},
            {}
        ], loop=True)

    # @mk2_button(4)
    # def prerefrain(self):
    #     """
    #     PREREFRAIN
    #     """
    #     self.pause_loopers()
    #     self.reset()
    #
    #     # Sequences
    #     seq192.select('solo', 'prerefrain_*')
    #
    #     # Transport
    #     transport.start()
    #
    #     # Samples
    #     self.open_samples()
    #     samplesFX2Delay.set('GuitarCrunch', 'Gain', -18.0)
    #     samplesFX2Delay.set('SamplesFX2Delay', 'Mute', 0.0)
    #
    #     # Vocals
    #     vocalsNano.set('meuf_exclu', 'on')
    #     vocalsKesch.set('normo_exclu', 'on')
    #
    #     # Keyboard
    #     jmjKeyboard.set_sound('ZTrumpets', boost=False)
    #
    #     synths.set('TrapFifth', 'Amp', 'Gain', 0.35)
    #     synths.set('TrapFifth', 'Pan', -0.33)
    #     synths.set('ZTrumpets', 'Pan', 0.33)
    #
    #     synthsFX2Delay.set('TrapFifth', 'Gain', -18.0)
    #     synthsFX2Delay.set('ZTrumpets', 'Gain', -18.0)
    #     synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)
    #
    #     self.engine.animate('filter_synths', 20, 22000, 64, 'b', 'exponential')
    #     # self.engine.animate('GuitarCrunch', None, -, 64, 'b', 'exponential')

    @pedalboard_button(5)
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
        self.open_samples()
        samplesFX2Delay.set('GuitarCrunch', 'Gain', -18.0)
        samplesFX2Delay.set('SamplesFX2Delay', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('meuf_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        # Keyboard
        jmjKeyboard.set_sound('ZTrumpets', boost=False)

        synths.set('TrapFifth', 'Amp', 'Gain', 0.35)
        synths.set('TrapFifth', 'Pan', -0.33)
        synths.set('ZTrumpets', 'Pan', 0.33)

        synthsFX2Delay.set('TrapFifth', 'Gain', -18.0)
        synthsFX2Delay.set('ZTrumpets', 'Gain', -18.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)

        self.engine.animate('filter_synths', 20, 22000, 64, 'b', 'exponential')

        # Sequences
        self.start_scene('sequence/refrain_p2', lambda: [
            self.wait(32, 'beat'),
            vocalsKesch.set('meuf', 'on')
        ])
        # self.engine.animate('GuitarCrunch', None, -, 64, 'b', 'exponential')

    @pedalboard_button(6)
    def theme(self):
        """
        THEME
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'theme_*')
        # seq192.select('on', 'intro_*')

        # Transport
        transport.start()

        # Samples
        self.open_samples()

        # Bass
        bassFX.set('distohi', 'on')
        bassFX.set('degrade', 'on')

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')
        vocalsFeat.set('meuf', 'on')

        # Keyboard
        jmjKeyboard.set_sound('ZTrumpets', boost=True)

        # Synths
        synthsFX2Delay.set('Trap', 'Gain', -14.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)

        # Bass
        bassfx.set('scape', 'poston')
        bassfx.set('wobble', 'poston')
        bassfx.set('wobble_subdivision', 6)

        # Séquences
        self.start_sequence('sequence/bx_theme_hiSynths', [
        { # bar 1
            1: lambda: [
                synthsFX2Delay.set('EasyClassical', 'Gain', -70.0),
                synthsFX2Delay.set('TrapFifth', 'Gain', -70.0),
                bassFX.reset('BassDegrade', 'MDA%20Degrade', 'rate'),
                bassFX.set('BassScapeIn', 'Mute', 1.0),
                bassFX.set('BassWobbleIn', 'Mute', 1.0),
                ],
            4: lambda: self.engine.animate('pitch_synths', 1, 0.8, 0.95, 'b', easing='cubic-in')
        },
        {
            1: lambda: self.engine.set('pitch_synths', 1)
        },# bars 2
        {  # bars 3
            4.5: lambda: [
                bassFX.set('BassScapeIn', 'Mute', 0.0),
                bassFX.set('BassWobbleIn', 'Mute', 0.0),
                bassFX.animate('BassDegrade', 'MDA%20Degrade', 'rate', None, 0.71, 1, 'beat'),
                vocalsKeschFX1Delay.set('active', 'on'),
                vocalsNanoFX1Delay.set('active', 'on'),
                ],
        },
        { # bar 4
            1: lambda: [
                vocalsKeschFX1Delay.set('pre', 'off'),
                vocalsNanoFX1Delay.set('pre', 'off'),
                bassFX.set('BassScapeIn', 'Mute', 1.0),
                bassFX.set('BassWobbleIn', 'Mute', 1.0),
                ],
            1.2: lambda: [
                bassFX.reset('BassDegrade', 'MDA%20Degrade', 'rate')
            ],
            3.5: lambda: [
                synthsFX2Delay.set('EasyClassical', 'Gain', -3.0),
                synthsFX2Delay.set('TrapFifth', 'Gain', -3.0),
                bassFX.set('BassWobbleIn', 'Mute', 0.0),
                bassFX.set('BassScapeIn', 'Mute', 0.0),
                bassFX.animate('BassDegrade', 'MDA%20Degrade', 'rate', None, 0.68, 1, 'beat'),

                ],
        },
        ], loop=True)

    @pedalboard_button(7)
    def pont_afrotrap(self):
        """
        PONT AFRO TRAP
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'pont_afro_trap_*')
        # seq192.select('couplet2_2*', 'on')

        # Transport
        transport.start()

        # Samples
        self.open_samples()

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')

        # Keyboard
        jmjKeyboard.set_sound('ZTrumpets', boost=True)

        synthsFX2Delay.set('Trap', 'Gain', -14.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)

        # Séquences
        self.start_scene('bx_whatif', lambda: [
            prodSampler.send('/instrument/play', 's:Bx_WhatIf'),
            self.wait(4, 'beat'), #bar 1
            self.wait(4, 'beat'), #bar 2
            self.wait(4, 'beat'), #bar 3
            vocalsKesch.set('normo_exclu', 'on'),
            self.wait(4, 'beat'), #bar 4
            self.couplet_2_1()
        ])

    def couplet_2_1(self):
        """
        COUPLET 2 PART 1 (ain't no suv...)
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'couplet2_2*')
        # seq192.select('off', 'couplet_*cHi_easyClassical')

        # Looper
        looper.record_on_start(0)

        # Transport
        transport.start()

        # Samples
        self.open_samples()

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        # Synths
        synths.set('Trap', 'Pan', -0.7)
        synths.set('ZStambul', 'Pan', 0.5)
        synths.set('EasyClassical', 'Pan', 0.3)

        synths.set('Trap', 'Amp', 'Gain', 0.35)

        # Keyboards
        jmjKeyboard.set_sound('ZDupieux')

        # BassFX
        bassFX.set('zynwah', 'on')


        # Séquence
        # self.start_sequence('couplet_2_1', [
        #     {}, # bar 1
        #     {}, # bar 2
        #     {}, # bar 3
        #     {   # bar 4
        #         2: lambda: seq192.select('off', '*'), # stop drums
        #         3.4: lambda: [
        #             vocalsKesch.set('meuf_exclu', 'on'),
        #             vocalsNano.set('meuf_exclu', 'on'),
        #         ],
        #         4.5: lambda: constantSampler.send('/instrument/play', 's:FunkyHit1', 100),
        #     },
        #     {   # bar 5: Alternate trap (be honest yo bum)
        #         1: lambda: seq192.select('solo', 'trap_*')
        #     },
        #     {}, # bar 6
        #     {}, # bar 7
        #     {   # bar 8
        #         1.5: lambda: prodSampler.send('/instrument/play', 's:Bx_YouWontRaise')
        #     },
        #     {
        #         1: lambda: self.start_scene('vers queen', lambda: self.queen())
        #     }
        # ], loop=False)

    @pedalboard_button(8)
    def theme_lick_me(self):
        # Séquence
        seq192.select('solo', 'themelickme*')

        # Transport
        self.pause_loopers()
        transport.start()

        # Audiolooper
        looper.trigger(0)

        # Samples
        self.open_samples_lickme()
        samplesFX2Delay.set('Samples5', 'Gain', -17.8)
        samplesFX2Delay.set('SamplesFX2Delay', 'Mute', 0.0)

        # Synths
        synthsFX3Delay.set('MajorVocals', 'Gain', -17.8)
        synthsFX3Delay.set('SynthsFX3Delay', 'Mute', 0.0)



        # Séquences
        self.start_sequence('sequence/theme_lickme_samplepitch', [
            {}, # bar 1
            {}, # bar 2
            {}, # bar 3
            { # bar 4
                1.2: lambda: postprocess.animate_pitch('Samples', 1, 0.1, 0.918, 's'),
                2.2: lambda: postprocess.animate_pitch('Samples', None, 1, 0.2, 's'),
            },
            {}, # bar 5
            {}, # bar 6
            {  # bar 7
                2.4: lambda: postprocess.animate_pitch('Samples', 1, 0.25, 0.918, 's'),
                2.8: lambda: postprocess.animate_pitch('Samples', None, 1, 0.1, 's'),
            },
            { # bar 8
                1.2: lambda: postprocess.animate_pitch('Samples', 1, 0.1, 0.918, 's'),
                3: lambda: postprocess.animate_pitch('Samples', None, 1, 0.2, 's'),
                3.62: lambda: postprocess.animate_pitch('Samples', 1, 0.1, 0.918, 's'),
                3.73: lambda: postprocess.animate_pitch('Samples', None, 1, 0.2, 's'),
                4.12: lambda: postprocess.animate_pitch('Samples', 1, 0.1, 0.918, 's'),
                4.15: lambda: postprocess.animate_pitch('Samples', None, 1, 0.2, 's'),
                4.4: lambda: postprocess.animate_pitch('Samples', 1, 0.1, 0.918, 's'),
                4.5: lambda: postprocess.animate_pitch('Samples', None, 1, 0.2, 's'),
                4.78: lambda: postprocess.animate_pitch('Samples', 1, 0.1, 0.918, 's'),
                4.85: lambda: postprocess.animate_pitch('Samples', None, 1, 0.2, 's'),
            }
        ], loop=True)

        self.start_sequence('sequence/theme_lickme_majorvocals', [
            {
                1.4: lambda: postprocess.animate_pitch('Synths', 1, 0.1, 0.515, 's'),
                3.25: lambda: postprocess.animate_pitch('Synths', None, 1, 0.1, 's'),
            }, # bar 1
            { # bar 2
                1.18: lambda: postprocess.animate_pitch('Synths', 1, 0.1, 0.515, 's'),
                2.3: lambda: postprocess.animate_pitch('Synths', None, 1, 0.1, 's'),
            },
            { # bar 3
                1.875: lambda: postprocess.animate_pitch('Synths', 1, 0.1, 0.515, 's'),
                2: lambda: postprocess.animate_pitch('Synths', None, 1, 0.1, 's'),
                2.875: lambda: postprocess.animate_pitch('Synths', 1, 0.1, 0.515, 's'),
                3.375: lambda: postprocess.animate_pitch('Synths', None, 1, 0.1, 's'),
            },
            { # bar 4
                1.2: lambda: postprocess.animate_pitch('Synths', 1, 0.1, 0.515, 's'),
                2.11: lambda: postprocess.animate_pitch('Synths', None, 1, 0.1, 's'),
            },
            {}, # bar 5
            {}, # bar 6
            {  # bar 7
                2.4: lambda: postprocess.animate_pitch('Synths', 1, 0.1, 0.515, 's'),
                2.8: lambda: postprocess.animate_pitch('Synths', None, 1, 0.1, 's'),
                4.82: lambda: postprocess.animate_pitch('Synths', 1, 0.1, 0.515, 's'),
            },
            { # bar 8
                3.1: lambda: postprocess.animate_pitch('Synths', None, 1, 0.1, 's'),
                3.62: lambda: postprocess.animate_pitch('Synths', 1, 0.1, 0.515, 's'),
                3.73: lambda: postprocess.animate_pitch('Synths', None, 1, 0.2, 's'),
                4.12: lambda: postprocess.animate_pitch('Synths', 1, 0.1, 0.515, 's'),
                4.15: lambda: postprocess.animate_pitch('Synths', None, 1, 0.2, 's'),
                4.4: lambda: postprocess.animate_pitch('Synths', 1, 0.1, 0.515, 's'),
                4.5: lambda: postprocess.animate_pitch('Synths', None, 1, 0.2, 's'),
                4.78: lambda: postprocess.animate_pitch('Synths', 1, 0.1, 0.515, 's'),
                4.85: lambda: postprocess.animate_pitch('Synths', None, 1, 0.2, 's'),
            }
        ], loop=True)



    @pedalboard_button(18)
    def alarrache(self):
        # Séquence
        seq192.select('solo', 'couplet2_3*')

        # Transport
        self.pause_loopers()
        transport.start()

        # Keyboards
        jmjKeyboard.set_sound('LowCTrap1')

        # Séquence
        self.start_sequence('couplet_2_1', [
            {   # bar 5: Alternate trap (be honest yo bum)
            },
            {}, # bar 6
            {}, # bar 7
            {   # bar 8
                1.5: lambda: [
                    prodSampler.send('/instrument/play', 's:Bx_YouWontRaise'),
                    seq192.select('solo', 'dummy')
                    ]
            },
            {
                1: lambda: [
                    seq192.select('solo', 'couplet2_2*'),
                    looper.trigger(0)
                    ]
            }
        ], loop=False)


    def queen(self):
        """
        QUEEN (as usual boy)
        ad lib, sortie nano
        """
        self.pause_loopers()
        self.reset()

        # Transport
        transport.start()

        # Samples
        self.open_samples()

        # Vocals
        vocalsFeat.set('normo_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        # Bass
        bassFX.set('zynwah', 'on')


        # Séquences
        seq192.select('solo', 'dummy')

        # Keyboards
        #jmjKeyboard.set_sound('ZDupieux')

    def queen_sortie(self):
        """
        QUEEN SORTIE
        drum stop, transition auto vers couplet 2 2
        """
        self.pause_loopers()
        self.reset()

        seq192.select('solo', 'trap2_*')


        # Transport
        transport.start()


        # Samples
        self.open_samples()


        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')

        self.start_sequence('queen sortie', [
            {}, # bar 1
            {}, # bar 2
            {}, # bar 3
            {}, # bar 4
            {
                1: lambda: self.start_scene('vers couplet 2 2', lambda: self.couplet_2_2())
            }
        ], loop=False)

    @mk2_button(5, 'cyan')
    def couplet_2_2(self):
        """
        COUPLET 2_2 (basse jouée, phili compton l.a)
        + break sur 4e mesure
        + transition auto vers hands up hands up (pretrap2)
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'couplet2_2_*')
        seq192.select('off', 'couplet2_2_*guitar*')
        # seq192.select('off', 'couplet_cLow_b*')


        # Transport
        transport.start()

        # Samples
        self.open_samples()

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        # Keyboard
        jmjKeyboard.set_sound('ZOrgan')

        # Bass
        bassFX.set('zynwah', 'on')

        # Synths
        synths.set('Trap', 'Pan', -0.7)
        synths.set('ZStambul', 'Pan', 0.5)
        synths.set('EasyClassical', 'Pan', 0.3)
        synths.set('Trap', 'Amp', 'Gain', 0.35)
        synths.set('DubstepHorn', 'Amp', 'Gain', 0.35)

        vocalsKeschFX1Delay.set('VocalsKeschFX1Delay', 'GxMultiBandDelay', 'multiplier', 2),


        # Séquence
        self.start_sequence('couplet_2_2', [
            {}, # bar 1
            {   # bar 2
                1.5: lambda:
                    [
                    vocalsKeschFX1Delay.set('active', 'on'),
                    vocalsKeschFX2Delay.set('active', 'on'),
                    vocalsKesch.set('meuf', 'on'),
                    ],
                2.4: lambda:
                    [
                        vocalsKeschFX1Delay.set('pre', 'off'),
                        vocalsKeschFX2Delay.set('pre', 'off'),
                        vocalsKesch.set('meuf', 'off'),
                    ]
            },
            {   # bar 3
                1.5: lambda: vocalsKeschFX2Delay.set('active', 'on'),
                2.4: lambda: vocalsKeschFX2Delay.set('pre', 'off'),
                4: lambda: seq192.select('off', '*')
            },
            {  # bar 4
                1: lambda: seq192.select('off', '*'),
                4.5: lambda: constantSampler.send('/instrument/play', 's:FunkyHit1', 100)
            },
            {  # bar 5
                1: lambda: [
                    seq192.select('solo', 'couplet2_2_*'),
                    # seq192.select('solo', 'couplet2_3*'),
                    seq192.select('off', 'couplet2_2_*guitar*'),
                    # seq192.select('off', 'couplet_cLow_b*')
                ]
            },
            {}, # bar 6
            {}, # bar 7
            {
                1.5: lambda: vocalsNanoFX2Delay.set('active', 'on'),
                4: lambda: [vocalsKesch.set('gars_exclu', 'on'), vocalsNanoFX2Delay.set('pre', 'off')]
            }, # bar 8
            {
                # 1: lambda: self.start_scene('couplet 2 2 vers trap', lambda: self.pretrap2())
            }

        ], loop=False)

    def pretrap2(self):
        """
        PRE TRAP 2 (hands up hands up)
        """
        self.pause_loopers()
        self.reset()

        # Transport
        transport.start()

        # Samples
        self.open_samples()

        # Vocals
        vocalsFeat.set('normo_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')


        # Séquences
        seq192.select('solo', 'pretrap_cLow_trap1')
        seq192.select('on', 'pretrap_cHi_trap')


        # Synths
        synthsFX3Delay.set('Trap', 'Gain', -24)
        synthsFX3Delay.set('SynthsFX3Delay', 'Mute', 0)

        synthsFX5Scape.set('Trap', 'Gain', -3)
        synthsFX5Scape.set('SynthsFX5Scape', 'Mute', 0)


        # Keyboards
        jmjKeyboard.set_sound('ZDupieux')

    @mk2_button(6, 'yellow')
    def pretrap_stop_manhooky(self):
        """
        TRAP STOP MANHOOKY (& du 4)
        """
        self.start_scene('trap_stop_manhooky', lambda: [
            prodSampler.send('/instrument/play', 's:Bx_YouWontRaise'),
            self.wait_next_cycle(),
            seq192.select('off', '*'),
            self.wait_next_cycle(),
            self.trap()
        ])

        jmjKeyboard.set_sound('ZDupieux')

    def afro(self):
        """
        AFRO
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'afro_*')

        # Transport
        transport.start()

        # Samples
        self.open_samples()

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')

        # Keyboard
        jmjKeyboard.set_sound('ZTrumpets', boost=True)

        synthsFX2Delay.set('Trap', 'Gain', -14.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)
