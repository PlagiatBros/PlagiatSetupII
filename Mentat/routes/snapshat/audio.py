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

            # Sequences
            seq192.select('solo', part + '_*')

            # Transport, loopers, BPM, Delays...
            #   ## Transport
            transport.start()
            #   ## Klick
            ### Default pattern

            #   ## Sooperlooper

            # Mix, FX, Synths Programs, Vocals...
            #   ## Samples
            samplesFX6Scape.set('Samples1', 'Gain', 'Gain', -6.0)
            samplesFX6Scape.set('SamplesFX6Scape', 'Gain', 'Mute', 0.0)
            samples.set('Samples1', 'Gain', 'Mute', 0.0)

            #   ## Bass
            ##### Default is dry

            #   ## Synths
            #   ## Vocals
            vocalsNano.set('gars_exclu', 'on')
            vocalsKesch.set('meuf_exclu', 'on')

            # Controllers
            #   ## Keyboards

            # Misc
            #   ## Previous sequence shutdown
            prodSampler.send("/instrument/stop", "s:Plagiat/Snapshat/Koto0")
            constantSampler.send("/instrument/stop", "s:BoringBloke")


        if part == 'couplet':
            # Sequences
            seq192.select('solo', part + '_*')

            # Transport, loopers, BPM, Delays...
            #   ## Transport
            transport.set_cycle(8)
            transport.start()
            #   ## Klick
            ### Default pattern

            #   ## Sooperlooper

            # Mix, FX, Synths Programs, Vocals...
            #   ## Samples
            samplesFX6Scape.set('Samples1', 'Gain', 'Gain', -6.0)
            samplesFX6Scape.set('SamplesFX6Scape', 'Gain', 'Mute', 0.0)
            samples.set('Samples1', 'Gain', 'Mute', 0.0)

            #   ## Bass
            ##### Default is dry

            #   ## Synths
            #   ## Vocals
            vocalsNano.set('meuf_exclu', 'on')
            vocalsKesch.set('meuf_exclu', 'on')

            # Controllers
            #   ## Keyboards

            # Misc


        if part == 'refrain':
            # Sequences
            seq192.select('solo', part + '_*')

            # Transport, loopers, BPM, Delays...
            #   ## Transport
            transport.start()

            #   ## Klick
            ### Default pattern

            #   ## Sooperlooper

            # Mix, FX, Synths Programs, Vocals...
            #   ## Samples
            samplesFX6Scape.set('Samples1', 'Gain', 'Gain', -6.0)
            samplesFX6Scape.set('SamplesFX6Scape', 'Gain', 'Mute', 0.0)
            samples.set('Samples1', 'Gain', 'Mute', 0.0)
            samples.set('Samples2', 'Gain', 'Mute', 0.0)

            #   ## Bass
            ##### Default is dry

            #   ## Synths
            #   ## Vocals
            vocalsNano.set('meuf_exclu', 'on')
            vocalsNanoFX2Delay.set('NanoMeuf', 'Gain', 'Gain', 0.0)
            vocalsNanoFX2Delay.set('VocalsNanoFX2Delay', 'Gain', 'Mute', 0.0)
            vocalsKesch.set('gars_exclu', 'on')
            vocalsKeschFX2Delay.set('KeschMeuf', 'Gain', 'Gain', 0.0)
            vocalsKeschFX2Delay.set('VocalsKeschFX2Delay', 'Gain', 'Mute', 0.0)

            # Controllers
            #   ## Keyboards

            # Misc

            # Sequences (Mentat)
            self.start_sequence('refrain')

        if part == 'contrechant':
            # Sequences
            seq192.select('on', part + '_*')

            # Mix, FX, Synths Programs, Vocals...
            #   ## Samples
            #   ## Bass
            #   ## Synths
            #   ## Vocals
            vocalsNanoFX3TrapVerb.set('NanoMeuf', 'Gain', 'Gain', -70.0) # en cas de sortie de Trap
            vocalsNanoFX3TrapVerb.set('VocalsNanoFX3TrapVerb', 'Gain', 'Mute', 1.0)

        if part == 'trap':
            # Mix, FX, Synths Programs, Vocals...
            #   ## Samples
            #   ## Bass
            #   ## Synths
            #   ## Vocals
            vocalsNanoFX3TrapVerb.set('NanoMeuf', 'Gain', 'Gain', 0.0)
            vocalsNanoFX3TrapVerb.set('VocalsNanoFX3TrapVerb', 'Gain', 'Mute', 0.0)

            # Controllers
            #   ## Keyboards
            jmjKeyboard.set_sound('LowCTrap1')

            # Misc

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
