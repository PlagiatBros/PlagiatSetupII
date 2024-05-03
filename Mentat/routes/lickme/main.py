from ..base import *

from modules import *

class LickMe(RouteBase):
    """
    BX Me-Lezim aka Lamborghini Vroom Vroom III
    """

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
        # microtonality.disable()
        microtonality.enable()
        microtonality.set_tuning(0.35, 0, 0, 0, 0, 0.35, 0, 0, 0.35, 0, 0, 0)

        # Autotuner Notes
        notes.set_notes(1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1)

        # Mk2
        mk2Control.set_mode('cut_samples', 'cut_synths')

        # Sample
        self.set_samples_aliases({
            'ZurnaTheme': 'Samples5',
            'ZurnaLongue': 'Samples3',
            'Sitar': 'Samples4'
        })




    def open_samples_lickme(self):
        samples.set('Sitar', 'Mute', 0.0)
        samples.set('ZurnaLongue', 'Mute', 0.0)
        samples.set('ZurnaTheme', 'Mute', 0.0)


    @pedalboard_button(1)
    @mk2_button(1, 'blue')
    def stop(self):
        """
        STOP
        """
        self.pause_loopers()
        transport.stop()


    @pedalboard_button(2)
    def lickme_start(self):
        """
        Bouclage Lick Me
        """
        # Séquence
        seq192.select('solo', 'coupletlickme_zHi_diplo*')

        # Looper
        looper.record_on_start(0)

        # Tap192
        constantSampler.send('/instrument/play', 's:AirHorn', 100)

        # Transport
        self.pause_loopers()
        transport.start()

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        inputs.set('keschmic', 'dynamic')

        # Synths
        synths.set('ZDiploLike', 'Pan', -0.15)
        synths.set('ZDiploLike', 'Amp', 'Gain', 0.8)
        synths.set_lead()

        synthsFX1Reverb.set('ZDiploLike', 'Gain', -6.0)
        synthsFX1Reverb.set('SynthsFX1Reverb', 'Mute', 0.0)

        synthsFX2Delay.set('ZDiploLike', 'Gain', -18.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'GxMultiBandDelay', 'feedback', 0.3)

        # Samples
        #samples.set_lead()

        # BassFX
        bassFX.set('zynwah', 'on')
        bassFX.set('scape', 'on')

        # Séquences
        self.start_scene('sequences/start_lickme', lambda: [
            self.wait(6*4, 'beat'),
            self.wait(2, 'beat'),
            self.wait(1.2, 'beat'),
            prodSampler.send('/instrument/play', 's:BX_arpegeSitar'),
            self.wait_next_cycle(),
            self.wait(1, 'beat'),
            looper.record(0),
            self.wait_next_cycle(),
            self.run(self.policeman_lick_me)
        ])


    def policeman_lick_me(self):
        """
        Hey Mister Policeman
        """
        # Séquence
        seq192.select('solo', 'coupletlickme*')

        # Transport
        self.pause_loopers()
        transport.start()

        # Looper
        looper.trigger(0)

        # Samples
        self.open_samples_lickme()
        #samples.set_lead()

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        inputs.set('keschmic', 'dynamic')


    @mk2_button(2, 'green')
    def couplet1_lickme(self):
        """
        COUPLET 1 LICK ME (crowds & trumpets)
        """
        # Séquence
        seq192.select('solo', 'couplet1lickme*')

        # Transport
        self.pause_loopers()
        transport.start()

        # Synths
        synths.set("ZStambul", 'Pan', -0.15)
        synths.set('MajorVocals', 'Amp', 'Gain', 0.4)

        synthsFX1Reverb.set('MajorVocals', 'Gain', -9.0)
        synthsFX1Reverb.set('SynthsFX1Reverb', 'Mute', 0.0)
        synthsFX2Delay.set('MajorVocals', 'Gain', -15.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)

        # Samples
        self.open_samples_lickme()
        #samples.set_lead()


        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        inputs.set('keschmic', 'dynamic')

        # Séquence
        self.start_sequence('sequence/couplet1', [
            {
                # bar 1
                1: lambda: seq192.select('off', 'couplet1lickme_zHi_stambul'),
                2.8: lambda: seq192.select('on', 'couplet1lickme_zHi_stambul')
            },
            {},
            {},
            {},
            { # bar 5
                1: lambda: looper.trigger(0)
            },
        ], loop=False)


    @pedalboard_button(3)
    def theme_lick_me(self):
        """
        THÈME LICK ME
        """
        # Séquence
        seq192.select('solo', 'themelickme*')

        # BassFX
        bassFX.set('zynwah', 'off')
        bassFX.set('scape', 'off')


        # Transport
        self.pause_loopers()
        transport.start()

        # Audiolooper
        looper.trigger(0)

        # Samples
        self.open_samples_lickme()
        samplesFX2Delay.set('Samples5', 'Gain', -15.8)
        samplesFX2Delay.set('SamplesFX2Delay', 'Mute', 0.0)
        samplesFX3Reverb.set('Samples5', 'Gain', -12)
        samplesFX3Reverb.set('SamplesFX3Reverb', 'Mute', 0.0)
        samplesFX7Degrade.set('Samples5', 'Gain', -12)
        samplesFX7Degrade.set('SamplesFX7Degrade', 'Mute', 0.0)
        #samples.set_lead('Samples5')

        # Synths
        synths.set('MajorVocals', 'Amp', 'Gain', 0.5)
        synths.set_lead('MajorVocals')

        synthsFX1Reverb.set('MajorVocals', 'Gain', -9.0)
        synthsFX1Reverb.set('SynthsFX1Reverb', 'Mute', 0.0)
        synthsFX2Delay.set('MajorVocals', 'Gain', -15.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)

        synthsFX3Delay.set('MajorVocals', 'Gain', -17.8)
        synthsFX3Delay.set('SynthsFX3Delay', 'Mute', 0.0)

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        inputs.set('keschmic', 'dynamic')

        # Séquences
        self.start_sequence('sequence/theme_lickme_samplepitch', [
            {}, # bar 1
            {}, # bar 2
            {}, # bar 3
            { # bar 4
                1.2: lambda: postprocess.animate_pitch('Samples', 1, 0.1, 0.918, 's'),
                2.2: lambda: postprocess.animate_pitch('Samples', None, 1, 0.2, 's'),
            },
            {}, # bar 5
            {}, # bar 6
            {  # bar 7
                2.4: lambda: postprocess.animate_pitch('Samples', 1, 0.25, 0.918, 's'),
                2.8: lambda: postprocess.animate_pitch('Samples', None, 1, 0.1, 's'),
            },
            { # bar 8
                1.2: lambda: postprocess.animate_pitch('Samples', 1, 0.1, 0.918, 's'),
                3: lambda: postprocess.animate_pitch('Samples', None, 1, 0.2, 's'),
                3.62: lambda: postprocess.animate_pitch('Samples', 1, 0.1, 0.918, 's'),
                3.73: lambda: postprocess.animate_pitch('Samples', None, 1, 0.2, 's'),
                4.12: lambda: postprocess.animate_pitch('Samples', 1, 0.1, 0.918, 's'),
                4.15: lambda: postprocess.animate_pitch('Samples', None, 1, 0.2, 's'),
                4.4: lambda: postprocess.animate_pitch('Samples', 1, 0.1, 0.918, 's'),
                4.5: lambda: postprocess.animate_pitch('Samples', None, 1, 0.2, 's'),
                4.78: lambda: postprocess.animate_pitch('Samples', 1, 0.1, 0.918, 's'),
                4.85: lambda: postprocess.animate_pitch('Samples', None, 1, 0.2, 's'),
            }
        ], loop=True)

        self.start_sequence('sequence/theme_lickme_majorvocals', [
            {
                1.4: lambda: postprocess.animate_pitch('Synths', 1, 0.1, 0.515, 's'),
                3.25: lambda: postprocess.animate_pitch('Synths', None, 1, 0.1, 's'),
            }, # bar 1
            { # bar 2
                1.18: lambda: postprocess.animate_pitch('Synths', 1, 0.1, 0.515, 's'),
                2.3: lambda: postprocess.animate_pitch('Synths', None, 1, 0.1, 's'),
            },
            { # bar 3
                1.875: lambda: postprocess.animate_pitch('Synths', 1, 0.1, 0.515, 's'),
                2: lambda: postprocess.animate_pitch('Synths', None, 1, 0.1, 's'),
                2.875: lambda: postprocess.animate_pitch('Synths', 1, 0.1, 0.515, 's'),
                3.375: lambda: postprocess.animate_pitch('Synths', None, 1, 0.1, 's'),
            },
            { # bar 4
                1.2: lambda: postprocess.animate_pitch('Synths', 1, 0.1, 0.515, 's'),
                2.11: lambda: postprocess.animate_pitch('Synths', None, 1, 0.1, 's'),
            },
            {}, # bar 5
            {}, # bar 6
            {  # bar 7
                2.4: lambda: postprocess.animate_pitch('Synths', 1, 0.1, 0.515, 's'),
                2.8: lambda: postprocess.animate_pitch('Synths', None, 1, 0.1, 's'),
                4.82: lambda: postprocess.animate_pitch('Synths', 1, 0.1, 0.515, 's'),
            },
            { # bar 8
                3.1: lambda: postprocess.animate_pitch('Synths', None, 1, 0.1, 's'),
                3.62: lambda: postprocess.animate_pitch('Synths', 1, 0.1, 0.515, 's'),
                3.73: lambda: postprocess.animate_pitch('Synths', None, 1, 0.2, 's'),
                4.12: lambda: postprocess.animate_pitch('Synths', 1, 0.1, 0.515, 's'),
                4.15: lambda: postprocess.animate_pitch('Synths', None, 1, 0.2, 's'),
                4.4: lambda: postprocess.animate_pitch('Synths', 1, 0.1, 0.515, 's'),
                4.5: lambda: postprocess.animate_pitch('Synths', None, 1, 0.2, 's'),
                4.78: lambda: postprocess.animate_pitch('Synths', 1, 0.1, 0.515, 's'),
                4.85: lambda: postprocess.animate_pitch('Synths', None, 1, 0.2, 's'),
            }
        ], loop=True)

    @mk2_button(3,  'green')
    def couplet2_lickme(self):
        """
        COUPLET 2 LICK ME (sex in the metaverse)
        """
        # Séquence
        seq192.select('solo', 'couplet2lickme*')

        # Transport
        self.pause_loopers()
        transport.start()

        # Samples
        self.open_samples_lickme()
        # samples.set_lead()

        # Vocals
        vocalsNano.set('normo_exclu', 'on')
        vocalsKesch.set('normo_exclu', 'on')
        vocalsFeat.set('normo_exclu', 'on')

        inputs.set('keschmic', 'dynamic')

        # Synths
        synths.set("ZStambul", 'Pan', -0.15)
        synths.set('MajorVocals', 'Amp', 'Gain', 0.4)
        synths.set_lead()

        synthsFX1Reverb.set('MajorVocals', 'Gain', -9.0)
        synthsFX1Reverb.set('SynthsFX1Reverb', 'Mute', 0.0)
        synthsFX2Delay.set('MajorVocals', 'Gain', -15.0)
        synthsFX2Delay.set('SynthsFX2Delay', 'Mute', 0.0)

        # Séquence
        self.start_sequence('sequence/couplet2', [
            {},
            {
                3.5: lambda: postprocess.animate_pitch('Synths', 1, 0.1, 0.515, 's'),
                3.8: lambda: postprocess.animate_pitch('Synths', None, 1, 0.1, 's'),
            },
            {},
            {},
            { # bar 5
                1: lambda: seq192.select('on', 'coupletlickme*'),
                2: lambda: seq192.select('off', 'couplet2lickme*')
            },
            {},{},{},
            {}, #bar 9
            {},{},{},
            {}, # bar 12
            {}, {}, {},
            { ## bar 16
                1: lambda: looper.trigger(0)
            }
        ], loop=False)
