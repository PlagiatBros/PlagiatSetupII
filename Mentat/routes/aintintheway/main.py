from ..base import *
from .video import Video
from .light import Light

from modules import *

class AintInTheWay(Video, Light, RouteBase):
    """
    Ain't In The Way
    """
    def set_notes(self, beachboys=False):
        if beachboys:
            notes.set_notes(1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0)
        else:
            notes.set_notes(1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0)


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
        microtonality.set_tuning(0, 0, 0, 0.35, 0, 0, 0, 0, 0, 0, 0.35, 0)

        # Autotuner Notes
        self.set_notes()

        # Mk2
        mk2Control.set_mode('cut_samples', 'cut_synths')

        # Sample
        self.set_samples_aliases({
            'Piano': 'Samples1',
        })

    def open_samples(self):
        samples.set('Piano', 'Mute', 0.0)


    @pedalboard_button(1)
    @mk2_button(1, 'blue')
    def stop(self):
        """
        STOP
        """
        self.pause_loopers()
        transport.stop()

    @pedalboard_button(2)
    @mk2_button(2, 'cyan')
    def intro(self):
        """
        INTRO
        """
        self.set_notes()

        self.pause_loopers()
        self.reset()

        # Séquences
        seq192.select('solo', 'intro_*')

        # Transport
        transport.set_tempo(120)
        transport.start()

        # Samples
        self.open_samples()

        # Vocals
        vocalsKesch.set('normo_exclu', 'on')
        vocalsNano.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        inputs.set('keschmic', 'dynamic')


    @pedalboard_button(3)
    @mk2_button(3, 'purple')
    def refrain1(self):
        """
        REFRAIN 1 (run bass 2e cycle)
        """
        self.set_notes()


        self.pause_loopers()
        self.reset()

        # Séquences
        seq192.select('solo', 'prerefrain_*')

        # Samples
        self.open_samples()

        # Vocals
        vocalsKesch.set('normo_exclu', 'on')
        vocalsNano.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        inputs.set('keschmic', 'dynamic')

        # Transport
        transport.set_tempo(120)
        transport.start()

        # Séquences
        self.start_scene('sequences/breakrefrain', lambda: [
            self.wait(7*4, 'beat'),
            seq192.select('on', 'break_prerefrain_*'),
            self.wait(4, 'beat'),
            seq192.select('solo', 'refrain_*')
        ])


    @pedalboard_button(5)
    @mk2_button(4, 'cyan')
    def couplet_part1(self):
        """
        COUPLET PART 1 & COUPLET 2
        """
        self.pause_loopers()
        self.reset()

        # Samples
        self.open_samples()

        # Séquences
        seq192.select('solo', 'couplet_part1_*')

        # Transport
        transport.set_tempo(120)
        transport.start()

        # jmjKeyboard
        jmjKeyboard.set_sound('ZTrumpets', lead=False)

        # Vocals
        vocalsKesch.set('normo_exclu', 'on')
        vocalsNano.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        inputs.set('keschmic', 'dynamic')

    @pedalboard_button(6)
    @mk2_button(5, 'cyan')
    def couplet_part2(self):
        """
        COUPLET PART 2
        """
        self.pause_loopers()
        self.reset()

        # Séquences
        seq192.select('solo', 'couplet_part2_*')

        # Samples
        self.open_samples()

        # Vocals
        vocalsKesch.set('normo_exclu', 'on')
        vocalsNano.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        inputs.set('keschmic', 'dynamic')

        # Transport
        transport.set_tempo(180)
        transport.start()

        # Keyboard
        jmjKeyboard.set_sound('ZTrumpets', lead=True)

    @mk2_button(7)
    @pedalboard_button(7)
    def theme(self):
        """
        THÈME
        """
        self.pause_loopers()
        self.reset()

        self.set_notes(True)

        # Séquences
        seq192.select('solo', 'theme_*')

        # Samples
        self.open_samples()

        # Synths
        synths.set('Trap', 'Amp', 'Gain', 0.25)

        synthsFX2Delay.set('Trap', 'Gain', -10.0)
        synthsFX2Delay.set('DubstepHorn', 'Gain', -6.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)

        synthsFX3Delay.set('Trap', 'Gain', -10.0)
        synthsFX3Delay.set('SynthsFX3Delay', 'Mute', 0.0)

        # Keyboard
        jmjKeyboard.set_sound('ZTrumpets', lead=True)

        # Transport
        transport.set_tempo(180)
        transport.start()

        # synthsFX3Delay.set('SynthsFX3Delay', 'Invada%20Delay%20Munge%20(mono%20in)', 'Delay%201', 180*3/2)
        # synthsFX3Delay.set('SynthsFX3Delay', 'Invada%20Delay%20Munge%20(mono%20in)', 'Delay%202', 180*3/2)

        # Vocals
        vocalsKesch.set('normo_exclu', 'on')
        vocalsNano.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        inputs.set('keschmic', 'static')

    @pedalboard_button(4)
    @mk2_button(6, 'purple')
    def refrain2(self):
        """
        REFRAIN 2 (avec bass)
        """
        self.pause_loopers()
        self.reset()

        # Séquences
        seq192.select('solo', 'refrain_*')

        # Transport
        transport.set_tempo(120)
        transport.start()

        # Samples
        self.open_samples()

        # Vocals
        vocalsKesch.set('normo_exclu', 'on')
        vocalsNano.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        inputs.set('keschmic', 'dynamic')

    @pedalboard_button(8)
    def salsa(self):
        """
        SALSA
        """
        self.pause_loopers()
        self.reset()

        seq192.select('solo', 'dummy')

        # Séquences
        self.start_scene('salsa', lambda: [
            self.wait(8*4, 'beat'),
            seq192.select('solo', 'couplet2_*')
            ]
        )

        # Samples
        self.open_samples()

        # Transport
        transport.set_tempo(180)
        transport.start()

        # jmjKeyboard
        jmjKeyboard.set_sound('SteelDrum', lead=True)

        # Vocals
        vocalsKesch.set('normo_exclu', 'on')
        vocalsNano.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        inputs.set('keschmic', 'dynamic')

    @pedalboard_button(9)
    def savoir_aimer(self):
        """
        SAVOIR AIMÉ
        """
        self.pause_loopers()
        self.reset()

        seq192.select('solo', 'dummy')


        # Samples
        self.open_samples()


        # Transport
        transport.set_tempo(120)
        transport.start()


        # jmjKeyboard
        jmjKeyboard.set_sound('SteelDrum', lead=False)

        inputs.set('keschmic', 'dynamic')
