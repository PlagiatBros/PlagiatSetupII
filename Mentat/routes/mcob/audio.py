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

        if part == 'couplet1-2': # Couplet 1 Prince/2Pac

            # Sequences
            seq192.select('solo', part + '_*')

            # Transport, loopers, BPM, Delays...
            #   ## Transport

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
            #### Barkline should always be opened

            #   ## Vocals
            vocalsNano.set('meuf_exclu', 'on')
            vocalsKesch.set('gars_exclu', 'on')

            # Controllers
            #   ## Keyboards

            # Sequences (Mentat)
            self.set_scene('sequence/princ2pac_launcher', self.scenes, 'prince2pac_launcher')

            # Misc

        if part == 'couplet1-3': # Couplet 1 Shaft (???)

            # Sequences
            seq192.select('solo', part + '_*')

            # Transport, loopers, BPM, Delays...
            #   ## Transport

            #   ## Klick
            ### Default pattern

            #   ## Sooperlooper

            # Mix, FX, Synths Programs, Vocals...
            #   ## Samples

            #   ## Bass
            ##### Default is dry

            #   ## Synths
            #### Barkline should always be opened

            #   ## Vocals
            vocalsNano.set('gars', 'on')
            vocalsNano.set('normo', 'on')
            vocalsKesch.set('gars_exclu', 'on')

            # Controllers
            #   ## Keyboards

            # Sequences (Mentat)
            self.set_scene('sequence/prince2pac_vocals_b', self.scenes, 'prince2pac_vocals_b')
            self.set_scene('sequence/prince2pac_basses_b', self.scenes, 'prince2pac_basses_b')

            # Misc


    def scenes(self, name):

        if name == 'prince2pac_launcher':

            while True:
                self.stop_scene('sequence/prince2pac_launcher')
                self.set_scene('sequence/prince2pac_vocals_a', self.scenes, 'prince2pac_vocals_a')
                self.set_scene('sequence/prince2pac_basses_a', self.scenes, 'prince2pac_basses_a')
                self.wait(4, 'beat')

        if name == 'prince2pac_vocals_a':

            while True:
                vocalsKesch.set('gars_exclu', 'on')
                self.wait(4, 'beat')
                self.wait(5*4, 'beat')

                vocalsKesch.set('gars', 'on')
                vocalsKesch.set('normo', 'on')
                self.wait(4, 'beat')
                self.wait(4, 'beat')

                vocalsKesch.set('normo_exclu', 'on')
                self.wait(4, 'beat')
                self.wait(2*4, 'beat')

                self.wait(1, 'beat')
                vocalsKesch.set('meuf', 'on')
                self.wait(1, 'beat')
                vocalsKesch.set('meuf', 'off')
                self.wait(1, 'beat')
                vocalsKesch.set('meuf', 'on')
                self.wait(1, 'beat')

                vocalsKesch.set('meuf', 'off')
                self.wait(4, 'beat')
                self.wait(3*4, 'beat')

        if name == 'prince2pac_basses_a':

            while True:
                self.wait(15*4, 'beat')
                self.wait(3, 'beat')
                self.set_scene('sequence/prince2pac_pitchdown', self.scenes, 'prince2pac_pitchdown')
                self.wait(1, 'beat')
                seq192.set('off', 'prince2pac_basssynth') # Préciser le nom de séquence # On coupe le bass synth et allez hop bass/batt

        if name == 'prince2pac_pitchdown':
            for name in outputs.submodules:
                postprocess.animate_pitch(name, 1, 0.25, 0.5, 'beat')
            self.wait(0.95, 'beat')
            for name in outputs.submodules:
                postprocess.animate_pitch(name, 0.25, 1, 0.05, 'beat')

        if name == 'prince2pac_vocals_b':
            vocalsKesch('meuf_exclu', 'on')
            vocalsKesch('normo', 'on')
            self.wait(4, 'beat')

            self.wait(2+2./3, 'beat')
            vocalsKesch('gars_exclu', 'on')
            self.wait(1./3, 'beat')
            self.wait(1, 'beat')

            self.wait(2*4, 'beat')

            vocalsKesch('gars_exclu', 'on')
            self.wait(4, 'beat')
            self.wait(2*4, 'beat')
            self.wait(3+2./3, 'beat')
            vocalsKesch('normo', 'on')
            self.wait(1./3, 'beat')

            self.wait(2*4, 'beat')

            vocalsKesch('normo_exclu', 'on')
            self.wait(2, 'beat')
            vocalsKesch('meuf', 'on')
            self.wait(2, 'beat')
            vocalsKesch('meuf', 'off')
            self.wait(3+0.5, 'beat')
            vocalsKesch('meuf', 'on')
            self.wait(0.5, 'beat')
            self.wait(1+0.5, 'beat')
            vocalsKesch('meuf', off)
            self.wait(0.5, 'beat')
            vocalsKesch('meuf', 'on')
            self.wait(1, 'beat')
            self.wait(0.5, 'beat')
            vocalsKesch('meuf', off)
            self.wait(0.5, 'beat')
            vocalsKesch('meuf', 'on')
            self.wait(4, 'beat')
            self.wait(1+0.5, 'beat')
            vocalsKesch('meuf', 'off')
            self.wait(0.5, 'beat')
            vocalsKesch('meuf', 'on')
            self.wait(2, 'beat')
            self.wait(2*4, 'beat')

        if name == 'prince2pac_basses_b':
            pass
