from ..base import RouteBase, mk2_button, pedalboard_button
from .video import Video
from .light import Light

from modules import *

class Mcob(Video, Light, RouteBase):

    def __init__(self):

        super().__init__(name='Mcob')

    def activate(self):
        """
        Called when the engine switches to this route.
        """
        transport.set_tempo(120)
        transport.set_cycle('4/4')

        # Setups, banks...
        seq192.set_screenset(self.name)
        prodSampler.set_kit(self.name)

        # Microtonality
        microtonality.enable()
        microtonality.set_tuning(0, 0, 0, 0, 0, 0.35, 0, 0, 0.35, 0, 0.35, 0)


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
        seq192.select('solo', part + '_*')

        # Transport
        transport.start()

        # Samples
        samplesFX6Scape.set('Samples2', 'Gain', 'Gain', -5.0)
        samplesFX6Scape.set('SamplesFX6Scape', 'Gain', 'Mute', 0.0)

        samples.set('Samples1', 'Gain', 'Mute', 0.0)
        samples.set('Samples2', 'Gain', 'Mute', 0.0)
        samples.set('Samples5', 'Gain', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('meuf_exclu', 'on')

        # Keyboard
        jmjKeyboard.set_sound('LowZDupieux')

    @mk2_button(2, 'purple')
    def refrain(self):
        """
        REFRAIN
        """

        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', part + '_*')

        # Transport
        transport.start()

        # Samples
        samplesFX6Scape.set('Samples2', 'Gain', 'Gain', -5.0)
        samplesFX6Scape.set('SamplesFX6Scape', 'Gain', 'Mute', 0.0)

        samples.set('Samples1', 'Gain', 'Mute', 0.0)
        samples.set('Samples2', 'Gain', 'Mute', 0.0)
        samples.set('Samples3', 'Gain', 'Mute', 0.0)
        samples.set('Samples5', 'Gain', 'Mute', 0.0)

        # Bass
        bassfx.set('distohi', 'on')

        # Vocals
        vocalsNano.set('meuf_exclu', 'on')
        vocalsKesch.set('meuf_exclu', 'on')

        # Keyboards
        jmjKeyboard.set_sound('LowZDubstep')

    @pedalboard_button(3)
    def couplet1_1(self):
        """
        COUPLET 1 - Trap "Look"
        """

        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', part + '_*')

        # Transport
        transport.start()

        # Samples
        samplesFX6Scape.set('Samples2', 'Gain', 'Gain', -10.0) # attention - 10 et - 5 dans setup précédent
        samplesFX6Scape.set('SamplesFX6Scape', 'Gain', 'Mute', 0.0)

        samplesFX2Delay.set('Samples2', 'Gain', 'Gain', -9.0)
        samplesFX2Delay.set('SamplesFX2Delay', 'Gain', 'Mute', 0.0)

        samples.set('Samples1', 'Gain', 'Mute', 0.0)
        samples.set('Samples2', 'Gain', 'Mute', 0.0)
        samples.set('Samples4', 'Gain', 'Mute', 0.0)


        # Vocals
        vocalsNano.set('meuf_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')

        vocalsNanoFX3TrapVerb.set('NanoMeuf', 'Gain', 'Gain', 0.0)
        vocalsNanoFX3TrapVerb.set('VocalsNanoFX3TrapVerb', 'Gain', 'Mute', 0.0)

    @pedalboard_button(4)
    def couplet1_2(self):
        """
        COUPLET 1 - Prince 2 Pac
        """

        # Sequences
        seq192.select('solo', part + '_*')

        # Samples
        samplesFX6Scape.set('Samples2', 'Gain', 'Gain', -10.0) # attention - 10 et - 5 dans setup précédent
        samplesFX6Scape.set('SamplesFX6Scape', 'Gain', 'Mute', 0.0)

        samplesFX2Delay.set('Samples2', 'Gain', 'Gain', -9.0)
        samplesFX2Delay.set('SamplesFX2Delay', 'Gain', 'Mute', 0.0)

        samples.set('Samples1', 'Gain', 'Mute', 0.0)
        samples.set('Samples2', 'Gain', 'Mute', 0.0)
        samples.set('Samples4', 'Gain', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('meuf_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')

        # Sequences (Mentat)
        self.start_scene('prince2pac_launcher', lambda: [
            self.wait_next_cycle(),
            self.start_sequence('prince2pac_vocals_a', self.sequences['prince2pac_vocals_a'], loop=False),
            self.start_sequence('prince2pac_basses_a', self.sequences['prince2pac_basses_a'], loop=False),
        ])

    @mk2_button(3, 'purple')
    def couplet1_3(self):
        """
        COUPLET 1 - Shaft
        """

        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', part + '_*')

        # Vocals
        vocalsNano.set('gars', 'on')
        vocalsNano.set('normo', 'on')
        vocalsKesch.set('gars_exclu', 'on')

        # Sequences (Mentat)
        self.start_sequence('prince2pac_vocals_b', self.sequences['prince2pac_vocals_b'], loop=False)
        self.start_sequence('prince2pac_basses_b', self.sequences['prince2pac_basses_b'], loop=False)


    sequences = {
        """
        Sequences for self.start_sequences
        """

        'prince2pac_vocals_a': [
            {   # bar 1
                'signature': '4/4',
                1: lambda: vocalsKesch.set('gars_exclu', 'on')
            },
            {}, {}, {}, {}, {}, # bars 2, 3, 4, 5, 6,
            {   # bar 7
                1: lambda: [vocalsKesch.set('gars', 'on'), vocalsKesch.set('normo', 'on')]
            },
            {}, {}, # bars 8, 9
            {   # bar 10
                1: lambda: vocalsKesch.set('normo_exclu', 'on')
            },
            {}, {}, # bars 11, 12
            {   # bar 13
                2: lambda: vocalsKesch.set('meuf', 'on'),
                3: lambda: vocalsKesch.set('meuf', 'off'),
                4: lambda: vocalsKesch.set('meuf', 'on'),
            },
            {   # bar 14
                1: lambda: vocalsKesch.set('meuf', 'off'),
            },
            {}, {}, {}, # bars 15, 16, 17
        ],

        'prince2pac_basses_a': [
            {'signature': '%s/4' % 15*4},
            {
                'signature': '4/4',
                4: lambda: postprocess.animate_pitch('*', 1, 0.25, 0.5, 'beat'),
                4.95: lambda: postprocess.animate_pitch('*', 0.25, 1, 0.05, 'beat')
            },
            {
                1: lambda: seq192.select('off', 'prince2pac_basssynth')
                # Préciser le nom de séquence # On coupe le bass synth et allez hop bass/batt
            }
        ],

        'prince2pac_vocals_b': [
            {   # bar 1
                'signature': '4/4',
                1: lambda: [vocalsKesch.set('meuf_exclu', 'on'), vocalsKesch.set('normo', 'on')],
            },
            {  # bar 2
                3 + 2/3: lambda: vocalsKesch.set('gars_exclu', 'on'),
            },
            {}, # bar 3
            {}, # bar 4
            {   # bar 5
                1: lambda: vocalsKesch.set('gars_exclu', 'on')
            },
            {}, # bar 6
            {}, # bar 7
            {   # bar 8
                4 + 2/3: lambda: vocalsKesch.set('normo', 'on')
            },
            {}, # bar 9
            {}, # bar 10
            {   # bar 11
                1: lambda: vocalsKesch.set('normo_exclu', 'on'),
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
            },
            {   # bar 15
                2.5: lambda: vocalsKesch.set('meuf', 'off'),
                3: lambda: vocalsKesch.set('meuf', 'on')
            },
            {},  # bar 16
            {},  # bar 17
        ],

        'prince2pac_basses_b': {
            # todo
        }

    }
