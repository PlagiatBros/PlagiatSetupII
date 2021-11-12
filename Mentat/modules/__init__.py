from mentat.module import Module
from mentat.engine import Engine
# from .klick import Klick

from .sooperlooper import SooperLooper
from .nonmixer import NonMixer
from .raysession import RaySession

engine = Engine('Mentat', 2001, '/home/plagiat/PlagiatSetup/Mentat')


raysession = RaySession('raysession', 'osc', 2000)

Inputs = NonMixer('Inputs', 'osc', 10000)
Outputs = NonMixer('Outputs', 'osc', 10001)
MonitorsNano = NonMixer('MonitorsNano', 'osc', 10002)
MonitorsKesch = NonMixer('MonitorsKesch', 'osc', 10003)

Bass = NonMixer('Bass', 'osc', 10010)
BassSynths = NonMixer('BassSynths', 'osc', 10020)
Synths = NonMixer('Synths', 'osc', 10030)
Samples = NonMixer('Samples', 'osc', 10040)
SamplesFX1Delay = NonMixer('SamplesFX1Delay', 'osc', 10041)
SamplesFX2Delay = NonMixer('SamplesFX2Delay', 'osc', 10042)
SamplesFX3Reverb = NonMixer('SamplesFX3Reverb', 'osc', 10043)
SamplesFX4Autofilter = NonMixer('SamplesFX4Autofilter', 'osc', 10044)
VocalsNano = NonMixer('VocalsNano', 'osc', 10050)
VocalsKesch = NonMixer('VocalsKesch', 'osc', 10060)

Looper = SooperLooper('Looper', 'osc', 9900)

# klick1 = Klick('klick-1', 'osc', 12000)
# klick2 = Klick('klick-2', 'osc', 13000)
#
# pedalboard = Pedalboard('pedalboard', 'osc', None)
#
# pedalboard2 = Pedalboard('pedalboard-2', 'osc', None)
# pedalboard3 = Pedalboard('pedalboard-3', 'osc', None)

# kbd = Module('kbd', 'midi')
# mon = Module('mon', 'midi')
