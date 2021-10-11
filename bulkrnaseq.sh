#!/bin/bash

module load anaconda
python3 bulkrnaseq.py

if [ ! -d bdbags ]; then
	mkdir bdbags
fi

for D in bulk-rna-bulk-new*
do
	if [ -d $D ]; then
		rm -rfv $D
	fi
done

for D in bulk-rna-published*
do
	if [ -d $D ]; then
		cp C2M2_datapackage.json $D/ 
	fi
done

mv -v bulk-rna-published* bdbags/
