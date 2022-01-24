#!/bin/bash

## --autoconnect a == ignore self connect
jackd -R --autoconnect a -d alsa -dhw:DSP -r 48000 -p 128 -n 2&
jack_wait -w
