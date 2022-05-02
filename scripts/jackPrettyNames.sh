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

change_mono_port_name "$seq192_c: seq192 10" "ProdSampler"
change_mono_port_name "$seq192_c: seq192 11" "ConstantSampler"

#Interface In
change_mono_port_name "system:capture_1" "Bass"
change_mono_port_name "system:capture_2" "VocalsKesch"
change_mono_port_name "system:capture_3" "VocalsNano"
change_mono_port_name "system:capture_4" "Kick"
change_mono_port_name "system:capture_5" "OH"
change_mono_port_name "system:capture_6" "Ambiance"
change_mono_port_name "system:capture_7" "VocalsLHommesPorcs"


#Interface out
change_mono_port_name "system:playback_1" "Synths_L"
change_mono_port_name "system:playback_2" "Synths_R"
change_mono_port_name "system:playback_3" "Kick"
change_mono_port_name "system:playback_4" "VocalsLhommesPorcs"

i=5
for name in NanoHeadphones KeschHeadphones
do
  change_mono_port_name "system:playback_$i" "$name-L"
  ((i++))
  change_mono_port_name "system:playback_$i" "$name-R"
  ((i++))
done

change_mono_port_name "system:playback_9" "Samples-L"
change_mono_port_name "system:playback_10" "Samples-R"
change_mono_port_name "system:playback_11" "Bass"
change_mono_port_name "system:playback_12" "BassSynths"
change_mono_port_name "system:playback_13" "VocalsNano"
change_mono_port_name "system:playback_14" "VocalsKesch"


# Sooperlooper
i=0
for name in BassPre BassPost BassSynthsOut SynthsOut VocalsNanoPre VocalsNanoPost VocalsKeschPre VocalsKeschPost
do
  change_mono_port_name "sooperlooper:loop"$i"_in_1" $name"_in"
  change_mono_port_name "sooperlooper:loop"$i"_out_1" $name"_out"
  ((i++))
done

#Tapeutape
#TODO : envisager un set de pretty names par morceau
