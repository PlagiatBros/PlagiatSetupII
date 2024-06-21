from mentat import Module
import os

class Joystick(Module):
    """
    PS3 Controller (mididings patch)
    """

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

    def toggle_tuner(self):
        pass
        #os.system('i3-msg scratchpad show')


    def route(self, address, args):

        if address == '/axis':
            pass

        elif address == '/button':
            if args[0] == 'dpad_up' and args[1] == 1:
                octave = int(self.engine.modules['JmjTranspose'].get('octave'))
                octave = min(2, octave + 1)
                self.engine.modules['JmjTranspose'].set('octave', octave)
            if args[0] == 'dpad_down'  and args[1] == 1:
                octave = int(self.engine.modules['JmjTranspose'].get('octave'))
                octave = max(-2, octave - 1)
                self.engine.modules['JmjTranspose'].set('octave', octave)
                #if args[0] == 'tr' and args[1]:
            #    toggle_tuner()

        elif address == '/status':
            pass

        return False
