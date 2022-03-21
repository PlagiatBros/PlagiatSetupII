MENTAT_JACK_MASTER = False
if MENTAT_JACK_MASTER:
    import jack

from mentat import Module

class Transport(Module):

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

        self.engine.root_module.add_alias_parameter('bass_scape_bpm', ['Bass', 'BassScape', 'C%2A%20Scape%20-%20Stereo%20delay%20with%20chromatic%20resonances/bpm'])


    def jack_callback(self, state, blocksize, pos, new_pos):

        pos.beats_per_minute = self.engine.tempo

        # pos.ticks_per_beat = 192.0
        # pos.beats_per_bar = self.engine.cycle_length
        # pos.beat_type = 8.0

    def set_tempo(self, bpm):

        self.engine.set_tempo(bpm)
        self.engine.modules['Looper'].set('tempo', bpm)
        self.engine.modules['Klick'].set('tempo', bpm)
        # self.engine.modules['Seq192'].set('tempo', bpm)
        # self.engine.modules['Loop192'].set('tempo', bpm)
        self.engine.root_module.set('bass_scape_bpm', bpm)

    def set_cycle(self, eighths, pattern=None):

        self.engine.set_cycle_length(eighths)

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
        self.engine.modules['Klick'].set('cycle', '%i/8' % eighths)

        self.engine.modules['Loop192'].set('cycle', eighths)
        self.engine.modules['Looper'].set('cycle', eighths)

    def start(self):

        self.engine.start_cycle()

        if MENTAT_JACK_MASTER and self.jack:

            if self.jack.transport_state == jack.ROLLING:
                self.jack.transport_frame = 0
            else:
                self.jack.transport_start()

        else:

            # self.engine.modules['Looper'].start()
            self.engine.modules['Seq192'].start()
            # self.engine.modules['Loop192'].start()

        self.engine.modules['Klick'].start()

    def stop(self):

        if MENTAT_JACK_MASTER and self.jack:

            self.jack.transport_stop()

        else:

            # self.engine.modules['Looper'].stop()
            self.engine.modules['Seq192'].stop()
            # self.engine.modules['Loop192'].stop()

        self.engine.modules['Klick'].stop()
