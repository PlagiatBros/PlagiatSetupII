# coding=utf8
from mididings import *
from mididings.event import PitchbendEvent
from mididings.extra.inotify import AutoRestart
from liblo import ServerThread
from mididings.extra.osc import SendOSC
import mididings.engine as _engine
import mididings.event as _event
from ports import get_port

config(
    backend='alsa',
    client_name='MonoSynthMicroTonal',
    out_ports=['TrapOut', 'EasyClassicalOut', 'DubstepHornOut', 'TrapFifthOut'],
    in_ports=['TrapIn', 'EasyClassicalIn', 'DubstepHornIn', 'TrapFifthIn']
)

monosynth_pitch =  [0 for i in range(12)]
manual_pitch = [0, 0, 0]
pb_factor = [1/12., 1/12., 1]
note = 0

def panic(path, args):
    for port in range(3):
        for note in range(128):
            _engine.output_event(_event.NoteOffEvent(port + 1, 1, note))

def pitch_panic(path, args):
    for port in range(3):
        manual_pitch[port] = 0
        _engine.output_event(_event.PitchbendEvent(port + 1, 1, int(monosynth_pitch[note] * pb_factor[port] + manual_pitch[port])))

def set_microtonal(path, args):
    global monosynth_pitch
    monosynth_pitch = [8192. * t / 2 for t in args]
    print('monosynth pitch: %s' % monosynth_pitch)


server = ServerThread(get_port('CalfPitcher'))
server.add_method('/monosynth/pitch', None, set_microtonal)
server.add_method('/panic', None, panic)
server.add_method('/pitch_panic', None, pitch_panic)
server.start()

def applyMicrotonal(ev):
    global note

    note = ev.note % 12
    port = ev.port - 1

    _engine.output_event(PitchbendEvent(ev.port, ev.channel, int(monosynth_pitch[note] * pb_factor[port] + manual_pitch[port])))
    _engine.output_event(ev)

def storePitchwheel(ev):
    port = ev.port - 1
    manual_pitch[port] = ev.value * pb_factor[port]
    if ev.channel != 1:
        ev.value =  int( ev.value * pb_factor[port])
    ev.value +=  int(monosynth_pitch[note] * pb_factor[port])
    _engine.output_event(ev)

run([
    Filter(NOTEON) >> Call(applyMicrotonal),
    Filter(NOTEOFF),
    Filter(PITCHBEND) >> [
        Call(storePitchwheel),
    ],
])
