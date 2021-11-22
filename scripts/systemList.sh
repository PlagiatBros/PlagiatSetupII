#!/bin/bash
DIR="/home/plagiat/PlagiatSetup"
dpkg --get-selections > $DIR/Debian/packages.list
uname -a > $DIR/Debian/kernel.version
cat /proc/mdstat > $DIR/Debian/mdstat
