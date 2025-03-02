import urllib

class Plugin():

    enable_feedback = False

    def __init__(self, plugin):

        self.plugin = plugin
        self.name = plugin.name
        self.mixer_name = plugin.parent_module.parent_module.name
        self.strip_name = plugin.parent_module.name
        self.id = '%s/%s/%s' % (self.mixer_name, self.strip_name, self.name)

        self.modal = {
            'id': self.id,
            'address': '/OpenStageControl/call',
            'preArgs': '["display_modal", "%s"]' % self.id,
            'type': 'modal',
            'label': urllib.parse.unquote(self.name),
            'popupLabel': '%s > %s' % (urllib.parse.unquote(self.strip_name), urllib.parse.unquote(self.name)),
            'layout': 'horizontal',
            'height': 30,
            'css': 'class: plugin-modal',
            'popupPadding': 1,
            'innerPadding': True,
            'popupHeight': 400,
            'popupWidth': 800,
            'widgets': []
        }

        self.widgets = []

        self.create_parameters()

    def create_parameters(self):

        control = {
            'type': 'panel',
            'padding': 0,
            'layout': 'horizontal',
            'expand': True,
            'contain': False,
            'widgets': []
        }
        feedback = {
            'type': 'panel',
            'padding': 1,
            'innerPadding': False,
            'layout': 'horizontal',
            'widgets': []
        }
        panel = {
            'type': 'panel',
            'padding': 0,
            'layout': 'horizontal',
            'expand': True,
            'widgets': [control]
        }

        for pname in self.plugin.parameters:

            if pname in self.plugin.meta_parameters:
                # hide meta parameters
                continue

            param = self.plugin.parameters[pname]

            if hasattr(param, 'range'):
                if param.feedback_only:
                    feedback['widgets'].append({
                        'type': 'fader',
                        'id': '%s/%s' % (self.id, param.name),
                        'design': 'compact',
                        'knobSize': 0,
                        'html': '<div class="label">%s</div><div class="value">@{this}</div>' % urllib.parse.unquote(pname),
                        'range': {'min': {'%.1f' % param.range[0]: param.range[0]}, 'max': {'%.1f' % param.range[1]: param.range[1]}},
                        # 'dashed': [2,2],
                        'address': '/%s/%s/%s' % (self.mixer_name, self.strip_name, self.name),
                        'preArgs': pname,
                        'default': param.args[0],
                        'interaction': False
                    })
                else:
                    control['widgets'].append({
                        'type': 'panel',
                        'layout': 'vertical',
                        'css': 'class: strip',
                        'html': '<div class="label center">%s</div>' % urllib.parse.unquote(pname),
                        'width': 100,
                        'widgets': [
                            {
                                'type': 'knob',
                                'id': '%s/%s' % (self.id, param.name),
                                'horizontal': True,
                                'pips': True,
                                'range': {'min': {'%.1f' % param.range[0]: param.range[0]}, 'max': {'%.1f' % param.range[1]: param.range[1]}},
                                'default': param.args[0],
                                'doubleTap': True,
                                'linkId': param.address,
                                'address': '/%s/%s/%s' % (self.mixer_name, self.strip_name, self.name),
                                'preArgs': pname,
                                'decimals': 5,
                                'pips': True,
                                'expand': True,
                                'design': 'solid'
                            },
                            {
                                'type': 'input',
                                'width': 120,
                                'decimals': 5,
                                'linkId': param.address,
                                'bypass': True,
                                'numeric': True
                            }
                        ]
                    })

        if feedback['widgets']:
            panel['widgets'].append(feedback)
            feedback['width'] = 50 * len(feedback['widgets'])

        self.widgets = [panel]
