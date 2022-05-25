from ..base import RouteBase, mk2_button, pedalboard_button
from .video import Video
from .light import Light

from modules import *

class StickItOut(Video, Light, RouteBase):

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
        microtonality.enable()
        microtonality.set_tuning(0, 0.35, 0, -0.35, 0, 0.35, 0, 0, 0, 0, 0.35, 0)

        # Autotuner Notes
        #               c     d     e  f     g     a     b
        notes.set_notes(0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1)


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
        INTRO (BASSE)
        """
        self.pause_loopers()
        self.reset()

        # Séquences
        seq192.select('solo', 'dummy')

        # Transport
        transport.start()



        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('meuf_exclu', 'on')

    @pedalboard_button(3)
    def couplet1(self):
        """
        COUPLET 1 (HERE WE GO)
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'couplet1-1_*')

        # Transport
        transport.start()



        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('meuf_exclu', 'on')

        # Synths
        synthsFX2Delay.set('Rhodes', 'Gain', -9.0)
        synthsFX2Delay.set('EasyClassical', 'Gain', -9.0)
        synthsFX2Delay.set('TrapFifth', 'Gain', -9.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)

        self.start_sequence('couplet1-1', [
            *[{} for i in range(12)], # bars 1 - 12
            { # bar 13
                1: lambda: [
                    vocalsKesch.set('normo_exclu', 'on'),
                    seq192.select('solo', 'allo_zLow_ragstep')
                    ]
            },
            { # bar 14
                2: lambda: seq192.select('on', 'allo_cHi_trapfifth')
            },
            { # bar 15
                1: lambda: seq192.select('off', 'allo_zLow_ragstep'),
                2: lambda: seq192.select('off', 'allo_cHi_trapfifth'),
                3 + 3/4. : lambda: seq192.select('on', 'couplet1-2_cHi_dubstephorn')
            },
            {
                # bar 16
                1: lambda: seq192.select('solo', 'couplet1-2_*')

            }


        ], loop=False)

    @pedalboard_button(4)
    def refrain(self):
        """
        REFRAIN
        """
        self.pause_loopers()
        self.reset()


        # Sequences
        seq192.select('solo', '2ref_*')

        # Transport
        transport.start()


        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('meuf_exclu', 'on')

        # Synths
        synths.set('Trapfifth', 'Pan', -0.5)
        synths.set('ZDiploLike', 'Pan', 0.5)
        synths.set('Rhodes', 'Pan', 0.3)
        synths.set('DubstepHorn', 'Pan', -0.3)
        synthsFX2Delay.set('Trapfifth', 'Gain', -10.0)
        synthsFX2Delay.set('DubstepHorn', 'Gain', -6.0)
        synthsFX2Delay.set('ZDiploLike', 'Gain', -9.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)

        # Sequences (Mentat)
        self.start_sequence('2ref_depitch', [
            { # bar 1
                4.4: lambda: postprocess.animate_pitch('Synths', 1.0, 0.75, 0.5, easing="exponential")
            },
            { # bar 2
                1: lambda: [
                    postprocess.set_pitch('Synths', 1.0),
                    seq192.select('solo', 'refrain_*'),
                    transport.start()
                ]
            }
        ], loop=False)




    @pedalboard_button(5)
    def theme_launcher(self):
        """
        THÈME (LAUNCHER)
        """
        self.pause_loopers()
        self.reset()

        # Sequence
        seq192.select('on', 'theme0_samples_launcher')

        # Samples
        samples.set('Samples1', 'Mute', 0.0)
        samples.set('Samples2', 'Mute', 0.0)
        samples.set('Samples3', 'Mute', 0.0)
        samples.set('Samples4', 'Mute', 0.0)
        samplesFX3Reverb.set('Samples[1-4]', 'Gain', -16.0)
        samplesFX3Reverb.set('SamplesFX3Reverb', 'Mute', 0.0)
        samplesFX2Delay.set('Samples[1-4]', 'Gain', -24.0)
        samplesFX2Delay.set('SamplesFX2Delay', 'Mute', 0.0)

        # Keyboards
        jmjKeyboard.set_sound("ZDupieux")

        # Sequences (Mentat)
        self.start_scene('theme_launcher',
        lambda: [
            self.wait_next_cycle(),
            self.theme()
        ])

    @pedalboard_button(6)
    def couplet2(self):
        """
        COUPLET 2 (WANNA GET OFF)
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'couplet2_*')

        # Transport
        transport.start()

        # Vocals
        vocalsNano.set('meuf_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')

        # Synths
        synthsFX2Delay.set('Trap', 'Gain', -16.0)
        synthsFX2Delay.set('TrapFifth', 'Gain', -16.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)

        self.start_sequence('couplet1-1', [
            *[{} for i in range(12)], # bars 1 - 12
            { # bar 13
                1: lambda: [
                    vocalsKesch.set('normo_exclu', 'on'),
                    vocalsNano.set('normo_exclu', 'on'),
                    seq192.select('off', 'couplet2_*Low*')
                ]
            },
            *[{} for i in range(8)], # bars 13 - 20
            { # bar 21
                1: lambda: [
                    seq192.select('on', 'couplet2-2_*'),
                    seq192.select('on', 'couplet2_cLow_trap1'),
                    seq192.select('on', 'couplet2_cHi_trap'),
                ]
            }
        ], loop=False)

    @pedalboard_button(7)
    def pontcouplet2(self):
        """
        PONT COUPLET 2
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'pontcouplet2_cHi_trap')

        # Transport
        transport.start()


        # Synths
        synthsFX2Delay.set('Trap', 'Gain', -16.0)
        synthsFX2Delay.set('TrapFifth', 'Gain', -16.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)

        self.start_sequence('saintgermain', [
            {}, # bar 1
            { # bar 2
                1: lambda: seq192.select('on', 'pontcouplet2-2_*')
            }
        ], loop=False)

    @pedalboard_button(3)
    def couplet2_final(self):
        """
        COUPLET 2 FINAL (cf. COUPLET 1)
        """
        pass

    @pedalboard_button(4)
    def refrain2(self):
        """
        REFRAIN 2 (cf. REFRAIN)
        """
        pass

    @pedalboard_button(9)
    def theme(self):
        """
        THÈME
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'dummy')

        # Transport
        transport.start()


        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('meuf_exclu', 'on')

        # Keyboards
        jmjKeyboard.set_sound("ZDupieux")

        # Samples
        samples.set('Samples1', 'Mute', 0.0)
        samples.set('Samples2', 'Mute', 0.0)
        samples.set('Samples3', 'Mute', 0.0)
        samples.set('Samples4', 'Mute', 0.0)
        samplesFX3Reverb.set('Samples[1-4]', 'Gain', -16.0)
        samplesFX3Reverb.set('SamplesFX3Reverb', 'Mute', 0.0)
        samplesFX2Delay.set('Samples[1-4]', 'Gain', -24.0)
        samplesFX2Delay.set('SamplesFX2Delay', 'Mute', 0.0)


        # Sequences (Mentat)
        self.start_sequence('theme', [
            { # bar 1
                1: lambda: [
                    loop192.send('loop/2/hit', 'record'),
                    prodSampler.send('/instrument/play', 's:Plagiat/StickItOut/LobbyLobbyBoy', 50),
                    prodSampler.send('/instrument/play', 's:Plagiat/StickItOut/LobbyLobbyPiano', 90),
                    prodSampler.send('/instrument/play', 's:Plagiat/StickItOut/LobbyLobbyClarAigue', 85),
                    prodSampler.send('/instrument/play', 's:Plagiat/StickItOut/LobbyLobbyClarGrave', 90)
                ]
            },
            { # bar 2
            }, {}, {} # bars 2 - 4
        ], loop=True)

        self.start_sequence('theme_on_demand', [
            {}, {}, {}, {}, # bars 1 - 4
            {
                1: lambda: seq192.select('solo', 'theme_*')
            }
        ], loop=False)
