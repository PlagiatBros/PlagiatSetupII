from ..base import *
from .video import Video
from .light import Light

from modules import *

class GrandOpening(Video, Light, RouteBase):

    def activate(self):
        """
        Called when the engine switches to this route.
        """

        super().activate()

        transport.set_tempo(100)
        transport.set_cycle('4/4')

        # Setups, banks...
        seq192.set_screenset(self.name)
        prodSampler.set_kit(self.name)

        # Microtonality
        microtonality.enable()
        microtonality.set_tuning(0, 0, 0, 0.35, 0, 0, 0, 0, 0, 0, 0.35, 0)

        # Autotuner Notes
        #               c     d     e  f     g     a     b
        notes.set_notes(1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0)

        # Mk2
        mk2Control.set_mode('cut_samples', 'cut_synths')
        chasttKeyboard.set_sound('LowCTrap1')


    @pedalboard_button(1)
    @mk2_button(1, 'blue')
    def stop(self):
        """
        STOP
        """
        self.pause_loopers()
        transport.stop()



    @pedalboard_button(2)
    @pedalboard_button(10)
    def intro(self):
        """
        INTRO (gimme twice, piano solo)
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'couplet1_pianoPitch')

        # Transport
        transport.start()

        # Keys
        jmjKeyboard.set_sound('Piano')

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        autotuneKeschNormo.set('correction', 0)
        inputs.set('keschmic', 'dynamic')

        self.start_scene('sequences/couplet1', lambda: [
            self.wait(4 * 4, 'beats'),
            self.run(self.couplet1)
        ])

    @pedalboard_button(3)
    def couplet1(self):
        """
        COUPLET 1 (ain't nobody)
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'couplet1_*')

        # Transport
        transport.start()

        # Keys
        jmjKeyboard.set_sound('Piano')

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        autotuneKeschNormo.set('correction', 1)
        inputs.set('keschmic', 'dynamic')

    @mk2_button(2, 'cyan')
    @pedalboard_button(4)
    def trumpets(self):
        """
        TRUMPETS
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'trumpets_*')

        # Transport
        transport.start()

        # Keys
        jmjKeyboard.set_sound('Piano')

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        autotuneKeschNormo.set('correction', 1)
        inputs.set('keschmic', 'dynamic')

    @mk2_button(3, 'cyan')
    @pedalboard_button(5)
    def couplet1b(self):
        """
        COUPLET 1 (ain't nobody)
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'couplet1b_*')

        # Transport
        transport.start()

        # Keys
        jmjKeyboard.set_sound('Piano')

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        autotuneKeschNormo.set('correction', 1)
        inputs.set('keschmic', 'dynamic')


    @pedalboard_button(6)
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

        # Synths
        synths.animate('ZTrumpets', 'Pan', -0.7, 0.7, 9, easing="exponential-mirror", loop=True)
        synths.animate('TenorSax', 'Pan', 0.7, -0.7, 9, easing="exponential-mirror", loop=True)
        synths.animate('Charang', 'Pan', 0.7, -0.7, 9, easing="exponential-mirror", loop=True)
        synths.set('TenorSax', 'Calf%20Mono%20Compressor', 'Bypass', 0.0)
        synths.set('TenorSax', 'Calf%20Multi%20Chorus', 'Active', 1.0)

        # Samples
        samplesFX6Scape.set('Samples1', 'Gain', -6.0)
        samplesFX6Scape.set('SamplesFX6Scape', 'Mute', 0.0)
        samples.set('Samples1', 'Mute', 0.0)
        samples.set('Samples2', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsNanoFX2Delay.set('active', 'on')
        vocalsKesch.set('normo_exclu', 'on')
        vocalsKeschFX2Delay.set('active', 'on')

        inputs.set('keschmic', 'static')

        # Sequences (Mentat)
        # self.start_sequence('refrain', {
        #     'signature': '8/4',
        #     1: lambda: vocalsKesch.set('gars_exclu', 'on'),
        #     6: lambda: vocalsKesch.set('meuf_exclu', 'on'),
        # })



    @pedalboard_button(7)
    def pont(self):
        """
        PONT
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'pont_*')

        # Transport
        transport.start()

        # Samples
        samplesFX6Scape.set('Samples1', 'Gain', -6.0)
        samplesFX6Scape.set('SamplesFX6Scape', 'Mute', 0.0)
        samples.set('Samples1', 'Mute', 0.0)

        prodSampler.send("/instrument/stop", "s:Plagiat/Snapshat/Koto0")
        constantSampler.send("/instrument/stop", "s:BoringBloke")

        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('meuf_exclu', 'on')

        inputs.set('keschmic', 'static')

        jmjKeyboard.set_sound('LowCTrap1')

    @pedalboard_button(8)
    def couplet2(self):
        """
        COUPLET 2
        """
        self.pause_loopers()
        self.reset()

        # Sequences
        seq192.select('solo', 'couplet_*')

        # Transport
        transport.start()

        # Samples
        samplesFX6Scape.set('Samples1', 'Gain', -6.0)
        samplesFX6Scape.set('SamplesFX6Scape', 'Mute', 0.0)
        samples.set('Samples1', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('meuf_exclu', 'on')
        vocalsKesch.set('meuf_exclu', 'on')

        inputs.set('keschmic', 'static')


    @mk2_button(5, 'purple')
    def contrechant(self):
        """
        CONTRECHANT (couplet)
        """
        # Sequences
        seq192.select('on', 'contrechant_*')

        # Vocals
        vocalsNanoFX3TrapVerb.set('NanoMeuf', 'Gain', -70.0) # en cas de sortie de Trap
        vocalsNanoFX3TrapVerb.set('VocalsNanoFX3TrapVerb', 'Mute', 1.0)


    @mk2_button(4, 'purple')
    def trap(self):
        """
        TRAP (couplet)
        """
        # Vocals
        vocalsNanoFX3TrapVerb.set('NanoMeuf', 'Gain', 0.0)
        vocalsNanoFX3TrapVerb.set('VocalsNanoFX3TrapVerb', 'Mute', 0.0)

        # Samples
        postprocess.animate_filter('Samples', None, 1000, 1)

        # Keyboards
        jmjKeyboard.set_sound('LowCTrap1')



    # @pedalboard_button(11)
    # def goto_mcob(self):
    #     """
    #     GOTO MCOB
    #     """
    #     engine.set_route('Mcob')
    #     engine.active_route.intro()




    @mk2_button(6, 'yellow')
    def nanomeuf(self):
        """
        VOCALS NANO ++
        """
        vocalsNano.set('meuf_exclu', 'on')

    @mk2_button(7, 'yellow')
    def nanonormo(self):
        """
        VOCALS NANO ==
        """
        vocalsNano.set('normo_exclu', 'on')

    @mk2_button(8, 'yellow')
    def nanogars(self):
        """
        VOCALS NANO --
        """
        vocalsNano.set('gars_exclu', 'on')



    @chastt_button(1)
    def chastt_note_1(self):
        chasttControlMidiOut.send('/note_on', 0, 45, 127)
        self.start_scene('chasttnoteoff', lambda: [
            self.wait(0.5, 'b'),
            chasttControlMidiOut.send('/note_off', 0, 45)
        ])
