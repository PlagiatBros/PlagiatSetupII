from mentat.module import Module

class Zynaddsubfx(Module):

    def __init__(self, *args, parts=[], **kwargs):

        super().__init__(*args, **kwargs)

        for part in parts:

            # add parameters for each part
            pass
