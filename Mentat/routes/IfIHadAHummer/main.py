
from ..base import RouteBase, mk2_button, pedalboard_button
from .video import Video
from .light import Light

from modules import *

class IfIHadAHummer(Video, Light, RouteBase):

    def activate(self):
        """
        Called when the engine switches to this route.
        """

        super().activate()

        transport.set_tempo(120)
        transport.set_cycle('4/4')

        # Setups, banks...
        seq192.set_screenset(self.name)
        prodSampler.set_kit(self.name)

        # Microtonality
        microtonality.enable()
        microtonality.set_tuning(0, 0, 0, 0.35, 0, 0, 0, 0, 0.35, 0, 0, 0.35)

        # Autotuner Notes
        #               c     d     e  f     g     a     b
        notes.set_notes(1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1)


    @pedalboard_button(1)
    @mk2_button(1, 'blue')
    def stop(self):
        """
        STOP
        """
        self.pause_loopers()
        transport.stop()

    @pedalboard_button(2)
    def refrain(self):
        """
        REFRAIN
        """
        
        self.pause_loopers()
        self.reset()

        # Séquences
        seq192.select('solo', 'refrain_*')

        # Transport
        transport.set_cycle('4/4')
        transport.start()

        # Vocals
        vocalsNano.set('meuf_exclu', 'on')
        vocalsKesch.set('meuf_exclu', 'on')

        #### TODO : autom pitchdown au bout de 4 tours ?
    
    @pedalboard_button(3)
    def couplet1(self):
        """
        COUPLET 1
        """

        self.pause_loopers()
        self.reset()

        # Séquences
        seq192.select('solo', 'couplet1_*')

        # Transport
        transport.set_cycle('7/8', 'XxXxXxx')
        transport.start()

        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')

        self.start_sequence('couplet1',[
            {}, {}, {}, {}, # bars 1 - 4
            {}, {}, {}, # bars 5 - 7
            { # bar 8
                3.2: lambda: [ # "My rhymes are on my double sworded tongua"
                    vocalsNano.set('normo_exclu', 'on'),
                    vocalsKesch.set('normo', 'on')
                ]
            },
            {}, # bar 9
            { # bar 10 
                2.55: lambda: vocalsKesch.set('normo', 'off'),
                3: lambda: vocalsNano.set('gars_exclu', 'on')
            },
            {}, {} # bars 11 - 12
            { # bar 13
                1: lambda: [ # "Mayday Mayday"
                    vocalsNano.set('meuf_exclu', 'on'),
                    vocalsNano.set('normo', 'on')
                ]
            },
            { # bar 14
                1: lambda: vocalsNano.set('normo', 'off')
            }
        ], loop=False)
        
