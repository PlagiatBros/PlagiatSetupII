from modules import *

class Audio():

    def part(self, part, modifier=False, *args, **kwargs):

        if not modifier:
            # stop all mentat sequences
            self.stop_scene('sequence/*')
            # pause all loops
            looper.pause()

        if part == 'stop':
            transport.stop()
            return

        # RAZ
        if not modifier:
            self.resetFX()
            self.resetSamples()


        if part == 'intro':

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
            samplesFX6Scape.set('Samples2', 'Gain', 'Gain', -5.0)
            samplesFX6Scape.set('SamplesFX6Scape', 'Gain', 'Mute', 0.0)

            samples.set('Samples1', 'Gain', 'Mute', 0.0)
            samples.set('Samples2', 'Gain', 'Mute', 0.0)
            samples.set('Samples5', 'Gain', 'Mute', 0.0)

            #   ## Bass
            ##### Default is dry

            #   ## Synths
            #   ## Vocals
            vocalsNano.set('gars_exclu', 'on')
            vocalsKesch.set('meuf_exclu', 'on')

            # Controllers
            #   ## Keyboards
            jmjKeyboard.set_scene('LowZDupieux')

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
            samplesFX6Scape.set('Samples2', 'Gain', 'Gain', -5.0)
            samplesFX6Scape.set('SamplesFX6Scape', 'Gain', 'Mute', 0.0)

            samples.set('Samples1', 'Gain', 'Mute', 0.0)
            samples.set('Samples2', 'Gain', 'Mute', 0.0)
            samples.set('Samples3', 'Gain', 'Mute', 0.0)
            samples.set('Samples5', 'Gain', 'Mute', 0.0)

            #   ## Bass
            ##### Default is dry
            bassfx.set_meta_parameter('distohi', 'on')

            #   ## Synths
            #   ## Vocals
            vocalsNano.set('meuf_exclu', 'on')
            vocalsKesch.set('meuf_exclu', 'on')

            # Controllers
            #   ## Keyboards
            jmjKeyboard.set_scene('LowZDubstep')
            #### Manque mk2 scène

            # Misc

        if part == 'couplet1-1': # Couplet 1 Trap "look"

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
            samplesFX6Scape.set('Samples2', 'Gain', 'Gain', -10.0) # attention - 10 et - 5 dans setup précédent
            samplesFX6Scape.set('SamplesFX6Scape', 'Gain', 'Mute', 0.0)

            samplesFX2Delay.set('Samples2', 'Gain', 'Gain', -9.0)
            samplesFX2Delay.set('SamplesFX2Delay', 'Gain', 'Mute', 0.0)

            samples.set('Samples1', 'Gain', 'Mute', 0.0)
            samples.set('Samples2', 'Gain', 'Mute', 0.0)
            samples.set('Samples4', 'Gain', 'Mute', 0.0)

            #   ## Bass
            ##### Default is dry

            #   ## Synths
            #   ## Vocals
            vocalsNano.set('meuf_exclu', 'on')
            vocalsKesch.set('gars_exclu', 'on')

            vocalsNanoFX3TrapVerb.set('NanoMeuf', 'Gain', 'Gain', 0.0)
            vocalsNanoFX3TrapVerb.set('VocalsNanoFX3TrapVerb', 'Gain', 'Mute', 0.0)


            # Controllers
            #   ## Keyboards
            
            # Misc


    def scenes(self, name):

        if name == 'refrain':

            while True:
                vocalsKesch.set('gars_exclu', 'on')
                self.wait(5, 'beat')
                vocalsKesch.set('meuf_exclu', 'on')
                self.wait(3, 'beat')

        if name == 'trap':

            postprocess.animate_filter('Samples', 20000, 1000, 1)
