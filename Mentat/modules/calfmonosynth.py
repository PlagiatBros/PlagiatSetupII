from mentat import Module

class CalfPitcher(Module):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.add_parameter('tuning', '/monosynth/pitch', 'f' * 12, default=[0.0] * 12)

class CalfMonoSynth(Module):

    def __init__(self, *args, pitcher_port=None, **kwargs):

        super().__init__(*args, **kwargs)

        for i in CalfMonoSynth.parameters:

            param = CalfMonoSynth.parameters[i]
            self.add_parameter(param['name'], '/%s/%i/set_parameter_value' % (self.name, i), param['type'])

    def set_waveform(self, wf, o):
        if wf in CalfMonoSynth.osctypes:
            self.set('O%i_Waveform' % o, CalfMonoSynth.osctypes[wf])

    def set_phasemode(self, pm):
        if pm in CalfMonoSynth.phasemodes:
            self.set('PhaseMode', CalfMonoSynth.phasemodes[pm])

    def set_filtertype(self, ft):
        if ft in CalfMonoSynth.filtertypes:
            self.set('Filter_Type', CalfMonoSynth.filtertypes[ft])

    def set_legatomode(self, lm):
        if lm in CalfMonoSynth.legatomodes:
            self.set('LegatoMode', CalfMonoSynth.legatomodes[lm])

    def set_lfotriggermode(self, ltm, l):
        if ltm in CalfMonoSynth.lfotriggermodes:
            self.set('LFO%i_TriggerMode' % l, CalfMonoSynth.lfotriggermodes[ltm])


    osctypes = {
        'sawtooth': 0,
        'square': 1,
        'pulse': 2,
        'sine': 3,
        'triangle': 4,
        'varistep': 5,
        'skewed_saw': 6,
        'skewed_square': 7,
        'smooth_brass': 8,
        'bass': 9,
        'dark_fm': 10,
        'multiwave': 11,
        'bell_fm': 12,
        'dark_pad': 13,
        'dco_saw': 14,
        'dco_maze': 15
    }

    phasemodes = {
        '0:0': 0,
        '0:180': 1,
        '0:90': 2,
        '90:90': 3,
        '90:270': 4,
        'Random': 5
    }

    filtertypes = {
        '12dBLowpass': 0,
        '24dBLowpass': 1,
        '2x12dBLowpass': 2,
        '12dBHipass': 3,
        'Lowpass+Notch': 4,
        'Hipass+Notch': 5,
        '6dBBandpass': 6,
        '2x6dBBandpass': 7
    }

    legatomodes = {
        'Retrig': 0,
        'Legato': 1,
        'FingerRetrig': 2,
        'FingerLegato': 3
    }

    lfotriggermodes = {
        'Retrig': 0,
        'Free': 1
    }

