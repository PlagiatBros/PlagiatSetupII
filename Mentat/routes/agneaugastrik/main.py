from ..base import RouteBase, mk2_button, pedalboard_button
from .video import Video
from .light import Light

from modules import *

class AgneauGastrik(Video, Light, RouteBase):

    klick_pattern =          'X.x.x.x.X.x.x.x.X.x.x.x.Xxx.x.x.X.x.x.xX.x.x.x.X.x.x.x.X.x.xxx.X.x.x.x.X.x'
    klick_pattern_reversed = 'X.x.x.x.X.x.x.x.X.x.xxx.X.x.x.x.X.xX.x.x.x.X.x.x.x.X.x.x.x.Xxx.x.x.X.x.x.x'

    def activate(self):
        """
        Called when the engine switches to this route.
        """

        super().activate()

        transport.set_tempo(150)
        transport.set_cycle('74/8', pattern=self.klick_pattern)

        # Setups, banks...
        seq192.set_screenset(self.name)
        prodSampler.set_kit(self.name)

        # Microtonality
        microtonality.enable()
        microtonality.set_tuning(0, 0, 0, 0, 0, 0.35, 0, 0, 0.35, 0, 0.35, 0)

        # Autotuner Notes
        #               c     d     e  f     g     a     b
        notes.set_notes(1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0)

        # Mk2
        mk2Control.set_mode('wobble')

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

        # Transport
        transport.stop()

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')

    @pedalboard_button(3)
    @pedalboard_button(10)
    def pre_couplet(self):
        """
        PRE COUPLET
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'precouplet_*')

        # Transport
        transport.start()

        # Samples
        samples.set('Samples1', 'Mute', 0.0)
        samples.set('Samples2', 'Mute', 0.0)
        samples.set('Samples3', 'Mute', 0.0)
        samples.set('Samples4', 'Mute', 0.0)
        samples.set('Samples5', 'Mute', 0.0)

        samplesFX2Delay.set('Samples3', 'Gain', -3.0)
        samplesFX2Delay.set('SamplesFX2Delay', 'Mute', 0.0)
        samplesFX5TapeDelay.set('Samples4', 'Gain', -4.0)
        samplesFX5TapeDelay.set('SamplesFX5TapeDelay', 'Mute', 0.0)

        # Synths
        synths.set('ZTrumpets', 'Pan', -0.7)
        synths.set('ZDiploLike', 'Pan', 0.7)
        synthsFX2Delay.set('ZDiploLike', 'Gain', -6.0)
        synthsFX2Delay.set('DubstepHorn', 'Gain', -3.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')

        # Sequences (Mentat)
        self.start_sequence('Yep!', [
            {'signature': '37/4', # bar 1
            18:  lambda: samplesFX5TapeDelay.set('SamplesFX5TapeDelay', 'Tape%20Delay%20Simulation', 'Tape%20speed%20(inches/sec%2C%201=normal)', 0.9),
            19.1: lambda: samplesFX5TapeDelay.animate('SamplesFX5TapeDelay', 'Tape%20Delay%20Simulation', 'Tape%20speed%20(inches/sec%2C%201=normal)', 0.9, 0.5, 3, easing='exponential'),
            35:  lambda: samplesFX5TapeDelay.set('SamplesFX5TapeDelay', 'Tape%20Delay%20Simulation', 'Tape%20speed%20(inches/sec%2C%201=normal)', 1.0),
            37.5: lambda: samplesFX5TapeDelay.animate('SamplesFX5TapeDelay', 'Tape%20Delay%20Simulation', 'Tape%20speed%20(inches/sec%2C%201=normal)', 1.0, 1.5, 3, easing='exponential')
            }
        ], loop=True)
        self.start_sequence('SynthsPan', [
            {'signature': '43/4', # bar 1
            1: lambda: [
                synths.animate('ZTrumpets', 'Pan', -0.7, 0.7, 43),
                synths.animate('ZDiploLike', 'Pan', 0.7, -0.7, 43)
                ]
            },
            {'signature': '43/4', # bar 1
            1: lambda: [
                synths.animate('ZTrumpets', 'Pan', 0.7, -0.7, 43),
                synths.animate('ZDiploLike', 'Pan', -0.7, 0.7, 43)
                ]
            }
        ], loop=True)


    @mk2_button(2, 'purple')
    def couplet_launcher(self):
        """
        COUPLET 1 LAUNCHER
        """
        self.pause_loopers()
        self.reset()

        transport.set_cycle('34/8')

        # Sequences
        seq192.select('solo', 'launcher_*')

        # Transport
        transport.start()

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')

        # Scene
        self.start_sequence('couplet_launcher', [
            {},
            {
                1: lambda: self.start_scene('launch_couplet1', lambda: self.couplet_1())
            }
        ])

    @mk2_button(3, 'cyan')
    def couplet_1(self):
        """
        COUPLET 1
        """
        self.pause_loopers()
        self.reset()

        transport.set_cycle('74/8', self.klick_pattern_reversed)

        # Sequences
        seq192.select('solo', 'couplet1_*')

        # Transport
        transport.start()

        # Samples
        samples.set('Samples1', 'Mute', 0.0)
        samples.set('Samples2', 'Mute', 0.0)
        samples.set('Samples3', 'Mute', 0.0)
        samples.set('Samples4', 'Mute', 0.0)
        samples.set('Samples5', 'Mute', 0.0)
        samplesFX2Delay.set('Samples3', 'Gain', -3.0)
        samplesFX2Delay.set('SamplesFX2Delay', 'Mute', 0.0)
        samplesFX5TapeDelay.set('Samples4', 'Gain', -4.0)
        samplesFX5TapeDelay.set('SamplesFX5TapeDelay', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')

        # Sequences (Mentat)
        self.start_sequence('couplet1', [
            {}, # smell it quick
            {   # kind of mate
                8: lambda: [
                    # nano: « frisco »
                    self.engine.set('cut_samples', 'on'),
                    self.engine.set('cut_synths', 'on'),
                ],
                9.5: lambda: [
                    self.engine.set('cut_samples', 'off'),
                    self.engine.set('cut_synths', 'off'),
                ],
            },
            {   # see it's easy
                1: lambda: seq192.select('solo', 'couplet1b_*')
            },
            {   # things accelerating
                1: lambda: seq192.select('solo', 'couplet1_*')
            },
        ], loop=False)
        self.start_sequence('Yep!', [
            {'signature': '37/4', # bar 1
            18:  lambda: samplesFX5TapeDelay.set('SamplesFX5TapeDelay', 'Tape%20Delay%20Simulation', 'Tape%20speed%20(inches/sec%2C%201=normal)', 0.9),
            19.1: lambda: samplesFX5TapeDelay.animate('SamplesFX5TapeDelay', 'Tape%20Delay%20Simulation', 'Tape%20speed%20(inches/sec%2C%201=normal)', 0.9, 0.5, 3, easing='exponential'),
            35:  lambda: samplesFX5TapeDelay.set('SamplesFX5TapeDelay', 'Tape%20Delay%20Simulation', 'Tape%20speed%20(inches/sec%2C%201=normal)', 1.0),
            37.5: lambda: samplesFX5TapeDelay.animate('SamplesFX5TapeDelay', 'Tape%20Delay%20Simulation', 'Tape%20speed%20(inches/sec%2C%201=normal)', 1.0, 1.5, 3, easing='exponential')
            }
        ], loop=True)


    @mk2_button(4, 'purple')
    def refrain(self):
        """
        REFRAIN
        """

        self.pause_loopers()
        self.reset()

        transport.set_cycle('74/8', self.klick_pattern)

        # Sequences
        seq192.select('solo', 'refrain_*')

        # Transport
        transport.start()

        # Samples
        samples.set('Samples1', 'Mute', 0.0)
        samples.set('Samples2', 'Mute', 0.0)
        samples.set('Samples3', 'Mute', 0.0)
        samples.set('Samples4', 'Mute', 0.0)
        samples.set('Samples5', 'Mute', 0.0)
        samplesFX5TapeDelay.set('Samples4', 'Gain', -12.0)
        samplesFX5TapeDelay.set('SamplesFX5TapeDelay', 'Mute', 0.0)

        # Synths
        synths.set('ZTrumpets', 'Pan', -0.7)
        synths.set('ZDiploLike', 'Pan', 0.7)
        synthsFX2Delay.set('ZDiploLikeWide', 'Gain', -6.0)
        synthsFX2Delay.set('DubstepHorn', 'Gain', -3.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)


        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsNanoFX2Delay.set('active', 'on')
        vocalsKesch.set('gars_exclu', 'on')
        vocalsKeschFX2Delay.set('active', 'on')

        # Sequences Mentat
        self.start_sequence('Yep!', [
            {'signature': '37/4', # bar 1
            18:  lambda: samplesFX5TapeDelay.animate('SamplesFX5TapeDelay', 'Tape%20Delay%20Simulation', 'Tape%20speed%20(inches/sec%2C%201=normal)', None, 0.9, 1),
            19.1: lambda: samplesFX5TapeDelay.animate('SamplesFX5TapeDelay', 'Tape%20Delay%20Simulation', 'Tape%20speed%20(inches/sec%2C%201=normal)', 0.9, 0.5, 3, easing='exponential'),
            35:  lambda: samplesFX5TapeDelay.animate('SamplesFX5TapeDelay', 'Tape%20Delay%20Simulation', 'Tape%20speed%20(inches/sec%2C%201=normal)', None, 1.0, 1),
            37.5: lambda: samplesFX5TapeDelay.animate('SamplesFX5TapeDelay', 'Tape%20Delay%20Simulation', 'Tape%20speed%20(inches/sec%2C%201=normal)', 1.0, 1.5, 3, easing='exponential')
            }
        ], loop=True)


    @pedalboard_button(4)
    def couplet_2(self):
        """
        COUPLET 2
        """
        self.pause_loopers()
        self.reset()

        transport.set_cycle('74/8', self.klick_pattern)

        # Sequences
        seq192.select('solo', 'couplet2_*')

        # Transport
        transport.start()

        # Loopers
        looper.trigger(0)

        ### TODO Filtrage Synths

        # Samples
        samples.set('Samples1', 'Mute', 0.0)
        samples.set('Samples2', 'Mute', 0.0)
        samples.set('Samples3', 'Mute', 0.0)
        samples.set('Samples4', 'Mute', 0.0)
        samples.set('Samples5', 'Mute', 0.0)
        samplesFX5TapeDelay.set('Samples4', 'Gain', -12.0)
        samplesFX5TapeDelay.set('SamplesFX5TapeDelay', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')

        # Sequences (Mentat)
        self.start_sequence('couplet2', [
            {    # me grow i warn ya
                'signature': '39/8',
            },
            {   # boutros boutros boutros
                'signature': '35/8',
                1: lambda: postprocess.trap_cut(4),
            },
            {    # go get
                'signature': '39/8',
            },
            {   # augustus ceasar
                'signature': '35/8',
                1: lambda: [
                ],
            },
            {   # one, take butter
                'signature': '16/4',
                16.5: lambda: self.start_scene('stop', lambda: self.stop())
            },
        ], loop=False)
        self.start_sequence('Yep!', [
            {'signature': '37/4', # bar 1
            18:  lambda: samplesFX5TapeDelay.animate('SamplesFX5TapeDelay', 'Tape%20Delay%20Simulation', 'Tape%20speed%20(inches/sec%2C%201=normal)', None, 0.9, 1),
            19.1: lambda: samplesFX5TapeDelay.animate('SamplesFX5TapeDelay', 'Tape%20Delay%20Simulation', 'Tape%20speed%20(inches/sec%2C%201=normal)', 0.9, 0.5, 3, easing='exponential'),
            35:  lambda: samplesFX5TapeDelay.animate('SamplesFX5TapeDelay', 'Tape%20Delay%20Simulation', 'Tape%20speed%20(inches/sec%2C%201=normal)', None, 1.0, 1),
            37.5: lambda: samplesFX5TapeDelay.animate('SamplesFX5TapeDelay', 'Tape%20Delay%20Simulation', 'Tape%20speed%20(inches/sec%2C%201=normal)', 1.0, 1.5, 3, easing='exponential')
            }
        ], loop=True)
