#!/bin/bash

DATASET=$1

if [ ! -d provenance ]; then
	mkdir provenance
fi

curl -s -X 'GET' \
        -H 'accept: application/json' \
        -H 'Authorization: Bearer '$TOKEN'' \
        'https://entity.api.hubmapconsortium.org/datasets/'$DATASET'/prov-info?format=json' > provenance/$DATASET.json
