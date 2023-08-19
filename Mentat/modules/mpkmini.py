from mentat import Module
from random import random

class Pad():
    def __init__(self, mpk, pad_number, feedback_note, input_note):

        self.mpk = mpk
        self.pad_number = pad_number
        self.feedback_note = feedback_note
        self.input_note = input_note

        self.state = 'off'

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

        self.pads = {}
        for i in range(8):
            self.pads[i+1]=Pad(
                self,
                pad_number = i + 1,
                feedback_note = i + 9,
                input_note = i + 44
            )

        self.start_scene('blinkies', self.update_blink)
        self.engine.add_event_callback('client_started', self.client_started)


        self.pads[4].set('on')
        self.pads[8].set('on')


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

        if address == '/note_on':
            channel, note, velocity = args

            if note == self.pads[8].input_note:
                self.engine.modules['Transport'].stop()
                self.engine.active_route.pause_loopers()
            elif note == self.pads[4].input_note:
                self.engine.modules['Transport'].trigger()

            elif note == self.pads[5].input_note:
                self.engine.modules['AudioLooper'].record(9)
            elif note == self.pads[6].input_note:
                self.engine.modules['AudioLooper'].overdub(9)
            elif note == self.pads[7].input_note:
                self.engine.modules['AudioLooper'].pause(9)

        if address == '/note_off':
            self.send_state()

        return False
