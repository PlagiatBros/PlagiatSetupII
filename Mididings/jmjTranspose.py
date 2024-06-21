from mididings import *
from mididings.event import PitchbendEvent
from mididings.extra.inotify import AutoRestart
from mididings.extra.osc import SendOSC
from mididings.extra.osc import OSCInterface
import mididings.engine as _engine
import mididings.event as _event
from ports import get_port

name = 'JmjTranspose'

inPort = get_port(name)
mentatPort = get_port('Mentat')

config(
    backend='alsa',
    client_name=name,
    out_ports=['out'],
    in_ports=['in']
)

hook(
    OSCInterface(inPort, mentatPort),
    AutoRestart()
)

out = Velocity(curve=2.5)  >> Output('out')

run(
    scenes = {
        1: Scene('0', Transpose(0) >> out),
        2: Scene('-2', Transpose(-24) >> out),
        3: Scene('-1', Transpose(-12) >> out),
        4: Scene('1', Transpose(12) >> out),
        5: Scene('2', Transpose(24) >> out),
    }
)
