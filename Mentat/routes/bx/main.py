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
        })

    def open_samples(self):
        samples.set('GuitarCrunch', 'Mute', 0.0)
        samples.set('GuitarNatural', 'Mute', 0.0)
        samples.set('GuitarChorus', 'Mute', 0.0)
        samples.set('Trumpets', 'Mute', 0.0)
        samplesFX3Reverb.set('Trumpets', 'Gain', -10.0)
        samplesFX3Reverb.set('SamplesFX3Reverb', 'Mute', 0.0)


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
        vocalsKesch.set('normo_exclu', 'on')

        # Keyboard
        jmjKeyboard.set_sound('ZTrumpets', boost=True)

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

    @mk2_button(2)
    def stop_basses(self):
        """
        STOP BASSES
        """
        # Séquences
        seq192.select('off', 'couplet_*Low*')

        self.start_scene('sequence/bx_heeee', lambda: [
            self.wait(3.6, 'beat'),
            prodSampler.send('/instrument/play', 's:Bx_Heee'),
            self.wait(1.4, 'beat'),
            self.pretrap()
        ])

    # @mk2_button(3)
    def pretrap(self):
        """
        PRE-TRAP
        """
        # Séquences
        seq192.select('solo', 'couplet_*')

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')


    @pedalboard_button(4)
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

        # Keyboard
        jmjKeyboard.set_sound('ZTrumpets', boost=True)

        synthsFX2Delay.set('Trap', 'Gain', -14.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)

    @mk2_button(4)
    def prerefrain(self):
        """
        PREREFRAIN
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'prerefrain_*')

        # Transport
        transport.start()

        # Samples
        self.open_samples()
        samplesFX2Delay.set('GuitarCrunch', 'Gain', -18.0)
        samplesFX2Delay.set('SamplesFX2Delay', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('meuf_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')

        # Keyboard
        jmjKeyboard.set_sound('ZTrumpets', boost=False)

        synths.set('TrapFifth', 'Amp', 'Gain', 0.35)
        synths.set('TrapFifth', 'Pan', -0.33)
        synths.set('ZTrumpets', 'Pan', 0.33)

        synthsFX2Delay.set('TrapFifth', 'Gain', -18.0)
        synthsFX2Delay.set('ZTrumpets', 'Gain', -18.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)

        self.engine.animate('filter_synths', 20, 22000, 64, 'b', 'exponential')
        # self.engine.animate('GuitarCrunch', None, -, 64, 'b', 'exponential')

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

        # Keyboard
        jmjKeyboard.set_sound('ZTrumpets', boost=False)

        synths.set('TrapFifth', 'Amp', 'Gain', 0.35)
        synths.set('TrapFifth', 'Pan', -0.33)
        synths.set('ZTrumpets', 'Pan', 0.33)

        synthsFX2Delay.set('TrapFifth', 'Gain', -18.0)
        synthsFX2Delay.set('ZTrumpets', 'Gain', -18.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)

        self.engine.animate('filter_synths', 20, 22000, 64, 'b', 'exponential')
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
        vocalsKesch.set('normo_exclu', 'on')

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
                ],
        },
        { # bar 4
            1: lambda: [
                bassFX.set('BassScapeIn', 'Mute', 1.0),
                bassFX.set('BassWobbleIn', 'Mute', 1.0),
                ],
            3.5: lambda: [
                synthsFX2Delay.set('EasyClassical', 'Gain', -3.0),
                synthsFX2Delay.set('TrapFifth', 'Gain', -3.0),
                bassFX.set('BassWobbleIn', 'Mute', 0.0),
                bassFX.set('BassScapeIn', 'Mute', 0.0),
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
        self.start_scene('sequence/bx_whatif', lambda: [
            prodSampler.send('/instrument/play', 's:Bx_WhatIf'),
            self.wait(4, 'beat'), #bar 1
            self.wait(4, 'beat'), #bar 2
            self.wait(3.51, 'beat'), #bar 3
            vocalsKesch.set('normo_exclu', 'on'),
            self.wait(0.49, 'beat'),
            self.wait(4, 'beat'), #bar 4
            self.couplet_2_1()
        ])

    def couplet_2_1(self):
        """
        COUPLET 2 PART 1 (ain't no suv...)
        """
        self.couplet()

        # Vocals
        vocalsKesch.set('meuf', 'on')

        # Séquence
        self.start_sequence('couplet_2_1', {
            {}, # bar 1
            {}, # bar 2
            {}, # bar 3
            {   # bar 4
                1: lambda: seq192.select('off', '*'),
                3: lambda: [
                    vocalsKesch.set('meuf_exclu', 'on'),
                    vocalsNano.set('meuf_exclu', 'on'),
                ]
            },
            {   # bar 5: Alternate trap
                1: lambda: seq192.select('solo', 'trap_*')
            },
            {}, # bar 6
            {}, # bar 7
            {   # bar 8
                1.5: lambda: prodSampler.send('/instrument/play', 's:Bx_YouWontRaise')
            },
            {}, # bar 9
            {}, # bar 10
            {}, # bar 11
            {}, # bar 12
            {   # bar 13
                1: lambda: self.trap_stop_basses()
            },
        }, loop=False)

    @mk2_button(5)
    def trap_stop_basses(self):
        """
        TRAP STOP BASSES
        """
        # Séquences
        seq192.select('off', 'trap_*Low*')

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')

    @mk2_button(6, 'orange')
    def trap_stop_manhooky(self):
        """
        TRAP STOP MANHOOKY (& du 4)
        """
        self.start_sequence('sequence/trap_stop_manhooky', lambda: [
            prodSampler.send('/instrument/play', 's:Bx_YouWontRaise'),
            self.wait(0.5, 'beat'),
            seq192.select('off', '*')
        ])

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
