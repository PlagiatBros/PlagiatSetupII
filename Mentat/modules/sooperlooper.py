from mentat.module import Module

class SooperLooper(Module):

    def __init__(self, *args, **kwargs):

        Module.__init__(self, *args, **kwargs)

        self.add_parameter('cycle', '/set', 'sf', static_args=['eighth_per_cycle'], default=8)
        self.add_parameter('tempo', '/set', 'sf', static_args=['tempo'], default=120)
