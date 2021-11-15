from mentat import Engine

from .raysession import RaySession
from .transport import Transport
from .klick import Klick
from .sooperlooper import SooperLooper
from .loop192 import Loop192
from .seq192 import Seq192
from .nonmixer import NonMixer

engine = Engine('Mentat', 2001, '/home/plagiat/PlagiatSetup/Mentat')

raysession = RaySession('raysession', 'osc', 16189)

transport = Transport('Transport')
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
