#!/bin/bash
# $1 client (chemin du dossier)
# $2 ancien groupe
# $3 nouveau groupe

sed -i -e "s/Group \(.*\) create :name \"$2\"/Group \1 create :name \"$3\"/g" $1/snapshot
