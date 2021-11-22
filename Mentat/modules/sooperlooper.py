from mentat import Module

class Loop(Module):

    def __init__(self, *args, loop_n, **kwargs):

        super().__init__(*args, **kwargs)

        self.add_parameter('wet', '/sl/%i/set' % loop_n, 'sf', static_args=['wet'], default=0)


class SooperLooper(Module):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.add_parameter('cycle', '/set', 'sf', static_args=['eighth_per_cycle'], default=8)
        self.add_parameter('tempo', '/set', 'sf', static_args=['tempo'], default=120)

        for i in range(16):
            self.add_submodule(Loop('%i' % i, loop_n=i, parent=self))



    def start(self):

        self.send('/set', 'sync_source', 0)
        self.send('/sl/-1/hit', 'sync', 0)
        self.send('/sl/-1/hit', 'trigger')
        self.send('/sl/-1/hit', 'sync', 1)
        self.send('/set', 'sync_source', -3)

        # reset wet depending on local state
        self.send_state()


    def stop(self):

        self.send('/sl/-1/set', 'pause_on', 0)
