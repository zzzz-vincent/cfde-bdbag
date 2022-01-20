#!/bin/bash

set -x

INPUT_DIRECTORY=$1

OUTPUT_DIRECTORY='cfde-bdbag'-$(date +"%Y-%m-%d")
if [ -d $OUTPUT_DIRECTORY ]; then
	rm -rfv $OUTPUT_DIRECTORY
fi

bash ./bags2bag.sh $INPUT_DIRECTORY
./copy_empty_files.sh $OUTPUT_DIRECTORY

OUTPUT_DIRECTORY='cfde-submission'-$(date +"%Y-%m-%d")
if [ -d $OUTPUT_DIRECTORY ]; then
        rm -rfv $OUTPUT_DIRECTORY
fi

python3 prepare_C2M2_submission.py
