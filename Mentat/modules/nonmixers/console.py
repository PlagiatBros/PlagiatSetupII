from ..nonmixer import NonMixer

class Console(NonMixer):

    def create_meta_parameters(self):

        super().create_meta_parameters()


        params = [(name, 'Mute') for name in self.submodules]

        multi = [0.0 if p[0] != 'FOH' else 1.0 for p in params]
        stereo = [1.0 if p[0] != 'FOH' else 0.0 for p in params]


        def getter(*mutes):
            if list(mutes) == multi:
                return 'multi'
            elif list(mutes) == stereo:
                return 'stereo'
            else:
                return '?'

        def setter(mode):
            for i, p in enumerate(params):
                if mode == 'multi':
                    self.set(*p, multi[i])
                elif mode == 'stereo':
                    self.set(*p, stereo[i])


        self.add_meta_parameter(
            'mode',
            params,
            getter, setter
        )
