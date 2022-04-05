from mididings import *

config(
    backend='alsa',
    client_name='cHiRouter',
    out_ports=['Rhodes', 'Trap', 'EasyClassical', 'DubstepHorn', 'TrapFifth'],
    in_ports=['MainIn', 'RhodesIn']
)

run([
    ChannelFilter(1) >> Output('Rhodes', 1),
    ChannelFilter(2) >> Output('Trap', 2),
    ChannelFilter(3) >> Output('EasyClassical', 3),
    ChannelFilter(4) >> Output('DubstepHorn', 4),
    ChannelFilter(5) >> Output('TrapFifth', 5),
])
