from mididings import *

config(
    backend='jack',
    client_name='cHiRouter',
    out_ports=['Rhodes', 'Trap', 'EasyClassical', 'DubstepHorn', 'TrapFifth'],
    in_ports=['MainIn', 'RhodesIn']
)

run([
    PortFilter('RhodesIn') >> ChannelFilter(1) >> Output('Rhodes', 1),
    PortFilter('MainIn') >> [
        ChannelFilter(2) >> Output('Trap', 2),
        ChannelFilter(3) >> Output('EasyClassical', 3),
        ChannelFilter(4) >> Output('DubstepHorn', 4),
        ChannelFilter(5) >> Output('TrapFifth', 5),
    ]
])
