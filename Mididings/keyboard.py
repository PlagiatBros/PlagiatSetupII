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
        out_ports=['ZLow', 'CLow', 'ZHi', 'CHiSf', 'CHi', 'ProdSampler', 'ConstantSampler', 'Fluid_TenorSax', 'Fluid_Charang', 'Fluid_OrchestraHit', 'Fluid_SteelDrum', 'Fluid_Rhodes', 'Fluid_MajorVocals', 'Mentat'],
        in_ports=['in']
    )

    hook(
        OSCInterface(inPort, mentatPort),
        AutoRestart()
    )

    generic_in = Transpose(-12) >> ~ChannelFilter(16) >> [
        Filter(NOTE),
        Filter(CTRL) >> [
            CtrlFilter(1), # Modulation
            CtrlFilter(64), # Pédale de sustain
            Discard()
            ],
        Filter(PITCHBEND)
        ]

    # Zyn LowSynths
    lowZDubstep = generic_in >> Output('ZLow', 1)
    lowZDancestep = generic_in >> Output('ZLow', 2)
    lowZRagstep = generic_in >> Output('ZLow', 3)
    lowZDupieux = generic_in >> Output('ZLow', 4)
    lowZPhrampton = generic_in >> Output('ZLow', 5)
    lowZSine = generic_in >> Output('ZLow', 6)
    lowZ8bit = generic_in >> Output('ZLow', 8)

    # Carla LowSynths
    lowCTrap1 = generic_in >> Output('CLow', 1)
    lowCTrap2 = generic_in >> Output('CLow', 2)
    lowCBarkline = generic_in >> Output('CLow', 3)
    lowCBoom = generic_in >> Output('CLow', 4)
    lowCBoomTrapLine = generic_in >> [
        Output('CLow', 2),
        Output('CLow', 3),
        Output('CLow', 4),
        ]
    lowCTrap3 = generic_in >> Output('CLow', 5)

    # Zyn HiSynths
    zDupieux = generic_in >> Output('ZHi', 1)
    zNotSoRhodes = generic_in >> Output('ZHi', 2)
    zOrgan = generic_in >> Output('ZHi', 3)
    zCosma = generic_in >> Output('ZHi', 5)
    zBombarde = generic_in >> Output('ZHi', 6)
    zTrumpets = generic_in >> Output('ZHi', 7)

    zStambul = generic_in >> Output('ZHi', 8)
    zDre = generic_in >> Output('ZHi', 9)
    zDiploLike = generic_in >> Output('ZHi', 11)
    zJestoProunk = generic_in >> Output('ZHi', 12)
    z8bits = generic_in >> Output('ZHi', 13)

    zDiploLikeWide = generic_in >> Output('ZHi', 14)

    # Carla HiSynths
    cDubstepHorn = generic_in >> Output('CHi', 4)
    cTrap = generic_in >> Output('CHi', 2)
    cEasyClassical = generic_in >> Output('CHi', 3)
    cTrapFifth = generic_in >> Output('CHi', 5)

    # Samples
    prodSampler = generic_in >> Output('ProdSampler')
    constantSampler = generic_in >> Output('ConstantSampler')

    # SoundFonts
    rhodes = generic_in >> Output('Fluid_Rhodes')
    tenorSax = generic_in >> Output('Fluid_TenorSax')
    charang = generic_in >> Output('Fluid_Charang')
    orchestraHit = generic_in >> Output('Fluid_OrchestraHit')
    steelDrum = generic_in >> Output('Fluid_SteelDrum')
    majorVocals = generic_in >> Output('Fluid_MajorVocals')

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
                Scene('LowZSine',
                    lowZSine
                ),
                Scene('LowZ8bits',
                    lowZ8bit
                ),
                Scene('LowCTrap1',
                    lowCTrap1
                ),
                Scene('LowCTrap2',
                    lowCTrap2
                ),
                Scene('LowCTrap3',
                    lowCTrap3
                ),
                Scene('LowCBarkline',
                    lowCBarkline
                ),
                Scene('LowCBoom',
                    lowCBoom
                ),
                Scene('LowCBoomTrapline',
                    lowCBoomTrapLine
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
                Scene('ZDiploLikeWide',
                    zDiploLikeWide
                ),
                Scene('ZJestoProunk',
                    zJestoProunk
                ),
                Scene('Z8bits',
                    z8bits
                ),
                Scene('DubstepHorn',
                    cDubstepHorn
                ),
                Scene('Trap',
                    cTrap
                ),
                Scene('EasyClassical',
                    cEasyClassical
                ),
                Scene('TrapFifth',
                    cTrapFifth
                ),
                Scene('Rhodes',
                    rhodes
                ),
                Scene('TenorSax',
                    tenorSax
                ),
                Scene('Charang',
                    charang
                ),
                Scene('OrchestraHit',
                    orchestraHit
                ),
                Scene('SteelDrum',
                    steelDrum
                ),
                Scene('MajorVocals',
                    majorVocals
                ),
            ]),
            3: SceneGroup('Misc', [
                Scene('ProdSampler',
                    prodSampler
                ),
                Scene('ConstantSampler',
                    constantSampler
                ),
                Scene('Mute',
                    Discard()
                ),
            ])
        },
        control =  CtrlFilter(7) >> Output('Mentat', 1), # Pédale de volume (-> filtre par mentat)
    )
