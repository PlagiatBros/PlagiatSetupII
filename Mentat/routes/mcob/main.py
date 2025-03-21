from ..base import RouteBase, mk2_button, pedalboard_button
from .video import Video
from .light import Light

from modules import *

class Mcob(Video, Light, RouteBase):
    """
    MCOB
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
        microtonality.enable()
        microtonality.set_tuning(0, 0, 0, 0, 0, 0.35, 0, 0, 0.35, 0, 0.35, 0)

        # Autotuner Notes
        #               c     d     e  f     g     a     b
        notes.set_notes(1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0) # Normalement g# uniquement sur "Yes I'm a cathedral"

        # Mk2
        mk2Control.set_mode('cut_samples', 'cut_synths')

    @pedalboard_button(1)
    @mk2_button(1, 'blue')
    def stop(self):
        """
        STOP
        zazad
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
        transport.set_tempo(120)
        transport.start()

        # Samples
        samplesFX6Scape.set('Samples2', 'Gain', -5.0)
        samplesFX6Scape.set('SamplesFX6Scape', 'Mute', 0.0)

        samples.set('Samples1', 'Mute', 0.0)
        samples.set('Samples2', 'Mute', 0.0)
        samples.set('Samples5', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('meuf_exclu', 'on')

        # Keyboard
        jmjKeyboard.set_sound('LowZDupieux')

    @pedalboard_button(5)
    def prerefrain0(self):
        """
        PRÉ-REFRAIN 0 (cf PRÉ-REFRAIN)
        """
        # méthode vide juste pour que le déroulé du morceau appairaisse de façon linéaire
        pass



    @mk2_button(2, 'purple')
    def refrain(self):
        """
        REFRAIN
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'refrain_*')

        # Transport
        transport.set_tempo(120)
        transport.start()

        # Samples
        samplesFX6Scape.set('Samples2', 'Gain', -5.0)
        samplesFX6Scape.set('SamplesFX6Scape', 'Mute', 0.0)

        samples.set('Samples1', 'Mute', 0.0)
        samples.set('Samples2', 'Mute', 0.0)
        samples.set('Samples3', 'Mute', 0.0)
        samples.set('Samples5', 'Mute', 0.0)

        # Bass
        bassfx.set('distohi', 'on')

        # Vocals
        vocalsNano.set('meuf_exclu', 'on')
        vocalsKesch.set('meuf_exclu', 'on')

        # Keyboards
        jmjKeyboard.set_sound('LowZDubstep')

        # Mk2
        mk2Control.set_mode('cut_samples', 'cut_synths', 'wobble')

    @pedalboard_button(3)
    def couplet1_1(self):
        """
        COUPLET 1 - Trap "Look"
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'couplet1-1_*')

        # Transport
        transport.set_tempo(120)
        transport.start()

        # Samples
        samplesFX6Scape.set('Samples2', 'Gain', -10.0) # attention - 10 et - 5 dans setup précédent
        samplesFX6Scape.set('SamplesFX6Scape', 'Mute', 0.0)

        samplesFX2Delay.set('Samples2', 'Gain', -9.0)
        samplesFX2Delay.set('SamplesFX2Delay', 'Mute', 0.0)

        samples.set('Samples1', 'Mute', 0.0)
        samples.set('Samples2', 'Mute', 0.0)
        samples.set('Samples4', 'Mute', 0.0)


        # Vocals
        vocalsNano.set('meuf_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')

        vocalsNanoFX3TrapVerb.set('NanoMeuf', 'Gain', 0.0)
        vocalsNanoFX3TrapVerb.set('VocalsNanoFX3TrapVerb', 'Mute', 0.0)


        # Mk2
        mk2Control.set_mode('cut_samples', 'cut_synths')

    @pedalboard_button(4)
    def couplet1_2(self):
        """
        COUPLET 1 - Prince 2 Pac
        """
        # Sequences
        seq192.select('solo', 'couplet1-2_*')
        seq192.select('off', 'couplet1-2_samples_princeguitar2')

        # Samples
        samplesFX6Scape.set('Samples2', 'Gain', -10.0) # attention - 10 et - 5 dans setup précédent
        samplesFX6Scape.set('SamplesFX6Scape', 'Mute', 0.0)

        samplesFX2Delay.set('Samples2', 'Gain', -9.0)
        samplesFX2Delay.set('SamplesFX2Delay', 'Mute', 0.0)

        samples.set('Samples1', 'Mute', 0.0)
        samples.set('Samples2', 'Mute', 0.0)
        samples.set('Samples4', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('meuf_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')

        # Mk2
        mk2Control.set_mode('cut_samples', 'cut_synths')

        # Sequences (Mentat)
        self.start_scene('prince2pac_launcher', lambda: [
            self.wait_next_cycle(),
            self.start_sequence('prince2pac_a', [
                {   # bar 1
                    'signature': '4/4',
                    1: lambda: vocalsKesch.set('gars_exclu', 'on')
                },
                {}, {}, {}, {}, {}, # bars 2, 3, 4, 5, 6,
                {   # bar 7
                    1: lambda: [vocalsKesch.set('gars', 'on'), vocalsKesch.set('normo', 'on')]
                },
                {}, # bars 8
                {   # bar 9
                    1: lambda: vocalsKesch.set('normo_exclu', 'on')
                },
                {}, {}, # bars 10, 11
                {   # bar 12
                    2: lambda: vocalsKesch.set('meuf', 'on'),
                    3: lambda: vocalsKesch.set('meuf', 'off'),
                    4: lambda: vocalsKesch.set('meuf', 'on'),
                },
                {   # bar 13
                    1: lambda: vocalsKesch.set('meuf', 'off'),
                },
                {}, {}, # bars 14, 15
                {   # bar 16
                    4: lambda: postprocess.animate_pitch('*', 1, 0.25, 0.5, 'beat'),
                    4.95: lambda: postprocess.animate_pitch('*', 0.25, 1, 0.05, 'beat')
                },
                {  # bar 17
                    1: lambda: [seq192.select('off', 'couplet1-2_cLow_*'), seq192.select('off', 'couplet1-2_samples_princeguitar'), seq192.select('on', 'couplet1-2_samples_princeguitar2'), seq192.select('on', 'couplet1-2_cLow_trap1')]
                    # On coupe le bass synth et allez hop bass/batt
                },
            ], loop=False),
        ])

    @mk2_button(3, 'purple')
    def couplet1_3(self):
        """
        COUPLET 1 - No Ambition
        """
        # Sequences
        seq192.select('solo', 'dummy')

        # Transport
        transport.set_tempo(120)
        transport.start()

        # Vocals
        vocalsNano.set('gars', 'on')
        vocalsNano.set('normo', 'on')
        vocalsKesch.set('gars_exclu', 'on')

        # Mk2
        mk2Control.set_mode('cut_samples', 'cut_synths')

        # Sequences (Mentat)
        self.start_sequence('prince2pac_b', [
            {   # bar 1
                'signature': '4/4',
                1: lambda: [vocalsKesch.set('meuf_exclu', 'on'), vocalsKesch.set('normo', 'on')],
            },
            {  # bar 2
                3 + 2/3: lambda: vocalsKesch.set('gars_exclu', 'on'),
            },
            {  # bar 3
                1: lambda:
                [
                    seq192.select('solo', 'couplet1-2_*'),
                    seq192.select('off', 'couplet1-2_samples_princeguitar2'),
                    transport.start()
                ]
            }, {}, # bar 4
            {   # bar 5
                1: lambda: vocalsKesch.set('gars_exclu', 'on')
            },
            {}, {}, # bar 6, 7
            {   # bar 8
                4 + 2/3: lambda: vocalsKesch.set('normo', 'on')
            },
            { # bar 9 - we not getting it woking
                1: lambda: seq192.select('solo', 'fummy')
            },
            {
                3.3: lambda: [
                    seq192.select('solo', 'couplet1-2_*'),
                    seq192.select('off', 'couplet1-2_samples_princeguitar2')
                ]
            }, # bar 10
            {   # bar 11
                1: lambda: vocalsKesch.set('normo_exclu', 'on'),
            },
            {
                3: lambda: vocalsKesch.set('meuf', 'on')
            },
            {   # bar 12
                1: lambda: vocalsKesch.set('meuf', 'off'),
                4.5: lambda: vocalsKesch.set('meuf', 'on')
            },
            {   # bar 13
                2.5: lambda: vocalsKesch.set('meuf', 'off'),
                3: lambda: vocalsKesch.set('meuf', 'on'),
                4.5: lambda: vocalsKesch.set('meuf', 'off'),
            },
            {   # bar 14
                1: lambda: vocalsKesch.set('meuf', 'on'),
                2.5: lambda: vocalsKesch.set('meuf', 'off'),
                3: lambda: vocalsKesch.set('meuf', 'on')
            },
            {}, {},  # bar 16, 17
        ], loop=False)


    @mk2_button(4, 'purple')
    def couplet1_4(self):
        """
        COUPLET 1 - Ragga
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'couplet1-4_*')

        # Transport
        transport.set_tempo(120)
        transport.start()

        # Samples
        samplesFX6Scape.set('Samples2', 'Gain', -10.0) # attention - 10 et - 5 dans setup précédent
        samplesFX6Scape.set('SamplesFX6Scape', 'Mute', 0.0)

        samplesFX2Delay.set('Samples2', 'Gain', -9.0)
        samplesFX2Delay.set('SamplesFX2Delay', 'Mute', 0.0)

        samples.set('Samples1', 'Mute', 0.0)
        samples.set('Samples2', 'Mute', 0.0)
        samples.set('Samples4', 'Mute', 0.0)

        # Vocals
        vocalsKesch.set('meuf_exclu', 'on')
        vocalsNano.set('gars_exclu', 'on')

        # Mk2
        mk2Control.set_mode('cut_samples', 'cut_synths')

    @pedalboard_button(5)
    def prerefrain(self):
        """
        PRE-REFRAIN
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'prerefrain_*')

        # Transport
        transport.set_tempo(120)
        transport.start()

        # Samples
        samplesFX6Scape.set('Samples2', 'Gain', -5.0)
        samplesFX6Scape.set('SamplesFX6Scape', 'Mute', 0.0)

        samples.set('Samples1', 'Mute', 0.0)
        samples.set('Samples2', 'Mute', 0.0)
        samples.set('Samples5', 'Mute', 0.0)

        # Vocals
        vocalsKesch.set('gars', 'on')
        vocalsKesch.set('meuf', 'on')
        vocalsNano.set('normo_exclu', 'on')

        # Keyboards
        jmjKeyboard.set_sound('ConstantSampler')


        # Mk2
        mk2Control.set_mode('cut_samples', 'cut_synths')

    @mk2_button(2)
    def refrain2(self):
        """
        REFRAIN 2 (cf REFRAIN)
        """
        # méthode vide juste pour que le déroulé du morceau appairaisse de façon linéaire
        pass

    @pedalboard_button(6)
    def couplet2(self):
        """
        COUPLET 2
        """
        self.pause_loopers()
        self.reset()

        # Looper
        looper.record_on_start(0)

        # Sequences
        seq192.select('solo', 'couplet2_*')

        # Transport
        transport.set_tempo(120)
        transport.start()

        # Samples
        samplesFX6Scape.set('Samples2', 'Gain', -10.0) # attention - 10 et - 5 dans setup précédent
        samplesFX6Scape.set('SamplesFX6Scape', 'Mute', 0.0)

        samplesFX2Delay.set('Samples2', 'Gain', -9.0)
        samplesFX2Delay.set('SamplesFX2Delay', 'Mute', 0.0)

        samples.set('Samples1', 'Mute', 0.0)
        samples.set('Samples2', 'Mute', 0.0)
        samples.set('Samples4', 'Mute', 0.0)

        # Vocals
        vocalsKesch.set('gars_exclu', 'on')

        # Keyboards
        jmjKeyboard.set_sound('ZNotSoRhodes')

        # Mk2
        mk2Control.set_mode('cut_samples', 'cut_synths')

        self.start_sequence('stop_looping', [
            {
                'signature': '32/4',
                32: lambda: looper.record(0),
            },
            {
                1: lambda: [
                        vocalsNano.set('gars_exclu', 'on'),
                        vocalsNanoFX2Delay.set('active', 'on'),
                        vocalsNanoFX4Disint.set('active', 'on')
                ]
            },
            {
                1: lambda: [
                    #  ready for my...
                    transport.stop(),
                    looper.pause(),
                ],
                2.5: lambda: jmjKeyboard.set_sound('LowZDubstep')
            }
        ], loop=False)

    @mk2_button(4)
    def couplet2_1(self):
        """
        Couplet 2-1 (RAGGA) (cf Couplet 1-4)
        """
        # méthode vide juste pour que le déroulé du morceau appairaisse de façon linéaire
        pass

    @pedalboard_button(7)
    def blast(self):
        """
        BLAST
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'blast1_*')

        # Transport
        transport.start()
        transport.set_tempo(120)

        # Samples
        samplesFX6Scape.set('Samples2', 'Gain', -5.0)
        samplesFX6Scape.set('SamplesFX6Scape', 'Mute', 0.0)

        samples.set('Samples1', 'Mute', 0.0)
        samples.set('Samples2', 'Mute', 0.0)
        samples.set('Samples3', 'Mute', 0.0)
        samples.set('Samples5', 'Mute', 0.0)

        # Mk2
        mk2Control.set_mode('cut_samples', 'cut_synths')

        # Scenes
        self.start_sequence('delayed_blast', {
            'signature': '32/4',
            33: lambda: [
                seq192.select('solo', 'blast2_*'),
                bassFX.set('distohi', 'on')
                ]
        })


    @pedalboard_button(8)
    def trance(self):
        """
        TRANCE
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'trance_*')

        # Samples
        samplesFX6Scape.set('Samples2', 'Gain', -5.0)
        samplesFX6Scape.set('SamplesFX6Scape', 'Mute', 0.0)

        samples.set('Samples1', 'Mute', 0.0)
        samples.set('Samples2', 'Mute', 0.0)
        samples.set('Samples5', 'Mute', 0.0)

        # Transport
        transport.start()
        transport.set_tempo(130)

        # Keyboards
        jmjKeyboard.set_sound('ZNotSoRhodes')

        # Mk2
        mk2Control.set_mode('cut_samples', 'cut_synths')
        
    @pedalboard_button(9)
    def rec_synth(self):
        """
        RECORD SYNTH
        """
        looper.record(3)

    @pedalboard_button(10)
    def loop_synth(self):
        """
        OVERDUB SYNTH
        """
        looper.overdub(3)

    @mk2_button(5, 'purple')
    def relance_trance(self):
        """
        RELANCE TRANCE
        """
        self.pause_loopers()
        self.reset()

        seq192.select('off', '*')


        # Looper
        looper.trigger('[0,3]')

        # Transport
        transport.set_tempo(130)
        transport.start()

        # Samples
        samplesFX6Scape.set('Samples2', 'Gain', -5.0)
        samplesFX6Scape.set('SamplesFX6Scape', 'Mute', 0.0)

        samples.set('Samples1', 'Mute', 0.0)
        samples.set('Samples2', 'Mute', 0.0)
        samples.set('Samples5', 'Mute', 0.0)

        # Vocals
        vocalsKesch.set('meuf_exclu', 'on') # TODO delay
        vocalsNano.set('meuf_exclu', 'on')

        # Keyboards
        jmjKeyboard.set_sound('ZBombarde', boost=True)

    @pedalboard_button(11)
    def goto_stagiaire(self):
        """
        GOTO STAGIAIRE
        """
        engine.set_route('Stagiaire')
        engine.active_route.intro()

    @mk2_button(6, 'yellow')
    def nanogars(self):
        """
        NANO GARS
        """
        vocalsNano.set('gars_exclu', 'on')

    @mk2_button(7, 'yellow')
    def nanomeuf(self):
        """
        NANO MEUF
        """
        vocalsNano.set('meuf_exclu', 'on')

    @mk2_button(8, 'yellow')
    def nanonormo(self):
        """
        NANO NORMO
        """
        vocalsNano.set('normo_exclu', 'on')
