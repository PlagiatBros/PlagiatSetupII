#!/bin/bash
killall -9 jackd ray-daemon raysession pulseaudio pipewire*
ray-daemon -r /home/plagiat/PlagiatSetup/RaySessions/ -s PlagiatLive -p 2000 &
raysession -r /home/plagiat/PlagiatSetup/RaySessions -p 2000 &
