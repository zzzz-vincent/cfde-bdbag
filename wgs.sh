#!/bin/bash

module load anaconda
python3 wgs.py

if [ ! -d bdbags ]; then
	mkdir bdbags
fi

for D in wgs-new*
do
	if [ -d $D ]; then
		rm -rfv $D
	fi
done

for D in wgs-published*
do
	if [ -d $D ]; then
		cp C2M2_datapackage.json $D/ 
	fi
done

mv -v wgs-published* bdbags
