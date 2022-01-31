from mentat import Module

class Autotune(Module):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for i in range(12):
            self.add_parameter('tuning_%i' % i, '/x42/parameter', 'if', static_args=[i + 26], default=0.0)

    def set_tuning(self, tunings):
        i = 0
        for tuning in tunings:
            self.set('tuning_%i' % i, tuning)
            i += 1
