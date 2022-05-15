from mentat import Module

class Notes(Module):
    """
    Notes (scale) manager for autotunes.
    """

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.autotunes = ['NanoMeuf', 'NanoNormo', 'NanoGars', 'KeschMeuf', 'KeschNormo', 'KeschGars']

    def set_notes(self, *notes):
        """
        Set allowed notes for autotunes.

        **Parameters**

        - `*notes`: 12 int arguments 1 (in-scale) 0 (out-of-scale)
        """

        modules = self.engine.modules

        # autotuner
        for at in self.autotunes:
            modules[at].set_notes(*notes)
