from ..nonmixer import NonMixer

class Inputs(NonMixer):

    def create_meta_parameters(self):

        super().create_meta_parameters()

        def getter(static_mute, dynamic_mute):
            if static_mute == 0.0 and dynamic_mute == 1.0:
                return 'static'
            if static_mute == 1.0 and dynamic_mute == 0.0:
                return 'dynamic'
            else:
                return '?'

        def setter(source):
            if source == 'static':
                self.set('VocalsKesch', 'Mute', 0.0)
                self.set('VocalsKeschB', 'Mute', 1.0)
            elif source == 'dynamic':
                self.set('VocalsKesch', 'Mute', 1.0)
                self.set('VocalsKeschB', 'Mute', 0.0)

        self.add_meta_parameter(
            'keschmic',
            [('VocalsKesch', 'Mute'), ('VocalsKeschB', 'Mute')],                                                   # params
            getter, setter
        )
