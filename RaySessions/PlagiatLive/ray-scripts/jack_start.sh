#!/bin/bash

## --autoconnect a == ignore self connect

jack_control eps port-max 4096
jack_control eps client-timeout 0
jack_control eps realtime True
jack_control eps self-connect-mode a
jack_control ds alsa
jack_control dps device hw:DSP
jack_control dps rate 48000
jack_control dps nperiods 2
jack_control dps period 128
jack_control start
jack_wait -w

# jackd -p 4096 -t 0 -R --autoconnect a -d alsa -dhw:DSP -r 48000 -p 128 -n 2 > /home/plagiat/PlagiatSetup/log/jackStart.log 2>&1 &
# jack_wait -w
