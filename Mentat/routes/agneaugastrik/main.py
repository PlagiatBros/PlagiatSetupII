from ..base import RouteBase, mk2_button, pedalboard_button
from .video import Video
from .light import Light

from modules import *

class AgneauGastrik(Video, Light, RouteBase):

    def activate(self):
        """
        Called when the engine switches to this route.
        """
        transport.set_tempo(150)
        transport.set_cycle('74/8', pattern='X.x.x.x.X.x.x.x.X.x.x.x.Xxx.x.x.X.x.x.xX.x.x.x.X.x.x.x.X.x.xxx.X.x.x.x.X.x')

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

        # Sequences
        seq192.select('solo', 'couplet1_launcher*')

        # Transport
        transport.start()

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')

        # Sequences (Mentat)
        self.start_sequence('refrain', {
            'signature': '8/4',
            1: lambda: vocalsKesch.set('gars_exclu', 'on'),
            6: lambda: vocalsKesch.set('meuf_exclu', 'on'),
        })

    @mk2_button(3, 'purple')
    def couplet_1(self):
        """
        COUPLET 1
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'couplet1_*')

        # Transport
        transport.start()

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')

        # Sequences (Mentat)
        self.start_sequence('refrain', {
            'signature': '8/4',
            1: lambda: vocalsKesch.set('gars_exclu', 'on'),
            6: lambda: vocalsKesch.set('meuf_exclu', 'on'),
        })
