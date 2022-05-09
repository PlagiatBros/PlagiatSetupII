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
        autotunes = ['NanoMeuf', 'NanoNormo', 'NanoGars', 'KeschMeuf', 'KeschNormo', 'KeschGars']
        for at in autotunes:
            #            c     d     e  f     g     a     b
            at.set_notes(1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0)

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
        samples.set('Samples1', 'Gain', 'Mute', 0.0)
        samples.set('Samples2', 'Gain', 'Mute', 0.0)
        samples.set('Samples3', 'Gain', 'Mute', 0.0)
        samples.set('Samples4', 'Gain', 'Mute', 0.0)
        samples.set('Samples5', 'Gain', 'Mute', 0.0)


        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')


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

    @mk2_button(3, 'purple')
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
        samples.set('Samples1', 'Gain', 'Mute', 0.0)
        samples.set('Samples2', 'Gain', 'Mute', 0.0)
        samples.set('Samples3', 'Gain', 'Mute', 0.0)
        samples.set('Samples4', 'Gain', 'Mute', 0.0)
        samples.set('Samples5', 'Gain', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')


        self.start_sequence('couplet1', [
            {}, # smell it quick
            {   # kind of mate
                8: lambda: [
                    # nano: « frisco »
                    outputs.set('Synths', 'Gain', 'Mute', 1),
                    outputs.set('Samples', 'Gain', 'Mute', 1),
                ],
                9.5: lambda: [
                    outputs.set('Synths', 'Gain', 'Mute', 0),
                    outputs.set('Samples', 'Gain', 'Mute', 0),
                ],
            },
            {   # see it's easy
                1: lambda: seq192.select('solo', 'couplet1b_*')
            },
            {   # things accelerating
                1: lambda: seq192.select('solo', 'couplet1_*')
            },
        ], loop=False)


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
        samples.set('Samples1', 'Gain', 'Mute', 0.0)
        samples.set('Samples2', 'Gain', 'Mute', 0.0)
        samples.set('Samples3', 'Gain', 'Mute', 0.0)
        samples.set('Samples4', 'Gain', 'Mute', 0.0)
        samples.set('Samples5', 'Gain', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')


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

        # Samples
        samples.set('Samples1', 'Gain', 'Mute', 0.0)
        samples.set('Samples2', 'Gain', 'Mute', 0.0)
        samples.set('Samples3', 'Gain', 'Mute', 0.0)
        samples.set('Samples4', 'Gain', 'Mute', 0.0)
        samples.set('Samples5', 'Gain', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')


        self.start_sequence('couplet2', [
            {    # me grow i warn ya
                'signature': '39/8',
            },
            {   # boutros boutros boutros
                'signature': '35/8',
                1: lambda: [
                ],
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
