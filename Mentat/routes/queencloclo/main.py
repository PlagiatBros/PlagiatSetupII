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
        samples.set('KJ', 'Gain', -4.0)
        # samples.set('GuitarChorus', 'Mute', 0.0)
        # samples.set('Trumpets', 'Mute', 0.0)
        samplesFX3Reverb.set('Violons', 'Gain', -10.0)
        samplesFX3Reverb.set('SamplesFX3Reverb', 'Mute', 0.0)
        samplesFX5TapeDelay.set('Violons', 'Gain', -12.0)
        samplesFX5TapeDelay.set('KJ', 'Gain', -14.0)
        samplesFX5TapeDelay.set('SamplesFX5TapeDelay', 'Mute', 0.0)
        samplesFX7Degrade.set('KJ', 'Gain', -3.0)
        samplesFX7Degrade.set('SamplesFX7Degrade', 'Mute', 0.0)




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


        # Keyboards
        jmjKeyboard.set_sound('ZTrumpets', lead=True)
        samples.set_lead()


        # Vocals
        vocalsKesch.set('meuf_exclu', 'on')
        vocalsNano.set('normo_exclu', 'on')
        vocalsChast.set('normo_exclu', 'on')

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
        # synths.set('DubstepHorn', 'Amp', 'Gain', 0.6)
        # synths.set('EasyClassical', 'Amp', 'Gain', 0.6)
        # synths.set('EasyClassical', 'Pan', -0.4)
        synths.set('ZTrumpets', 'Amp', 'Gain', 0.8)
        synths.set('ZStambul', 'Amp', 'Gain', 0.8)
        synths.set('ZStambul', 'Pan', 0.4)
        synths.set('ZNotSoRhodes', 'Amp', 'Gain', 1)
        synths.set('ZNotSoRhodes', 'Pan', -0.4)
        # synths.set('SteelDrums', 'Amp', 'Gain', 0.35)
        # synths.set('SteelDrums', 'Pan', 0.3)

        synths.set_lead('ZTrumpets')
        samples.set_lead()


        synthsFX5Scape.set('ZTrumpets', 'Gain', -9.0)
        synthsFX5Scape.set('SynthsFX5Scape', 'Mute', 0.0)

        # Vocals
        vocalsKesch.set('normo_exclu', 'on')
        vocalsNano.set('normo_exclu', 'on')
        vocalsChast.set('normo_exclu', 'on')

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
            samplesFX3Reverb.set('KJ', 'Gain', -12.0),
            samplesFX3Reverb.set('SamplesFX3Reverb', 'Mute', 0.0),
            samplesFX5TapeDelay.set('SamplesFX5TapeDelay', 'Mute', 1.0),
            self.wait(15, 'b'),
            looper.record(0)
        ])

        # set lead
        synths.set_lead()
        samples.set_lead()

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
        # synths.set('ZJestoProunk', 'Pan', -0.15)
        synths.set('ZDiploLike', 'Amp', 'Gain', 0.85)
        # synths.set('ZJestoProunk', 'Amp', 'Gain', 0.85)
        synths.set('ZNotSoRhodes', 'Pan', -0.15)

        synthsFX5Scape.animate('ZNotSoRhodes', 'Gain', -20, -9, 18, 'b', easing='linear-mirror', loop=True)
        synthsFX5Scape.set('SynthsFX5Scape', 'Mute', 0.0)
        synthsFX3Delay.animate('ZNotSoRhodes', 'Gain', -40, -20, 12, 'b', easing='linear-mirror', loop=True)
        synthsFX3Delay.set('SynthsFX3Delay', 'Mute', 0.0)

        # Lead
        synths.set_lead()
        samples.set_lead()

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
        synths.set('ZTrumpets', 'Amp', 'Gain', 0.6)
        synths.set('ZStambul', 'Amp', 'Gain', 0.8)
        synths.set('ZStambul', 'Pan', 0.4)
        synths.set('ZNotSoRhodes', 'Amp', 'Gain', 1)
        synths.set('ZNotSoRhodes', 'Pan', -0.4)
        # synths.set('SteelDrums', 'Amp', 'Gain', 0.35)
        # synths.set('SteelDrums', 'Pan', 0.3)


        # Lead
        synths.set_lead('ZTrumpets')
        samples.set_lead()

        postprocess.set_filter('synths', 4000)

        # Vocals
        vocalsKesch.set('normo_exclu', 'on')
        vocalsNano.set('normo_exclu', 'on')
        vocalsChast.set('normo_exclu', 'on')

        inputs.set('keschmic', 'dynamic')


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
        autotuneChastNormo.set_notes(*self.scale[2:], *self.scale[0:2])

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
        vocalsChast.set('normo_exclu', 'on')

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

        # lead
        synths.set_lead('TenorSax')
        samples.set_lead()

        # Synths
        synths.set('TenorSax', 'Calf%20Mono%20Compressor', 'Bypass', 0.0)
        synths.set('TenorSax', 'Calf%20Multi%20Chorus', 'Active', 1.0)
        synths.set('ZDupieux', 'Amp', 'Gain', 0.7)
        synths.set('ZDupieux', 'Pan', 0.1)
        synths.set('TrapFifth', 'Amp', 'Gain', 0.4)
        synths.set('TrapFifth', 'Pan', -0.1)
        synths.set('TenorSax', 'Amp', 'Gain', 0.8)
        synths.set('ZTrumpets', 'Amp', 'Gain', 0.5)
        synths.set('ZTrumpets', 'Pan', 0.4)
        synths.set('Charang', 'Amp', 'Gain', 0.5)
        synths.set('Charang', 'Pan', -0.4)

        synthsFX2Delay.set('ZDupieux', 'Gain', -9.0)
        synthsFX2Delay.set('ZTrumpets', 'Gain', -15.0)
        synthsFX2Delay.set('Charang', 'Gain', -15.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)

        synthsFX3Delay.set('ZDupieux', 'Gain', -15.0)
        synthsFX3Delay.set('SynthsFX3Delay', 'Mute', 0.0)

        synthsFX5Scape.set('ZDupieux', 'Gain', -4.0)
        synthsFX5Scape.set('SynthsFX5Scape', 'Mute', 0.0)

        # Vocals
        vocalsKesch.set('normo_exclu', 'on')
        vocalsNano.set('normo_exclu', 'on')
        vocalsChast.set('normo_exclu', 'on')

        inputs.set('keschmic', 'static')

         # Séquences
        self.start_sequence('sequences/refrain', [
            { # bar 1
                1: lambda: [
                    synthsFX2Delay.set('ZTrumpets', 'Gain', -70.0),
                    synthsFX2Delay.set('Charang', 'Gain', -70.0),
                    synthsFX2Delay.set('TenorSax', 'Gain', -70.0)
                    ]
            },
            {}, # bar 2
            {}, # bar 3
            { # bar 4
                3: lambda: [
                    synthsFX2Delay.set('ZTrumpets', 'Gain', -15.0),
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

        # lead
        synths.set_lead()
        samples.set_lead()


        # Samples
        self.open_samples()

        # Transport
        transport.start()

        # Synths
        synthsFX4TapeDelay.set('SynthsFX4TapeDelay', 'Mute', 0.0)
        synthsFX4TapeDelay.set('Rhodes', 'Gain', -20.0)
        synthsFX6Degrade.set('SynthsFX6Degrade', 'Mute', 0.0)
        synthsFX6Degrade.set('Piano', 'Gain', -24.0)

        # Vocals
        vocalsKesch.set('normo_exclu', 'on')
        vocalsNano.set('normo_exclu', 'on')
        vocalsChast.set('normo_exclu', 'on')

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

        # lead
        synths.set_lead('TenorSax')
        samples.set_lead()


        # Samples
        self.open_samples()

        # Transport
        transport.start()

        # Synths
        synths.set('TrapFifth', 'Amp', 'Gain', 0.5)
        synths.set('DubstepHorn', 'Amp', 'Gain', 0.5)
        synths.set('ZJestoProunk', 'Amp', 'Gain', 0.5)
        synths.set('TrapFifth', 'Pan', -0.4)
        synths.set('DubstepHorn', 'Pan', 0.4)
        synths.set('ZJestoProunk', 'Pan', 0.4)

        synthsFX4TapeDelay.set('SynthsFX4TapeDelay', 'Mute', 0.0)
        synthsFX4TapeDelay.set('Rhodes', 'Gain', -20.0)
        synthsFX6Degrade.set('SynthsFX6Degrade', 'Mute', 0.0)
        synthsFX6Degrade.set('Piano', 'Gain', -24.0)


        # Vocals
        vocalsKesch.set('normo_exclu', 'on')
        vocalsNano.set('normo_exclu', 'on')
        vocalsChast.set('normo_exclu', 'on')

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

        # lead
        synths.set_lead()
        samples.set_lead()


        # Synths
        synths.set('ZTrumpets', 'Amp', 'Gain', 0.9)
        midipanic.reset() # ppitch fix à cause du refrain

        # Vocals
        vocalsKesch.set('normo_exclu', 'on')
        vocalsNano.set('normo_exclu', 'on')
        vocalsChast.set('normo_exclu', 'on')

        inputs.set('keschmic', 'dynamic')

        # Keyboards
        jmjKeyboard.set_sound('LowZ8bits')

        # Séquences
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

        # Lead
        synths.set_lead('MajorVocals')
        samples.set_lead()

        # Synths

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
        seq192.select('on', 'couplet2c_zHi_diploLike')
        seq192.select('on', 'couplet2_salsa')
        seq192.select('on', 'couplet2_bass*')

        # lead
        samples.set_lead()
        synths.set_lead('MajorVocals')

        # Samples
        self.open_samples()

        # Transport
        transport.start()

        # Synths
        synthsFX6Degrade.set('SynthsFX6Degrade', 'Mute', 0.0)
        synthsFX6Degrade.set('Piano', 'Gain', -24.0)

        synths.set('SteelDrums', 'Amp', 'Gain', 0.7)
        synths.set('SteelDrums', 'Pan', 0)

        synths.set('ZDiploLike*', 'Amp', 'Gain', 0.36)
        synths.set('ZDiploLikeWide', 'Pan', -0.7)
        synths.set('ZDiploLike', 'Pan', 0.7)

        synthsFX1Reverb.set('ZDiplo*', 'Gain', -15.0)
        synthsFX1Reverb.set('SynthsFX1Reverb', 'Mute', 0.0)

        # Vocals
        vocalsKesch.set('normo_exclu', 'on')
        vocalsNano.set('normo_exclu', 'on')
        vocalsChast.set('normo_exclu', 'on')

        inputs.set('keschmic', 'dynamic')

        # Keyboards
        jmjKeyboard.set_sound('MajorVocals')

    @mk2_button(9)
    def uptranse(self):
        """
        Refrain Couplet couplet
        """
        self.couplet_refrainrefrain()
        transport.start()
        seq192.select('on', 'couplet2_uprefrain')

    @pedalboard_button(9)
    def transetranse(self):
        jmjKeyboard.set_sound('ZNotSoRhodes', lead=False)

        # LEAD
        synths.set_lead('MajorVocals')
        samples.set_lead()

        seq192.select('solo', 'dummy')
        transport.start()

    @pedalboard_button(10)
    def keyboard_transe_boucling(self):
        looper.record(3)

    @pedalboard_button(11)
    def keyboard_transe_overdubbing(self):
        looper.overdub(3)



    @pedalboard_button(7)
    def beethoven(self):
        transport.stop()
        self.pause_loopers()

        jmjKeyboard.set_sound('TenorSax', lead=True)

        # Lead
        samples.set_lead()

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
        jmjKeyboard.set_sound('TenorSax', lead=True)

        # Lead
        samples.set_lead()

        # Vocals
        vocalsKesch.set('meuf_exclu', 'on')
        vocalsNano.set('normo_exclu', 'on')
        vocalsChast.set('normo_exclu', 'on')

        inputs.set('keschmic', 'static')


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
        jmjKeyboard.set_sound('ZTrumpets', lead=False)

        synths.set_lead('ZBombarde')
        samples.set_lead()

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

        # Synths
        synths.set('ZTrumpets', 'Pan', -0.7)
        # synths.set('ZCosma', 'Amp', 'Gain', 0.9)
        synths.set('ZCosma', 'Pan', 0.7)
        synths.set('TenorSax', 'Amp', 'Gain', 0.9)

        # Transport
        transport.start()

        # Keyboards
        jmjKeyboard.set_sound('ZBombarde', lead=True)

        # LEAD
        samples.set_lead()

        inputs.set('keschmic', 'static')

    @gui_button(
        type='button',
        label='If I Had A Hummer',
        mode='momentary',
        height=80
        )
    def goto_hummerg(self):
        """
        GOTO Voiture de Filles
        """
        engine.set_route('IfIHadAHummer')
        engine.active_route.refrain()
