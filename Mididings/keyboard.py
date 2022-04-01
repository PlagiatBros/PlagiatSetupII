from mididings import *
from mididings.event import PitchbendEvent
from mididings.extra.inotify import AutoRestart
from mididings.extra.osc import SendOSC
from mididings.extra.osc import OSCInterface
import mididings.engine as _engine
import mididings.event as _event
from ports import get_port

def create_keyboard(name):

    inPort = get_port(name)
    mentatPort = get_port('Mentat')

    config(
        backend='alsa',
        client_name=name,
        out_ports=['ZLow', 'CLow', 'ZHi', 'CHiSf', 'CHi', 'ProdSampler', 'ConstantSampler'],
        in_ports=['in']
    )

    hook(
        OSCInterface(inPort, mentatPort),
        AutoRestart()
    )

    generic_in = Transpose(-12) >> [
        Filter(NOTE),
        Filter(CTRL) >> [
            CtrlFilter(1) >> SendOSC(mentatPort, '/pedalVolume', lambda ev: ev.value) >> Discard(), # Pédale de volume
            CtrlFilter(64), # Pédale de sustain
            Discard()
            ]
        ]

    # Zyn LowSynths
    lowZDubstep = generic_in >> Output('ZLow', 1)
    lowZDancestep = generic_in >> Output('ZLow', 2)
    lowZRagstep = generic_in >> Output('ZLow', 3)
    lowZDupieux = generic_in >> Output('ZLow', 4)
    lowZPhrampton = generic_in >> Output('ZLow', 5)

    # Carla LowSynths
    lowCTrap1 = generic_in >> Output('CLow', 1)
    lowCTrap2 = generic_in >> Output('CLow', 2)
    lowCBarkline = generic_in >> Output('CLow', 3)
    lowCBoom = generic_in >> Output('CLow', 4)

    # Zyn HiSynths
    zDupieux = generic_in >> Output('ZHi', 1)
    zNotSoRhodes = generic_in >> Output('ZHi', 2)
    zOrgan = generic_in >> [
        Output('ZHi', 3),
        Output('ZHi', 4),
        ]
    zCosma = generic_in >> Output('ZHi', 5)
    zBombarde = generic_in >> Output('ZHi', 6)
    zTrumpets = generic_in >> [
        Output('ZHi', 7),
        Output('ZHi', 8),
        Output('ZHi', 9),
        ]
    zStambul = generic_in >> Output('ZHi', 10)
    zDre = generic_in >> Output('ZHi', 11)
    zDiploLike = generic_in >> Output('ZHi', 12)
    zJestoProunk = generic_in >> Output('ZHi', 13)
    z8bits = generic_in >> [
        Output('ZHi', 14),
        Output('ZHi', 15),
        ]

    # Carla HiSynths
    cRhodes = generic_in >> Output('CHiSf')
    cDubstepHorn = generic_in >> Output('CHi', 1)
    cTrap = generic_in >> Output('CHi', 2)
    cEasyClassical = generic_in >> Output('CHi', 3)

    # Samples
    prodSampler = generic_in >> Output('ProdSampler')
    constantSampler = generic_in >> Output('ConstantSampler')

    run(
        scenes = {
            1: SceneGroup('LowSynths', [
                Scene('LowZDubstep',
                    lowZDubstep
                ),
                Scene('LowZDancestep',
                    lowZDancestep
                ),
                Scene('LowZRagstep',
                    lowZRagstep
                ),
                Scene('LowZDupieux',
                    lowZDupieux
                ),
                Scene('LowZPhrampton',
                    lowZPhrampton
                ),
                Scene('LowCTrap1',
                    lowCTrap1
                ),
                Scene('LowCTrap2',
                    lowCTrap2
                ),
                Scene('LowCBarkline',
                    lowCBarkline
                ),
                Scene('LowCBoom',
                    lowCBoom
                ),

            ]),
            2: SceneGroup('HiSynths', [
                Scene('ZDupieux',
                    zDupieux
                ),
                Scene('ZNotSoRhodes',
                    zNotSoRhodes
                ),
                Scene('ZOrgan',
                    zOrgan
                ),
                Scene('ZCosma',
                    zCosma
                ),
                Scene('ZBombarde',
                    zBombarde
                ),
                Scene('ZTrumpets',
                    zTrumpets
                ),
                Scene('ZStambul',
                    zStambul
                ),
                Scene('ZDre',
                    zDre
                ),
                Scene('ZDiploLike',
                    zDiploLike
                ),
                Scene('ZJestoProunk',
                    zJestoProunk
                ),
                Scene('Z8Bits',
                    z8bits
                ),
                Scene('CRhodes',
                    cRhodes
                ),
                Scene('CDubstepHorn',
                    cDubstepHorn
                ),
                Scene('CTrap',
                    cTrap
                ),
                Scene('CEasyClassical',
                    cEasyClassical
                ),

            ]),
            3: SceneGroup('Samples', [
                Scene('ProdSampler',
                    prodSampler
                ),
                Scene('ConstantSampler',
                    constantSampler
                ),

            ]),
        }

    )
