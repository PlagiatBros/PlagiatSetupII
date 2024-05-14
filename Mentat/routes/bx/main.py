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
            'Shamisen' : 'Samples5',
            'ZurnaTheme': 'Samples5',
            'ZurnaLongue': 'Samples3',
            'Sitar': 'Samples4'
        })

    def open_samples(self):
        samples.set('GuitarCrunch', 'Mute', 0.0)
        samples.set('GuitarNatural', 'Mute', 0.0)
        samples.set('GuitarChorus', 'Mute', 0.0)
        samples.set('Trumpets', 'Mute', 0.0)
        samples.set('Shamisen', 'Mute', 0.0)
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


    @mk2_button(2)
    def couplet1_tight(self):
        """
        COUPLET 1 TIGHT
        Chastitties: What U Say & Grab the bully
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'couplet1_tight*')
        seq192.select('off', 'couplet1_*guitar*')

        # Transport
        transport.start()

        # Samples
        self.open_samples()

        samples.set('Shamisen', 'Gain', -12.25)

        samplesFX6Scape.set('Shamisen', 'Gain', -5.5)
        samplesFX6Scape.set('SamplesFX6Scape', 'Mute', 0.0)

        samplesFX4Autofilter.set('Shamisen', 'Gain', -1)
        samplesFX4Autofilter.set('SamplesFX4Autofilter', 'Mute', 0.0)

        samplesFX7Degrade.set('Shamisen', 'Gain', -9)
        samplesFX7Degrade.set('SamplesFX7Degrade', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')

        inputs.set('keschmic', 'static')

        # Keyboard
        jmjKeyboard.set_sound('ZTrumpets', boost=False)

        # Synths
        synths.set('Trap', 'Pan', -0.7)
        synths.set('ZStambul', 'Pan', 0.5)
        synths.set('EasyClassical', 'Pan', 0.3)

        synths.set('Trap', 'Amp', 'Gain', 0.35)
        synths.set('ZStambul', 'Amp', 'Gain', 0.65)
        synths.set('EasyClassical', 'Amp', 'Gain', 0.55)

        synthsFX2Delay.set('Trap', 'Gain', -14.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)

        synths.animate('Trap', 'Pan', -0.7, 0.7, 80, 's',  easing='linear-mirror', loop='true')
        synths.animate('EasyClassical', 'Pan', 0.3, -0.1, 80, 's',  easing='linear-mirror', loop='true')
        synths.animate('ZStambul', 'Pan', 0.5, 0, 80, 's',  easing='linear-mirror', loop='true')


        # BassSynths
        bassSynths.set('BassTrap2', 'Amp', 'Gain', 0.9)
        bassSynths.set('BassBarkline', 'Amp', 'Gain', 1)
        bassSynths.set('BassBoom', 'Amp', 'Gain', 0.8)


        # Lead
        synths.set_lead()
        samples.set_lead()

    @pedalboard_button(2)
    def couplet1_aerien(self):
        """
        COUPLET 1 AERIEN
        Chastitties: don't look at that
        """
        # self.pause_loopers()
        # self.reset()

        # Sequences
        seq192.select('solo', 'couplet1_aerien*')

        # Transport
        # transport.start()

        # Samples
        self.open_samples()

        samples.set('Shamisen', 'Gain', -12.25)

        samplesFX6Scape.set('Shamisen', 'Gain', -5.5)
        samplesFX6Scape.set('SamplesFX6Scape', 'Mute', 0.0)

        samplesFX4Autofilter.set('Shamisen', 'Gain', -1)
        samplesFX4Autofilter.set('SamplesFX4Autofilter', 'Mute', 0.0)

        samplesFX7Degrade.set('Shamisen', 'Gain', -9)
        samplesFX7Degrade.set('SamplesFX7Degrade', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')

        inputs.set('keschmic', 'static')

        # Keyboard
        jmjKeyboard.set_sound('ZTrumpets', boost=True)

        # Synths
        synths.set('Trap', 'Pan', -0.7)
        synths.set('ZStambul', 'Pan', 0.5)
        synths.set('EasyClassical', 'Pan', 0.3)

        synths.set('Trap', 'Amp', 'Gain', 0.35)
        synths.set('ZStambul', 'Amp', 'Gain', 0.65)
        synths.set('EasyClassical', 'Amp', 'Gain', 0.55)

        synthsFX2Delay.set('Trap', 'Gain', -14.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)

        synths.animate('Trap', 'Pan', -0.7, 0.7, 80, 's',  easing='linear-mirror', loop='true')
        synths.animate('EasyClassical', 'Pan', 0.3, -0.1, 80, 's',  easing='linear-mirror', loop='true')
        synths.animate('ZStambul', 'Pan', 0.5, 0, 80, 's',  easing='linear-mirror', loop='true')

        # BassSynths
        bassSynths.set('BassTrap2', 'Amp', 'Gain', 0.9)
        bassSynths.set('BassBarkline', 'Amp', 'Gain', 1)
        bassSynths.set('BassBoom', 'Amp', 'Gain', 0.8)

        # Lead
        synths.set_lead()
        samples.set_lead()

    @mk2_button(3)
    def couplet1_knowers(self):
        """
        COUPLET 1 KNOWERS
        Chastitties: U push the goal trigga
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'couplet1_knowers*')


        # Transport
        transport.start()

        # Samples
        self.open_samples()

        samples.set('Shamisen', 'Gain', -12.25)

        samplesFX6Scape.set('Shamisen', 'Gain', -5.5)
        samplesFX6Scape.set('SamplesFX6Scape', 'Mute', 0.0)

        samplesFX4Autofilter.set('Shamisen', 'Gain', -1)
        samplesFX4Autofilter.set('SamplesFX4Autofilter', 'Mute', 0.0)

        samplesFX7Degrade.set('Shamisen', 'Gain', -9)
        samplesFX7Degrade.set('SamplesFX7Degrade', 'Mute', 0.0)

        # Synths
        synths.set('ZDupieux', 'Pan', 0.2)
        synths.set('ZDupieux', 'Amp', 'Gain', 0.9)
        synths.set('Z8bits', 'Pan', -0.2)
        synths.set('Z8bits', 'Amp', 'Gain', 0.9)

        synthsFX2Delay.set('Z8bits', 'Gain', -18.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')


        # Keyboard
        jmjKeyboard.set_sound('ZDupieux', boost=False)

        # Lead
        synths.set_lead('MajorVocals')
        samples.set_lead()

    @pedalboard_button(3)
    def couplet1_pont(self):
        """
        COUPLET 1 PONT MAJOR
        Tutti: BOYS
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'couplet1_pont*')
        seq192.select('on', 'couplet1_knowers*')


        # Transport
        transport.start()

        # Samples
        self.open_samples()

        samples.set('Shamisen', 'Gain', -12.25)

        samplesFX6Scape.set('Shamisen', 'Gain', -5.5)
        samplesFX6Scape.set('SamplesFX6Scape', 'Mute', 0.0)

        samplesFX4Autofilter.set('Shamisen', 'Gain', -1)
        samplesFX4Autofilter.set('SamplesFX4Autofilter', 'Mute', 0.0)

        samplesFX7Degrade.set('Shamisen', 'Gain', -9)
        samplesFX7Degrade.set('SamplesFX7Degrade', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')

        inputs.set('keschmic', 'dynamic')

        # Synths
        synths.set('ZDupieux', 'Pan', 0.2)
        synths.set('ZDupieux', 'Amp', 'Gain', 0.9)
        synths.set('Z8bits', 'Pan', -0.2)
        synths.set('Z8bits', 'Amp', 'Gain', 0.9)

        synthsFX2Delay.set('Z8bits', 'Gain', -18.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)


        # Keyboard
        jmjKeyboard.set_sound('MajorVocals', boost=True)

        # Lead
        samples.set_lead()

    @pedalboard_button(4)
    def couplet1_2tight(self):
        """
        COUPLET 1
        MISSY : "Same Way"
        """

        self.couplet1_tight()
        # self.pause_loopers()
        # self.reset()
        #
        # # Sequences
        # seq192.select('solo', 'couplet1_tight*')
        # seq192.select('on', 'couplet1_2tight*')
        # seq192.select('off', 'couplet1_tight_cHi*')
        #
        # # Transport
        # transport.start()
        #
        # # Samples
        # self.open_samples()
        #
        # samples.set('GuitarCrunch', 'Gain', -15)
        #
        # samplesFX6Scape.set('GuitarCrunch', 'Gain', -6.5)
        # samplesFX6Scape.set('SamplesFX6Scape', 'Mute', 0.0)
        #
        # samplesFX4Autofilter.set('GuitarCrunch', 'Gain', -2)
        # samplesFX4Autofilter.set('SamplesFX4Autofilter', 'Mute', 0.0)
        #
        # samplesFX7Degrade.set('GuitarCrunch', 'Gain', -11)
        # samplesFX7Degrade.set('SamplesFX7Degrade', 'Mute', 0.0)
        #
        # # Vocals
        # vocalsNano.set('normo_exclu', 'on')
        # vocalsFeat.set('normo_exclu', 'on')
        # vocalsKesch.set('normo_exclu', 'on')
        #
        # # Keyboard
        # jmjKeyboard.set_sound('ZTrumpets', boost=True)
        #
        # # Synths
        # synths.set('ZStambul', 'Pan', 0.5)
        # synths.set('Rhodes', 'Pan', 0.3)
        #
        # synths.set('ZStambul', 'Amp', 'Gain', 0.65)
        # synths.set('TenorSax', 'Amp', 'Gain', 0.5)
        #
        # synthsFX2Delay.set('Rhodes', 'Gain', -14.0)
        # synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)
        #
        # synths.animate('Rhodes', 'Pan', 0.3, -0.1, 80, 's',  easing='linear-mirror', loop='true')
        # synths.animate('ZStambul', 'Pan', 0.5, 0, 80, 's',  easing='linear-mirror', loop='true')
        #
        # # BassSynths
        # bassSynths.set('BassBarkline', 'Amp', 'Gain', 1)
        # bassSynths.set('BassBoom', 'Amp', 'Gain', 0.8)

        # VOCALS
        inputs.set('keschmic', 'static')

        # Sequence
        self.start_scene('sequence/couplet1_tight_p2', lambda: [
            self.wait(12, 'beat'),
            autotuneKeschNormo.set('correction', 0),
            self.wait(4, 'beat'),
            self.wait(14, 'beat'),
            seq192.select('solo', 'couplet1_3tight*'),
            seq192.select('on', 'couplet1_tight_samples_yeah'),
            seq192.select('on', 'couplet1_tight_samples_funkyHit'),
            samplesFX6Scape.set('SamplesFX6Scape', 'Mute', 1.0)
        ])

        # Samples
        samplesFX3Reverb.set('GuitarCrunch', 'Gain', -34.0)
        samplesFX3Reverb.set('GuitarNatural', 'Gain', -13.39)
        samplesFX3Reverb.set('GuitarChorus', 'Gain', -16.0)
        samplesFX3Reverb.set('SamplesFX3Reverb', 'Mute', 0.0)

        samplesFX2Delay.set('GuitarNatural', 'Gain', -13.39)
        samplesFX2Delay.set('SamplesFX2Delay', 'Mute', 0.0)

        # Lead
        synths.set_lead()
        samples.set_lead()




    @mk2_button(4)
    def pretrap(self):
        """
        PRE-TRAP
        """
        self.reset()
        self.pause_loopers()

        # Séquences
        # seq192.select('solo', 'pretrap_cHi_trap')
        seq192.select('solo', 'pretrap_cLow_trap1')

        # transport
        transport.start()

        # Samples
        self.open_samples()


        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        # VOCALS
        inputs.set('keschmic', 'dynamic')

        # Keyboards
        jmjKeyboard.set_sound('ZDupieux', boost=False)

        # Synths
        synthsFX2Delay.set('Trap', 'Gain', -14.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)

    @mk2_button(5, 'purple')
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

        # VOCALS
        inputs.set('keschmic', 'dynamics')

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

        synths.set('EasyClassical', 'Amp', 'Gain', 0.35)
        synthsFX1Reverb.set('EasyClassical', 'Gain', -2.5)
        synthsFX1Reverb.set('SynthsFX1Reverb', 'Mute', 0.0)

        synthsFX2Delay.set('EasyClassical', 'Gain', -9.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'GxMultiBandDelay', 'multiplier', 1.5),

        # BassSynths
        bassSynths.set('BassTrap2', 'Amp', 'Gain', 0.8)


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

        # VOCALS
        inputs.set('keschmic', 'dynamic')

        # Keyboard
        jmjKeyboard.set_sound('ZTrumpets', lead=False)

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
            vocalsKesch.set('meuf', 'on'),
            inputs.set('keschmic', 'static')
        ])

    @pedalboard_button(6)
    def theme(self):
        """
        THEME
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'theme_*')

        # Transport
        transport.start()

        # Samples
        self.open_samples()

        samples.set('Shamisen', 'Gain', -12.25)

        samplesFX6Scape.set('Shamisen', 'Gain', -5.5)
        samplesFX6Scape.set('SamplesFX6Scape', 'Mute', 0.0)

        samplesFX4Autofilter.set('Shamisen', 'Gain', -1)
        samplesFX4Autofilter.set('SamplesFX4Autofilter', 'Mute', 0.0)

        samplesFX7Degrade.set('Shamisen', 'Gain', -9)
        samplesFX7Degrade.set('SamplesFX7Degrade', 'Mute', 0.0)

        # Bass
        bassFX.set('distohi', 'on')
        bassFX.set('degrade', 'on')
        bassfx.set('scape', 'poston')
        bassfx.set('wobble', 'poston')
        bassfx.set('wobble_subdivision', 6)


        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')
        vocalsFeat.set('meuf', 'on')

        # VOCALS
        inputs.set('keschmic', 'static')

        # Keyboard
        jmjKeyboard.set_sound('ZTrumpets', lead=True)

        # Synths
        synths.set('Trap', 'Amp', 'Gain', 0.4)
        synths.set('TrapFifth', 'Amp', 'Gain', 0.4)
        synths.set('EasyClassical', 'Amp', 'Gain', 0.6)
        synths.set('Rhodes', 'Amp', 'Gain', 0.6)
        synths.set('ZDupieux', 'Amp', 'Gain', 0.4)
        synths.set('TenorSax', 'Amp', 'Gain', 0.4)

        synths.set('Trap', 'Pan', -0.6)
        synths.set('TrapFifth', 'Pan', 0.6)
        synths.set('ZDupieux', 'Pan', -0.2)
        synths.set('TenorSax', 'Pan', 0.2)

        synths.set('TenorSax', 'Calf%20Mono%20Compressor', 'Bypass', 0.0)
        synths.set('TenorSax', 'Calf%20Multi%20Chorus', 'Active', 1.0)

        synthsFX1Reverb.set('Trap', 'Gain', -9.0)
        synthsFX1Reverb.set('TrapFifth', 'Gain', -9.0)
        synthsFX1Reverb.set('EasyClassical', 'Gain', -9.0)
        synthsFX1Reverb.set('Rhodes', 'Gain', -9.0)
        synthsFX1Reverb.set('SynthsFX1Reverb', 'Mute', 0.0)


        synthsFX2Delay.set('Trap', 'Gain', -14.0)
        synthsFX2Delay.set('ZDupieux', 'Gain', -9.0)
        synthsFX2Delay.set('TenorSax', 'Gain', -9.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)

        synthsFX3Delay.set('ZTrumpets', 'Gain', -9.0)
        synthsFX3Delay.set('SynthsFX3Delay', 'Mute', 0.0)
        synthsFX3Delay.set('SynthsFX3Delay', 'Invada%20Delay%20Munge%20(mono%20in)', 'Delay%201', 0.15) #0.203)
        synthsFX3Delay.set('SynthsFX3Delay', 'Invada%20Delay%20Munge%20(mono%20in)', 'Feedback%201', 33)
        synthsFX3Delay.set('SynthsFX3Delay', 'Invada%20Delay%20Munge%20(mono%20in)', 'Delay%202', 0.25) #0.347)
        synthsFX3Delay.set('SynthsFX3Delay', 'Invada%20Delay%20Munge%20(mono%20in)', 'Feedback%202', 29)

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
            # 4: lambda: self.engine.animate('pitch_synths', 1, 0.8, 0.85, 'b', easing='cubic-in')
        },
        {
            # 1: lambda: self.engine.set('pitch_synths', 1.0)
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
                synthsFX2Delay.set('EasyClassical', 'Gain', -2.0),
                synthsFX2Delay.set('TrapFifth', 'Gain', -2.0),
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
        vocalsFeat.set('normo_exclu', 'on')

        # VOCALS
        inputs.set('keschmic', 'dynamic')


        # Keyboard
        jmjKeyboard.set_sound('ZTrumpets', boost=True)

        # Synths
        synths.set('Trap', 'Pan', -0.7)
        synths.set('ZStambul', 'Pan', 0.5)
        synths.set('EasyClassical', 'Pan', 0.3)

        synths.set('Trap', 'Amp', 'Gain', 0.35)
        synths.set('ZStambul', 'Amp', 'Gain', 0.65)
        synths.set('EasyClassical', 'Amp', 'Gain', 0.55)

        synthsFX2Delay.set('Trap', 'Gain', -14.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)

        synths.animate('Trap', 'Pan', -0.7, 0.7, 80, 's',  easing='linear-mirror', loop='true')
        synths.animate('EasyClassical', 'Pan', 0.3, -0.1, 80, 's',  easing='linear-mirror', loop='true')
        synths.animate('ZStambul', 'Pan', 0.5, 0, 80, 's',  easing='linear-mirror', loop='true')

        # Séquences
        self.start_scene('sequences/bx_whatif', lambda: [
            prodSampler.send('/instrument/play', 's:Bx_WhatIf'),
            self.wait(4, 'beat'), #bar 1
            self.wait(4, 'beat'), #bar 2
            self.wait(4, 'beat'), #bar 3
            self.wait(2, 'beat'), #bar 4
            vocalsKesch.set('meuf_exclu', 'on'),
            self.wait(2, 'beat'),
            self.run(self.couplet2_nu),
#            self.run(self.lickme_start)
        ])

    @pedalboard_button(99)
    def couplet2_nu(self):
        """
        COUPLET 2 (what U say)
        """
        self.couplet1_tight()
        vocalsKesch.set('meuf_exclu', 'on')
        # VOCALS
        inputs.set('keschmic', 'dynamic')


        seq192.select('on','//couplet*Low*')



    @mk2_button(6)
    def couplet2_keeping(self):
        """
        COUPLET 2 PONT (keeping windows shut)
        """
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
        prodSampler.send('/instrument/play', 's:Plagiat/BX/Bx_Car')

        # Séquences
        self.start_scene('sequences/keeping', lambda: [
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
            vocalsKesch.set('normo_exclu', 'on'),
            self.wait(1,'b'),
            self.run(lambda: [
                self.couplet2_nu(),
                vocalsKesch.set('normo_exclu', 'on')
            ]),
        ])

        self.start_scene('sequences/vxkesch_dude', lambda: [
            self.wait(2, 'b'),
            vocalsKesch.set('gars_exclu', 'on'),
            vocalsKeschFX1Delay.set('active', 'on'),
        ])

        # Vocals
        # vocalsKesch.set('normo_exclu', 'on')
        vocalsNano.set('normo_exclu', 'on')
        vocalsFeat.set('gars_exclu', 'on')
        # vocalsFeatFX1Delay.set('active', 'on'),

        # VOCALS
        inputs.set('keschmic', 'dynamic')

        # Samples
        #samples.set_lead()

    @mk2_button(7)
    def couplet2_jeez(self):
        """
        COUPLET 2 JEEZ (got wings)
        appui 2e temps
        """
        # Séquences
        seq192.select('off', '//couplet_*Low*')
        seq192.select('off', 'couplet_*samples*')


        # Séquences (Mentat)
        self.start_scene('sequences/bx_heeee', lambda: [
            self.wait(2.6, 'beat'),
            prodSampler.send('/instrument/play', 's:Bx_Heee'),
        ])
        self.start_scene('sequences/bx_asusual', lambda: [
            self.wait_next_cycle(),
            self.run(self.couplet2_knowers_asusual)
        ])


        # Vocals
        vocalsKesch.set('normo_exclu','on')

        # VOCALS
        inputs.set('keschmic', 'dynamic')

        # Keyboards
        jmjKeyboard.set_sound('ZDupieux', lead=False)

        # Samples
        #samples.set_lead()

    @pedalboard_button(98)
    def couplet2_knowers_asusual(self):
        """
        COUPLET 2 knowers (as usual)
        """
        self.couplet1_knowers()
        seq192.select('off', 'couplet1_knowers_zHi_dupieux')

        # VOCALS
        inputs.set('keschmic', 'dynamic')

    @pedalboard_button(8)
    def couplet2_knowers_phili(self):
        """
        COUPLET 2 knowers (compton phili)
        """
        looper.unpause(0)

        # VOCALS
        inputs.set('keschmic', 'dynamic')

        self.start_scene('lancement_basse_et_fx', lambda: [
            self.wait_next_cycle(),
            seq192.select('on', 'couplet1_knowers_zHi_dupieux'),
            self.start_sequence('couplet_2_2', [
                {}, # bar 1
                {   # bar 2
                    1.25: lambda:
                        [
                            vocalsKeschFX1Delay.set('active', 'on'),
                            vocalsKeschFX2Delay.set('active', 'on'),
                            vocalsKesch.set('meuf', 'on'),
                            vocalsFeatFX1Delay.set('active', 'on'),
                            vocalsFeatFX2Delay.set('active', 'on'),
                        ],
                    2.9: lambda:
                        [
                            vocalsKeschFX1Delay.set('pre', 'off'),
                            vocalsKeschFX2Delay.set('pre', 'off'),
                            vocalsKesch.set('meuf', 'off'),
                            vocalsFeatFX1Delay.set('pre', 'off'),
                            vocalsFeatFX2Delay.set('pre', 'off'),
                        ]
                },
                {   # bar 3
                    1: lambda: [
                        vocalsKeschFX2Delay.set('active', 'on'),
                        vocalsFeatFX2Delay.set('active', 'on')
                    ],
                    2.4: lambda: [
                        vocalsKeschFX2Delay.set('pre', 'off'),
                        vocalsFeatFX2Delay.set('pre', 'off')
                    ],
                }

            ], loop=False)

        ])


    @mk2_button(8, 'purple')
    def trapcouplet2(self):
        """
        COUPLET 2 TRAP (my bum is yo dashboard)
        """
        self.reset()

        # Séquence
        seq192.select('solo', 'trap2*')
        seq192.select('on', 'trap_*Low*')

        # Transport
        self.pause_loopers()
        transport.start()

        # Samples
        self.open_samples()
        samplesFX3Reverb.set('Trumpets', 'Gain', -6.0)
        samplesFX3Reverb.set('SamplesFX3Reverb', 'Mute', 0.0)

        # Keyboards
        jmjKeyboard.set_sound('ZDupieux', boost=False)

        # Vocals
        vocalsKesch.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')
        vocalsNano.set('normo_exclu', 'on')

        # VOCALS
        inputs.set('keschmic', 'dynamic')

        # Séquence
        self.start_sequence('couplet_2_1', [
            {   # bar 5: Alternate trap (be honest yo bum)
            },
            {}, # bar 6
            {}, # bar 7
            {   # bar 8
                1.5: lambda: [
                    prodSampler.send('/instrument/play', 's:Plagiat/BX/Bx_YouWontRaise'),
                    seq192.select('solo', 'dummy')
                    ]
            },
            {
                1: lambda: [
                    seq192.select('on', 'trap_*Low*'),
                    seq192.select('on', 'trapexclu_samples_shamisen'),


                    samples.set('Shamisen', 'Gain', -10.25),
                    samplesFX3Reverb.set('Shamisen', 'Gain', -6.0),
                    samplesFX3Reverb.set('SamplesFX3Reverb', 'Mute', 0.0)
                    ],
                1.3: lambda: postprocess.set_filter('Samples', 400),
                3: lambda: postprocess.animate_filter('Samples', 400, 20000, 3*4 + 2, 'beats', 'exponential'),
            }
        ], loop=False)




    @mk2_button(9, 'cyan')
    def geouerz(self):
        """
        GEOUERZ
        """
        # Transport
        transport.stop()
        self.pause_loopers()
        self.reset()

        # Keyboard
        jmjKeyboard.set_sound('Charang', lead=False)

        # VOCALS
        inputs.set('keschmic', 'dynamic')

    @mk2_button(10, 'cyan')
    def outro_click(self):
        """
        OUTRO
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('off', '*')

        # Transport
        transport.start()

        # Keyboard
        jmjKeyboard.set_sound('LowZDancestep')

    @mk2_button(11, 'cyan')
    def outro_outro(self):
        """
        TRANCE phase 2 (tkt)
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('off', '*')

        # Transport
        transport.start()

        # Keyboard
        jmjKeyboard.set_sound('MajorVocals', lead=True)

        # Loops
        looper.trigger(3)

        # Vx
        vocalsKesch.set('normo_exclu', 'on')

        inputs.set('keschmic', 'dynamic')


    @pedalboard_button(11)
    def rec_key(self):
        """
        REC BASS SYNTHS
        """
        looper.record(2)
