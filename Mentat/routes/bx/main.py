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
            'Samples1': 'GuitarCrunch',
            'Samples2': 'GuitarNatural',
            'Samples3': 'GuitarChorus',
            'Samples4': 'Trumpets',
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

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')

        # Keyboard
        jmjKeyboard.set_sound('ZTrumpets', boost=True)

        synthsFX2Delay.set('Trap', 'Gain', -14.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)

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
