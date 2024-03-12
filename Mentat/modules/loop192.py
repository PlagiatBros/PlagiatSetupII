from mentat import Module
import json


loops=[
    'ZHi',
    'ZLow',
    'CHi',
    'CLow',
    'Fluid_TenorSax',
    'Fluid_Charang',
    'Fluid_OrchestraHit',
    'Fluid_SteelDrum',
    'Fluid_Rhodes',
    'Fluid_MajorVocals',
    'ProdSampler',
    'ConstantSampler',
]

class Loop(Module):
    """
    Loop submodule (unnused)
    """

    def __init__(self, *args, loop_n, **kwargs):

        super().__init__(*args, **kwargs)

        self.loop_n = loop_n

    #     self.engine.add_event_callback('parameter_changed', self.parameter_changed)
    #
    # def parameter_changed(self, module, name, value):
    #     if module == self:ifif
    #         if name == 'mute':
    #             if self.get('mute'):
    #                 self.send('/loop/%s/hit' % self.loop_n, 'mute_on')
    #             else:
    #                 self.send('/loop/%s/hit' % self.loop_n, 'mute_off')
    #         elif name ==

class Loop192(Module):
    """
    Midilooper
    """

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.add_parameter('cycle', '/set', 'sf', static_args=['eighth_per_cycle'], default=8)
        self.add_parameter('tempo', '/set', 'sf', static_args=['tempo'], default=120)
        self.add_parameter('playing', None, 'i', default=0)

        i = 0
        for name in loops:
            loop = Loop(name, loop_n=i, parent=self)

            self.add_submodule(loop)
            loop.add_parameter('mute', None, 'i', default=0)
            loop.add_parameter('recording', None, 'i', default=0)
            loop.add_parameter('overdubbing', None, 'i', default=0)
            loop.add_parameter('waiting', None, 'i', default=0)



        self.start_scene('querystate', self.query_state)



    def query_state(self):
        while True:
            self.send('/status')
            self.wait(0.1, 's')


    def route(self, address, args):
        return False
        if address == '/status':
            data = json.loads(args[0])
            i = 0
            for loopstate in data['loops']:
                name = loops[i]
                self.set(name, 'mute', loopstate['mute'])
                self.set(name, 'recording', loopstate['recording'])
                self.set(name, 'waiting', loopstate['waiting'])
                self.set(name, 'overdubbing', loopstate['overdubbing'])



    def get_loop_n(self, name):
        if name in loops:
            return loops.index(name)
        elif name == '-1' or name == -1:
            return '*'

        return name

    def start(self):
        """
        Start playback
        """
        self.send('/play')
        self.set('playing', 1)

    def stop(self):
        """
        Stop playback
        """
        self.send('/stop')
        self.set('playing', 0)

    def record(self, i):
        """
        Record
        """
        self.send('/loop/%s/hit' % self.get_loop_n(i), 'record')

    def overdub(self, i):
        """
        Overdub
        """
        self.send('/loop/%s/hit' % self.get_loop_n(i), 'overdub')

    def pause(self, i):
        self.send('/loop/%s/hit' % self.get_loop_n(i), 'mute_on')

    def unpause(self, i):
        self.send('/loop/%s/hit' % self.get_loop_n(i), 'mute_off')
