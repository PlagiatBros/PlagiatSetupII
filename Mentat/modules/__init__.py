from mentat import Engine

from .raysession import RaySession
from .openstagecontrol import OpenStageControl
from .pedalboard import PedalBoard
from .transport import Transport
from .microtonality import MicroTonality
from .calfmonosynth import CalfMonoSynth
from .autotune import Autotune
from .klick import Klick
from .sooperlooper import SooperLooper
from .loop192 import Loop192
from .seq192 import Seq192
from .nonmixer import NonMixer
from .zynaddsubfx import Zynaddsubfx
from .tap192 import Tap192

engine = Engine('Mentat', 2001, '/home/plagiat/PlagiatSetup/Mentat')

raysession = RaySession('RaySession', 'osc', 2000)

openstagecontrol = OpenStageControl('OpenStageControl', 'osc', 3000)
pedalboard = PedalBoard('PedalBoard', 'osc', 3001)

klick = Klick('Klick', 'osc', 9800)

looper = SooperLooper('Looper', 'osc', 9900)
loop192 = Loop192('Loop192', 'osc', 9910)

seq192 = Seq192('Seq192', 'osc', 9920)

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

prodSampler = Tap192('ProdSampler', 'osc', 11040)
constantSampler = Tap192('ConstantSampler', 'osc', 11041)


# TODO ajouter les vraies instances avec les vrais ports
zyndummy = Zynaddsubfx('Zyn', 'osc', 12001, parts=[0])
calfdummy = CalfMonoSynth('Calf', 'osc', 12002, pitcher_port=12012)

# TODO mettre les vrais ports
autotuneNano = Autotune('AutotuneNano', 'osc', 20000 )
autotuneNanoUp = Autotune('AutotuneNanoUp', 'osc', 20001 )
autotuneNanoDown = Autotune('AutotuneNanoDown', 'osc', 20003 )
autotuneKesch = Autotune('AutotuneKesch', 'osc', 20004 )
autotuneKeschUp = Autotune('AutotuneKeschUp', 'osc', 20005 )
autotuneKeschDown = Autotune('AutotuneKeschDown', 'osc', 20006 )


# meta modules
microtonality = MicroTonality('MicroTonality')
transport = Transport('Transport')
