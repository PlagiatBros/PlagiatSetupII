from mentat import Module
from .keyboard import Keyboard

from math import copysign

class Mk2Keyboard(Keyboard):
    """
    Mk2 piano keyboard (mididings patch)
    """

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.set_sound('Mute')


class Mk2Control(Module):
    """
    Mk2 MIDI control interface
    """

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.sysex = []

        self.shift_key = False
        self.pressed_notes = 0
        self.modes = ['mute_samples']

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
            # self.logger.info('sending /sysex %s' % s)
            self.send('/sysex', *s)


    def set_mode(self, *modes):

        self.modes = modes

        if 'keyboard' not in self.modes:

            self.engine.modules['Mk2Keyboard'].set_sound('Mute')


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

                if mode == 'wobble':

                    self.engine.modules['BassFX'].set('wobble', 'on' if self.pressed_notes != 0 else 'off')

        if address == '/pitch_bend':

            if 'keyboard' not in self.modes or self.shift_key:

                clamp = copysign(max(abs(args[1]) - 2048,0) / (8192 - 2048), args[1])

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

                    if cc < 112:
                        # pads 1-11
                        self.engine.route('osc', 'mk2', '/mk2/button', [cc - 100])
                    else:
                        if cc == 112:
                            self.engine.modules['AudioLooper'].record(5)
                        elif cc == 113:
                            self.engine.modules['AudioLooper'].overdub(5)
                        elif cc == 114:
                            self.engine.modules['AudioLooper'].pause(5)
                        elif cc == 116:
                            self.engine.modules['Transport'].trigger()

                if args[2] == 0:
                    self.resend_lights()


            if cc == 19:
                # vx roll
                self.engine.modules['VocalsNano'].set(self.voices[args[2] % 3], 'on')


            if cc == 20:
                # granular in
                self.engine.modules['VocalsNanoFX6Granular'].set('NanoMeuf', 'Gain', 70 * args[2] / 127 - 70)
                self.engine.modules['VocalsNanoFX6Granular'].set('NanoGars', 'Gain',70 * args[2] / 127 - 70)
                self.engine.modules['VocalsNanoFX6Granular'].set('NanoNormo', 'Gain', 70 * args[2] / 127 - 70)
                self.engine.modules['VocalsNanoFX6Granular'].set('pre', 'on' if args[2] != 0 else 'off')
            if cc ==21:
                self.engine.modules['VocalsNanoFX6Granular'].set('VocalsNanoFX6Granular', 'ZamGrains', 'Grains', 100*args[2] / 127 )
            if cc ==22:
                self.engine.modules['VocalsNanoFX6Granular'].set('VocalsNanoFX6Granular', 'ZamGrains', 'Grain%20Speed', 20*args[2] / 127-0.9 )
            if cc ==23:
                self.engine.modules['VocalsNanoFX6Granular'].set('VocalsNanoFX6Granular', 'ZamGrains', 'Play%20Speed', 20*args[2] / 127-0.9 )
            if cc ==24:
                self.engine.modules['VocalsNanoFX6Granular'].set('VocalsNanoFX6Granular', 'ZamGrains', 'Loop%20time', 1000*args[2] / 127-0.9 )
            if cc ==12:
                self.engine.modules['VocalsNanoFX6Granular'].set('VocalsNanoFX6Granular', 'ZamGrains', 'Freeze', 1 if args[2] > 64 else 0)



            if cc == 25:
                self.logger.info('BassFX degrade %f' % (args[2] / 127))
                self.engine.modules['BassFX'].set('BassDegrade', 'MDA%20Degrade', 'Rate',  args[2] / 127)

            if cc == 26:
                self.engine.modules['BassFX'].set('wobble_subdivision', 1 + args[2] % 8)
                self.logger.info('BassFX wobble div %d' % (1+args[2]%8))


            if cc in [41, 42]:

                if args[2] == 0 and self.last_cc == args:
                    # bug when releasing both buttons at the same time (same cc with value 0 sent twice and missing 0 value for the other button)
                    cc = 41 if cc == 42 else 42
                self.last_cc = args

                if cc == 41:
                    self.engine.modules['VocalsNano'].set('NanoIn', 'Gate', 'Range%20(dB)', -90 if args[2] == 0 else 0)

                if cc == 42:
                    # tmp vx pitch reset
                    for at in ['NanoMeuf', 'NanoNormo', 'NanoGars']:
                        if args[2] == 0:
                            self.engine.modules[at].reset('offset')
                        else:
                            self.engine.modules[at].set('offset', 0)

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
        0x00, 0x00, 0x00, # buttons 9-11
    	mk2colors['red'], mk2colors['red'],mk2colors['yellow'], # sl vx post rec/overdub/pause
    	0x00, mk2colors['purple']
    ]
