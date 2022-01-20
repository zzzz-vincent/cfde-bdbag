#!/bin/bash

rm -f *.done *.computing

OUTPUT_DIRECTORY=codex-published-0dc91e6484430c2db25b6765dd6aa565/
if [ -d $OUTPUT_DIRECTORY ]; then
	rm -r $OUTPUT_DIRECTORY
fi

python3 codex.py
bash ./copy_empty_files.sh $OUTPUT_DIRECTORY

if [ -d $OUTPUT_DIRECTORY ]; then
	python check-submissions.py -d $OUTPUT_DIRECTORY
	exit 0
else
	echo "Folder "$OUTPUT_DIRECTORY" not found."
	exit 1
fi

