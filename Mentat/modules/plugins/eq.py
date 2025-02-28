from .default import Plugin

class AceEQ(Plugin):

    def create_parameters(self):
        self.modal['popupHeight'] =800
        self.widgets = [{
            'id': self.id + '/eq_fragment',
            'type': 'fragment',
            'expand': True,
            'file': 'eq.json',
            'props': {
                'variables': {
                    'address': '/%s/%s/%s' % (self.mixer_name, self.strip_name, self.name)
                }
            }
        }]
