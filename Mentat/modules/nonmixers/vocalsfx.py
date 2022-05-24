from ..nonmixer import NonMixer

class VocalsFX(NonMixer):

    def create_meta_parameters(self):

        name = self.name
        prefix =  self.name[6:].partition('FX')[0] # Nano or Kesch

        def pre_getter(pre_m, pre_n, pre_g):
            return 'off' if pre_m == 1 and pre_n == 1 and pre_g == 1  else 'on'# 3 == all muted

        def pre_setter(state):

            vx = self.engine.modules['Vocals%s' % prefix]
            for v in 'Meuf', 'Normo', 'Gars':
                if vx.get(v.lower()) == 'on' and state == 'on':
                    self.set(prefix + v, 'Mute', 0)
                else:
                    self.set(prefix + v, 'Mute', 1)

            if state == 'on':
                self.set('post', 'on')

        self.add_meta_parameter(
            'pre',
            [['%s%s' % (prefix, v), 'Mute'] for v in ['Meuf', 'Normo', 'Gars']],
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

        def active_getter(pre, post):
            return 'off' if pre == 'off' and post == 'off' else 'on'

        def active_setter(state):
            if state == 'on':
                self.set('pre', 'on')
            else:
                self.set('post', 'off')

        self.add_meta_parameter(
            'active',
            ['pre', 'post'],
            active_getter,
            active_setter
        )
