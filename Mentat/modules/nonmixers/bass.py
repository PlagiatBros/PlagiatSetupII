from ..nonmixer import NonMixer

class Bass(NonMixer):

    def create_meta_parameters(self):

        super().create_meta_parameters()

        def getter(leduc_mute, fbass_mute):
            if leduc_mute == 0.0 and fbass_mute == 1.0:
                return 'leduc'
            if leduc_mute == 1.0 and fbass_mute == 0.0:
                return 'fbass'
            else:
                return '?'

        def setter(source):
            if source == 'leduc':
                self.set('BassDry', 'Mute', 0.0)
                self.set('FBassDry', 'Mute', 1.0)
            elif source == 'fbass':
                self.set('BassDry', 'Mute', 1.0)
                self.set('FBassDry', 'Mute', 0.0)

        self.add_meta_parameter(
            'source',
            [('BassDry', 'Mute'), ('FBassDry', 'Mute')],                                                   # params
            getter, setter
        )
