#!/bin/bash

DIRECTORY=$1

cd empty
for FILE in *
do
        if [ ! -f $DIRECTORY/$FILE ]; then
		echo cp $FILE $DIRECTORY/$FILE
	fi
done
