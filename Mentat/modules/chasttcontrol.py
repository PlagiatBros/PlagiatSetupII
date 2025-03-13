from mentat import Module
from .keyboard import Keyboard

from math import copysign

class ChasttKeyboard(Keyboard):
    """
    Mk2 piano keyboard (mididings patch)
    """

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.set_sound('LowCTrap1')


class ChasttControl(Module):
    """
    Mk2 MIDI control interface
    """

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.sysex = []

        self.shift_key = False
        self.pressed_notes = 0
        self.modes = ['keyboard']

        self.voices = ['gars_exclu', 'meuf_exclu', 'normo_exclu']
        self.current_voice = 0

        self.last_cc = None

    def set_lights(self, lights):
        """
        Generates sysex messages for setting colors on pads

        **Parameters**

        - `lights`:
            `dict` with pad number as keys (1-indexed) and color names as values. Omitted pad will be turned off.
            Available color: red, blue, green purple, cyan, yellow, white
        """
        self.logger.info('setting lights')
        self.sysex = []
        for i in range(1,17):
            color = self.default_colors[i-1]
            if i in lights:
                color = self.mk2colors['purple']
                if type(lights) == dict:
                    color =  self.mk2colors[lights[i]]
                elif i == 1:
                    color = self.mk2colors['blue']
                elif i == 8:
                    color = self.mk2colors['red']

            self.sysex.append([0xf0, 0x00, 0x20, 0x6b, 0x7f, 0x42, 0x02, 0x00, 0x10, 111 + i, color, 0xf7])

        self.resend_lights()

    def resend_lights(self):
        """
        Send sysex messages to mk2
        """

        for s in self.sysex:
            self.send('/sysex', *s)


    def set_mode(self, *modes):

        self.modes = modes

        if 'keyboard' not in self.modes:

            self.engine.modules['ChasttKeyboard'].set_sound('Mute')


    def parse_controls(self, address, args):

        if '/note' in address:

            old_pressed_notes = self.pressed_notes
            if address == '/note_on':
                self.pressed_notes += 1
            elif address == '/note_off':
                self.pressed_notes -= 1
                if self.pressed_notes < 0:
                    self.pressed_notes = 0

            for mode in self.modes:

                if 'cut' in mode:
                    self.engine.set(mode, 'on' if self.pressed_notes else 'off')

        if address == '/pitch_bend':

            deadzone = 0 # 2048
            clamp = copysign(max(abs(args[1]) - deadzone,0) / (8192 - deadzone), args[1])

            p = 1.0 + clamp * 0.75

            self.engine.modules['PostProcess'].set_pitch('*', p)

    def route(self, address, args):
        """
        Route controls from mk2.
        Reset colors whenever a pad is hit, otherwise it dosen't stay lit.
        """
        #self.logger.info('%s %s' %(address, args))

        self.parse_controls(address, args)

        if address == '/control_change':

            cc = args[1]

            if cc > 100 and cc < 117:

                if args[2] == 127:

                    if cc < 109:
                        # pads 1-8
                        self.engine.route('osc', 'chastt', '/chastt/button', [cc - 100])
                    else:
                        if cc == 109:
                            self.engine.modules['VocalsChast'].set('gars_exclu', 'on')
                        elif cc == 110:
                            self.engine.modules['VocalsChast'].set('normo_exclu', 'on')
                        elif cc == 111:
                            self.engine.modules['VocalsChast'].set('meuf_exclu', 'on')
                        elif cc == 112:
                            self.engine.modules['AudioLooper'].record(9)
                        elif cc == 113:
                            self.engine.modules['AudioLooper'].overdub(9)
                        elif cc == 114:
                            self.engine.modules['AudioLooper'].pause(9)
                        elif cc == 115:
                            self.engine.modules['ConstantSampler'].send('/instrument/play', 's:Plagiat/ConstantKit/AirHorn', 80)
                        elif cc == 116:
                            self.engine.active_route.stop()

                        # elif cc == 116:
                        #     self.engine.modules['Transport'].trigger()

                if args[2] == 0:
                    self.resend_lights()


            if cc == 18:
                self.engine.modules['MonitorsChast'].set('MonitorsChast', 'Gain', args[2] / 127 * 76 - 70)

            if cc in [41, 42]:

                if args[2] == 0 and self.last_cc == args:
                    # bug when releasing both buttons at the same time (same cc with value 0 sent twice and missing 0 value for the other button)
                    cc = 41 if cc == 42 else 42
                self.last_cc = args

                if cc == 41:
                    self.engine.modules['VocalsChast'].set('ChastIn', 'Gate', 'Range%20(dB)', -90 if args[2] == 0 else 0)

        elif address == '/sysex':

            if args[:-2] == [240, 0, 32, 107, 127, 66, 2, 0, 0, 46]:
                self.shift_key = args[-2] == 127

        return False

    mk2colors = mk2colors = {
        'red': 1,
        'blue': 16,
        'green': 4,
        'purple': 17,
        'cyan': 20,
        'yellow': 5,
        'white': 127
    }

    default_colors = [
    	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, # buttons 1-8
        mk2colors['yellow'], mk2colors['yellow'], mk2colors['yellow'], # buttons 9-11
    	mk2colors['red'], mk2colors['red'],mk2colors['yellow'], # sl vx post rec/overdub/pause
    	mk2colors['purple'], mk2colors['blue']
    ]
