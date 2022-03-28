from mentat import Module

import os

class RaySession(Module):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.client_statuses = {}
        self.client_init = []

        self.send('/ray/server/monitor_quit')
        self.send('/ray/server/monitor_announce')

    def route(self, address, args):

        if address == '/ray/monitor/client_state':
            name = args[0]
            status = args[1]
            if status:
                self.client_started(name)
            else:
                self.client_stopped(name)

        elif address == '/ray/monitor/client_event':
            name = args[0]
            event = args[1]
            if event == 'ready':
                if name not in self.client_statuses or self.client_statuses[name] == 0:
                    self.client_started(name)
            elif event == 'stopped_by_server':
                self.client_stopped(name)
            elif event == 'stopped_by_itself':
                self.client_stopped(name)
                self.info('module %s crashed')
                os.popen('dunstify -u critical -a Mentat -t 0 "%s" "a crashé"' % name)

        return False


    def client_started(self, name):

        self.client_statuses[name] = 1

        if name in self.engine.modules:
            module = self.engine.modules[name]
            if name not in self.client_init:
                # first start: load default state if any
                # module.load('default')
                self.client_init.append(name)
            else:
                # restart: send state
                self.logger.info('client %s restarted, sending state' % name)
                module.send_state()

    def client_stopped(self, name):

        self.client_statuses[name] = 0
