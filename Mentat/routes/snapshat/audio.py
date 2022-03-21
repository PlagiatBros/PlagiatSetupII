from modules import *

class Audio():

    def part(self, part, *args, **kwargs):

        if part == 'pont':
            # Sequences
            seq192.select('solo', part + '*')

            # Transport, BPM, Delays...
            _bpm = 90
            #   ## Transport
            transport.set_tempo(_bpm)
            transport.start()
            #   ## Klick
            klick.start()
            #   ## Delays
                # Bass scape
                # Bass Tape Delay
                # Synths Tape Delay
                # Samples Munge Delay
                # Samples Multiband Delay
                # Samples Tape Delay
                # Samples Scape Delay
                # Vocals Munge
                # Vocals Multiband Delay
                # Vocals Tape Delay
                # Vocals Scape Delay



            # Mix, FX, Synths Programs, Vocals...
            #   ## Mix
            #   ## FX
            #   ## Samples
            #   ## Synths
            #   ## Vocals

            # Controllers
            #   ## Keyboards

            # Misc
            #   ## Previous sequence shutdown
                # NoteOff 57 & 59


        if part == 'couplet':

            transport.set_tempo(90)
            seq192.select('solo', part + '*')
            transport.start()

        if part == 'refrain':

            transport.set_tempo(90)
            seq192.select('solo', part + '*')
            transport.start()

        if part == 'contrechant':

            seq192.select('on', part + '*')

        if part == 'trap':
            pass
