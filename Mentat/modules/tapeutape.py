from mentat.module import Module

class Tapeutape(Module):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.kits = {
            'trackA': 1
        }

    def set_kit(self, name):

        if name in self.kits:

            self.send('/control', 1, 0, self.kits[name])

        else:

            self.error('Unknown kit %s' % name)
