# import Route base class
from mentat import Route

# import engine & modules objects
# so that they can be used in the routing
from modules import *

class GlobalRoute(Route):
    """
    GlobalRoute object for routing that shouldn't
    change between tracks. Perfect place to manage
    active route selection.

    Every route inherits from it (ensures the global routing is always active)
    Inherits from Route class (required for the engine)
    """

    def route(self, protocol, port, address, args):

        # if address == '/active_keys':
        #     return

        # print('global route:', port, address, args)

        if address == '/set_route':
            engine.set_route(args[0])

    def resetFX(self):

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
        for i in range (1,6):
            samples.set('Samples' + str(i), 'Gain', 'Mute', 1.0)
