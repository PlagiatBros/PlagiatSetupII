from ..base import *
from .video import Video
from .light import Light

from modules import *

from random import randint

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

        # Mk2
        mk2Control.set_mode('cut_samples', 'cut_synths')

        chasttKeyboard.set_sound('LowZ8bits')

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
        INTRO (KEY)
        """
        self.pause_loopers()
        self.reset()

        # Séquences
        # seq192.select('solo', 'couplet1-1_cHi_trap')
        seq192.select('solo', 'couplet1-1_sf_rhodes')


        # Transport
        transport.start()

        # Keyboards
        jmjKeyboard.set_sound('LowZRagstep')
        mk2Keyboard.set_sound('Mute')

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('meuf_exclu', 'on')

    @pedalboard_button(11)
    def intro_autoto(self):
        """
        INTRO (KEY AUTO)
        """

        self.pause_loopers()
        self.reset()

        # Séquences
        seq192.select('solo', 'dummy')


        # Transport
        transport.start()

        # Keyboards
        jmjKeyboard.set_sound('MajorVocals')
        mk2Keyboard.set_sound('Mute')

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('meuf_exclu', 'on')

        self.start_sequence('vocalpitch', [
            {
            1: lambda: jmjTranspose.set('octave-bonus', randint(-2,0)),
            1.5: lambda: jmjTranspose.set('octave-bonus', 0),
            2: lambda: jmjTranspose.set('octave-bonus', 0),
            2.5: lambda: jmjTranspose.set('octave-bonus', randint(-2,0)),
            3: lambda: jmjTranspose.set('octave-bonus', 0),
            },
        ], loop=True)

    @chastt_button(2, 'cyan')
    def couplet_1_surcouche_basse(self):
        self.start_scene('heuss', lambda: [
            self.wait_next_cycle(),
            seq192.select('on', 'heuss_*')
            ]
        )



    @mk2_button(2)
    def couplet1_1(self):
        """
        Couplet 1 (Part 1)
        """
        self.pause_loopers()
        self.reset()
        self.resetFX()

        # Loopers
        #looper.trigger(0)

        # Séquences
        seq192.select('solo', 'pont_bassslap*')

        # Transport
        transport.start()

        # Keyboards
        jmjKeyboard.set_sound('ZJestoProunk')

        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')
        vocalsChast.set('normo_exclu', 'on')

        self.engine.set('ChastNormo', 'correction', 0)

        inputs.set('keschmic', 'static')

        # Synths
        synthsFX2Delay.set('ZDupieux', 'Gain', -9.0)
        synthsFX2Delay.set('DubstepHorn', 'Gain', -9.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)

        synths.set('ZDupieux', 'Amp', 'Gain', 0.8)
        synths.set('ZTrumpets', 'Pan', 0.3)
        synths.set('DubstepHorn', 'Pan',-0.3)

        synths.set_lead('')


        self.start_scene('coupletchast', lambda: [
            self.wait(16, 'b'),
            seq192.select('solo', 'couplet1-0_*'),
            self.wait(10 * 4, 'b'),
            seq192.select('solo', 'couplet1-0up_*'),
            ])

    @pedalboard_button(3)
    def couplet1_2(self):
        """
        COUPLET 1 (Part 2)
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'allo_zLow_ragstep')

        # Transport
        transport.start()


        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')

        inputs.set('keschmic', 'dynamic')

        # Synths
        synthsFX2Delay.set('Rhodes', 'Gain', -9.0)
        synthsFX2Delay.set('EasyClassical', 'Gain', -9.0)
        synthsFX2Delay.set('TrapFifth', 'Gain', -9.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)

        self.start_sequence('couplet1-2', [
            { # bar 13
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
        vocalsKesch.set('normo_exclu', 'on')
        for name in ['KeschNormo', 'ChastNormo']:
            self.engine.set(name, 'correction', 0)

        inputs.set('keschmic', 'dynamic')


        # Synths
        synths.set('TrapFifth', 'Pan', -0.5)
        synths.set('ZDiploLike', 'Pan', 0.5)
        synths.set('Rhodes', 'Pan', 0.3)
        synths.set('DubstepHorn', 'Pan', -0.3)
        synthsFX2Delay.set('TrapFifth', 'Gain', -10.0)
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

        # Vocals
#        vocalsKesch.set('_exclu', 'on')
        inputs.set('keschmic', 'static')

        # Sequences (Mentat)
        self.start_scene('sequences/theme_launcher',
        lambda: [
            self.wait_next_cycle(),
            self.run(self.theme)
        ])


    # @pedalboard_button(6)
    @mk2_button(4)
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

        inputs.set('keschmic', 'dynamic')

        # Synths
        synthsFX2Delay.set('Trap', 'Gain', -16.0)
        synthsFX2Delay.set('TrapFifth', 'Gain', -16.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)

        # Keyboards
        jmjKeyboard.set_sound('ZJestoProunk')

        self.start_sequence('couplet1-1', [
            *[{} for i in range(12)], # bars 1 - 12
            { # bar 13
                1: lambda: [
                    vocalsKesch.set('normo_exclu', 'on'),
#                    vocalsKesch.set('gars', 'on'),
                    vocalsNano.set('normo_exclu', 'on'),
                    seq192.select('off', 'couplet2_*')
                ]
            },
            *[{} for i in range(7)], # bars 14 - 20
            { # bar 21
                1: lambda: [
                    vocalsKesch.set('gars', 'off'),
                    seq192.select('on', 'couplet2-2_*'),
                    seq192.select('on', 'couplet2_cLow_trap1'),
                    seq192.select('on', 'couplet2_cHi_trap'),
                ]
            }
        ], loop=False)

    @pedalboard_button(7)
    def pontcouplet2(self):
        """
        LOUNGE
        chastt on da bass
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

        # Keyboards
        jmjKeyboard.set_sound('ConstantSampler')
        mk2Keyboard.set_sound('LowZ8bits')
        samples.set_lead('ConstantSampler')

        # Samples
        samplesFX3Reverb.set('SamplesFX3Reverb', 'Mute', 0.0)
        samplesFX6Scape.set('SamplesFX6Scape', 'Mute', 0.0)
        samplesFX7Degrade.set('SamplesFX7Degrade', 'Mute', 0.0)

        # Vocals
        inputs.set('keschmic', 'static')


    @mk2_button(5, 'purple')
    def lounge_disco(self):
        """
        LOUNGE DISCO
        """
        seq192.select('solo', 'disco_*')
        jmjKeyboard.set_sound('ZTrumpets', lead=True)

    @mk2_button(6, 'purple')
    def lounge_drop(self):
        """
        LOUNGE DROP
        to danzz
        """
        self.pause_loopers()
        self.reset()

        jmjKeyboard.set_sound('ZDupieux', lead=False)
        seq192.select('solo', 'daftdrunk_*')
        synths.animate('ZTrumpets', 'Amp', 'Gain', 0,  1, 8*4, mode='b', easing='exponential')
        self.start_scene('droplounge', lambda: [
            self.wait(4*7, 'b'),
            jmjKeyboard.set_sound('MajorVocals', lead=True),
            self.wait(4*1, 'b'),
            seq192.select('solo', 'aceofbaise_*')
        ])

        # Transport
        transport.start()


    @pedalboard_button(8)
    def couplet2_final(self):
        """
        COUPLET 2 FINAL (cf. COUPLET 1)
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

        inputs.set('keschmic', 'dynamic')




        # Synths
        synths.animate('MajorVocals', 'Pan', 0.8,  -0.8, 4,  loop=True)
        synths.animate('Trap', 'Pan', -0.8, 0.8, 4, easing='random', loop=True)

        synthsFX2Delay.set('Rhodes', 'Gain', -9.0)
        synthsFX2Delay.set('EasyClassical', 'Gain', -9.0)
        synthsFX2Delay.set('TrapFifth', 'Gain', -9.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)

        jmjKeyboard.set_sound('ZTrumpets', lead=False)


    @pedalboard_button(4)
    def refrain2(self):
        """
        REFRAIN 2 (cf. REFRAIN)
        """
        pass

    def theme(self, auto=True):
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
        vocalsKesch.set('normo_exclu', 'on')

        inputs.set('keschmic', 'static')

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

        midipanic.reset()

        # Sequences (Mentat)
        self.start_sequence('theme', [
            { # bar 1
                1: lambda: [
#                    loop192.send('loop/2/hit', 'record'),
                    prodSampler.send('/instrument/play', 's:Plagiat/StickItOut/LobbyLobbyBoy', 50),
                    prodSampler.send('/instrument/play', 's:Plagiat/StickItOut/LobbyLobbyPiano', 90),
                    prodSampler.send('/instrument/play', 's:Plagiat/StickItOut/LobbyLobbyClarAigue', 85),
                    prodSampler.send('/instrument/play', 's:Plagiat/StickItOut/LobbyLobbyClarGrave', 90)
                ]
            },
            { # bar 2
            }, {}, {} # bars 2 - 4
        ], loop=True)


        self.start_scene('sequences/theme_on_demand', lambda: [
            self.wait(16),
            self.run(self.theme_mesh, pitch=True)
        ])

    @pedalboard_button(9)
    def theme_launcher_2(self):
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

        # Vocals
#        vocalsKesch.set('_exclu', 'on')

        # Sequences (Mentat)
        self.start_scene('sequences/theme_launcher',
            lambda: [
                self.wait_next_cycle(),
                self.run(self.theme2)
                ])


    def theme2(self):
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
                    midipanic.reset(),
#                    loop192.send('loop/2/hit', 'record'),
                    prodSampler.send('/instrument/play', 's:Plagiat/StickItOut/LobbyLobbyBoy', 50),
                    prodSampler.send('/instrument/play', 's:Plagiat/StickItOut/LobbyLobbyPiano', 90),
                    prodSampler.send('/instrument/play', 's:Plagiat/StickItOut/LobbyLobbyClarAigue', 85),
                    prodSampler.send('/instrument/play', 's:Plagiat/StickItOut/LobbyLobbyClarGrave', 90)
                ]
            },
            { # bar 2
            }, {}, {} # bars 2 - 4
        ], loop=True)


    @pedalboard_button(10)
    def theme_mesh(self, pitch=False):
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('on', 'theme_*')

        # Transport
        transport.start()


        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')

        inputs.set('keschmic', 'static')

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

        self.start_sequence('theme', [
            { # bar 1
                1: lambda: [
                    midipanic.reset(),
#                    loop192.send('loop/2/hit', 'record'),
                    prodSampler.send('/instrument/play', 's:Plagiat/StickItOut/LobbyLobbyBoy', 50),
                    prodSampler.send('/instrument/play', 's:Plagiat/StickItOut/LobbyLobbyPiano', 90),
                    prodSampler.send('/instrument/play', 's:Plagiat/StickItOut/LobbyLobbyClarAigue', 85),
                    prodSampler.send('/instrument/play', 's:Plagiat/StickItOut/LobbyLobbyClarGrave', 90)
                ]
            },
            { # bar 2
            }, {}, {} # bars 2 - 4
        ], loop=True)

        if pitch:
            self.start_sequence('pitchdown', [
                {
                    1: lambda: postprocess.animate_pitch('*', 1.0, 0.25, 0.4),
                    1.65: lambda: postprocess.animate_pitch('*', 0.25, 1.0, 0.1)
                },
                {},{},{},
                {},{},{},{},
            ], loop=True)
        else:
            bassfx.set('distohi', 'on')


    @mk2_button(7, 'cyan')
    def theme_2(self):
        self.theme_mesh(True)

    @mk2_button(8, 'blue')
    def organ(self):
        self.stop()

        # Keyboards
        jmjKeyboard.set_sound("ZOrgan")




    """
    St Germain Controls
    """
    @gui_button(
        type='button',
        mode='push',
        label='Reverb',
        preArgs='Gain',
        on=0,
        off=-70,
        address='/SamplesFX3Reverb/ConstantSampler',
        height=80
    )
    def samples_reverb(self):
        pass

    @gui_button(
        type='button',
        mode='push',
        label='Scape',
        preArgs='Gain',
        on=0,
        off=-70,
        address='/SamplesFX6Scape/ConstantSampler',
        height=80
    )
    def samples_scape(self):
        pass

    @gui_button(
        type='fader',
        html='Degrade (@{this}dB)',
        horizontal=True,
        design='compact',
        address='/SamplesFX7Degrade/ConstantSampler',
        preArgs='Gain',
        range={'min':-70, 'max': 6},
        height=80
        )
    def samples_degrade(self):
        pass

    @gui_button(
        type='button',
        label='seq pontcoulet',
        mode='tap',
        design='compact',
        address='/Seq192/call',
        preArgs=['select', 'toggle'],
        on='aceofbaise*',
        height=80
        )
    def seq_pontcoulet(self):
        pass



    @chastt_button(8, 'red')
    def bassactive(self):
        seq192.select('toggle', 'lounge_zLow_8bits')


    @chastt_button(3, 'blue')
    def clapit(self):
        constantSampler.send('/instrument/play', 's:Clap', 100)

    @chastt_button(5, 'blue')
    def stickit(self):
        constantSampler.send('/instrument/play', 's:Stick', 100)

    #
    # @chastt_button(1)
    # def chastt_note_5(self):
    #     self.engine.modules['ConstantSampler'].send('/instrument/play', 's:Plagiat/ConstantKit/Clap', 127)
    #
    # @chastt_button(2)
    # def chastt_note_6(self):
    #     self.engine.modules['ConstantSampler'].send('/instrument/play', 's:Plagiat/ConstantKit/Stick', 127)
    #
    #
    # @chastt_button(3)
    # def chastt_note_7(self):
    #     self.engine.modules['ConstantSampler'].send('/instrument/stop', 's:Plagiat/ConstantKit/Jajaja_Bourvil')
    #     self.engine.modules['ConstantSampler'].send('/instrument/play', 's:Plagiat/ConstantKit/Jajaja_Bourvil', 127)
    #     self.start_scene('stopbourvil', lambda: [
    #         self.wait(0.5, 'b'),
    #         self.engine.modules['ConstantSampler'].send('/instrument/stop', 's:Plagiat/ConstantKit/Jajaja_Bourvil')
    #     ])
    #
    # @chastt_button(4)
    # def chastt_note_8(self):
    #     self.engine.modules['ConstantSampler'].send('/instrument/stop', 's:Plagiat/ConstantKit/Jajaja_Busta')
    #     self.engine.modules['ConstantSampler'].send('/instrument/play', 's:Plagiat/ConstantKit/Jajaja_Busta', 127)
    #     self.start_scene('stopbourvil', lambda: [
    #         self.wait(0.4, 'b'),
    #         self.engine.modules['ConstantSampler'].send('/instrument/stop', 's:Plagiat/ConstantKit/Jajaja_Busta')
    #     ])
