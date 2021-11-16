#!/bin/bash
# Renomme les ports dans le fichier de patch de ray-session
# $1 = chemin du dossier
# $2 = ancien port
# $3 = nouveau port

sed -i -e "s/$1 ($2)/$1 ($3)/g"  PlagiatLive.patch.xml
