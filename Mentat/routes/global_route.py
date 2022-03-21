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
