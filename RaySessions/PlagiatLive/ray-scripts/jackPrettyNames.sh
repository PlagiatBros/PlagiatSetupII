#!/bin/bash

change_mono_port_name () {
  jack_property -p -s "$1" http://jackaudio.org/metadata/pretty-name "$2"
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
  ((i++))
done

#Zyn HiSynths
i=0
for name in Dupieux NotSoRhodes Organ1 Organ2 CosmaDupieux Bombarde Trumpets1 Trumpets2 Trumpets3 Stambul Dre DiploLike JestoProunk 8bits 8bitsSub
do
  echo $i": ZynAddSubFX.ZHiSynths:part$i/out- >> "$name
  change_stereo_port_name "ZynAddSubFX.ZHiSynths:part$i/out-" "$name/Out-"
  ((i++))
done

# Main MIDI Sequencer
i=1
seq192_c=`jack_lsp |grep seq192| grep "seq192 2"|cut -f1,2 -d ":"`
for name in ZLowSynths CLowSynths ZHiSynths CHiSynths
do
  change_mono_port_name "$seq192_c: seq192 $i" $name
  ((i++))
done

change_mono_port_name "$seq192_c: seq192 10" "Samples"

#Interface In

#Interface out

#Tapeutape
#TODO : envisager un set de pretty names par morceau
