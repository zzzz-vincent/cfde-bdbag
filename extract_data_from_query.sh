#!/bin/bash

HID=$1 
bash ./query_ancestors_api.sh $HID 
bash ./query_entity_api.sh $HID
bash ./query_entity_prov_api.sh $HID

GROUP_NAME=$(cat datasets/$HID.json | jq '.upload.group_name' | xargs)
if [[ ! -z "$GROUP_NAME" ]]; then
	GROUP_NAME=$(cat datasets/$HID.json | jq .group_name | xargs)
fi

GROUP_UUID=$(cat datasets/$HID.json | jq '.upload.group_uuid' | xargs)
if [[ ! -z "$GROUP_UUID" ]]; then
	GROUP_UUID=$(cat datasets/$HID.json | jq .group_uuid | xargs)
fi

HUBMAP_ID=$(cat datasets/$HID.json | jq '.hubmap_id' | xargs)
HUBMAP_UUID=$(cat datasets/$HID.json | jq '.uuid' | xargs)
STATUS=$(cat datasets/$HID.json | jq '.status' | xargs)
DATA_TYPES=$(cat datasets/$HID.json | jq '.data_types' | grep '"' | xargs)

SAMPLE_ID=$(cat datasets/$HID.json | jq .direct_ancestors | jq .[].hubmap_id | xargs)
SAMPLE_UUID=$(cat provenance/$HID.json | jq .organ_hubmap_id | grep '"' | xargs)

ORGAN_TYPE=$(cat provenance/$HID.json | jq .organ_type | grep '"' | xargs)
if [ "$ORGAN_TYPE" = "kidney (left)" ]; then
	ORGAN_TYPE='left kidney'
fi

if [ "$ORGAN_TYPE" = "kidney (right)" ]; then
        ORGAN_TYPE='right kidney'
fi

ORGAN_ID=$(cat provenance/$HID.json | jq .organ_hubmap_id | grep '"' | xargs)
DONOR_ID=$(cat ancestors/$HID.json | jq .[3].hubmap_id | xargs)

FULL_PATH='/hive/hubmap/data/protected/'$GROUP_NAME'/'$HUBMAP_UUID
if [ ! -d "$FULL_PATH" ]; then
	FULL_PATH='/hive/hubmap/data/public/'$HUBMAP_UUID
	if [ ! -d "$FULL_PATH" ]; then
		FULL_PATH='null'
	fi
fi

echo -e $GROUP_NAME'\t'$GROUP_UUID'\t'$HUBMAP_ID'\t'$HUBMAP_UUID'\t'$STATUS'\t'$DATA_TYPES'\t'$SAMPLE_ID'\t'$SAMPLE_UUID'\t'$ORGAN_TYPE'\t'$ORGAN_ID'\t'$DONOR_ID'\t'$FULL_PATH
