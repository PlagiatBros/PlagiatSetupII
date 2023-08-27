from ..base import *
from .video import Video
from .light import Light

from modules import *

class QueenCloclo(Video, Light, RouteBase):
    """
    Queen Cloclo
    """

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
        microtonality.enable()
        microtonality.set_tuning(0, -0.35, 0, 0, 0, 0.35, 0, 0, 0, 0, 0.35, 0)

        # Autotuner Notes
        #               c     d     e  f     g     a     b
        notes.set_notes(1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0)

        # Mk2
        mk2Control.set_mode('cut_samples', 'cut_synths')

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

    @mk2_button(2, 'cyan')
    def couplet(self):
        """
        COUPLET 1
        """
        self.pause_loopers()
        self.reset()

        # Séquences
        seq192.select('solo', 'couplet_*')

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

        # Looper
        looper.trigger(0)

        # Vocals
        vocalsKesch.set('normo_exclu', 'on')
        vocalsNano.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

    @pedalboard_button(3)
    @mk2_button(3, 'cyan')
    def alt_couplet(self):
        """
        COUPLET ALTERNATIF
        """
        self.pause_loopers()
        self.reset()

        # Séquences
        seq192.select('solo', 'alt_couplet_*')

        # Synths
        synths.set('ZDiploLike', 'Pan', 0.15)
        synths.set('ZJestoProunk', 'Pan', -0.15)
        synths.set('ZDiploLike', 'Amp', 'Gain', 0.85)
        synths.set('ZJestoProunk', 'Amp', 'Gain', 0.85)

        # Transport
        transport.start()

    @mk2_button(4, 'white')
    def up_alt_couplet(self):
        """
        UP COUPLET ALTERNATIF
        """
        self.pause_loopers()
        self.reset()

        # Séquences
        seq192.select('on', 'alt2_couplet_*')

        # Synths
        synths.set('SteelDrums', 'Pan', 0.3)
        synths.set('ZJestoProunk', 'Pan', -0.3)
        synths.set('ZDiploLike', 'Amp', 'Gain', 0.85)
        synths.set('ZJestoProunk', 'Amp', 'Gain', 0.85)
        synths.set('SteelDrums', 'Amp', 'Gain', 0.85)

        # Samples
        self.open_samples()


    @pedalboard_button(2)
    @mk2_button(5, 'purple')
    def refrain(self):
        """
        REFRAIN
        """
        self.pause_loopers()
        self.reset()

        self.open_samples()

        # Séquences
        seq192.select('solo', 'refrain_*')

        # Basse
        bassFX.set('distohi', 'on')


        # Transport
        transport.start()

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


    @mk2_button(6, 'white')
    def break_couplet(self):
        """
        BREAK COUPLET (il reste des haricots)
        """
        self.pause_loopers()
        self.reset()

        # Séquences
        seq192.select('solo', 'break_*')

        # Samples
        self.open_samples()


    @mk2_button(7, 'cyan')
    def alt2_couplet(self):
        """
        COUPLET ALTERNATIF 2 (we got beans)
        """
        self.pause_loopers()
        self.reset()

        # Séquences
        # seq192.select('solo', 'alt*')
        seq192.select('solo', 'up_theme_sf_tenorsax')

        # Synths
        synths.set('SteelDrums', 'Pan', 0.3)
        synths.set('ZJestoProunk', 'Pan', -0.3)
        synths.set('ZTrumpets', 'Amp', 'Gain', 0.5)


        # Samples
        self.open_samples()

        # Transport
        transport.start()

    @mk2_button(8, 'cyan')
    def alt2b_couplet(self):
        """
        COUPLET ALTERNATIF 2b -what do we need
        """
        self.pause_loopers()
        self.reset()

        # Séquences
        seq192.select('solo', 'alt*')

        # Synths
        synths.set('SteelDrums', 'Pan', 0.3)
        synths.set('ZJestoProunk', 'Pan', -0.3)
        # synths.set('ZTrumpets', 'Amp', 'Gain', 0.5)
        synths.set('ZDiploLike', 'Amp', 'Gain', 0.85)
        synths.set('ZJestoProunk', 'Amp', 'Gain', 0.85)
        synths.set('SteelDrums', 'Amp', 'Gain', 0.85)


        # Keyboards
        mk2Control.set_mode('cut_samples', 'cut_synths', 'cut_basssynths')

        # Samples
        self.open_samples()

        # Transport
        transport.start()


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
        mk2Control.set_mode('cut_samples', 'cut_synths')

        # Vocals
        vocalsKesch.set('meuf_exclu', 'on')
        vocalsNano.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')


    @pedalboard_button(9)
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
        mk2Control.set_mode('cut_samples', 'cut_synths')


    @pedalboard_button(10)
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
        mk2Control.set_mode('cut_samples', 'cut_synths')
