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

class JmjTranspose(Keyboard):
    """
    Midi octave transpose from jmj
    """

    octave_scenes = {
        0: 1,
        -4: 2,
        -3: 3,
        -2: 4,
        -1: 5,
        1: 6,
        2: 7,
        3: 8,
        4: 9,
    }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.add_parameter('octave', None, 'i', default=0)
        self.add_parameter('octave-bonus', None, 'i', default=0)

        self.add_event_callback('parameter_changed', self.parameter_changed)

    def parameter_changed(self, module, name, value):

        if name in ['octave', 'octave-bonus']:
            oct = self.get('octave') + self.get('octave-bonus')
            if oct > 4:
                oct = 4
            elif oct < -4:
                oct = -4
            elif oct not in self.octave_scenes:
                oct = 0
            self.send('/mididings/switch_scene', self.octave_scenes[oct])




class JmjKeyboardMidi(Module):
    """
    Midi controls from jmj
    """

    def route(self, address, args):

        if address == '/control_change':
            if args[1] == 7: #  7 m-audio, 11 ben UZ
                self.engine.modules['JmjKeyboard'].set_filter(args[2])

class JmjKeyboard(Keyboard):
    """
    Jean-Michel Jarring Effects & Planche à Touches Incorporated (mididings patch)
    """

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.set_sound('ZDupieux')


    def set_sound(self, name, boost=False, lead=None):

        old_sound = self.get('current_sound')

        super().set_sound(name, boost, lead)

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
