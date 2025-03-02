from .default import Plugin

class AceComp(Plugin):

    enable_feedback = True

    def create_parameters(self):
        self.modal['popupHeight'] = 800
        self.modal['popupPadding'] = 8
        self.widgets = [{
            'id': self.id + '/eq_fragment',
            'type': 'fragment',
            'expand': True,
            'file': 'comp.json',
            'props': {
                'variables': {
                    'address': '/%s/%s/%s' % (self.mixer_name, self.strip_name, self.name)
                }
            }
        }]
