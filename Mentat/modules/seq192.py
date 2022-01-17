from mentat import Module

class Seq192(Module):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.add_parameter('tempo', '/bpm', 'f', default=120)
        self.add_parameter('screenset', '/screenset', 'i', default=0)

        self.screenset_map = {
            'Snapshat': 0
        }

    def start(self):
        self.send('/play')

    def stop(self):
        self.send('/stop')

    def set_screenset(self, name):
        if name in self.screenset_map:
            self.set('screenset', self.screenset_map('name'))
        else:
            self.logger.error('screenset %s not found' % name)

    def select(self, *args):
        self.send('/sequence', *args)
