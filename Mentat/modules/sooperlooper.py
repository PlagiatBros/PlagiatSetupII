from mentat import Module

class Loop(Module):
    """
    Loop submodule (unnused)
    """

    def __init__(self, *args, loop_n, **kwargs):

        super().__init__(*args, **kwargs)

        # self.add_parameter('wet', '/sl/%i/set' % loop_n, 'sf', static_args=['wet'], default=0)

class SooperLooper(Module):
    """
    Audio looper
    """

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.add_parameter('cycle', '/set', 'sf', static_args=['eighth_per_cycle'], default=8)
        self.add_parameter('tempo', '/set', 'sf', static_args=['tempo'], default=120)

        for i in range(16):
            self.add_submodule(Loop('loop_%i' % i, loop_n=i, parent=self))

        self.pending_record = None

    def start(self):
        """
        Reset cycle start position
        """
        self.send('/set', 'sync_source', 0)
        if self.pending_record is not None:
            self.send('/sl/%s/set' % self.pending_record, 'sync', 0)
            self.send('/sl/%s/hit' % self.pending_record, 'record')
            self.send('/sl/%s/set' % self.pending_record, 'sync', 1)
            self.pending_record = None
        self.send('/set', 'sync_source', -3)

    def reset(self, i='-1'):
        """
        Reset loop(s) (remove audio content and duration)

        **Parameters**

        - `i`:
            - loop number or
            - osc pattern to affect multiple loops (examples: '[1,2,5]', '[2-5]'...)
            - `-1` to affect all loops
        """
        self.send('/sl/%s/hit' % i, 'undo_all')

    def trigger(self, i='-1'):
        """
        Trig loop(s) (reset playback head to the beginning)

        **Parameters**

        - `i`:
            - loop number or
            - osc pattern to affect multiple loops (examples: '[1,2,5]', '[2-5]'...)
            - `-1` to affect all loops
        """
        self.send('/sl/%s/set' % i, 'sync', 0)
        self.send('/sl/%s/hit' % i, 'pause_off')
        self.send('/sl/%s/hit' % i, 'trigger')
        self.send('/sl/%s/set' % i, 'sync', 1)

    def record(self, i):
        """
        Start recording at next cycle.
        WARNING: record will not start before the beginning of the 3rd cycle after transport.start() was called/

        **Parameters**

        - `i`:
            - loop number or
            - osc pattern to affect multiple loops (examples: '[1,2,5]', '[2-5]'...)
            - `-1` to affect all loops
        """
        self.send('/sl/%s/hit' % i, 'record')

    def record_on_start(self, i):
        """
        Start recording next time transport.start()

        **Parameters**

        - `i`:
            - loop number or
            - osc pattern to affect multiple loops (examples: '[1,2,5]', '[2-5]'...)
            - `-1` to affect all loops
        """
        self.pending_record = i

    def overdub(self, i):
        """
        Start overdubing now

        **Parameters**

        - `i`:
            - loop number or
            - osc pattern to affect multiple loops (examples: '[1,2,5]', '[2-5]'...)
            - `-1` to affect all loops
        """
        self.send('/sl/%s/hit' % i, 'overdub')

    def pause(self, i='-1'):
        """
        Pause playback

        **Parameters**

        - `i`:
            - loop number or
            - osc pattern to affect multiple loops (examples: '[1,2,5]', '[2-5]'...)
            - `-1` to affect all loops
        """
        self.send('/sl/%s/hit' % i, 'pause_off')
        self.send('/sl/%s/hit' % i, 'pause_on')
