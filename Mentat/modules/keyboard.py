from mentat import Module

class Keyboard(Module):
    """
    Base module for keyboard sound banks (mididings patches)
    """

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.send('/mididings/query')

        self.add_parameter('scene', '/mididings/switch_scene', 'i', default=1)
        self.add_parameter('subscene', '/mididings/switch_subscene', 'i', default=1)

        self.add_parameter('sounds', None, 's', default='')
        self.add_parameter('current_sound', None, 's', default='')
        self.add_parameter('boost', None, 'i', default=0)

        self.sounds = []

        self.scenes = {}
        self.pending_scene = None


    def route(self, address, args):
        """
        Retrieve available sounds from mididings
        """
        if address == '/mididings/begin_scenes':
            self.scenes = {}
            self.sounds = []

        elif address == '/mididings/add_scene':

            scene_number, scene_name, *subscenes = args
            self.scenes[scene_name] = {
                'number': scene_number,
                'subscenes': subscenes
            }
            self.sounds += subscenes


        elif address == '/mididings/end_scenes':
            if self.scenes and self.pending_scene != None:
                self.set_sound(self.pending_scene)
                self.pending_scene = None
            self.set('sounds', ','.join(self.sounds))

        return False

    def set_sound(self, name, boost=False, lead=None):
        """
        Set sound by name

        **Parameters**

        - `name`: name of sound (subscene in mididings patch)
        """
        if lead == None :
            # transition from legacy "boost" argname
            lead = boost


        if not self.scenes:
            self.pending_scene = name
        else:
            for scene in self.scenes:
                if name in self.scenes[scene]['subscenes']:
                    self.set('scene', self.scenes[scene]['number'])
                    self.set('subscene', self.scenes[scene]['subscenes'].index(name) + 1)
                    self.set('current_sound', name)
                    self.logger.info('switched to sound "%s"' % name)

                    if lead:
                        self.engine.modules['Synths'].set_lead(name)

                    return
            self.logger.error('sound "%s" not found' % name)


    def set_boost(self, boost=False):
        return
        """
        for scene in self.scenes:
            for subs in self.scenes[scene]['subscenes']:
                if subs.startswith('C') and 'Sampler' not in subs:
                    subs = subs[1:]
                if not subs.startswith('Low') and subs in self.engine.modules['Synths'].submodules:
                    self.engine.modules['Synths'].set(subs, 'Aux-A', 'Gain', -70.0)

        name = self.get('current_sound')
        if boost and not name.startswith('Low'):
            if name in self.engine.modules['Synths'].submodules:
                self.logger.info('|-> boost on "%s" sound' % name)
                self.engine.modules['Synths'].set(name, 'Aux-A', 'Gain', 0.0)

        self.set('boost', int(boost))
        """
