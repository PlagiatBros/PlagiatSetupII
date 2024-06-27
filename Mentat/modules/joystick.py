from mentat import Module
from math import ceil
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
            if args[0] in ['rx', 'ry']:
                oct = 0
                if args[1] != 0:
                    if args[0] == 'rx':
                        oct = args[1] / abs(args[1])
                    else:
                        oct = 2 * args[1] / abs(args[1])
                    if args[0] == 'ry':
                        oct = -1 * oct
                self.engine.modules['JmjTranspose'].set('octave-bonus', oct)

        elif address == '/button':
            if args[0] == 'a' and args[1] == 1:
                # CROIX
                octave = int(self.engine.modules['JmjTranspose'].get('octave'))
                octave = max(-2, octave - 1)
                self.engine.modules['JmjTranspose'].set('octave', octave)
            if args[0] == 'y'  and args[1] == 1:
                # TRIANGLE
                octave = int(self.engine.modules['JmjTranspose'].get('octave'))
                octave = min(2, octave + 1)
                self.engine.modules['JmjTranspose'].set('octave', octave)
                #if args[0] == 'tr' and args[1]:
            #    toggle_tuner()

        elif address == '/status':
            pass

        return False
