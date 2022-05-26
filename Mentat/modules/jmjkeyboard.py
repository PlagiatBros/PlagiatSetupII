from .keyboard import Keyboard
from mentat import Module


zyn_parts = {
    'ZDupieux': [0],
    'ZNotSoRhodes': [1],
    'ZOrgan': [2, 3],
    'ZCosma': [4],
    'ZBombarde': [5],
#    'ZTrumpets': [6,7,8],
    'ZStambul': [9],
    'ZDre': [10],
    'ZDiploLike': [11],
    'ZJestoProunk': [12],
    'Z8bits': [13, 14],
    'ZDiploLikeWide': [15],
}

class JmjKeyboardMidi(Module):
    """
    Midi controls from jmj
    """

    def route(self, address, args):

        if address == '/control_change':
            if args[1] == 7:
                self.engine.modules['JmjKeyboard'].set_filter(args[2])

class JmjKeyboard(Keyboard):
    """
    Jean-Michel Jarring Effects & Planche à Touches Incorporated (mididings patch)
    """

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.set_sound('ZDupieux')


    def set_sound(self, name, boost=False):

        old_sound = self.get('current_sound')

        super().set_sound(name, boost)

        new_sound = self.get('current_sound')

        if old_sound in zyn_parts:
            for part in zyn_parts[old_sound]:
                self.engine.modules['ZHiSynths'].send('/part%i/Pefxbypass1' % part, True)
                self.engine.modules['ZHiSynths'].send('/part%i/partefx1/parameter11' % part, 127)

        if new_sound in zyn_parts:
            for part in zyn_parts[new_sound]:
                self.engine.modules['ZHiSynths'].send('/part%i/Pefxbypass1' % part, False)

    def set_filter(self, freq):
        sound = self.get('current_sound')
        if sound in zyn_parts:
            for part in zyn_parts[sound]:
                self.engine.modules['ZHiSynths'].send('/part%i/partefx1/parameter11' % part, freq)
