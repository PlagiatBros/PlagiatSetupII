from ..base import *
from .video import Video
from .light import Light

from modules import *

class DDD(Video, Light, RouteBase):
    """
    Dirty Dirty Dirty
    """

    def activate(self):
        """
        Called when the engine switches to this route.
        """

        super().activate()

        transport.set_tempo(80)
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
            'MetP': 'Samples1',
            'Animox': 'Samples3',
            'Ambiance': 'Samples4',
            'BEP': 'Samples5',
        })

    def open_samples(self):
        samples.set('MetP', 'Mute', 0.0)
        samples.set('Animox', 'Mute', 0.0)
        samples.set('Ambiance', 'Mute', 0.0)
        samples.set('BEP', 'Mute', 0.0)


        samplesFX3Reverb.set('Ambiance', 'Gain', -15.0)
        samplesFX3Reverb.set('Animox', 'Gain', -18.0)
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

        # Synths
        synths.set('EasyClassical', 'Amp', 'Gain', 0.9)
        # synthsFX2Delay.set('EasyClassical', 'Gain', -14.0)
        # synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)
        # synthsFX2Delay.set('SynthsFX2Delay', 'GxMultiBandDelay', 'multiplier', 4)
        # synthsFX2Delay.set('SynthsFX2Delay', 'GxMultiBandDelay', 'feedback', 0.2)
        synthsFX3Delay.set('EasyClassical', 'Gain', -10.0)
        synthsFX3Delay.set('SynthsFX3Delay', 'Mute', 0.0)
        synthsFX3Delay.set('SynthsFX3Delay', 'Invada%20Delay%20Munge%20(mono%20in)', 'Delay%201', 0.203)
        synthsFX3Delay.set('SynthsFX3Delay', 'Invada%20Delay%20Munge%20(mono%20in)', 'Feedback%201', 33)
        synthsFX3Delay.set('SynthsFX3Delay', 'Invada%20Delay%20Munge%20(mono%20in)', 'Delay%202', 0.347)
        synthsFX3Delay.set('SynthsFX3Delay', 'Invada%20Delay%20Munge%20(mono%20in)', 'Feedback%202', 29)

        # BassSynths
        bassSynths.set('BassTrap2', 'Amp', 'Gain', 1)
        bassSynths.set('BassBarkline', 'Amp', 'Gain', 0.9)
        bassSynths.set('BassBoom', 'Amp', 'Gain', 0.8)


        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        # Keyboard
        jmjKeyboard.set_sound('ZTrumpets', boost=True)



    @mk2_button(2)
    def couplet1_1(self):
        """
        COUPLET 1-1 (Ass tonishing)
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'couplet1*')

        # Transport
        transport.start()

        # Samples
        self.open_samples()

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        # Keyboard
        jmjKeyboard.set_sound('ZTrumpets', boost=True)


        self.start_scene('sequences/couplet_1', lambda: [
            self.wait(4*4, 'beats'),
            # der believe I'm a
            seq192.select('off', 'couplet1_sf_orchestraHit'),
            self.wait(4*4, 'beats'),
            # But I won't die trying
            seq192.select('on', 'couplet1_sf_orchestraHit'),
            seq192.select('on', 'upcouplet1_*'),
            self.wait(4*4, 'beats'),
            # mula mula
            seq192.select('solo', 'intro_*')
        ])


    @pedalboard_button(3)
    def prerefrain(self):
        """
        PREREFRAIN MariLouiz
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'prerefrain_*')

        # Transport
        transport.start()

        # Samples
        self.open_samples()
        samplesFX3Reverb.set('MetP', 'Gain', -18.0)

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('meuf_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        # Keyboard
        jmjKeyboard.set_sound('ZTrumpets', boost=True)


    @pedalboard_button(4)
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
        samplesFX1Delay.set('Samples1', 'Gain', -18.0)
        samplesFX1Delay.set('SamplesFX1Delay', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('meuf_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        # Keyboard
        jmjKeyboard.set_sound('ZTrumpets', boost=True)

        # Bass FX
        bassFX.set('distohi', 'on')


    @pedalboard_button(5)
    def couplet2_1(self):
        """
        COUPLET 2_1 (you tell me)
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'couplet2-1_*')

        # Transport
        transport.start()

        # Samples
        self.open_samples()

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        # Keyboard
        jmjKeyboard.set_sound('ZTrumpets', boost=True)


    @mk2_button(3)
    def couplet2_2(self):
        """
        COUPLET 2_2 (chuis un @male deconstruit)
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'couplet2-2_*')

        # Transport
        transport.start()

        # Samples
        self.open_samples()

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        # Keyboard
        jmjKeyboard.set_sound('ZTrumpets', boost=True)

        # rhode fade in
        # synths.set('ZNotSoRhodes', 'Amp', 'Gain', 0)
        synths.set('MajorVocals', 'Amp', 'Gain', 0.5)

        synthsFX1Reverb.set('Rhodes', 'Gain', -10.0)
        synthsFX1Reverb.set('SynthsFX1Reverb', 'Mute', 0.0)


        synthsFX3Delay.set('MajorVocals', 'Gain', -10.0)
        synthsFX3Delay.set('SynthsFX3Delay', 'Mute', 0.0)
        synthsFX3Delay.set('SynthsFX3Delay', 'Invada%20Delay%20Munge%20(mono%20in)', 'Delay%201', 0.203)
        synthsFX3Delay.set('SynthsFX3Delay', 'Invada%20Delay%20Munge%20(mono%20in)', 'Feedback%201', 33)
        synthsFX3Delay.set('SynthsFX3Delay', 'Invada%20Delay%20Munge%20(mono%20in)', 'Delay%202', 0.347)
        synthsFX3Delay.set('SynthsFX3Delay', 'Invada%20Delay%20Munge%20(mono%20in)', 'Feedback%202', 29)

        # self.start_scene('sequences/rhode_fadein', lambda: [
        #     self.wait(2*4, 'beats'),
        #     synths.animate('ZNotSoRhodes', 'Amp', 'Gain', 0, 1, 2*4, 'beats')
        # ])

    @pedalboard_button(6)
    def couplet2_3(self):
        """
        COUPLET 2_3 (let's go back)
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'couplet2-3_*')

        # Transport
        transport.start()

        # Samples
        self.open_samples()

        samplesFX1Delay.set('BEP', 'Gain', -12.0)
        samplesFX1Delay.set('SamplesFX1Delay', 'Mute', 0.0)
        samplesFX1Delay.set('SamplesFX1Delay', 'GxMultiBandDelay', 'multiplier', 4)
        samplesFX1Delay.set('SamplesFX1Delay', 'GxMultiBandDelay', 'DELAY3', 161)
        samplesFX1Delay.set('SamplesFX1Delay', 'GxMultiBandDelay', 'FEEDBACK3', 96)

        # Synths
        synths.set('Z8bits', 'Amp', 'Gain', 0.5)

        synthsFX4TapeDelay.set('Z8bits', 'Gain', -18)
        synthsFX4TapeDelay.set('SynthsFX4TapeDelay', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        # Keyboard
        jmjKeyboard.set_sound('ZTrumpets', boost=True)

        # Séquences
        self.start_sequence('couplet2_3_tapedelay', [
            { # bar 1
                1: lambda: synthsFX4TapeDelay.animate('SynthsFX4TapeDelay', 'Tape%20Delay%20Simulation', 'Tape%20speed%20(inches/sec%2C%201=normal)', None, 1, 0.1, 's')
            },
            {}, {}, {}, {}, {}, {},
            { # bar 8
                1: lambda: synthsFX4TapeDelay.animate('SynthsFX4TapeDelay', 'Tape%20Delay%20Simulation', 'Tape%20speed%20(inches/sec%2C%201=normal)', 1, 0.2, 4, 'b')
            }
        ])

    @pedalboard_button(7)
    def couplet2_freeze(self):
        self.pause_loopers()
        self.reset()

        # Séquences
        seq192.select('solo', 'couplet2-break_zLow_dubstep')
        seq192.select('on', 'couplet2-3_zHi_8bits')

        # Transport
        transport.start()

        self.start_scene('freeze', lambda: [
            postprocess.animate_pitch('*', 1, 0.2, 6, 'beats'),
            synthsFX4TapeDelay.animate('SynthsFX4TapeDelay', 'Tape%20Delay%20Simulation', 'Tape%20speed%20(inches/sec%2C%201=normal)', 1, 0.2, 4, 'b'),
            postprocess.set_filter('Synths', 600),
            self.wait(7, 'beats'),
            postprocess.animate_pitch('*', None, 1, 1, 'beats'),
            postprocess.animate_filter('Synths', None, 20000, 0.75, 'beats'),
            self.wait_next_cycle(),
            self.couplet2_3()
        ])
