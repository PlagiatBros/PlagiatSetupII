from mentat import Module


class MidiPanic(Module):
    """
    Utility for resetting all synths
    """

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

    # def route(self, address, args):
    #     print(address, args)

    def reset(self):
        #self.engine.modules['CalfPitcher'].send('/pitch_panic')

        for channel in range(16):
            self.send('/pitch_bend', channel, 0)
            self.send('/control_change', channel, 1, 0)  # modulation
            self.send('/control_change', channel, 64, 0) # sustain

    def panic(self):
        #self.engine.modules['CalfPitcher'].send('/panic')
        for channel in range(16):
            self.send('/control_change', channel, 123, 0)# all notes off
