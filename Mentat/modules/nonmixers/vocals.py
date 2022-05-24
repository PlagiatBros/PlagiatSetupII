from ..nonmixer import NonMixer

class Vocals(NonMixer):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)


    def create_meta_parameters(self):

        strip_prefix = self.name[6:] # remove "Vocals" prefix

        fxs = [self.engine.modules[name] for name in self.engine.modules if 'FX' in name and strip_prefix in name]

        for name in ['normo', 'gars', 'meuf']:

            def closure(name):

                strip_name = strip_prefix + name.capitalize()
                ab_strip_name = strip_prefix + 'AB' + name.capitalize()

                def getter(mute, ab_mute):
                    if mute == 0.0 and ab_mute == 0.0:
                        return 'on'
                    elif mute == 1.0 and ab_mute == 1.0:
                        return 'off'
                    else:
                        return '?'

                def setter(state):
                    if state == 'on':
                        self.set(strip_name, 'Mute', 0.0)
                        self.set(ab_strip_name, 'Mute', 0.0)
                        for vx in ['normo', 'gars', 'meuf']:
                            if vx != name:
                                vx_strip_name = strip_prefix + vx.capitalize()
                                self.set(vx_strip_name, 'Aux-A', 'Gain', 0)
                                self.set(vx_strip_name, 'Aux-B', 'Gain', -70)
                    elif state == 'off':
                        self.set(strip_name, 'Mute', 1.0)
                        self.set(ab_strip_name, 'Mute', 1.0)

                    for fx in fxs:
                        if fx.get('pre') == 'on' and fx.get('post') == 'on':
                            fx.set('%s%s' % (strip_prefix, name.capitalize()), 'Mute', 0 if state == 'on' else 1)


                self.add_meta_parameter(
                    name,
                    [[strip_name, 'Mute'], [ab_strip_name, 'Mute']],
                    getter,
                    setter
                )

            closure(name)


        for name in ['normo', 'gars', 'meuf']:

            def closure(name):

                self.add_meta_parameter(
                    name + '_exclu',
                    ['normo', 'gars', 'meuf'],
                    lambda n,g,m: None,
                    lambda state: [self.set(n, 'on' if n == name else 'off') for n in ['normo', 'gars', 'meuf']]
                )

            closure(name)
