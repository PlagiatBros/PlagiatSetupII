from modules import *

class Audio():

    def part(self, part, modifier=False, *args, **kwargs):

        if not modifier:
            # stop all mentat sequences
            self.stop_sequence('*')
            # pause all loops
            looper.pause()

        if part == 'stop':
            transport.stop()
            return

        # RAZ
        if not modifier:
            self.resetFX()
            self.resetSamples()

        if part == 'pont':
            """
            PONT / INTRO
            """

            # Sequences
            seq192.select('solo', part + '_*')

            # Transport
            transport.start()

            # Samples
            samplesFX6Scape.set('Samples1', 'Gain', 'Gain', -6.0)
            samplesFX6Scape.set('SamplesFX6Scape', 'Gain', 'Mute', 0.0)
            samples.set('Samples1', 'Gain', 'Mute', 0.0)

            prodSampler.send("/instrument/stop", "s:Plagiat/Snapshat/Koto0")
            constantSampler.send("/instrument/stop", "s:BoringBloke")

            # Vocals
            vocalsNano.set('gars_exclu', 'on')
            vocalsKesch.set('meuf_exclu', 'on')

        if part == 'couplet':
            """
            COUPLET
            """

            # Sequences
            seq192.select('solo', part + '_*')

            # Transport
            transport.start()

            # Samples
            samplesFX6Scape.set('Samples1', 'Gain', 'Gain', -6.0)
            samplesFX6Scape.set('SamplesFX6Scape', 'Gain', 'Mute', 0.0)
            samples.set('Samples1', 'Gain', 'Mute', 0.0)

            # Vocals
            vocalsNano.set('meuf_exclu', 'on')
            vocalsKesch.set('meuf_exclu', 'on')

        if part == 'refrain':
            """
            REFRAIN
            """

            # Sequences
            seq192.select('solo', part + '_*')

            # Transport
            transport.start()

            # Samples
            samplesFX6Scape.set('Samples1', 'Gain', 'Gain', -6.0)
            samplesFX6Scape.set('SamplesFX6Scape', 'Gain', 'Mute', 0.0)
            samples.set('Samples1', 'Gain', 'Mute', 0.0)
            samples.set('Samples2', 'Gain', 'Mute', 0.0)

            # Vocals
            vocalsNano.set('meuf_exclu', 'on')
            vocalsNanoFX2Delay.set('NanoMeuf', 'Gain', 'Gain', 0.0)
            vocalsNanoFX2Delay.set('VocalsNanoFX2Delay', 'Gain', 'Mute', 0.0)
            vocalsKesch.set('gars_exclu', 'on')
            vocalsKeschFX2Delay.set('KeschMeuf', 'Gain', 'Gain', 0.0)
            vocalsKeschFX2Delay.set('VocalsKeschFX2Delay', 'Gain', 'Mute', 0.0)

            # Sequences (Mentat)
            self.start_sequence('refrain')

        if part == 'contrechant':
            """
            CONTRECHANT
            """

            # Sequences
            seq192.select('on', part + '_*')

            # Vocals
            vocalsNanoFX3TrapVerb.set('NanoMeuf', 'Gain', 'Gain', -70.0) # en cas de sortie de Trap
            vocalsNanoFX3TrapVerb.set('VocalsNanoFX3TrapVerb', 'Gain', 'Mute', 1.0)

        if part == 'trap':
            """
            TRAP
            """

            # Vocals
            vocalsNanoFX3TrapVerb.set('NanoMeuf', 'Gain', 'Gain', 0.0)
            vocalsNanoFX3TrapVerb.set('VocalsNanoFX3TrapVerb', 'Gain', 'Mute', 0.0)

            # Keyboards
            jmjKeyboard.set_sound('LowCTrap1')

            # Sequences (Mentat)
            self.start_sequence('trap')


        if part == 'goto_mcob':

            engine.set_route('mcob')
            engine.active_route.part('intro')

        if part == 'nanomeuf':
            vocalsNano.set('meuf_exclu', 'on')

        if part == 'nanonormo':
            vocalsNano.set('normo_exclu', 'on')

        if part == 'nanogars':
            vocalsNano.set('gars_exclu', 'on')


    def sequences(self, name):

        if name == 'refrain':

            while True:
                vocalsKesch.set('gars_exclu', 'on')
                self.wait(5, 'beat')
                vocalsKesch.set('meuf_exclu', 'on')
                self.wait(3, 'beat')

        if name == 'trap':

            postprocess.animate_filter('Samples', 20000, 1000, 1)
