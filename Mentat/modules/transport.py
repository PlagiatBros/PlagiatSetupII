from mentat import Module

class Transport(Module):
    """
    Transport manager (tempo, time signature, klick pattern, playback)
    """

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

    def set_tempo(self, bpm):
        """
        Set tempo.
        Set sooperlooper's tempo and let jack transport do the rest (sl is transport master).
        Some delays are synced to the tempo as well.

        **Parameters**

        - `bpm`: beats per minute
        """

        self.engine.set_tempo(bpm)

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
                ('VocalsKeschFX1Delay', 'VocalsKeschFX1Delay')
                ]:
            if strip in self.engine.modules[mixer].submodules:
                self.engine.modules[mixer].set(strip, 'GxMultiBandDelay', 'DELAY1', bpm)
                self.engine.modules[mixer].set(strip, 'GxMultiBandDelay', 'DELAY2', bpm)
                self.engine.modules[mixer].set(strip, 'GxMultiBandDelay', 'DELAY3', bpm)
                self.engine.modules[mixer].set(strip, 'GxMultiBandDelay', 'DELAY4', bpm)
                self.engine.modules[mixer].set(strip, 'GxMultiBandDelay', 'DELAY5', bpm)
            else:
                # just in case non mixer infos are not loaded yet
                self.start_scene(strip + '_bpm', lambda: [
                    self.wait(1, 's'),
                    self.engine.modules[mixer].set(strip, 'GxMultiBandDelay', 'DELAY1', bpm),
                    self.engine.modules[mixer].set(strip, 'GxMultiBandDelay', 'DELAY2', bpm),
                    self.engine.modules[mixer].set(strip, 'GxMultiBandDelay', 'DELAY3', bpm),
                    self.engine.modules[mixer].set(strip, 'GxMultiBandDelay', 'DELAY4', bpm),
                    self.engine.modules[mixer].set(strip, 'GxMultiBandDelay', 'DELAY5', bpm)
                ])

        # Invada Delay + Munge (Mono In)
        for mixer, strip in [
                ('SamplesFX2Delay', 'SamplesFX2Delay'),
                ('SynthsFX3Delay', 'SynthsFX3Delay'),
                ('VocalsNanoFX2Delay', 'VocalsNanoFX2Delay'),
                ('VocalsKeschFX2Delay', 'VocalsKeschFX2Delay')
                ]:
            if strip in self.engine.modules[mixer].submodules:
                self.engine.modules[mixer].set(strip, 'Invada%20Delay%20Munge%20(mono%20in)', 'Delay%201', 60./bpm)
                self.engine.modules[mixer].set(strip, 'Invada%20Delay%20Munge%20(mono%20in)', 'Delay%202', 60./bpm)
            else:
                # just in case non mixer infos are not loaded yet
                self.start_scene(strip + '_bpm', lambda: [
                    self.wait(1, 's'),
                    self.engine.modules[mixer].set(strip, 'Invada%20Delay%20Munge%20(mono%20in)', 'Delay%201', 60./bpm),
                    self.engine.modules[mixer].set(strip, 'Invada%20Delay%20Munge%20(mono%20in)', 'Delay%202', 60./bpm)
                ])

        # Tape Delay Simulator
        for mixer, strip in [
                ('BassFX', 'BassTapeDelay'),
                ('SamplesFX5TapeDelay', 'SamplesFX5TapeDelay'),
                ('SynthsFX4TapeDelay', 'SynthsFX4TapeDelay'),
                ('VocalsNanoFX8TapeDelay', 'VocalsNanoFX8TapeDelay'),
                ('VocalsKeschFX8TapeDelay', 'VocalsKeschFX8TapeDelay')
                ]:
            if strip in self.engine.modules[mixer].submodules:
                self.engine.modules[mixer].set(strip, 'Tape%20Delay%20Simulation', 'Tap%201%20distance%20(inches)', 60./bpm)
                self.engine.modules[mixer].set(strip, 'Tape%20Delay%20Simulation', 'Tap%202%20distance%20(inches)', 2*60./bpm)
                self.engine.modules[mixer].set(strip, 'Tape%20Delay%20Simulation', 'Tap%203%20distance%20(inches)', 3*60./bpm)
                self.engine.modules[mixer].set(strip, 'Tape%20Delay%20Simulation', 'Tap%204%20distance%20(inches)', 4*60./bpm)
            else:
                # just in case non mixer infos are not loaded yet
                self.start_scene(strip + '_bpm', lambda: [
                    self.wait(1, 's'),
                self.engine.modules[mixer].set(strip, 'Tape%20Delay%20Simulation', 'Tap%201%20distance%20(inches)', 60./bpm),
                self.engine.modules[mixer].set(strip, 'Tape%20Delay%20Simulation', 'Tap%202%20distance%20(inches)', 2*60./bpm),
                self.engine.modules[mixer].set(strip, 'Tape%20Delay%20Simulation', 'Tap%203%20distance%20(inches)', 3*60./bpm),
                self.engine.modules[mixer].set(strip, 'Tape%20Delay%20Simulation', 'Tap%204%20distance%20(inches)', 4*60./bpm)
                ])

        # Scape Delay
        for mixer, strip in [
                ('BassFX', 'BassScape'),
                ('SamplesFX6Scape', 'SamplesFX6Scape'),
                ('SynthsFX5Scape', 'SynthsFX5Scape'),
                ('VocalsNanoFX9Scape', 'VocalsNanoFX9Scape'),
                ('VocalsKeschFX9Scape', 'VocalsKeschFX9Scape')
                ]:
            if strip in self.engine.modules[mixer].submodules:
                self.engine.modules[mixer].set(strip, 'Scape', 'bpm', bpm)
            else:
                # just in case non mixer infos are not loaded yet
                self.start_scene(strip + '_bpm', lambda: [
                    self.wait(1, 's'), self.engine.modules[mixer].set(strip, 'Scape', 'bpm', bpm)
                ])

        # Wobble
        for mixer, strip in [
                ('BassFX', 'BassWobble')
            ]:
            if strip in self.engine.modules[mixer].submodules:
                self.engine.modules[mixer].set(strip, 'MDA%20RezFilter', 'LFO%20rate', bpm/60.)
            else:
                # just in case non mixer infos are not loaded yet
                self.start_scene(strip + '_bpm', lambda: [
                    self.wait(1, 's'), self.engine.modules[mixer].set(strip, 'MDA%20RezFilter', 'LFO%20rate', bpm/60.)
                ])

        # Zam Grains
        for mixer, strip in [
                ('VocalsNanoFX6Granular', 'VocalsNanoFX6Granular'),
                ('VocalsKeschFX6Granular', 'VocalsKeschFX6Granular')
            ]:
            if strip in self.engine.modules[mixer].submodules:
                self.engine.modules[mixer].set(strip, 'ZamGrains', 'Grain%20Speed', bpm/120.)
                self.engine.modules[mixer].set(strip, 'ZamGrains', 'Play%20Speed', bpm/120.)
            else:
                # just in case non mixer infos are not loaded yet
                self.start_scene(strip + '_bpm', lambda: [
                    self.wait(1, 's'),
                    self.engine.modules[mixer].set(strip, 'ZamGrains', 'Grain%20Speed', bpm/120.),
                    self.engine.modules[mixer].set(strip, 'ZamGrains', 'Play%20Speed', bpm/120.)
                ])

        # Bitrot Repeater
        for mixer, strip in [
                ('VocalsNanoFX7Slice', 'VocalsNanoFX7Slice'),
                ('VocalsKeschFX7Slice', 'VocalsKeschFX7Slice')
            ]:
            if strip in self.engine.modules[mixer].submodules:
                self.engine.modules[mixer].set(strip, 'Bitrot%20Repeat', 'BPM', bpm)
            else:
                # just in case non mixer infos are not loaded yet
                self.start_scene(strip + '_bpm', lambda: [
                    self.wait(1, 's'), self.engine.modules[mixer].set(strip, 'Bitrot%20Repeat', 'BPM', bpm)
                ])


        # Autofilter
        for mixer, strip in [
                ('SamplesFX4Autofilter', 'SamplesFX4Autofilter')
            ]:
            if strip in self.engine.modules[mixer].submodules:
                self.engine.modules[mixer].set(strip, 'C%2A%20AutoFilter%20-%20Self-modulating%20resonant%20filter', 'rate', 60./bpm)
            else:
                # just in case non mixer infos are not loaded yet
                self.start_scene(strip + '_bpm', lambda: [
                    self.wait(1, 's'), self.engine.modules[mixer].set(strip, 'C%2A%20AutoFilter%20-%20Self-modulating%20resonant%20filter', 'rate', 60./bpm)
                ])


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
        self.engine.modules['Klick'].set('cycle', int(nom), int(denom))
        self.engine.modules['Klick'].set('pattern', pattern)

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

    def stop(self):
        """
        Stop transport.
        Tell seq192 to stop and let jack transport do the rest.
        Klick is stopped manually.
        """

        self.engine.modules['Seq192'].stop()

        self.engine.modules['Klick'].stop()

        self.engine.modules['OpenStageControl'].set('rolling', 0)
