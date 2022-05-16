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
            pass
            #if args[0] == 'tr' and args[1]:
            #    toggle_tuner()

        elif address == '/status':
            pass

        return False
