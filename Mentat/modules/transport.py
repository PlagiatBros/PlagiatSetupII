MENTAT_JACK_MASTER = False
if MENTAT_JACK_MASTER:
    import jack

from mentat import Module

class Transport(Module):
    """
    Transport manager (tempo, time signature, klick pattern, playback)
    """

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        if MENTAT_JACK_MASTER:
            try:
                self.jack = jack.Client(self.engine.name, no_start_server=True)
                self.jack.set_timebase_callback(callback=self.jack_callback)
                self.jack.activate()
                self.add_event_callback('engine_stopping', lambda: [
                    self.jack.release_timebase(),
                    self.jack.deactivate()
                ])

            except jack.JackOpenError:
                self.logger.error('Jack is not running, jack transport module disabled')
                self.jack = None

    def jack_callback(self, state, blocksize, pos, new_pos):

        pos.beats_per_minute = self.engine.tempo

        # pos.ticks_per_beat = 192.0
        # pos.beats_per_bar = self.engine.cycle_length
        # pos.beat_type = 8.0

    def set_tempo(self, bpm):
        """
        Set tempo.
        Set sooperlooper's tempo and let jack transport do the rest (sl is transport master).
        Some delays are synced to the tempo as well.

        **Parameters**

        - `bpm`: beats per minute
        """

        self.engine.set_tempo(bpm)

        if not MENTAT_JACK_MASTER:
            self.engine.modules['Looper'].set('tempo', bpm)

        self.engine.modules['Klick'].set('tempo', bpm)

        for mixer, strip in [
                ('BassFX', 'BassScape'),
                ('SynthsFX5Scape', 'SynthsFX5Scape')]:
            self.engine.modules[mixer].set(strip, 'Scape', 'bpm', bpm)

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

        self.engine.modules['Klick'].set('pattern', pattern)
        self.engine.modules['Klick'].set('cycle', signature)

        self.engine.modules['Loop192'].set('cycle', eighths)
        self.engine.modules['Looper'].set('cycle', eighths)

    def start(self):
        """
        Start transport.
        Tell seq192 to start and let jack transport do the rest.
        Klick is started manually.
        """

        self.engine.start_cycle()

        if MENTAT_JACK_MASTER and self.jack:

            if self.jack.transport_state == jack.ROLLING:
                self.jack.transport_frame = 0
            else:
                self.jack.transport_start()

        else:

            # seq192 will start jack transport
            self.engine.modules['Seq192'].start()

        self.engine.modules['Klick'].start()

    def stop(self):
        """
        Stop transport.
        Tell seq192 to stop and let jack transport do the rest.
        Klick is stopped manually.
        """

        if MENTAT_JACK_MASTER and self.jack:

            self.jack.transport_stop()

        else:

            # seq192 will stop jack transport
            self.engine.modules['Seq192'].stop()

        self.engine.modules['Klick'].stop()
