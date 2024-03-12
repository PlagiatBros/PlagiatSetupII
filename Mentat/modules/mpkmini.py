from mentat import Module
from random import random
from math import pow

class Pad():
    def __init__(self, mpk, pad_number, feedback_note, input_note):

        self.mpk = mpk
        self.pad_number = pad_number
        self.feedback_note = feedback_note
        self.input_note = input_note

        self.state = 'off'
        self.last_cc = -1

    def set(self, state):
        if state in ['on', 'off', 'blink']:
            self.state = state
            if state == 'on':
                self.light(True)
            if state == 'off':
                self.light(False)

    def light(self, lit):
        self.mpk.send('/note_on', 0, self.feedback_note, 127 if lit else 0)


class MpkControl(Module):
    """
    Mpk MIDI control interface
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

        # self.pads = {}
        # for i in range(8):
        #     self.pads[i+1]=Pad(
        #         self,
        #         pad_number = i + 1,
        #         feedback_note = i + 9,
        #         input_note = i + 44
        #     )
        #
        # self.start_scene('blinkies', self.update_blink)
        # self.engine.add_event_callback('client_started', self.client_started)
        #
        #
        # self.pads[4].set('on')
        # self.pads[8].set('on')
        #

    def client_started(self, name):
        if name == 'AudioLooper':
            self.engine.modules['AudioLooper'].submodules['loop_9'].add_event_callback('parameter_changed', self.loop_state_changed)
            self.engine.modules['RaySession'].alsa_patcher.add_event_callback('alsa_connections_changed', self.alsa_connections_changed)

    def alsa_connections_changed(self):
        self.send_state()

    def loop_state_changed(self, mod, name, value):
        loop = self.engine.modules['AudioLooper'].submodules['loop_9']

        if loop.get('waiting'):
            self.pads[5].set('blink')
        elif loop.get('recording'):
            self.pads[5].set('on')
        else:
            self.pads[5].set('off')

        if loop.get('overdubbing'):
            self.pads[6].set('on')
        else:
            self.pads[6].set('off')

    def send_state(self):
        for i in self.pads:
            pad = self.pads[i]
            pad.set(pad.state)

    def update_blink(self):
        while True:
            self.wait(0.25, 's')
            for i in self.pads:
                pad = self.pads[i]
                if pad.state == 'blink':
                    pad.light(True)
            self.wait(0.25, 's')
            for i in self.pads:
                pad = self.pads[i]
                if pad.state == 'blink':
                    pad.light(False)

    def route(self, address, args):
        """
        Route controls from mk2.
        Reset colors whenever a pad is hit, otherwise it dosen't stay lit.
        """
        self.logger.info('%s %s' %(address, args))

        if address == '/pitch_bend':

            p = 1.0 + args[1] / 8192 * 0.75
            self.engine.modules['PostProcess'].set_pitch('*', p)
        #
        # if address == '/note_on':
        #     channel, note, velocity = args
        #
        #     if note == self.pads[8].input_note:
        #         self.engine.modules['Transport'].stop()
        #         self.engine.active_route.pause_loopers()
        #     elif note == self.pads[4].input_note:
        #         self.engine.modules['Transport'].trigger()
        #
        #     elif note == self.pads[5].input_note:
        #         self.engine.modules['AudioLooper'].record(9)
        #     elif note == self.pads[6].input_note:
        #         self.engine.modules['AudioLooper'].overdub(9)
        #     elif note == self.pads[7].input_note:
        #         self.engine.modules['AudioLooper'].pause(9)

        print(address, args)

        if address == '/control_change':
            ch, cc, val = args

            if cc == 24:
                # granular in
                self.engine.modules['VocalsFeatFX6Granular'].set('FeatMeuf', 'Gain', 70 * val / 127 - 70)
                self.engine.modules['VocalsFeatFX6Granular'].set('FeatGars', 'Gain',70 * val / 127 - 70)
                self.engine.modules['VocalsFeatFX6Granular'].set('FeatNormo', 'Gain', 70 * val / 127 - 70)
                self.engine.modules['VocalsFeatFX6Granular'].set('pre', 'on' if val != 0 else 'off')
            if cc == 25:
                self.engine.modules['VocalsFeatFX6Granular'].set('VocalsFeatFX6Granular', 'ZamGrains', 'Freeze', 1 if val > 64 else 0)

            if cc == 1:
                self.engine.modules['VocalsFeatFX6Granular'].set('VocalsFeatFX6Granular', 'ZamGrains', 'Grains', 100*val / 127 )
            if cc == 2:
                self.engine.modules['VocalsFeatFX6Granular'].set('VocalsFeatFX6Granular', 'ZamGrains', 'Grain%20Speed', 20 * pow(val / 127, 2) )
            if cc == 3:
                self.engine.modules['VocalsFeatFX6Granular'].set('VocalsFeatFX6Granular', 'ZamGrains', 'Play%20Speed', 20 * pow(val / 127, 2) )
            if cc == 4:
                self.engine.modules['VocalsFeatFX6Granular'].set('VocalsFeatFX6Granular', 'ZamGrains', 'Loop%20time', 900*val / 127 +100 )
            self.last_cc = cc

        elif address == '/note_on':
            ch, note, val = args
            if ch == 9:
                samples = {
                    40: 'Clap',
                    38: 'Stick',
                    46: 'HH',
                    44: 'FunkyHit1',
                    37: 'Karkab1',
                    36: 'Karkab2',
                    42: 'Karkab3',
                    82: 'AirHorn'
                }
                if note in samples:
                    self.engine.modules['ConstantSampler'].send('/instrument/play', 's:Plagiat/ConstantKit/%s' % samples[note], val)


        # if address == '/note_on':
        #     self.route('/control_change', [0, self.last_cc, args[2]])
        # if address == '/note_off':
        #     self.route('/control_change', [0, self.last_cc, 0])

        return False
