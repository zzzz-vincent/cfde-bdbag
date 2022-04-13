#!/bin/bash

DATASET=$1

if [ ! -d datasets ]; then
	mkdir datasets
fi

curl -s -X 'GET' \
        -H 'accept: application/json' \
        -H 'Authorization: Bearer '$TOKEN'' \
        'https://entity.api.hubmapconsortium.org/entities/'$DATASET > datasets/$DATASET.json
