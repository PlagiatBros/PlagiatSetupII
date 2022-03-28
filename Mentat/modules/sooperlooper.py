from mentat import Module

class Loop(Module):

    def __init__(self, *args, loop_n, **kwargs):

        super().__init__(*args, **kwargs)

        # self.add_parameter('wet', '/sl/%i/set' % loop_n, 'sf', static_args=['wet'], default=0)


class SooperLooper(Module):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.add_parameter('cycle', '/set', 'sf', static_args=['eighth_per_cycle'], default=8)
        self.add_parameter('tempo', '/set', 'sf', static_args=['tempo'], default=120)

        for i in range(16):
            self.add_submodule(Loop('loop_%i' % i, loop_n=i, parent=self))



    def reset(self, i='-1'):
        self.send('/sl/%s/hit' % i, 'undo_all')

    def trigger(self, i='-1'):
        self.send('/set', 'sync_source', 0)
        self.send('/sl/%s/set' % i, 'sync', 0)
        self.send('/sl/%s/hit' % i, 'trigger')
        self.send('/sl/%s/set' % i, 'sync', 1)
        self.send('/set', 'sync_source', -3)

    def record(self, i):
        self.send('/sl/%s/hit' % i, 'record')

    def overdub(self, i):
        self.send('/sl/%s/hit' % i, 'overdub')

    def pause(self, i='-1'):
        self.send('/sl/%s/hit' % i, 'pause_on')
