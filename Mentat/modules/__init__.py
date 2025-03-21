from sys import argv

from mentat import Engine, Module

from .raysession import RaySession
from .openstagecontrol import OpenStageControl
from .pedalboard import PedalBoard
from .transport import Transport
from .microtonality import MicroTonality
from .postprocess import PostProcess
from .calfmonosynth import CalfMonoSynth, CalfPitcher
from .autotune import Autotune
from .klick import Klick
from .sooperlooper import SooperLooper
from .loop192 import Loop192
from .seq192 import Seq192
from .nonmixer import NonMixer
from .nonmixers import *
from .zynaddsubfx import ZynAddSubFx, ZynPart
from .tap192 import Tap192
from .mk2minilab import Mk2Control, Mk2Keyboard
from .chasttcontrol import ChasttControl, ChasttKeyboard
from .mpkmini import MpkControl
from .jmjkeyboard import JmjKeyboard, JmjKeyboardMidi, JmjTranspose
from .joystick import Joystick
from .notes import Notes
from .midipanic import MidiPanic
from .fluidsynth import FluidSynth

"""
Engine
"""
engine = Engine('Mentat', 2001, '/home/plagiat/PlagiatSetup/Mentat', tcp_port=55001, debug='--debug' in argv)
raysession = RaySession('RaySession', 'osc', 2000)


"""
Controllers
"""
openstagecontrol = OpenStageControl('OpenStageControl', 'osc', 3000)
openstagecontrolKeyboardOut = Module('OpenStageControlKeyboardOut', 'midi')
pedalboard = PedalBoard('PedalBoard', 'osc', 3001)
jmjKeyboardMidi = JmjKeyboardMidi('JmjKeyboardMidi', 'midi')
jmjKeyboard = JmjKeyboard('JmjKeyboard', 'osc', 3002)
jmjTranspose = JmjTranspose('JmjTranspose', 'osc', 3006)

mk2Keyboard = Mk2Keyboard('Mk2Keyboard', 'osc', 3003)
mk2Control = Mk2Control('Mk2Control', 'midi')

chasttKeyboard = ChasttKeyboard('ChasttKeyboard', 'osc', 3005)
chasttControl = ChasttControl('ChasttControl', 'midi')

joystick = Joystick('Joystick', 'osc', 3004)
mpkControl = MpkControl('MpkControl', 'midi')


"""
Loopers
"""
looper = SooperLooper('AudioLooper', 'osc', 9951)
loop192 = Loop192('Loop192', 'osc', 9910)

"""
Sequencers
"""
klick = Klick('Klick', 'osc', 9800)
seq192 = Seq192('Seq192', 'osc', 9920)

"""
Mixers
"""
inputs = Inputs('Inputs', 'osc', 10000)
outputs = Outputs('Outputs', 'osc', 10001)
monitorsNano = NonMixer('MonitorsNano', 'osc', 10002)
monitorsKesch = NonMixer('MonitorsKesch', 'osc', 10003)
# (drums) 10004
monitorsChast = NonMixer('MonitorsChast', 'osc', 10005)
console = Console('Console', 'osc', 10006)

bass = Bass('Bass', 'osc', 10010)
bassFX = bassfx = BassFX('BassFX', 'osc', 10011)

bassSynths = NonMixer('BassSynths', 'osc', 10020)

synths = Synths('Synths', 'osc', 10030)
synthsFX1Reverb = NonMixer('SynthsFX1Reverb', 'osc', 10031)
synthsFX2Delay = NonMixer('SynthsFX2Delay', 'osc', 10032)
synthsFX3Delay = NonMixer('SynthsFX3Delay', 'osc', 10033)
synthsFX4TapeDelay = NonMixer('SynthsFX4TapeDelay', 'osc', 10034)
synthsFX5Scape = NonMixer('SynthsFX5Scape', 'osc', 10035)
synthsFX6Degrade = NonMixer('SynthsFX6Degrade', 'osc', 10036)

