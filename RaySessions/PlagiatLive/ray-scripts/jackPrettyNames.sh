#!/bin/bash

change_mono_port_name () {
  jack_property -p -s "$1$out" http://jackaudio.org/metadata/pretty-name "$2$out"
}

change_stereo_port_name () {
  for out in L R
  do
    jack_property -p -s "$1$out" http://jackaudio.org/metadata/pretty-name "$2$out"
  done
}

#Zyn BassSynths
i=0
for name in Dubstep Dancestep Ragstep Dupieux Phrampton
do
  change_stereo_port_name "ZynAddSubFX.ZLowSynths:part$i/out-" "$name/Out-"
  let i++
done