CalfMonoSynth.parameters = {
    0: {'name': 'O1_Waveform', 'type': 'i', 'values': CalfMonoSynth.osctypes},
    1: {'name': 'O2_Waveform', 'type': 'i', 'values': CalfMonoSynth.osctypes},
    2: {'name': 'O1_PW', 'type': 'f', 'min': -1, 'max': 1},
    3: {'name': 'O2_PW', 'type': 'f', 'min': -1, 'max': 1},
    4: {'name': 'O1-2_Detune', 'type': 'f', 'min': 0, 'max': 100 },
    5: {'name': 'O2_Transpose', 'type': 'i', 'min': -24, 'max': 24},
    6: {'name': 'PhaseMode', 'type': 'i', 'values': CalfMonoSynth.phasemodes},
    7: {'name': 'O1-2_Mix', 'type': 'f', 'min': 0, 'max': 1 },
    8: {'name': 'Filter_Type', 'type': 'i', 'values': CalfMonoSynth.filtertypes},
    9: {'name': 'Filter_Cutoff', 'type': 'f', 'min': 10, 'max': 16000},
    10: {'name': 'Filter_Resonance', 'type': 'f', 'min': 0.7, 'max': 8},
    11: {'name': 'Key_Separation', 'type': 'f','min': -2400, 'max': 2400},
    12: {'name': 'ADSR1->Cutoff', 'type': 'f', 'min': -10800, 'max': 10800},
    13: {'name': 'ADSR1->Resonance', 'type': 'f', 'min': 0, 'max': 1},
    14: {'name': 'ADSR1->Amp', 'type': 'i', 'min': 0, 'max': 1},
    15: {'name': 'ADSR1_Attack', 'type': 'f', 'min': 1, 'max': 20000},
    16: {'name': 'ADSR1_Decay', 'type': 'f', 'min': 10, 'max': 20000},
    17: {'name': 'ADSR1_Sustain', 'type': 'f', 'min': 0, 'max': 1},
    18: {'name': 'ADSR1_Fade', 'type': 'f', 'min': -10000, 'max': 10000},
    19: {'name': 'ADSR1_Release', 'type': 'f', 'min': 10, 'max': 20000},
    20: {'name': 'KeyFollow', 'type': 'f', 'min': 0, 'max': 2},
    21: {'name': 'LegatoMode', 'type': 'i', 'values': CalfMonoSynth.legatomodes},
    22: {'name': 'Portamento', 'type': 'f', 'min': 1, 'max': 2000},
    23: {'name': 'Velocity->Filter', 'type': 'f', 'min': 0, 'max': 1},
    24: {'name': 'Velocity->Amp', 'type': 'f', 'min': 0, 'max': 1},
    25: {'name': 'Volume', 'type': 'f', 'min': 0, 'max': 1}, #0.5 = -6dB ?
    26: {'name': 'PBRange', 'type': 'f', 'min': 0, 'max': 2400},
    27: {'name': 'LFO1Rate', 'type': 'f', 'min': 0.01, 'max': 20},
    28: {'name': 'LFO1Delay', 'type': 'f', 'min': 0, 'max': 5},
    29: {'name': 'LFO1->Filter', 'type': 'f', 'min': -4800, 'max': 4800},
    30: {'name': 'LFO1->Pitch', 'type': 'f', 'min': 0, 'max': 1200},
    31: {'name': 'LFO1->PW', 'type': 'f', 'min': 0, 'max': 1},
    32: {'name': 'ModWheel->LFO1', 'type': 'f', 'min': 0, 'max': 1},
    33: {'name': 'ScaleDetune', 'type': 'f', 'min': 0, 'max': 1},
    34: {'name': 'ADSR2->Cutoff', 'type': 'f', 'min': -10800, 'max': 10800},
    35: {'name': 'ADSR2->Resonance', 'type': 'f', 'min': 0, 'max': 1},
    36: {'name': 'ADSR2->Amp', 'type': 'i', 'min': 0, 'max': 1},
    37: {'name': 'ADSR2_Attack', 'type': 'f', 'min': 1, 'max': 20000},
    38: {'name': 'ADSR2_Decay', 'type': 'f', 'min': 10, 'max': 20000},
    39: {'name': 'ADSR2_Sustain', 'type': 'f', 'min': 0, 'max': 1},
    40: {'name': 'ADSR2_Fade', 'type': 'f', 'min': -10000, 'max': 10000},
    41: {'name': 'ADSR2_Release', 'type': 'f', 'min': 10, 'max': 20000},
    42: {'name': 'O1_Stretch', 'type': 'f', 'min': 1, 'max': 16},
    43: {'name': 'O1_Window', 'type': 'f', 'min': 0, 'max': 1},
    44: {'name': 'LFO1_TriggerMode', 'type': 'i', 'values': CalfMonoSynth.lfotriggermodes},
    45: {'name': 'LFO2_TriggerMode', 'type': 'i', 'values': CalfMonoSynth.lfotriggermodes},
    46: {'name': 'LFO2Rate', 'type': 'f', 'min': 0.01, 'max': 20},
    47: {'name': 'LFO2Delay', 'type': 'f', 'min': 0.1, 'max': 5},
    48: {'name': 'O2_Unison', 'type': 'f', 'min': 0, 'max': 1},
    49: {'name': 'O2_UnisonDetune', 'type': 'f', 'min': 0.01, 'max': 20},
    50: {'name': 'O1_Transpose', 'type': 'i', 'min': -24, 'max': 24},
    51: {'name': 'MidiChannel', 'type': 'i', 'min': 0, 'max': 15}
}
