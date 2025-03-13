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

        extra_dict = {
            'A': 'Kick',
            'B': 'Snare',
            'C': 'VocalsNano',
            'D': 'Feat',
        }


        def extraface_getter(a,b,c,d):
            if 0 in [a,b,c,d]:
                index = [a,b,c,d].index(0)
                return list(extra_dict.values())[index]
            else:
                return 'None'

        def extraface_setter(extra):
            for aux in extra_dict:
                self.set('ExtraFace', f'Aux-{aux}', 'Gain', 0 if extra == extra_dict[aux] else -70)

        self.add_meta_parameter(
            'extraface',
            [('ExtraFace', f'Aux-{x}', 'Gain') for x in 'ABCD'],
            extraface_getter,
            extraface_setter,
        )


        def extrabutt_getter(a,b,c,d):
            if 0 in [a,b,c,d]:
                index = [a,b,c,d].index(0)
                return list(extra_dict.values())[index]
            else:
                return 'None'

        def extrabutt_setter(extra):
            for aux in extra_dict:
                self.set('ExtraButt', f'Aux-{aux}', 'Gain', 0 if extra == extra_dict[aux] else -70)

        self.add_meta_parameter(
            'extrabutt',
            [('ExtraButt', f'Aux-{x}', 'Gain') for x in 'ABCD'],
            extrabutt_getter,
            extrabutt_setter,
        )
