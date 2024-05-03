from ..base import *
from .video import Video
from .light import Light

from modules import *

class QueenCloclo(Video, Light, RouteBase):
    """
    Queen Cloclo
    """
    scale=[1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0]
    def activate(self):
        """
        Called when the engine switches to this route.
        """

        super().activate()

        transport.set_tempo(110)
        transport.set_cycle('4/4')

        # Setups, banks...
        seq192.set_screenset(self.name)
        prodSampler.set_kit(self.name)

        # Microtonality
        # microtonality.disable()
        microtonality.disable()
        # microtonality.set_tuning(0, -0.35, 0, 0, 0, 0.35, 0, 0, 0, 0, 0.35, 0)

        # Autotuner Notes
        #               c     d     e  f     g     a     b
        notes.set_notes(*self.scale)

        # Mk2
        mk2Control.set_mode('cut_basssynths')
        chasttKeyboard.set_sound('LowCTrap1')

        # Sample
        self.set_samples_aliases({
            'KJ': 'Samples1',
            'Violons': 'Samples2',
        #     'GuitarChorus': 'Samples3',
        #     'Trumpets': 'Samples4',
        })

    def open_samples(self):
        samples.set('KJ', 'Mute', 0.0)
        samples.set('Violons', 'Mute', 0.0)
        # samples.set('GuitarChorus', 'Mute', 0.0)
        # samples.set('Trumpets', 'Mute', 0.0)
        samplesFX3Reverb.set('Violons', 'Gain', -10.0)
        samplesFX3Reverb.set('SamplesFX3Reverb', 'Mute', 0.0)
        samplesFX5TapeDelay.set('Violons', 'Gain', -12.0)
        samplesFX5TapeDelay.set('KJ', 'Gain', -12.0)
        samplesFX5TapeDelay.set('SamplesFX5TapeDelay', 'Mute', 0.0)



    @pedalboard_button(1)
    @mk2_button(1, 'blue')
    def stop(self):
        """
        STOP
        """
        self.pause_loopers()
        transport.stop()

    @pedalboard_button(2)
    def preintro(self):
        """
        PRE-INTRO
        """
        self.pause_loopers()
        self.reset()
        notes.set_notes(*self.scale)

        # Séquences
        seq192.select('solo', 'couplet_zHi_trumpets')

        # Transport
        transport.start()

        # Synths
        jmjKeyboard.set_sound('ZTrumpets', lead=True)

        # Vocals
        vocalsKesch.set('meuf_exclu', 'on')
        vocalsNano.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        inputs.set('keschmic', 'static')

    @mk2_button(2, 'cyan')
    def intro(self):
        """
        INTRO (bass-bat)
        """
        self.pause_loopers()
        self.reset()
        notes.set_notes(*self.scale)

        # Séquences
        seq192.select('solo', 'couplet_*')
        seq192.select('off', 'couplet_cLow_Barkline_half')

        # Samples
        self.open_samples()

        # Transport
        transport.start()

        # Synths
        synths.set('DubstepHorn', 'Amp', 'Gain', 0.6)
        synths.set('EasyClassical', 'Amp', 'Gain', 0.6)
        synths.set('EasyClassical', 'Pan', -0.4)
        synths.set('ZStambul', 'Amp', 'Gain', 0.6)
        synths.set('ZStambul', 'Pan', 0.4)
        synths.set('SteelDrums', 'Amp', 'Gain', 0.35)
        synths.set('SteelDrums', 'Pan', 0.3)

        # Vocals
        vocalsKesch.set('normo_exclu', 'on')
        vocalsNano.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        inputs.set('keschmic', 'dynamic')

    @pedalboard_button(3)
    def couplet1a(self):
        """
        COUPLET 1A (come on this song)
        filtrage synth, trig bass loop
        """
        postprocess.animate_filter('synths', 400, 22000, 4, 'beat', easing='exponential-in')
        self.start_scene('sequences/couplet1a', lambda:[
            self.wait(3, 'b'),
            looper.record(0),
            self.wait_next_cycle(),
            seq192.select('off', 'couplet_zHi_trumpets'),
            self.wait(15, 'b'),
            looper.record(0)
        ])

        # Vocals
        self.engine.set('NanoNormo', 'correction', 0)
        self.engine.set('KeschNormo', 'correction', 0)

        inputs.set('keschmic', 'dynamic')

    @mk2_button(3, 'cyan')
    def couplet1b(self):
        """
        COUPLET 1B (in the name)
        """
        self.pause_loopers()
        self.reset()
        notes.set_notes(*self.scale)

        # Séquences
        seq192.select('solo', 'alt_couplet_*')

        # Synths
        synths.set('ZDiploLike', 'Pan', 0.15)
        synths.set('ZJestoProunk', 'Pan', -0.15)
        synths.set('ZDiploLike', 'Amp', 'Gain', 0.85)
        synths.set('ZJestoProunk', 'Amp', 'Gain', 0.85)

        # Transport
        transport.start()

        self.start_scene('sequences/couplet1c', lambda: [
            self.wait(4*4, 'beats'),
            seq192.select('solo', 'alt2_couplet_*samples_violons'),
            self.wait(2*4, 'beats'),
            self.run(self.couplet1c)
        ])

        # Vocals
        inputs.set('keschmic', 'dynamic')

    @mk2_button(99)
    def couplet1c(self):
        """
        COUPLET 1C (we empty)
        """
        self.pause_loopers()
        self.reset()
        notes.set_notes(*self.scale)

        # Séquences
        seq192.select('solo', 'couplet_*')
        seq192.select('off', 'couplet_cLow_Barkline_full')

        # Samples
        self.open_samples()

        # Transport
        transport.start()

        # Looper
        looper.trigger(0)

        # Synths
        synths.set('DubstepHorn', 'Amp', 'Gain', 0.6)
        synths.set('EasyClassical', 'Amp', 'Gain', 0.6)
        synths.set('EasyClassical', 'Pan', -0.4)
        synths.set('ZStambul', 'Amp', 'Gain', 0.6)
        synths.set('ZStambul', 'Pan', 0.4)
        synths.set('SteelDrums', 'Amp', 'Gain', 0.35)
        synths.set('SteelDrums', 'Pan', 0.3)

        # Vocals
        vocalsKesch.set('normo_exclu', 'on')
        vocalsNano.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        inputs.set('keschmic', 'dynamic')

    # def up_alt_couplet(self):
    #     """
    #     UP COUPLET ALTERNATIF
    #     """
    #     self.pause_loopers()
    #     self.reset()
    #
    #     # Séquences
    #     seq192.select('on', 'alt2_couplet_*')
    #
    #     # Synths
    #     synths.set('SteelDrums', 'Pan', 0.3)
    #     synths.set('ZJestoProunk', 'Pan', -0.3)
    #     synths.set('ZDiploLike', 'Amp', 'Gain', 0.85)
    #     synths.set('ZJestoProunk', 'Amp', 'Gain', 0.85)
    #     synths.set('SteelDrums', 'Amp', 'Gain', 0.85)
    #
    #     # Samples
    #     self.open_samples()


    @mk2_button(4, 'purple')
    def prerefrain(self):
        """
        PREREFRAIN (loop vx seules)
        """
        self.pause_loopers()
        self.reset()
        notes.set_notes(*self.scale)

        # Séquences
        seq192.select('solo', 'dummy')

        # Loopers
        looper.record_on_start('[5,7,9]')

        # Transport
        transport.start()

        # harmo chastitties
        autotuneFeatNormo.set_notes(*self.scale[2:], *self.scale[0:2])

        self.start_scene('sequences/autorefrain', lambda: [
            self.wait(15),
            looper.record('[5,7]'), #,9]'),
            self.wait(1),
            # self.run(self.refrain1)
        ])

        # Keyboards
        jmjKeyboard.set_sound('ZTrumpets')


        # Vocals
        vocalsKesch.set('normo_exclu', 'on')
        vocalsNano.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        inputs.set('keschmic', 'dynamic')

    @mk2_button(5, 'purple')
    def refrain1(self,):
        """
        REFRAIN 1
        """

        self.reset()
        notes.set_notes(*self.scale)

        self.open_samples()

        # Séquences
        seq192.select('solo', 'refrain_*')

        # Transport
        transport.start()
        looper.trigger('[5,7]')

        # Basse
        bassFX.set('distohi', 'on')

        # Synths
        synths.set('TenorSax', 'Calf%20Mono%20Compressor', 'Bypass', 0.0)
        synths.set('TenorSax', 'Calf%20Multi%20Chorus', 'Active', 1.0)
        synths.set('ZDupieux', 'Amp', 'Gain', 0.9)
        synths.set('TrapFifth', 'Amp', 'Gain', 0.45)
        synthsFX2Delay.set('ZDupieux', 'Gain', -9.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)
        synthsFX5Scape.set('ZDupieux', 'Gain', -4.0)
        synthsFX5Scape.set('SynthsFX5Scape', 'Mute', 0.0)

        # Vocals
        vocalsKesch.set('normo_exclu', 'on')
        vocalsNano.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        inputs.set('keschmic', 'static')

         # Séquences
        self.start_sequence('sequences/refrain', [
            { # bar 1
                1: lambda: [
                    synthsFX2Delay.set('Charang', 'Gain', -70.0),
                    synthsFX2Delay.set('TenorSax', 'Gain', -70.0)
                    ]
            },
            {}, # bar 2
            {}, # bar 3
            { # bar 4
                3: lambda: [
                    synthsFX2Delay.set('Charang', 'Gain', -15.0),
                    synthsFX2Delay.set('TenorSax', 'Gain', -15.0)
                ]

            }
         ], loop=True)

    @mk2_button(6, 'cyan')
    def couplet2a(self):
        """
        COUPLET 2a
        """
        self.pause_loopers()
        self.reset()
        notes.set_notes(*self.scale)

        # Séquences
        seq192.select('solo', 'couplet2_Piano')
        seq192.select('on', 'couplet2_contrechant_court')

        # Samples
        self.open_samples()

        # Transport
        transport.start()

        # Synths
        synths.set('DubstepHorn', 'Amp', 'Gain', 0.6)
        synths.set('EasyClassical', 'Amp', 'Gain', 0.6)
        synths.set('EasyClassical', 'Pan', -0.4)
        synths.set('ZStambul', 'Amp', 'Gain', 0.6)
        synths.set('ZStambul', 'Pan', 0.4)
        synths.set('SteelDrums', 'Amp', 'Gain', 0.35)
        synths.set('SteelDrums', 'Pan', 0.3)

        synthsFX4TapeDelay.set('SynthsFX4TapeDelay', 'Mute', 0)
        synthsFX4TapeDelay.set('Rhodes', 'Gain', -20)
        synthsFX6Degrade.set('SynthsFX6Degrade', 'Mute', 0)
        synthsFX6Degrade.set('Piano', 'Gain', -24)

        # Vocals
        vocalsKesch.set('normo_exclu', 'on')
        vocalsNano.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        inputs.set('keschmic', 'dynamic')

    @mk2_button(7, 'cyan')
    def couplet2b(self):
        """
        COUPLET 2b
        """
        self.pause_loopers()
        self.reset()

        # Séquences
        seq192.select('solo', 'couplet2_Piano2')
        seq192.select('on', 'couplet2_contrechant_court')
        seq192.select('on', 'couplet2_contrechant_long')

        # Samples
        self.open_samples()

        # Transport
        transport.start()

        # Synths
        synths.set('DubstepHorn', 'Amp', 'Gain', 0.6)
        synths.set('EasyClassical', 'Amp', 'Gain', 0.6)
        synths.set('EasyClassical', 'Pan', -0.4)
        synths.set('ZStambul', 'Amp', 'Gain', 0.6)
        synths.set('ZStambul', 'Pan', 0.4)
        synths.set('SteelDrums', 'Amp', 'Gain', 0.35)
        synths.set('SteelDrums', 'Pan', 0.3)

        # Vocals
        vocalsKesch.set('normo_exclu', 'on')
        vocalsNano.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        inputs.set('keschmic', 'dynamic')

        # Keyboards
        jmjKeyboard.set_sound('LowZ8bits')
        mk2Control.set_mode('stopit')
        mk2Keyboard.set_sound('LowCTrap1')

    @pedalboard_button(5)
    def couplet2refrain(self):
        """
        COUPLET 2 Refrain
        """
        self.pause_loopers()
        self.reset()

        # Samples
        self.open_samples()

        notes.set_notes([1]*12)

        # Séquences
        # seq192.select('solo', 'couplet2_Piano')
        seq192.select('solo', 'gonnadgun_zHi_trumpets')
        # seq192.select('on', 'couplet2_contrechant_long')
        # seq192.select('on', 'couplet2_refrain')

        # Transport
        transport.start()


        # Synths
        synths.set('DubstepHorn', 'Amp', 'Gain', 0.6)
        synths.set('EasyClassical', 'Amp', 'Gain', 0.6)
        synths.set('EasyClassical', 'Pan', -0.4)
        synths.set('ZStambul', 'Amp', 'Gain', 0.6)
        synths.set('ZStambul', 'Pan', 0.4)
        synths.set('SteelDrums', 'Amp', 'Gain', 0.35)
        synths.set('SteelDrums', 'Pan', 0.3)

        # Vocals
        vocalsKesch.set('normo_exclu', 'on')
        vocalsNano.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        inputs.set('keschmic', 'dynamic')

        # Keyboards
        jmjKeyboard.set_sound('LowZ8bits')

        # Séquences
        # self.start_sequence('sequence/gonnadgunseq', [
        #     {
        #         1: lambda: [
        #             seq192.select('solo', 'couplet2_contrechant_court'),
        #             seq192.select('on', 'couplet2_contrechant_long'),
        #             ],
        #         2.5: lambda: [
        #             seq192.select('solo', 'dummy')
        #         ]
        #         },
        # ],
        # loop=True)
        self.start_scene('sequence/gonnadgun', lambda: [
            self.wait(16, 'beat'),
            self.run(self.couplet_refrainrefrain)
        ])



    def couplet_refrainrefrain(self):

        self.stop_sequence('*')

        # Séquences
        seq192.select('solo', 'couplet2_contrechant_court'),
        seq192.select('on', 'couplet2_contrechant_long'),
        seq192.select('on', 'couplet2_refrain')

        # Keyboards
        jmjKeyboard.set_sound('MajorVocals',lead=True)

        # Vocals
        inputs.set('keschmic', 'dynamic')

    @pedalboard_button(6)
    def refrain_coupletcouplet(self):
        """
        Refrain Couplet couplet
        """
        self.couplet_refrainrefrain()
        transport.start()



    @mk2_button(8, 'cyan')
    def couplet2bc(self):
        """
        COUPLET 2c
        """
        self.pause_loopers()
        self.reset()

        # Séquences
        seq192.select('solo', 'couplet2_Piano')
        seq192.select('on', 'couplet2_salsa')
        seq192.select('on', 'couplet2_bass*')

        # Samples
        self.open_samples()

        # Transport
        transport.start()

        # Synths
        synths.set('DubstepHorn', 'Amp', 'Gain', 0.6)
        synths.set('EasyClassical', 'Amp', 'Gain', 0.6)
        synths.set('EasyClassical', 'Pan', -0.4)
        synths.set('ZStambul', 'Amp', 'Gain', 0.6)
        synths.set('ZStambul', 'Pan', 0.4)
        synths.set('SteelDrums', 'Amp', 'Gain', 0.35)
        synths.set('SteelDrums', 'Pan', 0.3)

        # Vocals
        vocalsKesch.set('normo_exclu', 'on')
        vocalsNano.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        inputs.set('keschmic', 'dynamic')

        # Keyboards
        jmjKeyboard.set_sound('MajorVocals', lead=True)

    #
    # @mk2_button(6, 'white')
    # def break_couplet(self):
    #     """
    #     BREAK COUPLET (il reste des haricots)
    #     """
    #     self.pause_loopers()
    #     self.reset()
    #
    #     # Séquences
    #     seq192.select('solo', 'break_*')
    #
    #     # Samples
    #     self.open_samples()
    #
    #
    # @mk2_button(7, 'cyan')
    # def alt2_couplet(self):
    #     """
    #     COUPLET ALTERNATIF 2 (we got beans)
    #     """
    #     self.pause_loopers()
    #     self.reset()
    #
    #     # Séquences
    #     # seq192.select('solo', 'alt*')
    #     seq192.select('solo', 'up_theme_sf_tenorsax')
    #
    #     # Synths
    #     synths.set('SteelDrums', 'Pan', 0.3)
    #     synths.set('ZJestoProunk', 'Pan', -0.3)
    #     synths.set('ZTrumpets', 'Amp', 'Gain', 0.5)
    #
    #
    #     # Samples
    #     self.open_samples()
    #
    #     # Transport
    #     transport.start()
    #
    # @mk2_button(8, 'cyan')
    # def alt2b_couplet(self):
    #     """
    #     COUPLET ALTERNATIF 2b -what do we need
    #     """
    #     self.pause_loopers()
    #     self.reset()
    #
    #     # Séquences
    #     seq192.select('solo', 'alt*')
    #
    #     # Synths
    #     synths.set('SteelDrums', 'Pan', 0.3)
    #     synths.set('ZJestoProunk', 'Pan', -0.3)
    #     # synths.set('ZTrumpets', 'Amp', 'Gain', 0.5)
    #     synths.set('ZDiploLike', 'Amp', 'Gain', 0.85)
    #     synths.set('ZJestoProunk', 'Amp', 'Gain', 0.85)
    #     synths.set('SteelDrums', 'Amp', 'Gain', 0.85)
    #
    #
    #     # Samples
    #     self.open_samples()
    #
    #     # Transport
    #     transport.start()
    #
    #
    @pedalboard_button(7)
    def beethoven(self):
        transport.stop()
        self.pause_loopers()

        jmjKeyboard.set_sound('TenorSax')

        # Vocals
        vocalsKesch.set('meuf_exclu', 'on')
        inputs.set('keschmic', 'dynamic')

    @pedalboard_button(8)
    def theme(self):
        """
        THÈME
        """
        self.pause_loopers()
        self.reset()

        self.open_samples()

        # Séquences
        seq192.select('solo', 'theme_*')


        # Transport
        transport.start()

        # Keyboards
        jmjKeyboard.set_sound('TenorSax')

        # Vocals
        vocalsKesch.set('meuf_exclu', 'on')
        vocalsNano.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        inputs.set('keschmic', 'static')

    @mk2_button(9)
    def uptranse(self):
        """
        Refrain Couplet couplet
        """
        self.couplet_refrainrefrain()
        transport.start()
        seq192.select('on', 'couplet2_uprefrain')

    @mk2_button(10)
    def bridge(self):
        """
        8bridge
        """
        self.pause_loopers()
        self.reset()

        self.open_samples()

        # Séquences
        seq192.select('solo', '8bridge_*')


        # Transport
        transport.start()

        # Keyboards
        jmjKeyboard.set_sound('ZTrumpets')

        inputs.set('keschmic', 'static')


    @mk2_button(11)
    def up_theme(self):
        """
        UP THÈME
        """
        self.pause_loopers()
        self.reset()

        self.open_samples()

        # Séquences
        seq192.select('on', 'up_theme_*')


        # Transport
        transport.start()

        # Keyboards
        jmjKeyboard.set_sound('ZBombarde')

        inputs.set('keschmic', 'static')

    @pedalboard_button(9)
    def transetranse(self):
        jmjKeyboard.set_sound('ZNotSoRhodes', lead=False)
        seq192.select('solo', 'dummy')
        transport.start()

    @pedalboard_button(10)
    def keyboard_transe_boucling(self):
        looper.record(3)

    @pedalboard_button(11)
    def keyboard_transe_overdubbing(self):
        looper.overdub(3)


    @chastt_button(1)
    def chastt_note_1(self):
        chasttKeyboard.play_note(45, 0.5)
