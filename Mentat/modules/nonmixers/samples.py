from ..nonmixer import NonMixer

class Samples(NonMixer):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.samples_strip = []

    def create_meta_parameters(self):

        super().create_meta_parameters()


        self.samples_strip = [name for name in self.submodules if name not in ['SamplesOut']]
        params = [(name, 'Aux-A', 'Gain') for name in self.samples_strip]


        def getter(*auxes):
            for p in params:
                if self.get(*p) != -70:
                    return p[0]
            return ''

        def setter(lead):
            for p in params:
                self.set(*p, -9 if p[0] == lead else -70)

        self.add_meta_parameter(
            'lead',
            params,
            getter, setter
        )

    def set_lead(self, lead=''):
        if lead == '' or lead in self.samples_strip:
            self.logger.info('set_lead: %s' % lead)
            self.set('lead', lead)
        else:
            self.logger.error('set_lead: unknown sample strip %s' % lead)
