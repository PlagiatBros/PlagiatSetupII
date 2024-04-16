# import Route base class
from mentat import Route

# import engine & modules objects
# so that they can be used in the routing
from modules import *

from inspect import getmembers

method_index = 0
class pedalboard_button():
    """
    Decorator for route methods that can be called directly
    from pedalboard button messages
    """
    def __init__(self, button):
        self.button = button
    def __call__(self, method):
        if not hasattr(method, 'index'):
            global method_index
            method.index = method_index
            method_index += 1
        if not hasattr(method, 'pedalboard_buttons'):
            method.pedalboard_buttons = {}
        method.pedalboard_buttons[self.button] = True
        return method

class mk2_button():
    """
    Decorator for route methods that can be called directly
    from mk2 button messages

    Handles the buttons' colors.
    """
    def __init__(self, button, color='cyan'):
        self.button = button
        self.color = color
    def __call__(self, method):
        if not hasattr(method, 'index'):
            global method_index
            method.index = method_index
            method_index += 1
        if not hasattr(method, 'mk2_buttons'):
            method.mk2_buttons = {}
        if not self.button in method.mk2_buttons:
            method.mk2_buttons[self.button] = self.color
        return method

class gui_button():
    """
    Decorator for route methods that can be called directly
    from gui buttons
    """
    def __init__(self, **data):
        self.data = data
    def __call__(self, method):
        if not hasattr(method, 'index'):
            global method_index
            method.gui_data = dict(self.data)
            method.index = method_index
            method_index += 1
        method.gui_button = True
        return method


class RouteBase(Route):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.direct_routing = {
            '/pedalBoard/button': {},
            '/mk2/button': {},
        }
        self.mk2_lights = {}

        for name, method in getmembers(self):

            if hasattr(method, 'pedalboard_buttons'):
                for button in method.pedalboard_buttons:
                    if button not in self.direct_routing['/pedalBoard/button']:
                        self.direct_routing['/pedalBoard/button'][button] = []
                    self.direct_routing['/pedalBoard/button'][button].insert(0, method)

            if hasattr(method, 'mk2_buttons'):
                for button in method.mk2_buttons:
                    if button not in self.direct_routing['/mk2/button']:
                        self.direct_routing['/mk2/button'][button] = []
                    self.direct_routing['/mk2/button'][button].insert(0, method)
                    self.mk2_lights[button] = method.mk2_buttons[button]

    def activate(self):

        mk2Control.set_lights(self.mk2_lights)

        super().activate()


    def route(self, protocol, port, address, args):
        """
        Base routing for all routes
        """
        if address in self.direct_routing:
            if len(args) > 0 and args[0] in self.direct_routing[address]:
                for method in self.direct_routing[address][args[0]]:
                    method()

        if address == '/set_route':
            engine.set_route(args[0])


    def start_sequence(self, name, sequence, loop=True):
        """
        Start scene with sequence prefix and self.play_sequence() as method

        **Parameters**

        - `name`: name of sequence
        - `sequence`: see Route.play_sequences()
        - `loop`: see Route.play_sequences()
        """
        self.start_scene('sequences/%s' % name, self.play_sequence, sequence, loop)

    def stop_sequence(self, name):
        """
        Stop scene with sequence prefix

        **Parameters**

        - `name`: name of sequence
        """
        self.stop_scene('sequences/%s' % name)
        self.stop_scene('sequence/%s' % name)

    def resetFX(self):
        """
        Reset effects
        """
        # BassFX
        bassFX.reset('BassDegrade', 'MDA%20Degrade', 'rate')
        bass.set('BassDry', 'GxChorus-Stereo', 'BYPASS', 0)

        for name in bassFX.meta_parameters:
            bassFX.set(name, 'off')


        for name, mod in engine.modules.items():

            # Synths Pan
            if name == 'Synths' or name == 'BassSynths':
                for name in mod.submodules:
                    if 'Pan' in mod.submodules[name].parameters:
                        mod.submodules[name].set('Pan', 0.0)
                    if 'Amp' in mod.submodules[name].submodules:
                        mod.submodules[name].set('Amp', 'Gain', 1.0)


            # SynthsFX
            elif 'SynthsFX' in name:

                for name in mod.submodules:
                    # Ins
                    if name not in mod.name:
                        mod.set(name, 'Gain', -70.0)


                # Outs
                mod.set(mod.name, 'Mute', 1.0)


            # SamplesFX
            elif 'SamplesFX' in name:
                for i in range(1,6):
                    # Ins
                    mod.set('Samples' + str(i), 'Gain', -70.0)

                mod.set('ConstantSampler', 'Gain', -70.0)

                # Outs
                mod.set(name, 'Mute', 1.0)

            # VocalsFX
            elif 'VocalsNanoFX' in name or 'VocalsKeschFX' in name:
                mod.set('pre', 'off')
                v = 'Nano' if 'Nano' in name else 'Kesch'
                # mod.set('%sAB' % v, 'Mute', 1)
            elif 'VocalsFeatFX' in name:
                mod.set('pre', 'off')

            elif name in ['NanoMeuf', 'NanoNormo', 'NanoGars', 'KeschMeuf', 'KeschNormo', 'KeschGars',  'FeatMeuf', 'FeatNormo', 'FeatGars']:
                mod.set('correction', 1)


        for mixer, strip in [
                ('SamplesFX1Delay', 'SamplesFX1Delay'),
                ('SynthsFX2Delay', 'SynthsFX2Delay'),
                ('VocalsNanoFX1Delay', 'VocalsNanoFX1Delay'),
                ('VocalsKeschFX1Delay', 'VocalsKeschFX1Delay'),
                ('VocalsFeatFX1Delay', 'VocalsFeatFX1Delay')
                ]:

            self.engine.modules[mixer].set(strip, 'GxMultiBandDelay', 'feedback', 0.5)


        samplesFX2Delay.set('SamplesFX2Delay', 'ReverseDelay', 'Wet', -70)
        synthsFX3Delay.set('SynthsFX3Delay', 'AutoFilter', 'dsp/bypass', 1)

        postprocess.set_filter('*', 21600)
        postprocess.set_pitch('*', 1)

    def resetSamples(self):
        """
        Reset (mute) all samples
        """
        for i in range (1,6):
            samples.set('Samples' + str(i), 'Mute', 1.0)
            samples.set('Samples' + str(i), 'Gain', 0)

    def reset_leads(self):
        """
        Reset leads gain boosts
        """
        synths.set_lead()
        # samples.set_lead(None)

    def pause_loopers(self):
        """
        Pause loopers and looped scenes (sequences)
        """
        # stop all mentat sequences
        self.stop_sequence('*')
        # pause all loops
        looper.pause()

    def reset(self):
        """
        Reset samples and effects
        """
        self.resetFX()
        self.resetSamples()
        self.reset_leads()

        self.engine.set('cut', 'off')


    def set_samples_aliases(self, aliases):
        for name, mod in engine.modules.items():
            if name == 'Samples' or 'SamplesFX' in name:
                mod.set_aliases(aliases)
