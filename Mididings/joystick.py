# coding=utf8
from utils.joystick import Joystick
from ports import get_port

import mididings
from mididings.engine import output_event
from mididings.event import PitchbendEvent, NoteOnEvent, CtrlEvent
from mididings.extra.inotify import AutoRestart
from liblo import ServerThread

mididings.config(
    backend = 'alsa',
    client_name = 'Joystick',
    out_ports = ['out']
)

mentatPort = get_port('Mentat')

server = ServerThread(get_port('Joystick'))
server.start()

def process(type, name, value):

    server.send(mentatPort, '/%s' % type, name, value)

    if type == 'axis':
        if name == 'x':
            output_event(PitchbendEvent('out', 2, int(value * 8192)))
        #elif name == 'rx':
        #    output_event(CtrlEvent('out', 1, 1, int(100 * abs(value))))

    elif type == 'status':
        if name == 'connected' and value == 0:
            process('axis', 'x', 0)
            process('axis', 'rx', 0)

mididings.hook(
    Joystick(dev=0, callback=process),
    #AutoRestart()
)

mididings.run(mididings.Pass())
