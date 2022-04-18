#!/bin/bash

DATASET=$1

if [ ! -d ancestors ]; then
	mkdir ancestors
fi

curl -s -X 'GET' \
	-H 'accept: application/json' \
	-H 'Authorization: Bearer '$TOKEN'' \
	'https://entity.api.hubmapconsortium.org/ancestors/'$DATASET > ancestors/$DATASET.json
