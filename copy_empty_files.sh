#!/bin/bash

DIRECTORY=$1

for FILE in empty/*
do
	if [ ! -f $DIRECTORY/"${FILE##*/}" ]; then
		cp $FILE $DIRECTORY/"${FILE##*/}"
	fi
done
