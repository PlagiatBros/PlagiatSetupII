from mentat import Module
import fnmatch


class PostProcess(Module):
    """
    Post processing effects managers for main mix outputs (bass, synths, samples, vocals)
    """


    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        root = self.engine.root_module

        autotunes = ['NanoMeuf', 'NanoNormo', 'NanoGars', 'KeschMeuf', 'KeschNormo', 'KeschGars']
        basses = ['Bass', 'BassSynths']

        """
        Pitch shifter
        """
        root.add_meta_parameter(
            'pitch_vocals',
            [[autotune, 'pitch'] for autotune in autotunes],
            getter= lambda *p: p[0],
            setter= lambda p: [root.set(autotune, 'pitch', p) for autotune in autotunes]
        )

        root.add_meta_parameter(
            'pitch_bass',
            [['Outputs', bass, 'Pitchshifter', 'Pitch'] for bass in basses],
            getter= lambda *p: p[0],
            setter= lambda p: [root.set('Outputs', bass, 'Pitchshifter', 'Pitch', p) for bass in basses]
        )

        root.add_meta_parameter(
            'pitch_synths',
            [['Outputs', 'Synths', 'Pitchshifter', 'Pitch']],
            getter= lambda p: p,
            setter= lambda p: root.set('Outputs', 'Synths', 'Pitchshifter', 'Pitch', p)
        )

        root.add_meta_parameter(
            'pitch_samples',
            [['Outputs', 'Samples', 'Pitchshifter', 'Pitch']],
            getter= lambda p: p,
            setter= lambda p: root.set('Outputs', 'Samples', 'Pitchshifter', 'Pitch', p)
        )

        pitches = ['vocals', 'bass', 'synths', 'samples']
        root.add_meta_parameter(
            'pitch',
            ['pitch_%s' % pitch for pitch in pitches],
            getter= lambda *p: p[0],
            setter= lambda p: [root.set('pitch_%s' % pitch, p) for pitch in pitches]
        )

        """
        Lowpass filter
        """
        root.add_meta_parameter(
            'filter_bass',
            [['Outputs', bass, 'Lowpass', 'Cutoff'] for bass in basses],
            getter= lambda *f: f[0],
            setter= lambda f: [root.set('Outputs', bass, 'Lowpass', 'Cutoff', f) for bass in basses]
        )

        root.add_meta_parameter(
            'filter_synths',
            [['Outputs', 'Synths', 'Lowpass', 'Cutoff']],
            getter= lambda f: f,
            setter= lambda f: [root.set('Outputs', 'Synths', 'Lowpass', 'Cutoff', f)]
        )

        root.add_meta_parameter(
            'filter_samples',
            [['Outputs', 'Samples', 'Lowpass', 'Cutoff']],
            getter= lambda f: f,
            setter= lambda f: [root.set('Outputs', 'Samples', 'Lowpass', 'Cutoff', f)]
        )

        filters = ['bass', 'synths', 'samples']
        root.add_meta_parameter(
            'filter',
            ['filter_%s' % filter for filter in filters],
            getter= lambda *f: f[0],
            setter= lambda f: [root.set('filter_%s' % filter, f) for filter in filters]
        )

        """
        Cut
        """
        for strip in ['Bass', 'BassSynths', 'Synths', 'Samples']:
            def closure(strip):
                params = [['Outputs', strip, 'Mute'], ['Outputs', strip, 'Aux-A', 'Gain'], ['Outputs', strip, 'Aux-B', 'Gain'], ['Outputs', strip, 'Aux-C', 'Gain']]
                def getter(mute, auxa, auxb, auxc):
                    if mute == 1 and auxa == -70 and auxb == -70 and auxc == -70:
                        return 'on'
                    else:
                        return 'off'
                def setter(state):
                    for p in params:
                        if state == 'on':
                            root.set(*p, -70 if p[-1] == 'Gain' else 1)
                        if state == 'off':
                            root.set(*p, 0 if p[-1] == 'Gain' else 0)
                root.add_meta_parameter(
                    'cut_%s' % strip.lower(),
                    params,
                    getter,
                    setter
                )

            closure(strip)

        cuts = ['cut_bass', 'cut_basssynths', 'cut_synths', 'cut_samples']
        root.add_meta_parameter(
            'cut',
            cuts,
            getter= lambda *states: 'off' if 'on' not in states else 'on',
            setter= lambda state: [root.set('%s' % cut, state) for cut in cuts]
        )



    def set_pitch(self, strip, pitch):
        """
        Set pitch shifting parameter for one or multiple strips.
        For vocals this is handled at the autotuner's level, for the others with AM Pitchshifter

        **Parameters**

        - `strip`: '*', 'vocals', 'bass', 'synths' or 'samples'. Can be a list to target multiple strips.
        - `pitch`: pitch multiplier (0.5 = -1 octave, 2 = +1 octave)
        """
        if type(strip) is list:
            for n in strip:
                self.set_pitch(n, pitch)
            return

        root = self.engine.root_module

        if strip == '*':
            root.set('pitch', pitch)
        else:
            root.set('pitch_%s' % strip.lower(), pitch)

    def animate_pitch(self, strip, start, end, duration, mode='beats', easing='linear'):
        """
        Animate pitch shifting for one or multiple strips

        **Parameters**

        - `strip`: '*', 'vocals', 'bass', 'synths' or 'samples'. Can be a list to target multiple strips.
        - `start`: pitch multiplier start value (0.5 = -1 octave, 2 = +1 octave)
        - `end`: pitch multiplier end value (0.5 = -1 octave, 2 = +1 octave)
        - `duration`: animation duration
        - `mode`: beats or seconds
        - `easing`: interpolation curve (see mentat's documentation)
        """

        if type(strip) is list:
            for n in strip:
                self.animate_pitch(n, start, end, duration, mode, easing)
            return

        root = self.engine.root_module

        if strip == '*':
            root.animate('pitch', start, end, duration, mode, easing)
        else:
            root.animate('pitch_%s' % strip.lower(), start, end, duration, mode, easing)


    def set_filter(self, strip, freq):
        """
        Set lowpass filter cutoff parameter for one or multiple strips, or list of names

        **Parameters**

        - `strip`: '*', 'bass', 'synths' or 'samples'. Can be a list to target multiple strips.
        - `freq`: cutoff frequency in Hz
        """
        if type(strip) is list:
            for n in strip:
                self.set_filter(n, freq)
            return

        root = self.engine.root_module

        if strip == '*':
            root.set('filter', freq)
        else:
            root.set('filter_%s' % strip.lower(), freq)

    def animate_filter(self, strip, start, end, duration, mode='beats', easing='linear'):
        """
        Animate lowpass filter cutoff for one or multiple strips

        **Parameters**

        - `strip`: '*', 'bass', 'synths' or 'samples'. Can be a list to target multiple strips.
        - `start`: cutoff frequency start value in Hz
        - `end`: cutoff frequency end value in Hz
        - `duration`: animation duration
        - `mode`: beats or seconds
        - `easing`: interpolation curve (see mentat's documentation)
        """
        if type(strip) is list:
            for n in strip:
                self.animate_filter(n, start, end, duration, mode, easing)
            return

        root = self.engine.root_module

        if strip == '*':
            root.animate('filter', start, end, duration, mode, easing)
        else:
            root.animate('filter_%s' % strip.lower(), start, end, duration, mode, easing)


    def trap_cut(self, duration):
        root = self.engine.root_module
        def scene():
            for i in range(int(duration)):
                root.set('cut', 'on')
                self.wait(0.5, 'beat')
                root.set('cut', 'off')
                self.wait(0.5, 'beat')

        self.start_scene('trap_cut', scene)

    def slice(self):
        pass

    def animate_slice(self):
        pass
