from mentat import Module

class Tapeutape(Module):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.kit_aliases = {
            'trackA': 1
        }

        self.add_parameter('kit', '/control', 'iii', static_args=[1, 0], default=8)


    def set_kit(self, name):

        if name in self.kit_aliases:

            self.set('kit', self.kit_aliases[name])

        else:

            self.error('Unknown kit %s' % name)
