from mentat.module import Module

import os

class RaySession(Module):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.ray_version = "0.12.0"

        self.statuses = {}

    def initialize(self, *args, **kwargs):

        super().initialize(*args, **kwargs)

        self.send('/ray/server/gui_disannounce')
        self.send('/ray/server/gui_announce', self.ray_version, 0, "", os.getpid(), 0)


    def route(self, address, args):

        if address == '/ray/gui/client/status' and len(args) == 2:
            """
            name: client_id
            status: 0 or 1
            """
            name = args[0]#.lower()
            status = args[1]

            if name not in self.statuses:
                self.statuses[name] = -1

            if self.statuses[name] != status:
                self.info('%s is %s' % (name, "running" if status else "stopped"))
                self.statuses[name] = status
                if not status:
                    # stopped normally
                    pass
                elif name in self.engine.modules:
                    # started normally
                    module = self.engine.modules[name]
                    module.load('default')

        if address == '/ray/gui/server/message':
            if 'terminated itself' in args[0] or 'terminé de lui-même' in args[0]:
                name = args[0].split(':')[0]
                self.info('module %s crashed')
                os.popen('dunstify -u critical -a Mentat -t 0 "%s" "a crashé"' % name)


        return False
