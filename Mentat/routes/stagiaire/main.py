from ..base import RouteBase, mk2_button, pedalboard_button
from .video import Video
from .light import Light

from modules import *

class Stagiaire(Video, Light, RouteBase):
    """
    Stagiaire
    """

    def activate(self):
        """
        Called when the engine switches to this route.
        """

        super().activate()

        transport.set_tempo(117)
        transport.set_cycle('4/4')

        # Setups, banks...
        seq192.set_screenset(self.name)
        prodSampler.set_kit(self.name)

        # Microtonality
        microtonality.disable()

        # Autotuner Notes
        #               c     d     e  f     g     a     b
        notes.set_notes(1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0)

        # Mk2
        mk2Control.set_mode('cut_samples', 'cut_synths')

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
        INTRO (fin du sample)
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'intro_*')

        # Transport
        transport.set_tempo(117)
        transport.start()

        # Samples
        samplesFX2Delay.set('Samples2', 'Gain', -12.0) #### TODO FX Delay 2 = Munge ?
        samplesFX2Delay.set('SamplesFX2Delay', 'Mute', 0.0)

        samples.set('Samples1', 'Mute', 0.0)
        samples.set('Samples2', 'Mute', 0.0)
        samples.set('Samples4', 'Mute', 0.0)
        samples.set('Samples5', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')

        # Sequences (Mentat)
        self.start_sequence('intro', [
            {}, {}, {}, # bar 1 - 3
            { # bar 4
                1: lambda: [ seq192.select('solo', 'introS_*'), transport.start()]
            }
        ], loop=False)

    @pedalboard_button(3)
    def intro_stagiaire(self):
        """
        INTRO Stagiaire
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'introS_*')

        # Transport
        transport.set_tempo(117)
        transport.start()

        # Samples
        samplesFX2Delay.set('Samples2', 'Gain', -12.0) #### TODO FX Delay 2 = Munge ?
        samplesFX2Delay.set('SamplesFX2Delay', 'Mute', 0.0)

        samples.set('Samples1', 'Mute', 0.0)
        samples.set('Samples2', 'Mute', 0.0)
        samples.set('Samples4', 'Mute', 0.0)
        samples.set('Samples5', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')

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
        transport.set_tempo(117)
        transport.start()
        #### TODO Trapcut tempo 234

        # Samples
        samplesFX2Delay.set('Samples2', 'Gain', -12.0) #### TODO FX Delay 2 = Munge ?
        samplesFX2Delay.set('SamplesFX2Delay', 'Mute', 0.0)

        samples.set('Samples2', 'Mute', 0.0) # flûte
        samples.set('Samples5', 'Mute', 0.0) # percu

        # Synths
        synthsFX1Reverb.set('EasyClassical', 'Gain', -9.0)
        synthsFX1Reverb.set('SynthsFX1Reverb', 'Mute', 0.0)
        synthsFX2Delay.set('EasyClassical', 'Gain', -9.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')

    @pedalboard_button(5)
    def afro(self):
        """
        PONT AFRO
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'afro_*')

        # Transport
        transport.set_tempo(125)
        transport.start()

        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')

        # Keyboards
        jmjKeyboard.set_sound('ZCosma', boost=True)

    @pedalboard_button(6)
    def theme(self):
        """
        THÈME
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'theme_*')

        # Transport
        transport.set_tempo(125)
        transport.start() #### TODO à l'origine pas de relance de transport -> pourquoi ?

        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')

        # Keyboards
        jmjKeyboard.set_sound('ZCosma', boost=True)

    @mk2_button(2, 'purple')
    def afro2(self):
        """
        AFRO 2
        """
        self.pause_loopers()
        self.reset()

        # Looper
        looper.trigger(0)

        # Sequences
        seq192.select('solo', 'afro_*')

        # Transport
        transport.set_tempo(125)
        transport.start()

        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')
        vocalsKesch.set('normo', 'on')

    @pedalboard_button(7)
    def refrain(self):
        """
        REFRAIN
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'refrain_*')

        # Transport
        transport.set_tempo(125)
        transport.start()

        # Samples
        samples.set('Samples1', 'Mute', 0.0) # gtr
        samples.set('Samples2', 'Mute', 0.0) # flûte
        samples.set('Samples5', 'Mute', 0.0) # percu

        samplesFX2Delay.set('Samples2', 'Gain', -12.0) #### TODO FX Delay 2 = Munge ?
        samplesFX2Delay.set('SamplesFX2Delay', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')

        vocalsKeschFX2Delay.set('active', 'on')
        vocalsNanoFX2Delay.set('active', 'on')

        # TODO: c koi se bordél
        # Séquences (Mentat)
        self.start_sequence('refrain_stagiaire', [
            {'signature': '4/4'}, # bar 1
            { # bar 2
            },
            { # bar 3
                2: lambda: vocalsKesch.set('meuf_exclu', 'on')
            },
            { # bar 4
                3: lambda: vocalsKesch.set('gars_exclu', 'on')
            },
            { # bar 5
            },
            { # bar 6
            },
            { # bar 7
            },
            { # bar 8
            },
        ], loop=True)



    @pedalboard_button(4)
    def trap2(self):
        """
        TRAP 2 (cf. TRAP)
        """
        # méthode vide juste pour que le déroulé du morceau appairaisse de façon linéaire
        pass

    @mk2_button(3, 'purple')
    def afro3(self):
        """
        AFRO 3 (BUTTER cf. AFRO)
        """
        self.afro2()
        vocalsKesch.set('gars_exclu', 'on')

    @pedalboard_button(7)
    def refrain2(self):
        """
        REFRAIN 2 (cf. REFRAIN)
        """
        # méthode vide juste pour que le déroulé du morceau appairaisse de façon linéaire
        pass

    @mk2_button(5, 'yellow')
    def nanogars(self):
        """
        NANO GARS
        """
        vocalsNano.set('gars_exclu', 'on')

    @mk2_button(6, 'yellow')
    def nanomeuf(self):
        """
        NANO MEUF
        """
        vocalsNano.set('meuf_exclu', 'on')

    @mk2_button(7, 'yellow')
    def nanonormo(self):
        """
        NANO NORMO
        """
        vocalsNano.set('normo_exclu', 'on')

    ### TODO TRAPCUT @mk2_button(5, 'purple')
