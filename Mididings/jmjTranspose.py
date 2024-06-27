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

invertPedal= Pass()
# [CtrlFilter(64) >> [
#     CtrlValueFilter(0) >> Ctrl(64, 127),
#     CtrlValueFilter(127) >> Ctrl(64, 0),
#     ], ~CtrlFilter(64)]
run(
    scenes = {
        1: Scene('0', [Filter(NOTE)  >> Transpose(0), ~Filter(NOTE) >> invertPedal]  >> out),
        2: Scene('-4', [Filter(NOTE)  >> Transpose(-4 * 12), ~Filter(NOTE) >> invertPedal] >> out),
        3: Scene('-3', [Filter(NOTE)  >> Transpose(-3 * 12), ~Filter(NOTE) >> invertPedal] >> out),
        4: Scene('-2', [Filter(NOTE)  >> Transpose(-2 * 12), ~Filter(NOTE) >> invertPedal] >> out),
        5: Scene('-1', [Filter(NOTE)  >> Transpose(-1 * 12), ~Filter(NOTE) >> invertPedal] >> out),
        6: Scene('1', [Filter(NOTE)  >> Transpose(1 * 12), ~Filter(NOTE) >> invertPedal] >> out),
        7: Scene('2', [Filter(NOTE)  >> Transpose(2 * 12), ~Filter(NOTE) >> invertPedal] >> out),
        8: Scene('3', [Filter(NOTE)  >> Transpose(3 * 12), ~Filter(NOTE) >> invertPedal] >> out),
        9: Scene('4', [Filter(NOTE)  >> Transpose(4 * 12), ~Filter(NOTE) >> invertPedal] >> out),
    }
)
