from mentat import Module
from .keyboard import Keyboard

class ChasttKeyboard(Keyboard):
    """
    Chastt piano keyboard (mididings patch)
    """

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.set_sound('LowCTrap1')

    def play_note(self, note, duration=1, velocity=127):
        self.engine.modules['ChasttControlMidiOut'].send('/note_off', 0, note)
        self.engine.modules['ChasttControlMidiOut'].send('/note_on', 0, note, 127)
        self.start_scene('chastt/noteoff/%i' % note, lambda: [
            self.wait(duration, 'b'),
            self.engine.modules['ChasttControlMidiOut'].send('/note_off', 0, note)
        ])

class ChasttControl(Module):
    """
    Feat ctrls
    """

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

    def route(self, address, args):
        self.logger.info('%s %s' %(address, args))

        if address == '/chastt/pitch':
            self.engine.modules['PostProcess'].set_pitch('*', args[0])

        elif address == '/chastt/button':
            pass

        else:
            return False


    def set_lights(self, lights):
        pass
