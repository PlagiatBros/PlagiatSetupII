#!/bin/bash

## --autoconnect a == ignore self connect
jackd -p 4096 -t 0 -R --autoconnect a -d alsa -dhw:DSP -r 48000 -p 128 -n 2 > /home/plagiat/PlagiatSetup/log/jackStart.log 2>&1 &
jack_wait -w
