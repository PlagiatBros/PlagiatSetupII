
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
                3.8: lambda: [ # "My rhymes are on my double sworded tongua"
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
        

    @pedalboard_button(4)
    def prerefrain(self):
        """
        PRÉ-REFRAIN
        """

        self.pause_loopers()
        self.reset()

        # Séquences
        seq192.select('solo', 'prerefrain_*')

        # Transport
        transport.set_cycle('4/4', 'Xxxx')
        transport.start()

        # Vocals
        vocalsNano.set('meuf_exclu', 'on')
        vocalsKesch.set('gars_exclu', 'on')

    @pedalboard_button(2)
    def refrain2(self):
        """
        REFRAIN 2 (cf. REFRAIN)
        """
        pass

    @pedalboardd_button(6)
    def couplet2(self):
        """
        COUPLET 2
        """

        self.pause_loopers()
        self.reset()

        # Séquences
        seq192.select('solo', 'couplet2_*')

        # Transport
        transport.set_cycle('7/8', 'XxXxXxx')
        transport.start()

        # Vocals
        vocalsNano.set('gars_exclu', 'on')
        vocalsKesch.set('meuf_exclu', 'on')

        self.start_sequence('couplet2',[
            *[{} for i in range(8)], # bars 1 - 8
            { # bar 9
                1: lambda: vocalsNano.set('meuf_exclu', 'on')
            },
            {}, {}, {} # bars 10 - 12
            {}, # bar 13
            { # bar 14
                3.5: lambda: vocalsKesch.set('gars_exclu', 'on')
            }
        ], loop=False)
        
    @pedalboard_button(2)
    def refrain3(self):
        """
        REFRAIN 3 (cf. REFRAIN)
        """
        #### TODO : pitchdown auto sur fin de refrain ?
        pass

    @pedalboard_button(7)
    def transe(self):
        """
        TRANSE
        """
        self.pause_loopers()
        self.reset()

        # Séquences
        seq192.select('solo', 'transe_*')

        # Transport
        transport.set_cycle('4/4', 'Xxxx')
        transport.start()

        # Basses
        bassfx.set('distohi', 'on')
        bassfx.set('scape', 'on')
