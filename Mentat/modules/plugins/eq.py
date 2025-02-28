from .default import Plugin

class AceEQ(Plugin):

    def create_parameters(self):

        self.widgets = [{
            'id': self.id + '/eq_fragment',
            'type': 'fragment',
            'file': 'eq.json',
            'props': {
                'address': '/%s/%s/%s' % (self.mixer_name, self.strip_name, self.name)
            }
        }]
