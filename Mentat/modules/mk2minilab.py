from mentat import Module
from .keyboard import Keyboard


class Mk2Keyboard(Keyboard):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

class Mk2Control(Module):
    """
    MIDI control interface
    """

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.colors = []

    def set_lights(self, lights):

        for i in range(1,17):
            self.colors = []
            color = Mk2Minilab.default_colors[i-1]
            if i in pads:
                color = Mk2Minilab.mk2colors['purple']
                if type(lights) == dict:
                    color =  Mk2Minilab.mk2colors[lights[i]]
                elif i == 1:
                    color = Mk2Minilab.mk2colors['blue']
                elif i == 8:
                    color = Mk2Minilab.mk2colors['red']
                self.colors.append(push)
            self.send('/sysex', [0xf0, 0x00, 0x20, 0x6b, 0x7f, 0x42, 0x02, 0x00, 0x10, 111 + i, color, 0xf7])

    def resend_lights(self):

        for c in self.colors:
            self.send('/sysex', color)

    def route(self, address, args):

        if address == '/control':

            cc = args[0]
            if cc > 100 and cc < 117:

                if cc < 109:
                    # pads 1-8
                    self.engine.route('osc', 'mk2', '/mk2/button', [cc - 100])
                else:
                    pass

                self.resend_lights()

        return False

Mk2Control.mk2colors = mk2colors = {
    'red': 1,
    'blue': 16,
    'green': 4,
    'purple': 17,
    'cyan': 20,
    'yellow': 5,
    'white': 127
}

Mk2Control.default_colors = [
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, # buttons 1-8
	mk2colors['red'], mk2colors['red'],mk2colors['yellow'], # sl vx pre rec/overdub/pause
	mk2colors['red'], mk2colors['red'],mk2colors['yellow'], # sl vx post rec/overdub/pause
	0x00, mk2colors['purple']
]