from mididings import *

config(
    backend='jack',
    client_name='cLowRouter',
    out_ports=['Trap1', 'Trap2', 'Trap3', 'Barkline', 'Boom'],
    in_ports=['In']
)

run([
    ChannelFilter(1) >> Output('Trap1', 1),
    ChannelFilter(2) >> Transpose(-12) >> Output('Trap2', 2),
    ChannelFilter(3) >> Output('Barkline', 3),
    ChannelFilter(4) >> Output('Boom', 4),
    ChannelFilter(5) >> Output('Trap3', 5),
])
