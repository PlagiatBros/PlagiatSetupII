from ..base import *
from .video import Video
from .light import Light

from modules import *

class AintInTheWay(Video, Light, RouteBase):
    """
    Ain't In The Way
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
        # self.set_samples_aliases({
        #     'GuitarCrunch': 'Samples1',
        #     'GuitarNatural': 'Samples2',
        #     'GuitarChorus': 'Samples3',
        #     'Trumpets': 'Samples4',
        # })

    def open_samples(self):
        pass
        # samples.set('GuitarCrunch', 'Mute', 0.0)
        # samples.set('GuitarNatural', 'Mute', 0.0)
        # samples.set('GuitarChorus', 'Mute', 0.0)
        # samples.set('Trumpets', 'Mute', 0.0)
        # samplesFX3Reverb.set('Trumpets', 'Gain', -10.0)
        # samplesFX3Reverb.set('SamplesFX3Reverb', 'Mute', 0.0)


    @pedalboard_button(1)
    @mk2_button(1, 'blue')
    def stop(self):
        """
        STOP
        """
        self.pause_loopers()
        transport.stop()

    @pedalboard_button(2)
    @mk2_button(2, 'purple')
    def intro(self):
        """
        INTRO
        """
        self.pause_loopers()
        self.reset()


        # Transport
        transport.start()

        # Séquences
        seq192.select('solo', 'intro_*')

    @pedalboard_button(3)
    @mk2_button(3, 'purple')
    def prerefrain(self):
        """
        PRÉ-REFRAIN
        """
        self.pause_loopers()
        self.reset()


        # Transport
        transport.start()

        # Séquences
        seq192.select('solo', 'prerefrain_*')

        self.start_scene('breakrefrain', lambda: [
            self.wait(3*4, 'beat'),
            seq192.select('on', 'break_prerefrain_*')
        ])

    @pedalboard_button(4)
    @mk2_button(4, 'purple')
    def refrain(self):
        """
        REFRAIN
        """
        self.pause_loopers()
        self.reset()


        # Transport
        transport.start()

        # Séquences
        seq192.select('solo', 'refrain_*')