samples = Samples('Samples', 'osc', 10040)
samplesFX1Delay = NonMixer('SamplesFX1Delay', 'osc', 10041)
samplesFX2Delay = NonMixer('SamplesFX2Delay', 'osc', 10042)
samplesFX3Reverb = NonMixer('SamplesFX3Reverb', 'osc', 10043)
samplesFX4Autofilter = NonMixer('SamplesFX4Autofilter', 'osc', 10044)
samplesFX5TapeDelay = NonMixer('SamplesFX5TapeDelay', 'osc', 10045)
samplesFX6Scape = NonMixer('SamplesFX6Scape', 'osc', 10046)
samplesFX7Degrade = NonMixer('SamplesFX7Degrade', 'osc', 10047)

vocalsNano = Vocals('VocalsNano', 'osc', 10050)
vocalsNanoFX1Delay = VocalsFX('VocalsNanoFX1Delay', 'osc', 10051)
vocalsNanoFX2Delay = VocalsFX('VocalsNanoFX2Delay', 'osc', 10052)
vocalsNanoFX3TrapVerb = VocalsFX('VocalsNanoFX3TrapVerb', 'osc', 10053)
vocalsNanoFX4Disint = VocalsFX('VocalsNanoFX4Disint', 'osc', 10054)
vocalsNanoFX5RingMod = VocalsFX('VocalsNanoFX5RingMod', 'osc', 10055)
vocalsNanoFX6Granular = VocalsFX('VocalsNanoFX6Granular', 'osc', 10056)
vocalsNanoFX7Slice = VocalsFX('VocalsNanoFX7Slice', 'osc', 10057)
vocalsNanoFX8TapeDelay = VocalsFX('VocalsNanoFX8TapeDelay', 'osc', 10058)
vocalsNanoFX9Scape = VocalsFX('VocalsNanoFX9Scape', 'osc', 10059)

vocalsKesch = Vocals('VocalsKesch', 'osc', 10060)
vocalsKeschFX1Delay = VocalsFX('VocalsKeschFX1Delay', 'osc', 10061)
vocalsKeschFX2Delay = VocalsFX('VocalsKeschFX2Delay', 'osc', 10062)
vocalsKeschFX3TrapVerb = VocalsFX('VocalsKeschFX3TrapVerb', 'osc', 10063)
vocalsKeschFX4Disint = VocalsFX('VocalsKeschFX4Disint', 'osc', 10064)
vocalsKeschFX5RingMod = VocalsFX('VocalsKeschFX5RingMod', 'osc', 10065)
vocalsKeschFX6Granular = VocalsFX('VocalsKeschFX6Granular', 'osc', 10066)
vocalsKeschFX7Slice = VocalsFX('VocalsKeschFX7Slice', 'osc', 10067)
vocalsKeschFX8TapeDelay = VocalsFX('VocalsKeschFX8TapeDelay', 'osc', 10068)
vocalsKeschFX9Scape = VocalsFX('VocalsKeschFX9Scape', 'osc', 10069)

vocalsChast = Vocals('VocalsChast', 'osc', 10070)
vocalsChastFX1Delay = VocalsFX('VocalsChastFX1Delay', 'osc', 10071)
vocalsChastFX2Delay = VocalsFX('VocalsChastFX2Delay', 'osc', 10072)
vocalsChastFX3TrapVerb = VocalsFX('VocalsChastFX3TrapVerb', 'osc', 10073)
vocalsChastFX4Disint = VocalsFX('VocalsChastFX4Disint', 'osc', 10074)
vocalsChastFX5RingMod = VocalsFX('VocalsChastFX5RingMod', 'osc', 10075)
vocalsChastFX6Granular = VocalsFX('VocalsChastFX6Granular', 'osc', 10076)
vocalsChastFX7Slice = VocalsFX('VocalsChastFX7Slice', 'osc', 10077)
vocalsChastFX8TapeDelay = VocalsFX('VocalsChastFX8TapeDelay', 'osc', 10078)
vocalsChastFX9Scape = VocalsFX('VocalsChastFX9Scape', 'osc', 10079)

"""
Samplers
"""
prodSampler = Tap192('ProdSampler', 'osc', 11040)
constantSampler = Tap192('ConstantSampler', 'osc', 11041)

