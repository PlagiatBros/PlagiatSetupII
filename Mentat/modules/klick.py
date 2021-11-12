from mentat.module import Module

class Klick(Module):

    def __init__(self, *args, **kwargs):

        Module.__init__(self, *args, **kwargs)

        self.add_parameter('pattern', '/klick/simple/set_pattern', 's')
        self.add_parameter('tempo', '/klick/simple/set_tempo', 'f')

    def start(self):
        self.send('/klick/metro/start')

    def stop(self):
        self.send('/klick/metro/stop')
