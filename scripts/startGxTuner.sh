#!/bin/bash
killall broadwayd
killall gxtuner
broadwayd -p 30000 :0&
GDK_BACKEND=broadway gxtuner -x 0 -y -40  -w 850 -l 420
