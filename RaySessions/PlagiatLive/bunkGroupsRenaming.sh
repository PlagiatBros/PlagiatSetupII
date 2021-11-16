#!/bin/bash
# Modifie dans les dossiers Non-Mixer le nom d'un groupe, ainsi que dans le jackpatch
# $1 : le client concerné (chemin du dossier)
# $2 : l'ancien groupe concerné
# $3 : le nouveau groupe


./groupsRenaming.sh $1 $2 $3
./jackPatchBunkPortsRenaming.sh $2 $3
