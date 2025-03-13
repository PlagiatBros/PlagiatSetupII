from mentat import Module

from math import log10

class Transport(Module):
    """
    Transport manager (tempo, time signature, klick pattern, playback)
    """

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.rolling = False

    def set_tempo(self, bpm):
        """
        Set tempo.
        Set sooperlooper's tempo and let jack transport do the rest (sl is transport master).
        Some delays are synced to the tempo as well.

        **Parameters**

        - `bpm`: beats per minute
        """

        self.engine.set_tempo(bpm)

        self.rolling = False

        self.engine.modules['Seq192'].set('tempo', bpm)
        self.engine.modules['AudioLooper'].set('tempo', bpm)
        self.engine.modules['Klick'].set('tempo', bpm)

        self.engine.modules['OpenStageControl'].set('tempo', bpm)

        #### TODO : Mentat devrait trouver tout seul qui a des plugs à régler en scannant les sous-modules
        # GX Multiband Delay
        for mixer, strip in [
                ('SamplesFX1Delay', 'SamplesFX1Delay'),
                ('SynthsFX2Delay', 'SynthsFX2Delay'),
                ('VocalsNanoFX1Delay', 'VocalsNanoFX1Delay'),
                ('VocalsKeschFX1Delay', 'VocalsKeschFX1Delay'),
                ('VocalsChastFX1Delay', 'VocalsChastFX1Delay'),
                ]:

            self.engine.modules[mixer].set(strip, 'GxMultiBandDelay', 'bpm', bpm)
            self.engine.modules[mixer].set(strip, 'GxMultiBandDelay', 'multiplier', 1)

        # Invada Delay + Munge (Mono In)
        for mixer, strip in [
                ('SamplesFX2Delay', 'SamplesFX2Delay'),
                ('SynthsFX3Delay', 'SynthsFX3Delay'),
                ('VocalsNanoFX2Delay', 'VocalsNanoFX2Delay'),
                ('VocalsKeschFX2Delay', 'VocalsKeschFX2Delay'),
                ('VocalsChastFX2Delay', 'VocalsChastFX2Delay'),
                ]:
            self.engine.modules[mixer].set(strip, 'Invada%20Delay%20Munge%20(mono%20in)', 'Delay%201', 60./bpm*2) # half notes
            self.engine.modules[mixer].set(strip, 'Invada%20Delay%20Munge%20(mono%20in)', 'Delay%202', 60./bpm*2) # half notes
            self.engine.modules[mixer].set(strip, 'Invada%20Delay%20Munge%20(mono%20in)', 'Feedback%201', 50) # half notes
            self.engine.modules[mixer].set(strip, 'Invada%20Delay%20Munge%20(mono%20in)', 'Feedback%202', 50) # half notes

        # Tape Delay Simulator
        for mixer, strip in [
                ('BassFX', 'BassTapeDelay'),
                ('SamplesFX5TapeDelay', 'SamplesFX5TapeDelay'),
                ('SynthsFX4TapeDelay', 'SynthsFX4TapeDelay'),
                ('VocalsNanoFX8TapeDelay', 'VocalsNanoFX8TapeDelay'),
                ('VocalsKeschFX8TapeDelay', 'VocalsKeschFX8TapeDelay'),
                ('VocalsChastFX8TapeDelay', 'VocalsChastFX8TapeDelay')
                ]:
            self.engine.modules[mixer].set(strip, 'Tape%20Delay%20Simulation', 'Tap%201%20distance%20(inches)', 60./bpm)
            self.engine.modules[mixer].set(strip, 'Tape%20Delay%20Simulation', 'Tap%202%20distance%20(inches)', 2*60./bpm)
            self.engine.modules[mixer].set(strip, 'Tape%20Delay%20Simulation', 'Tap%203%20distance%20(inches)', 3*60./bpm)
            self.engine.modules[mixer].set(strip, 'Tape%20Delay%20Simulation', 'Tap%204%20distance%20(inches)', 4*60./bpm)
            self.engine.modules[mixer].set(strip, 'Tape%20Delay%20Simulation', 'Tape%20speed%20(inches/sec%2C%201=normal)', 1.0)

        # Scape Delay
        for mixer, strip in [
                ('BassFX', 'BassScape'),
                ('SamplesFX6Scape', 'SamplesFX6Scape'),
                ('SynthsFX5Scape', 'SynthsFX5Scape'),
                ('VocalsNanoFX9Scape', 'VocalsNanoFX9Scape'),
                ('VocalsKeschFX9Scape', 'VocalsKeschFX9Scape'),
                ('VocalsChastFX9Scape', 'VocalsChastFX9Scape')
                ]:
            self.engine.modules[mixer].set(strip, 'Scape', 'bpm', bpm)

        # Wobble
        if self.engine.modules['BassFX'].get_parameter('wobble_bpm'):
            self.engine.modules['BassFX'].set('wobble_bpm', bpm)
            self.engine.modules['BassFX'].set('wobble_subdivision', 3)
        # for mixer, strip in [
        #         ('BassFX', 'BassWobble')
        #     ]:
        #     denom = 3
        #     param = (log10((bpm/60.)*denom) + 1.5) / 3
        #
        #     self.engine.modules[mixer].set(strip, 'MDA%20RezFilter', 'LFO%20Rate', param)

        # Zam Grains
        for mixer, strip in [
                ('VocalsNanoFX6Granular', 'VocalsNanoFX6Granular'),
                ('VocalsKeschFX6Granular', 'VocalsKeschFX6Granular'),
                ('VocalsChastFX6Granular', 'VocalsChastFX6Granular'),
            ]:
            self.engine.modules[mixer].set(strip, 'ZamGrains', 'Grain%20Speed', bpm/120.)
            self.engine.modules[mixer].set(strip, 'ZamGrains', 'Play%20Speed', bpm/120.)

        # Bitrot Repeater
        for mixer, strip in [
                ('VocalsNanoFX7Slice', 'VocalsNanoFX7Slice'),
                ('VocalsKeschFX7Slice', 'VocalsKeschFX7Slice'),
                ('VocalsChastFX7Slice', 'VocalsChastFX7Slice'),
            ]:
            self.engine.modules[mixer].set(strip, 'Bitrot%20Repeat', 'BPM', bpm)

        # Autofilter
        for mixer, strip in [
                ('SamplesFX4Autofilter', 'SamplesFX4Autofilter')
            ]:
            self.engine.modules[mixer].set(strip, 'AutoFilter', 'rate', 60./bpm)

        # Zam Delay
        for mixer, strip in [
            ('VocalsNano', 'NanoMeuf'),
            ('VocalsNano', 'NanoNormo'),
            ('VocalsNano', 'NanoGars'),
            ('VocalsKesch', 'KeschMeuf'),
            ('VocalsKesch', 'KeschNormo'),
            ('VocalsKesch', 'KeschGars'),
            ('VocalsChast', 'ChastMeuf'),
            ('VocalsChast', 'ChastNormo'),
            ('VocalsChast', 'ChastGars'),
            ]:
            self.engine.modules[mixer].set(strip, 'ZamDelay', 'Time', bpm/60.*250)


    def set_cycle(self, signature, pattern=None):
        """
        Set time signature (cycle length)

        **Parameters**

        - `signature`: musical time signature string ('4/4') or eigths per cycle number (legacy)
        - `pattern`:
            klick pattern (X = accented beat, x = normal beat, . = silence).
            If `None`, a default pattern is generated (straight quarter notes with an accent on beat 1)
        """

        if type(signature) in [float, int]:
            signature = '%s/8' % signature

        self.engine.set_time_signature(signature)

        eighths = int(self.engine.cycle_length * 2)

        if pattern is None:
            pattern = ''
            for i in range(eighths):
                if i == 0:
                    pattern += 'X'
                elif i % 2:
                    pattern += '.'
                else:
                    pattern += 'x'

        nom, denom = signature.split('/')
        self.engine.modules['Klick'].set('cycle', int(nom), int(denom), force_send=True)
        self.engine.modules['Klick'].set('pattern', pattern, force_send=True)

        self.engine.modules['Loop192'].set('cycle', eighths)
        self.engine.modules['AudioLooper'].set('cycle', eighths)

        self.engine.modules['OpenStageControl'].set('signature', signature)

    def start(self):
        """
        Start transport.
        Tell seq192 to start and let jack transport do the rest.
        Klick is started manually.
        """

        self.engine.start_cycle()

        self.engine.modules['Seq192'].start()

        # sooperlooper needs a cycle start hack
        self.engine.modules['AudioLooper'].start()

        self.engine.modules['Klick'].start()

        self.engine.modules['OpenStageControl'].set('rolling', 1)
        self.rolling = True

    def stop(self):
        """
        Stop transport.
        Tell seq192 to stop and let jack transport do the rest.
        Klick is stopped manually.
        """

        self.engine.modules['Seq192'].stop()

        self.engine.modules['Klick'].stop()

        self.engine.modules['OpenStageControl'].set('rolling', 0)
        self.rolling = False

    def trigger(self):
        """
        Start transport and trigger rolling loops
        """
        if self.rolling:
            for loop in self.engine.modules['AudioLooper'].submodules.values():
                if loop.get('playing'):
                    self.engine.modules['AudioLooper'].trigger(loop.get('n'))


        self.start()
