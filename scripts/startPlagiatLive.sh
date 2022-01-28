#!/bin/bash
killall -9 jackd ray-daemon raysession pulseaudio pipewire*
ray-daemon -r /home/plagiat/PlagiatSetup/RaySessions/ -s PlagiatLive -p 2000 &
#ray-daemon -r /home/plagiat/PlagiatSetup/RaySessions/ -p 2000 &
#ray_control --port 2000 open_session PlagiatLive
raysession -r /home/plagiat/PlagiatSetup/RaySessions -p 2000 &
