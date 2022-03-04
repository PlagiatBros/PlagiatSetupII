#!/bin/bash

# Restart failed clients
for client in $(ray_control list_clients not_started); do
    echo "Restarting $client"
    ray_control client $client start;
done

# Notify failed restarts
for client in $(ray_control list_clients not_started); do
    dunstify -u critical -a RaySession -t 0 "$client\
failed to start"
done
