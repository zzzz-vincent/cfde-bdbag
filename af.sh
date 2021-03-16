#!/bin/bash

module load anaconda
python3 af.py

if [ ! -d bdbags ]; then
	mkdir bdbags
fi

for D in af-new*
do
	if [ -d $D ]; then
		rm -rfv $D
	fi
done

for D in af-published*
do
	if [ -d $D ]; then
		cp C2M2_datapackage.json $D/ 
	fi
done

mv -v af-published* bdbags/
