# import Route base class
from mentat import Route

# import engine & modules objects
# so that they can be used in the routing
from modules import *

from inspect import getmembers

class pedalboard_button():
    """
    Decorator for route methods that can be called directly
    from pedalboard button messages
    """
    def __init__(self, button):
        self.button = button
    def __call__(self, method):
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
        if not hasattr(method, 'mk2_buttons'):
            method.mk2_buttons = {}
        method.mk2_buttons[self.button] = self.color
        return method

class RouteBase(Route):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.direct_routing = {
            '/pedalboard/button': {},
            '/mk2/button': {},
        }
        self.mk2_lights = {}

        for name, method in getmembers(self):

            if hasattr(method, 'pedalboard_buttons'):
                for button in method.pedalboard_buttons:
                    if button not in self.direct_routing['/pedalboard/button']:
                        self.direct_routing['/pedalboard/button'][button] = []
                    self.direct_routing['/pedalboard/button'][button].insert(0, method)

            if hasattr(method, 'mk2_buttons'):
                for button in method.mk2_buttons:
                    if button not in self.direct_routing['/pedalboard/button']:
                        self.direct_routing['/pedalboard/button'][button] = []
                    self.direct_routing['/pedalboard/button'][button].insert(0, method)
                    self.mk2_lights[button] = method.mk2_buttons[button]

    def activate(self):

        mk2Control.set_lights(self.mk2_lights)

        super().activate()


    def route(self, protocol, port, address, args):
        """
        Base routing for all routes
        """
        if address in self.direct_routing:
            if args[0] in self.direct_routing[address]:
                for method in self.direct_routing[address][args[0]]:
                    method()

        if address == '/set_route':
            engine.set_route(args[0])


    def start_sequence(self, name, *args, **kwargs):
        """
        Start scene with sequence prefix and self.play_sequence() as method
        """
        self.start_scene('sequences/%s' % name, self.play_sequence, *args, **kwargs)

    def stop_sequence(self, name, *args, **kwargs):
        """
        Stop scene with sequence prefix
        """
        self.stop_scene('sequences/%s' % name)

    def resetFX(self):
        """
        Reset effects
        """
        # BassFX
        for name in bassFX.meta_parameters:
            bassFX.set(name, 'off')


        for name, mod in engine.modules.items():

            # SynthsFX
            if 'SynthsFX' in name:
                for name in mod.submodules:
                    # Ins
                    if name not in mod.name:
                        mod.set(name, 'Gain', 'Gain', -70.0)

                # Outs
                mod.set(mod.name, 'Gain', 'Mute', 1.0)


            # SamplesFX
            elif 'SamplesFX' in name:
                for i in range(1,6):
                    # Ins
                    mod.set('Samples' + str(i), 'Gain', 'Gain', -70.0)

                # Outs
                mod.set(name, 'Gain', 'Mute', 1.0)

            # VocalsFX
            elif 'VocalsNanoFX' in name or 'VocalsKeschFX' in name:
                for name in mod.submodules:
                    # Ins
                    if name not in mod.name:
                        mod.set(name, 'Gain', 'Gain', -70.0)
                # Outs
                mod.set(name, 'Gain', 'Mute', 1.0)

    def resetSamples(self):
        """
        Reset (mute) all samples
        """
        for i in range (1,6):
            samples.set('Samples' + str(i), 'Gain', 'Mute', 1.0)

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
