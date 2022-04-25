#!/bin/bash

echo "launching GUI"
raysession -r /home/plagiat/PlagiatSetup/RaySessions -p 2000 > /home/plagiat/PlagiatSetup/log/raysession.log 2>&1 &

#echo "jack pretty naming"
#bash /home/plagiat/PlagiatSetup/scripts/jackPrettyNames.sh
