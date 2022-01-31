import liblo
import sys
import time

port = 22097
server = liblo.Server(port)
to_receive = 0
start = 0
timeout = 5

def send(n):
    global to_receive, start
    print('Sending %i messages...' % n)
    to_receive = n
    start = time.time()
    for i in range(n):
        server.send('osc.udp://127.0.0.1:%i' % port, '/oezihjdguzagdzakxsqucgeifgezufgezfsqygazz', 1, 2.0, "teergiiuhihihef")

def receive(path, args):
    global to_receive
    to_receive -= 1
    if to_receive == 0:
        delta = time.time() - start
        print('All messages received in %f seconds' % delta)

server.add_method(None, None, receive)

for x in range(100):

    send(int(sys.argv[1]))

    while True:
        while server.recv(0):
            pass
        time.sleep(0.001)
        # server.recv(100)
        if time.time() - start > timeout:
            print('Timeout exceeded, %i messages lost' % to_receive)
            break
        elif to_receive == 0:
            break



server.free()
