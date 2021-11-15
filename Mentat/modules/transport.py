from mentat import Module

class Transport(Module):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

    def set_tempo(self, bpm):

        self.engine.set_tempo(bpm)
        self.engine.modules['Klick'].set('tempo', bpm)
        self.engine.modules['Seq192'].set('tempo', bpm)
        self.engine.modules['Loop192'].set('tempo', bpm)
        self.engine.modules['Looper'].set('tempo', bpm)


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
        self.engine.modules['Klick'].start()
        self.engine.modules['Seq192'].start()
        self.engine.modules['Loop192'].start()
        self.engine.modules['Looper'].start()

    def stop(self):

        self.engine.modules['Klick'].stop()
        self.engine.modules['Seq192'].stop()
        self.engine.modules['Loop192'].stop()
        self.engine.modules['Looper'].stop()
