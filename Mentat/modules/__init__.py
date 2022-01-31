from mentat import Engine, Module

from .raysession import RaySession
from .openstagecontrol import OpenStageControl
from .pedalboard import PedalBoard
from .transport import Transport
from .microtonality import MicroTonality
from .calfmonosynth import CalfMonoSynth, CalfPitcher
from .autotune import Autotune
from .klick import Klick
from .sooperlooper import SooperLooper
from .loop192 import Loop192
from .seq192 import Seq192
from .nonmixer import NonMixer
from .zynaddsubfx import ZynAddSubFx, ZynPart
from .tap192 import Tap192
from .mk2minilab import Mk2Control, Mk2Keyboard
from .jmjkeyboard import JmjKeyboard
from .joystick import Joystick

"""
Engine
"""
engine = Engine('Mentat', 2001, '/home/plagiat/PlagiatSetup/Mentat')
raysession = RaySession('RaySession', 'osc', 2000)


"""
Controllers
"""
openstagecontrol = OpenStageControl('OpenStageControl', 'osc', 3000)
pedalboard = PedalBoard('PedalBoard', 'osc', 3001)
jmjKeyboard = JmjKeyboard('JmjKeyboard', 'osc', 3002)
mk2Keyboard = Mk2Keyboard('Mk2Keyboard', 'osc', 3003)
mk2Control = Mk2Control('Mk2Control', 'midi')
joystick = Joystick('Joystick', 'osc', 3004)


"""
Loopers
"""
looper = SooperLooper('Looper', 'osc', 9900)
loop192 = Loop192('Loop192', 'osc', 9910)

"""
Sequencers
"""
klick = Klick('Klick', 'osc', 9800)
seq192 = Seq192('Seq192', 'osc', 9920)

"""
Mixers
"""
inputs = NonMixer('Inputs', 'osc', 10000)
outputs = NonMixer('Outputs', 'osc', 10001)
monitorsNano = NonMixer('MonitorsNano', 'osc', 10002)
monitorsKesch = NonMixer('MonitorsKesch', 'osc', 10003)

bass = NonMixer('Bass', 'osc', 10010)
bassSynths = NonMixer('BassSynths', 'osc', 10020)
synths = NonMixer('Synths', 'osc', 10030)
samples = NonMixer('Samples', 'osc', 10040)
samplesFX1Delay = NonMixer('SamplesFX1Delay', 'osc', 10041)
samplesFX2Delay = NonMixer('SamplesFX2Delay', 'osc', 10042)
samplesFX3Reverb = NonMixer('SamplesFX3Reverb', 'osc', 10043)
samplesFX4Autofilter = NonMixer('SamplesFX4Autofilter', 'osc', 10044)
vocalsNano = NonMixer('VocalsNano', 'osc', 10050)
vocalsKesch = NonMixer('VocalsKesch', 'osc', 10060)

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
    CalfMonoSynth('CRhodes', parent=carlatreble),
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
Autotunes
"""
# TODO mettre les vrais ports
autotuneNano = Autotune('AutotuneNano', 'osc', 20000 )
autotuneNanoUp = Autotune('AutotuneNanoUp', 'osc', 20001 )
autotuneNanoDown = Autotune('AutotuneNanoDown', 'osc', 20003 )
autotuneKesch = Autotune('AutotuneKesch', 'osc', 20004 )
autotuneKeschUp = Autotune('AutotuneKeschUp', 'osc', 20005 )
autotuneKeschDown = Autotune('AutotuneKeschDown', 'osc', 20006 )


"""
Miscellaneous
"""
microtonality = MicroTonality('MicroTonality')
transport = Transport('Transport')
