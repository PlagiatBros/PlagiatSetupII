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
    out_ports=['Out'],
    in_ports=['In']
)

monosynth_pitch =  [0 for i in range(12)]

manual_pitch = {
    2: 0,
    3: 0,
    4: 0,
    5: 0
}

pb_factor = {
    2: 2,
    3: 2,
    4: 24,
    5: 2
}

note = 0

def panic(path, args):
    for channel in pb_factor:
        for note in range(128):
            _engine.output_event(_event.NoteOffEvent(1, channel, note))

def pitch_panic(path, args):
    for channel in pb_factor:
        manual_pitch[channel] = 0
        _engine.output_event(_event.PitchbendEvent(1, channel, int(monosynth_pitch[note] / pb_factor[channel] + manual_pitch[channel])))

def set_microtonal(path, args):
    global monosynth_pitch
    monosynth_pitch = [8192. * t for t in args]
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
    channel = ev.channel

    pitch = int(monosynth_pitch[note] / pb_factor[channel] + manual_pitch[channel])
    pitch = max(-8192,min(pitch,8191))

    _engine.output_event(PitchbendEvent(ev.port, ev.channel, pitch))
    _engine.output_event(ev)

def storePitchwheel(ev):
    port = ev.port - 1
    channel = ev.channel
    manual_pitch[channel] = ev.value

    pitch = ev.value + int(monosynth_pitch[note] / pb_factor[channel])
    pitch = max(-8192,min(pitch,8191))
    ev.value = pitch

    _engine.output_event(ev)

run([
    Filter(CTRL) >> CtrlFilter(1,64, 123, 122, 124),
    Filter(NOTEON) >> Call(applyMicrotonal),
    Filter(NOTEOFF),
    Filter(PITCHBEND) >> [
        Call(storePitchwheel),
    ],
])
