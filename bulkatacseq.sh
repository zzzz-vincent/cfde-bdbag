#!/bin/bash

module load anaconda
python3 bulkatacseq.py

if [ ! -d bdbags ]; then
	mkdir bdbags
fi

for D in atacseq-bulk-new*
do
	if [ -d $D ]; then
		rm -rfv $D
	fi
done

for D in atacseq-bulk-published*
do
	if [ -d $D ]; then
		cp C2M2_datapackage.json $D/ 
	fi
done

mv -v atacseq-bulk-published* bdbags/