"""
Synths
"""
carlabass = Module('LowCSynths', 'osc', 9720)
carlabass.add_submodule(
    CalfMonoSynth('LowCTrap1', parent=carlabass),
    CalfMonoSynth('LowCTrap2', parent=carlabass),
    CalfMonoSynth('LowCBarkline', parent=carlabass),
    CalfMonoSynth('LowCBoom', parent=carlabass),
)

carlatreble = Module('HiCSynths', 'osc', 9730)
carlatreble.add_submodule(
    CalfMonoSynth('CDubstepHorn', parent=carlatreble),
    CalfMonoSynth('CTrap', parent=carlatreble),
    CalfMonoSynth('CEasyClassical', parent=carlatreble),
)
calfpitcher = CalfPitcher('CalfPitcher', 'osc', 9740)


zynbass =  ZynAddSubFx('ZLowSynths', 'osc', 9820)
zynbass.add_submodule(
    ZynPart('LowZDubstep', parent=zynbass, parts=[0]),
    ZynPart('LowZDancestep', parent=zynbass, parts=[1]),
    ZynPart('LowZRagstep', parent=zynbass, parts=[2]),
    ZynPart('LowZDupieux', parent=zynbass, parts=[3]),
    ZynPart('LowZPhrampton', parent=zynbass, parts=[4])
)

zyntreble =  ZynAddSubFx('ZHiSynths', 'osc', 9830)
zyntreble.add_submodule(
    ZynPart('ZDupieux', parent=zyntreble, parts=[0]),
    ZynPart('ZNotSoRhodes', parent=zyntreble, parts=[1]),
    ZynPart('ZOrgan', parent=zyntreble, parts=[2, 3]),
    ZynPart('ZCosma', parent=zyntreble, parts=[4]),
    ZynPart('ZBombarde', parent=zyntreble, parts=[5]),
    ZynPart('ZTrumpets', parent=zyntreble, parts=[6, 7, 8]),
    ZynPart('ZStambul', parent=zyntreble, parts=[9]),
    ZynPart('ZDre', parent=zyntreble, parts=[10]),
    ZynPart('ZDiploLike', parent=zyntreble, parts=[11]),
    ZynPart('ZJestoProunk', parent=zyntreble, parts=[12]),
    ZynPart('Z8bits', parent=zyntreble, parts=[13, 14])
)

"""
Fluid synths
"""
rhodes = FluidSynth('Rhodes', 'midi')
tenorsax = FluidSynth('TenorSax', 'midi')
charang = FluidSynth('Charang', 'midi')
steeldrums = FluidSynth('SteelDrums', 'midi')
orchestrahit = FluidSynth('OrchestraHit', 'midi')
majorvocals = FluidSynth('MajorVocals', 'midi')
piano = FluidSynth('Piano', 'midi')


"""
Autotunes
"""
autotuneNanoMeuf = Autotune('NanoMeuf', 'osc', 12050, offset=4.0)
autotuneNanoNormo = Autotune('NanoNormo', 'osc', 12051, offset=0.0)
autotuneNanoGars = Autotune('NanoGars', 'osc', 12052, offset=-4.0)

autotuneKeschMeuf = Autotune('KeschMeuf', 'osc', 12060, offset=4.0)
autotuneKeschNormo = Autotune('KeschNormo', 'osc', 12061, offset=0.0)
autotuneKeschGars = Autotune('KeschGars', 'osc', 12062, offset=-4.0)

autotuneChastMeuf = Autotune('ChastMeuf', 'osc', 12070, offset=4.0)
autotuneChastNormo = Autotune('ChastNormo', 'osc', 12071, offset=0.0)
autotuneChastGars = Autotune('ChastGars', 'osc', 12072, offset=-4.0)


"""
Miscellaneous
"""
microtonality = MicroTonality('MicroTonality')
transport = Transport('Transport')
postprocess = PostProcess('PostProcess')
notes = Notes('Notes')
midipanic = MidiPanic('MidiPanic', 'midi')
