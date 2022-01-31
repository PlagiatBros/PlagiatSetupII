from modules import *

class Audio():

    def part(self, part, *args, **kwargs):


        if part == 'couplet':

            transport.set_tempo(90)
            seq192.select('solo', part)
            transport.start()


        if part == 'refrain':

            transport.set_tempo(90)
            transport.start()
