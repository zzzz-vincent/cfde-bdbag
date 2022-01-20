#!/bin/bash

rm -f *.done *.computing

if [ -d codex-published-0dc91e6484430c2db25b6765dd6aa565 ]; then
	rm -r codex-published-0dc91e6484430c2db25b6765dd6aa565
fi

python3 codex.py

if [ -d codex-published-0dc91e6484430c2db25b6765dd6aa565 ]; then
	python check-submissions.py -d codex-published-0dc91e6484430c2db25b6765dd6aa565/
	exit 0
else
	echo "Folder "codex-published-0dc91e6484430c2db25b6765dd6aa565" not found."
	exit 1
fi

