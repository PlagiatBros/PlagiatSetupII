from mentat import Module

import os

class RaySession(Module):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.ray_version = "0.12.0"

        self.client_statuses = {}
        self.client_init = []

        if not self.engine.restarted:
            self.send('/nsm/server/announce', 'RaySessionMonitor', ':monitor:', '', 1, 1,  os.getpid())
        else:
            self.send('/nsm/server/monitor_reset')

    def route(self, address, args):

        self.info([address, args])

        if address == '/nsm/client/open':
            self.send('/reply', '/nsm/client/open', '')

        elif address == '/nsm/client/monitor/client_state':
            name = args[0]
            status = args[1]
            if status:
                self.client_started(name)
            else:
                self.client_stopped(name)

        elif address == '/nsm/client/monitor/client_event':
            name = args[0]
            event = args[1]
            if event == 'client_ready':
                if name not in self.client_statuses or self.client_statuses[name] == 0:
                    self.client_started(name)
            elif event == 'client_stopped_by_server':
                self.client_stopped(name)
            elif event == 'client_stopped_by_itself':
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
                module.load('default')
                self.client_init.append(name)
            else:
                # restart: send state
                module.send_state()

    def client_stopped(self, name):

        self.client_statuses[name] = 0
