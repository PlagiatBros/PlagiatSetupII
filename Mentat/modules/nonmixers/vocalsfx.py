from ..nonmixer import NonMixer

class VocalsFX(NonMixer):

    def create_meta_parameters(self):

        name = self.name
        prefix =  self.name[6:].partition('FX')[0] # Nano or Kesch

        def pre_getter(pre_m, pre_n, pre_g):
            return 'off' if pre_m + pre_n + pre_g == -210  else 'on'# -70db * 3

        def pre_setter(state):
            for v in 'Meuf', 'Normo', 'Gars':
                self.set(prefix + v, 'Gain', 0 if state == 'on' else -70)
            if state == 'on':
                self.set('post', 'on')

        self.add_meta_parameter(
            'pre',
            [['%s%s' % (prefix, v), 'Gain'] for v in ['Meuf', 'Normo', 'Gars']],
            pre_getter,
            pre_setter
        )

        def post_getter(post_mute):
            return 'off' if post_mute == 1 else 'on'

        def post_setter(state):
            self.set(name, 'Mute', 0 if state == 'on' else 1)
            if state == 'off':
                self.set('pre', 'off')

        self.add_meta_parameter(
            'post',
            [[name, 'Mute']],
            post_getter,
            post_setter
        )
