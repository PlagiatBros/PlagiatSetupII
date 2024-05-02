from ..base import *
from .video import Video
from .light import Light

from modules import *

class RamenerMooncup(Video, Light, RouteBase):

    def activate(self):
        """
        Called when the engine switches to this route.
        """

        super().activate()

        transport.set_tempo(150)
        transport.set_cycle('4/4')

        # Setups, banks...
        seq192.set_screenset(self.name)
        prodSampler.set_kit(self.name)

        # Microtonality
        microtonality.enable()
        microtonality.set_tuning(0, 0, 0, 0, 0, 0.35, 0, 0, -0.35, 0, 0.35, 0)

        # Autotuner Notes
        #               c     d     e  f     g     a     b
        notes.set_notes(1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0)

        # Mk2
        mk2Control.set_mode('cut_samples')



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
        samples.set('Samples1', 'Mute', 0.0)
        samples.set('Samples2', 'Mute', 0.0)
        samples.set('Samples3', 'Mute', 0.0)
        samples.set('Samples4', 'Mute', 0.0)
        samples.set('Samples5', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('meuf_exclu', 'on')

        inputs.set('keschmic', 'static')

    @mk2_button(2, 'purple')
    def couplet1(self):
        """
        COUPLET 1
        """
        # Samples
        samples.set('Samples1', 'Mute', 0.0)
        samples.set('Samples[1-5]', 'Gain', -9.0)
        samplesFX3Reverb.set('Samples[1-5]', 'Gain', -12.0)
        samplesFX3Reverb.set('SamplesFX3Reverb', 'Mute', 0.0)
        samplesFX2Delay.set('Samples[2-4]', 'Gain', -16.0)
        samplesFX2Delay.set('SamplesFX2Delay', 'Mute', 0.0)
        postprocess.animate_pitch('*', 1, 0.25, 0.75)

        # TODO ???: envoyer samples dans la reverb
        # TODO ???: stereo samples

        # Looper
        looper.record(0)


        # Vocals
        inputs.set('keschmic', 'static')

        # Sequences (Mentat)
        self.start_scene('sequences/couplet1_delayed', lambda:[
            self.wait_next_cycle(),
            postprocess.animate_pitch('*', None, 1, 0.1),

            self.start_sequence('couplet', [
                *[{} for i in range(7)], # bars 1 - 7
                { # bar 8
                    4: lambda: looper.record(0),
                    4.9: inputs.set('keschmic', 'dynamic')
                },
                *[{} for i in range(29)], # bars 9 - 21
                { # bar 22
                    1: lambda: postprocess.animate_pitch(['Samples', 'Synth*'], 1, 0.25, 1),
                    2: lambda: seq192.select('solo', 'dummy'),
                    2 + 0.4: lambda: postprocess.animate_pitch(['Samples', 'Synths'], None, 1, 0.1),
                    2 + 1/2. : lambda: [
                        samples.set('Samples[1-5]', 'Gain', -9.0),
                        samplesFX2Delay.set('Samples[2-4]', 'Gain', -16.0),
                        samplesFX6Scape.set('Samples1', 'Gain', -12.0),
                        samplesFX5TapeDelay.set('Samples[1-5]', 'Gain', -18.0),
                        samplesFX2Delay.set('SamplesFX2Delay', 'Mute', 0.0),
                        samplesFX6Scape.set('SamplesFX6Scape', 'Mute', 0.0),
                        samplesFX5TapeDelay.set('SamplesFX5TapeDelay', 'Mute', 0.0),

                        # Sequences
                        seq192.select('solo', 'couplet1_*'),
                        seq192.select('on', 'intro_samples_voix4'),

                        # Vocals
                        vocalsNano.set('meuf_exclu', 'on'),
                        vocalsKesch.set('gars_exclu', 'on')
                    ],
                },
            ], loop=False)


        ])

    @mk2_button(3, 'purple')
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
        samples.set('Samples1', 'Mute', 0.0)
        samplesFX2Delay.set('Samples1', 'Gain', -3.0),
        samplesFX6Scape.set('Samples1', 'Gain', -18.0),
        samplesFX5TapeDelay.set('Samples1', 'Gain', -6.0),
        samplesFX2Delay.set('SamplesFX2Delay', 'Mute', 0.0),
        samplesFX2Delay.set('SamplesFX2Delay', 'Invada%20Delay%20Munge%20(mono%20in)', 'Delay%201', 0.342)
        samplesFX2Delay.set('SamplesFX2Delay', 'Invada%20Delay%20Munge%20(mono%20in)', 'Delay%202', 1.09)
        samplesFX2Delay.set('SamplesFX2Delay', 'ReverseDelay', 'Wet', -5)
        samplesFX6Scape.set('SamplesFX6Scape', 'Mute', 0.0),
        samplesFX5TapeDelay.set('SamplesFX5TapeDelay', 'Mute', 0.0),

        # Sequences (Mentat)
        self.start_sequence('delays', [
            { 'signature': '25/4', # bar 1
                1: lambda: samplesFX5TapeDelay.animate('SamplesFX5TapeDelay', 'Tape%20Delay%20Simulation', 'Tape%20speed%20(inches/sec%2C%201=normal)', 1.0, 0.3, 14),
                14: lambda: samplesFX5TapeDelay.animate('SamplesFX5TapeDelay', 'Tape%20Delay%20Simulation', 'Tape%20speed%20(inches/sec%2C%201=normal)', 0.3, 1.0, 9)
            }
        ], loop=True)

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')

        inputs.set('keschmic', 'static')

    @mk2_button(4, 'purple')
    def couplet2_intro(self):
        """
        COUPLET 2 (INTRO)
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'couplet2-1_*')

        # Transport
        transport.start()

        # Samples
        samplesFX2Delay.set('Samples1', 'Gain', -18.0),
        samplesFX2Delay.set('SamplesFX2Delay', 'Mute', 0.0),
        samples.set('Samples[1-5]', 'Mute', 0.0)

        # Keyboards
        jmjKeyboard.set_sound('LowZDancestep')

        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')
        vocalsKesch.set('meuf', 'on')

        inputs.set('keschmic', 'dynamic')

    @pedalboard_button(4)
    def couplet2_main(self):
        """
        COUPLET 2 (MAIN - "Should I...")
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'couplet2-2_*')

        # Transport
        transport.start()

        # Samples
        samples.set('Samples[1-4]', 'Mute', 0.0)

        samplesFX4Autofilter.set('Samples2', 'Gain', -6.0)
        samplesFX4Autofilter.set('Samples3', 'Gain', 6.0)
        samplesFX4Autofilter.set('SamplesFX4Autofilter', 'Mute', 0.0)

        samplesFX5TapeDelay.set('Samples1', 'Gain', -3.0)
        samplesFX5TapeDelay.set('Samples2', 'Gain', -3.0)
        samplesFX5TapeDelay.set('Samples3', 'Gain', -6.0)
        samplesFX5TapeDelay.set('Samples4', 'Gain', -9.0)
        samplesFX5TapeDelay.set('SamplesFX5TapeDelay', 'Mute', 0.0)

        samplesFX7Degrade.set('Samples1', 'Gain', -6.0)
        samplesFX7Degrade.set('Samples2', 'Gain', -6.0)
        samplesFX7Degrade.set('Samples3', 'Gain', 6.0)
        samplesFX7Degrade.set('Samples4', 'Gain', -12.0)
        samplesFX7Degrade.set('SamplesFX7Degrade', 'Mute', 0.0)


        samplesFX6Scape.set('SamplesFX7Degrade', 'Gain', -6.0)
        samplesFX6Scape.set('SamplesFX6Scape', 'Mute', 0.0)



        # Keyboards
        jmjKeyboard.set_sound('LowZDubstep')

        # Vocals
        vocalsNano.set('meuf_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')

        # Sequences (Mentat)
        self.start_sequence('couplet_fuckedup', [
            { # bar 1
            1: lambda: [
                samplesFX5TapeDelay.animate('SamplesFX5TapeDelay', 'Tape%20Delay%20Simulation', 'Tape%20speed%20(inches/sec%2C%201=normal)', 1.0, 0.3, 8, easing='exponential'),
                samplesFX5TapeDelay.set('Samples1', 'Gain', -3.0),
                samplesFX5TapeDelay.set('Samples2', 'Gain', -3.0),
                samplesFX5TapeDelay.set('Samples3', 'Gain', -6.0),
                samplesFX5TapeDelay.set('Samples4', 'Gain', -9.0),
                samples.set('Samples[1-4]', 'Mute', 0.0),
                samplesFX4Autofilter.set('SamplesFX4Autofilter', 'Mute', 0.0),
                samplesFX6Scape.set('SamplesFX6Scape', 'Mute', 0.0),
                samplesFX7Degrade.set('SamplesFX7Degrade', 'Mute', 0.0)
                ]
            },
            { # bar 2
            4.5: lambda: [
                samples.set('Samples[1-4]', 'Mute', 1.0),
                samplesFX4Autofilter.set('SamplesFX4Autofilter', 'Mute', 1.0),
                samplesFX6Scape.set('SamplesFX6Scape', 'Mute', 1.0),
                samplesFX7Degrade.set('SamplesFX7Degrade', 'Mute', 1.0),
                samplesFX5TapeDelay.set('Samples1', 'Gain', -70.0),
                samplesFX5TapeDelay.set('Samples2', 'Gain', -70.0),
                samplesFX5TapeDelay.set('Samples3', 'Gain', -70.0),
                samplesFX5TapeDelay.set('Samples4', 'Gain', -70.0),
                ]
            }
        ], loop=True)

        self.start_sequence('couplet2-2', [
            *[{} for i in range(15)], # bars 1 - 15
            { # bar 16
                3 + 1/2.: lambda: [

                    # Looper
                    looper.unpause(0),

                    # Vocals
                    vocalsKesch.set('meuf_exclu', 'on')
                ]
            },
            { # bar 17
                1: lambda: [
                    # Samples
                    samples.set('Samples[1-5]', 'Mute', 0.0),

                    # Sequences
                    seq192.select('solo', 'couplet2-3*'),

                    # Vocals
                    vocalsNano.set('gars_exclu', 'on')
                ]
            }
        ], loop=False)

    @mk2_button(3, 'purple')
    def refrain2(self):
        """
        REFRAIN (cf. REFRAIN)
        """
        pass

    @pedalboard_button(5)
    def refrain_messe(self):
        """
        REFRAIN MESSE
        """
        self.pause_loopers()
        self.reset()

        # Transport
        transport.stop()

        # Keyboards
        jmjKeyboard.set_sound('ZOrgan')

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')

        inputs.set('keschmic', 'static')

    @pedalboard_button(6)
    def disco(self):
        """
        DISCO
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'disco_*')

        # Transport
        transport.start()

        # Samples
        samples.set('Samples1', 'Mute', 0.0)

        # Keyboards
        jmjKeyboard.set_sound('ZTrumpets', boost=True)

        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')

        inputs.set('keschmic', 'static')

    @mk2_button(5)
    def startingblocks(self):
        """
        RELANCE STARTING BLOCKS
        """
        self.pause_loopers()
        self.reset()

        # Looper
        looper.trigger('0')

        # Séquences
        seq192.select('solo', 'disco_*')

        # Samples
        samples.set('Samples1', 'Mute', 0.0)

        # Transport
        transport.start()


    @pedalboard_button(7)
    def disco2(self):
        """
        DISCO 2 DROP THE BASS
        """
        self.disco()
        # Keyboards
        jmjKeyboard.set_sound('LowZDubstep')


    @pedalboard_button(8)
    def ramener_launcher(self):
        """
        RAMENER LAUNCHER
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'ramener0_*')

        # Transport
        transport.start()

        # Samples
        samples.set('Samples1', 'Mute', 0.0)
        samples.set('Samples2', 'Mute', 0.0)

        # Keyboards
        jmjKeyboard.set_sound('LowZDancestep')

        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')

        inputs.set('keschmic', 'static')

        self.start_sequence('ramener', [
            {}, {}, # bars 1-2
            {
                3: lambda: postprocess.animate_pitch('Samples', None, 0.25, 2),
                4 + 1/2.: lambda: seq192.select('solo', 'dummy')
            },
            {
                1: lambda: [
                    seq192.select('solo', 'ramener*'),
                    postprocess.animate_pitch('Samples', None, 1, 0.1),
                ]
            }
        ], loop=False)


    @pedalboard_button(9)
    def ramener_mesh(self):
        """
        RAMENER MESSHUGAH
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'dummy')

        # Transport
        transport.start()

        # Samples
        samples.set('Samples1', 'Mute', 0.0)
        constantSampler.send('/instrument/play', 's:Plagiat/ConstantKit/AirHorn', 100)

        # Vocals
        vocalsNano.set('meuf_exclu', 'on')
        vocalsNano.set('normo', 'on')
        vocalsNano.set('gars', 'on')
        vocalsNanoFX2Delay.set('Nano*', 'Gain', 0.0)
        vocalsNanoFX2Delay.set('VocalsNanoFX2Delay', 'Mute', 0.0)
        vocalsKesch.set('meuf_exclu', 'on')
        vocalsKesch.set('normo', 'on')
        vocalsKesch.set('gars', 'on')
        vocalsKeschFX2Delay.set('Kesch*', 'Gain', 0.0)
        vocalsKeschFX2Delay.set('VocalsKeschFX2Delay', 'Mute', 0.0)

        inputs.set('keschmic', 'static')


        self.start_sequence('ramener', [
            {
                3: lambda: postprocess.animate_pitch('Samples', 1, 0.25, 2),
                4 + 1/2.: lambda: seq192.select('solo', 'dummy')
            },
            {
                1: lambda: [
                    seq192.select('solo', 'ramener*'),
                    samples.set('Samples1', 'Mute', 0.0),
                    postprocess.animate_pitch('Samples', None, 1, 0.1)
                ]
            }
        ], loop=False)

        bassfx.set('distohi', 'on')

    @pedalboard_button(10)
    def ramener(self):
        """
        RAMENER
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'ramener*')

        # Transport
        transport.start()

        # Samples
        samples.set('Samples1', 'Mute', 0.0)


        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')

        inputs.set('keschmic', 'static')

    @gui_button()
    def ramener_synth_on(self):
        """
        TRANSE SYNTH ON
        """
        seq192.select('on', 'ramener1*')

    @gui_button()
    def ramener_synth_off(self):
        """
        TRANSE SYNTH OFF
        """
        seq192.select('off', 'ramener1*')


    @mk2_button(6, 'yellow')
    def nanogars(self):
        """
        VOCALS NANO GARS
        """
        vocalsNano.set('gars_exclu', 'on')

    @mk2_button(7, 'yellow')
    def nanomeuf(self):
        """
        VOCALS NANO MEUF
        """
        vocalsNano.set('meuf_exclu', 'on')

    @mk2_button(8, 'yellow')
    def nanonormo(self):
        """
        VOCALS NANO NORMO
        """
        vocalsNano.set('normo_exclu', 'on')
