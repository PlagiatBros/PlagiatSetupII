
from ..base import *
from .video import Video
from .light import Light

from modules import *

class IfIHadAHummer(Video, Light, RouteBase):

    def activate(self):
        """
        Called when the engine switches to this route.
        """

        super().activate()

        transport.set_tempo(140)
        transport.set_cycle('4/4')

        # Setups, banks...
        seq192.set_screenset(self.name)
        prodSampler.set_kit(self.name)

        # Microtonality
        microtonality.enable()
        microtonality.set_tuning(0, 0, 0, 0.35, 0, 0, 0, 0, 0.35, 0, 0, 0.35)

        # Autotuner Notes
        #               c     d     e  f     g     a     b
        notes.set_notes(1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1)

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

    @mk2_button(2)
    @pedalboard_button(2)
    def refrain(self):
        """
        REFRAIN
        """

        self.pause_loopers()
        self.reset()

        # Séquences
        seq192.select('solo', 'refrain_*')

        # Transport
        transport.set_cycle('4/4')
        transport.start()

        # Samples
        samples.set('Samples1', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('meuf_exclu', 'on')
        vocalsKesch.set('meuf_exclu', 'on')

        # Keyboards
        jmjKeyboard.set_sound('LowZDancestep')

        #### TODO : autom pitchdown au bout de 4 tours ?

    @mk2_button(3)
    def couplet1(self):
        """
        COUPLET 1
        """

        self.pause_loopers()
        self.reset()

        # Séquences
        seq192.select('solo', 'couplet_*')

        # Transport
        transport.set_cycle('7/8', 'X.x.x.x')
        transport.start()

        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')

        # Samples
        samples.set('Samples1', 'Mute', 0.0)
        samples.set('Samples2', 'Mute', 0.0)

        self.start_sequence('couplet1',[
            {}, {}, {}, {}, # bars 1 - 4
            {}, {}, {}, # bars 5 - 7
            { # bar 8
                3.8: lambda: [ # "My rhymes are on my double sworded tongua"
                    vocalsNano.set('normo_exclu', 'on'),
                    vocalsKesch.set('normo', 'on')
                ]
            },
            {}, # bar 9
            { # bar 10
                2.55: lambda: vocalsKesch.set('normo', 'off'),
                3: lambda: vocalsNano.set('gars_exclu', 'on')
            },
            {}, {}, # bars 11 - 12
            { # bar 13
                1: lambda: [ # "Mayday Mayday"
                    vocalsNano.set('meuf_exclu', 'on'),
                    vocalsNano.set('normo', 'on')
                ]
            },
            { # bar 14
                1: lambda: vocalsNano.set('normo', 'off')
            },
            { # bar 15
                1: lambda: vocalsKesch.set('normo', 'on'),
                3: lambda: vocalsKeschFX1Delay.set('pre', 'on')

            },
            { # bar 16
                1: lambda: [
                    vocalsKeschFX1Delay.set('pre', 'off'),
                    vocalsKesch.set('normo', 'off')
                ]
            }
        ], loop=False)

    @pedalboard_button(3)
    def bridgit_jones(self):
        """
        PONT
        """
        self.pause_loopers()
        self.reset()

        # Transport
        transport.set_cycle('4/4')
        transport.start()

        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')

        # Sequences
        seq192.select('solo', 'refrainPP_*')

        # Sequences
        self.start_sequence('bridgit_jones',
            [
            {}, {}, {}, {}, # bars 1 - 4
            {}, {}, {}, # bars 5 - 7
            { # bar 8
                2.75: lambda: postprocess.animate_pitch('*', 1, 0.25, 1.5),
                4.35: lambda : postprocess.animate_pitch('*', None, 1, 0.15)
            },
            { # bar 9
                1: lambda: [seq192.select('on', 'refrain_*'), samples.set('Samples1', 'Mute', 0.0)]
            }
            ], loop=False
        )


    @pedalboard_button(4)
    def prerefrain(self):
        """
        PRÉ-REFRAIN
        """
        self.refrain()
        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')

        # Sequences
        seq192.select('on', 'refrainPP_*')

    @pedalboard_button(6)
    @mk2_button(4, 'green')
    def refrainUp(self):
        """
        REFRAIN UP
        """

        self.pause_loopers()
        self.reset()

        # Séquences
        seq192.select('solo', 'refrainUp_*')

        # Transport
        transport.set_cycle('4/4')
        transport.start()

        # Samples
        samples.set('Samples1', 'Mute', 0.0)

        # Synths
        synths.set('Trap', 'Amp', 'Gain', 0.5)
        synths.set('EasyClassical', 'Amp', 'Gain', 0.5)
        synths.set('Rhodes', 'Amp', 'Gain', 0.5)
        synthsFX2Delay.set('Trap', 'Gain', -15.0)
        synthsFX2Delay.set('EasyClassical', 'Gain', -15.0)
        synthsFX2Delay.set('Rhodes', 'Gain', -15.0)
        synthsFX2Delay.set('ZTrumpets', 'Gain', -9.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)

        jmjKeyboard.set_sound('LowZDancestep')

        # Vocals
        vocalsNano.set('meuf_exclu', 'on')
        vocalsKesch.set('meuf_exclu', 'on')
#        vocalsKeschFX4Disint.set('active', 'on')
        vocalsKeschFX5RingMod.set('active', 'on')

        # Bass
        bassfx.set('distohi', 'on')

        self.start_sequence('refrainUp', [
            {   # bar 1
                1: lambda : postprocess.set_pitch('Samples', 1)
            },
            {}, {}, # bars 2 - 3
            {   # bar 4
                1: lambda : postprocess.animate_pitch('Samples', 1, 0.85, 3, easing='cubic-in')
            }
        ], loop=True)

    @pedalboard_button(5)
    def refrain2(self):
        """
        REFRAIN 2
        """
        self.refrain()
#        vocalsKesch.set('normo', 'on')
        vocalsNano.set('normo_exclu', 'on')
        seq192.select('on', 'refrain2_*')

        self.start_sequence('delay_refrain', [
            {
                1: lambda: vocalsKeschFX2Delay.set('pre', 'off')
            },
            {
                2.5: lambda: vocalsKeschFX2Delay.set('pre', 'on')
            }
        ], loop=True)

    @mk2_button(5)
    def couplet2(self):
        """
        COUPLET 2
        """

        self.pause_loopers()
        self.reset()

        # Séquences
        seq192.select('solo', 'couplet_*')

        # Transport
        transport.set_cycle('7/8', 'X.x.x.x')
        transport.start()

        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('meuf_exclu', 'on')

        # Samples
        samples.set('Samples1', 'Mute', 0.0)
        samples.set('Samples2', 'Mute', 0.0)

        # Bass
#        bassfx.set('distohi', 'on')

        self.start_sequence('couplet2',[
            { # bar 1
#                4: lambda: vocalsKesch.set('normo', 'on')
            },
            { # bar 2
                4: lambda: bassfx.set('distohi', 'off')
            },
            {}, # bar 3
            { # bar 4
                4: lambda: vocalsKesch.set('normo', 'off')
            },
            *[{} for i in range(4)], # bars 5 - 8
            { # bar 9
                1: lambda: vocalsNano.set('meuf_exclu', 'on')
            },
            {}, {}, {}, # bars 10 - 12
            { # bar 13
                4: lambda: vocalsKeschFX2Delay.set('active', 'on')
            },
            {}, # bar 14
            {}, # bars 15
            {   # bars 16
                1: lambda: vocalsKesch.set('normo_exclu', 'on')
            },
            { # bar 17
                1: lambda: [vocalsKeschFX2Delay.set('pre', 'off'), seq192.select('solo', 'coupletR_*')]
            }
        ], loop=False)

    @mk2_button(6, 'blue')
    def enquatre(self):
        """
        PONT EN QUATRE
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'dummy')


        # Transport
        transport.set_cycle('4/4')
        transport.start()

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')
        vocalsKeschFX2Delay.set('active', 'on')


        # Sequences
        self.start_sequence('bridgit_jones',
            [
            {}, # bar 1
            { # bar 2
                4: lambda: vocalsKesch.set('normo_exclu', 'on')
            },
            { # bar 3
                1: lambda: [
                    vocalsKeschFX2Delay.set('active', 'off'),
                    seq192.select('solo', 'refrainPP_*'),
                    seq192.select('on', 'refrain_*'),
                    samples.set('Samples1', 'Mute', 0.0), transport.start()
                ]
            }
            ], loop=False
        )

    @pedalboard_button(5)
    def stopadisto(self):
        """
        DISTO OFF
        """
        bassfx.set('distohi', 'on')

    @pedalboard_button(2)
    def refrain3(self):
        """
        REFRAIN 3 (cf. REFRAIN)
        """
        #### TODO : pitchdown auto sur fin de refrain ?
        pass

    @mk2_button(7)
    def transe(self):
        """
        TRANSE
        """
        self.pause_loopers()
        self.reset()

        # Séquences
        seq192.select('solo', 'transe_*')

        # Transport
        transport.set_cycle('4/4', 'Xxxx')
        transport.start()

        # Basses
        bassfx.set('distohi', 'on')
        bassfx.set('scape', 'on')
        bassfx.set('tapedelay', 'on')


        # Samples
        samples.set('Samples2', 'Mute', 0.0)

    @pedalboard_button(7)
    def transe_loop_basssynth(self):
        """
        LOOP BASS SYNTH
        """
        looper.record(2)

    @pedalboard_button(8)
    def transe_loop_synth(self):
        """
        LOOP SYNTH
        """
        looper.record(3)

    @gui_button()
    def do_synth(self):
        """
        DO
        """
        seq192.select('on', '//refrainUp_cHi_easy*')

    @gui_button()
    def domin_synth(self):
        """
        DO MIN
        """
        seq192.select('on', '//refrainUp*')

    @gui_button()
    def bdelay_off(self):
        """
        BASS DELAY OFF
        """
        bassfx.set('tapedelay', 'off')

    @gui_button()
    def bdelay_on(self):
        """
        BASS DELAY ON
        """
        bassfx.set('tapedelay', 'on')
