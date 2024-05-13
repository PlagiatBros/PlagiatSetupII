#!/bin/bash
export SOUND_CARD_PCI_ID=05:00.0
sudo setpci -v -d *:* latency_timer=b0
sudo setpci -v -s $SOUND_CARD_PCI_ID latency_timer=ff
