#!/bin/bash

module load anaconda
python3 scrnaseq.py

if [ ! -d bdbags ]; then
	mkdir bdbags
fi

for D in scrnaseq-new*
do
	if [ -d $D ]; then
		rm -rfv $D
	fi
done

for D in scrnaseq-published*
do
	if [ -d $D ]; then
		cp C2M2_datapackage.json $D/ 
	fi
done

for D in scrnaseq-published*
do
	if [ -f bdbags/$D ]; then
  		rm -rfv bdbags/$D
	fi
 
	mv -v $D bdbags
done
