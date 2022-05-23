from mentat import Module

class PedalBoard(Module):
    """
    Pedalboard controller
    """

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.route_select = False

        self.route_map = {
            1: 'Snapshat'
        }


    def route(self, address, args):
        """
        Let  messages pass, unless we're in route selection mode (toggle with button 12)
        """
        if address != '/pedalBoard/button':
            return False

        if args[0] > 12:

            self.bass_pedal(args[0] - 12)
            return False

        elif args[0] == 12:

            self.route_select = not self.route_select

            if self.route_select:
                self.logger.info('switched to route selection mode')
            else:
                self.logger.info('switched normal mode')

            return False # bypass further routing

        elif self.route_select:

            if args[0] in self.route_map:
                self.engine.set_route(self.route_map[args[0]])
            else:
                self.logger.info('no route in map for button %i' % args[0])

            self.route_select = False

            return False # bypass further routing

        else:
            pass

    def bass_pedal(self, button):

        if button == 1:

            self.engine.modules['AudioLooper'].record(0)

        elif button == 2:

            self.engine.modules['AudioLooper'].overdub(0)

        elif button == 3:

            self.engine.modules['AudioLooper'].pause(0)

        elif button == 4:

            self.engine.modules['OpenStageControl'].transport_start()

        elif button == 5:

            self.engine.modules['ConstantSampler'].send('/instrument/play', 's:Plagiat/ConstantKit/AirHorn', 100)
