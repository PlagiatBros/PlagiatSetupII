from mentat import Module

class Seq192(Module):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.add_parameter('tempo', '/bpm', 'f', default=120)

    def start(self):
        self.send('/play')

    def stop(self):
        self.send('/stop')
