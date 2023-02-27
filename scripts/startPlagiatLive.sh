#!/bin/bash
killall -9 jackd ray-daemon raysession pulseaudio pipewire*
#jack_control stop

if [ "$1" = "debug" ]
then
    echo "Debug"
    ray-daemon --debug -r /home/plagiat/PlagiatSetup/RaySessions/ -s PlagiatLive -p 2000 > /home/plagiat/PlagiatSetup/log/startPlagiatLive-raydaemon.log 2>&1 &
else
    ray-daemon -r /home/plagiat/PlagiatSetup/RaySessions/ -s PlagiatLive -p 2000 > /home/plagiat/PlagiatSetup/log/startPlagiatLive-raydaemon.log 2>&1 &
fi
#ray-daemon -r /home/plagiat/PlagiatSetup/RaySessions/ -p 2000 &
#ray_control --port 2000 open_session PlagiatLive
#raysession -r /home/plagiat/PlagiatSetup/RaySessions -p 2000 &
