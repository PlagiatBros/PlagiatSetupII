from pyalsa import alsaseq

from mentat import Module

class AlsaPort():
    def __init__(self, name, id):
        self.name = name
        self.id = id


class AlsaClient():

    def __init__(self, name, id, ports):

        self.name = name
        self.id = id
        self.ports = {}

        for port in ports:
            port_name, port_id, connection_list = port
            self.ports[port_name] = AlsaPort(port_name, port_id)


class AlsaPatcher(Module):
    """
    A dead simple Alsa MIDI patcher inspired by asspatch
    """

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.seq = alsaseq.Sequencer(clientname='alsapatcher')

        self.connections = []

        self.clients = {}

    def load(self, file):
        """
        Load a patch from file. Each line must be of the following form:
        clientname:portname |> clientname:portname
        """
        self.connections = []

        try:
            f = open(file, 'r')
        except:
            self.logger.error('Error: Alsa MIDI: could not open patch file "%s"' % file)
            return

        i=0
        for line in f.readlines():
            i += 1

            if len(line):
                src, _, dest = line.partition('|>')
                src_client_name, _, src_port_name = src.strip().rpartition(':')
                dest_client_name, _, dest_port_name = dest.strip().rpartition(':')

                if len(src_client_name) and len(src_port_name) and len(dest_client_name) and len(dest_port_name):

                    self.connections.append((src_client_name, src_port_name, dest_client_name, dest_port_name))

                else:
                    self.logger.error('Error: Alsa MIDI: could not parse connection "%s" at line %i' % (line, i))

    def get_client(self, name):

        if name in self.clients:
            return self.clients[name]
        else:
            self.logger.error('Error: Alsa MIDI: client "%s" not found' % name)


    def get_port(self, client, port_name):

            if port_name in client.ports:
                return client.ports[port_name]
            else:
                self.logger('Error: Alsa MIDI: port "%s" not found in client "%s"' % (port_name, client.name))


    def apply_patch(self):
        """
        Apply patch : attempt to make very connection in memory and ignore reconnection errors.
        """

        for connection in self.connections:

            src_client_name, src_port_name, dest_client_name, dest_port_name = connection

            src_client = self.get_client(src_client_name)
            dest_client = self.get_client(dest_client_name)

            if src_client and dest_client:

                src_port = self.get_port(src_client, src_port_name)
                dest_port = self.get_port(dest_client, dest_port_name)

                if src_port and dest_port:

                    try:
                        self.seq.connect_ports((src_client.id, src_port.id), (dest_client.id, dest_port.id))
                    except:
                        # already connected
                        pass


    def get_alsa_connections(self):
        """
        connection_list(...) method of alsaseq.Sequencer instance
            connection_list() -> list

            List all clients and their ports connections.

            Returns:
              (list) a list of tuples: client_name, client_id, port_list:.
                client_name -- the client's name.
                client_id -- the client's id.
                port_list -- a list of tuples: port_name, port_id, connection_list:
                  port_name -- the name of the port.
                  port_id -- the port id.
                  connection_list -- a list of tuples: read_conn, write_conn:
                    read_conn -- a list of (client_id, port_id, info) tuples this
                                 port is connected to (sends events);
                                 info is the same of the get_connect_info() method.
                    write_conn -- a list of (client_id, port_id, info) tuples this
                                  port is connected from (receives events);
                                  info is the same of the get_connect_info() method.
        """

        clients = self.seq.connection_list()

        for client in clients:

            client_name, client_id, port_list = client

            self.clients[client_name] = AlsaClient(
                name=client_name,
                id=client_id,
                ports=port_list
            )

    def connect(self, timeout=0.5):
        """
        Query alsa ports and apply
        """
        self.start_scene('connect', lambda:[
            self.wait(timeout, 'seconds'),
            self.get_alsa_connections(),
            self.apply_patch()
        ])