#!/bin/bash

set -x

DATA=$1

OUTPUT_DIRECTORY='cfde-submission'-$(date +"%Y%m%d")
if [ -d $OUTPUT_DIRECTORY ]; then
	rm -rf $OUTPUT_DIRECTORY
fi
mkdir $OUTPUT_DIRECTORY

function create_file_tsv(){
	FILE=$1
        OUTPUT_DIRECTORY='cfde-submission'-$(date +"%Y%m%d")
	if [ ! -f $OUTPUT_DIRECTORY/file.tsv ]; then
		head -n1 $FILE > $OUTPUT_DIRECTORY/file.tsv
	fi

	tail -n +2 $FILE >> $OUTPUT_DIRECTORY/file.tsv
}

function create_biosample_tsv(){
	FILE=$1
        OUTPUT_DIRECTORY='cfde-submission'-$(date +"%Y%m%d")
	if [ ! -f $OUTPUT_DIRECTORY/biosample.tsv ]; then
		head -n1 $FILE > $OUTPUT_DIRECTORY/biosample.tsv
	fi

	tail -n +2 $FILE >> $OUTPUT_DIRECTORY/biosample.tsv
}

function create_collection_tsv(){
	FILE=$1
        OUTPUT_DIRECTORY='cfde-submission'-$(date +"%Y%m%d")
	if [ ! -f $OUTPUT_DIRECTORY/temp.tsv ]; then
		head -n1 $FILE > $OUTPUT_DIRECTORY/temp.tsv
	fi

	tail -n +2 $FILE >> $OUTPUT_DIRECTORY/temp.tsv
}

function create_project_tsv(){
	FILE=$1
        OUTPUT_DIRECTORY='cfde-submission'-$(date +"%Y%m%d")
	
	if [ ! -f $OUTPUT_DIRECTORY/temp.tsv ]; then
	        cp project.tsv $OUTPUT_DIRECTORY/temp.tsv
	fi

	tail -n +2 $FILE >> $OUTPUT_DIRECTORY/temp.tsv
}

export -f create_file_tsv
export -f create_project_tsv
export -f create_collection_tsv
export -f create_biosample_tsv

find $DATA -type f -name 'file.tsv' -exec bash -c 'create_file_tsv "$0"' {} \;

find $DATA -type f -name 'biosample.tsv' -exec bash -c 'create_biosample_tsv "$0"' {} \;

find $DATA -type f -name 'project.tsv' -exec bash -c 'create_project_tsv "$0"' {} \;
cat $OUTPUT_DIRECTORY/temp.tsv | perl -ne 'print unless $seen{$_}++' > $OUTPUT_DIRECTORY/project.tsv
rm -f $OUTPUT_DIRECTORY/temp.tsv

find $DATA -type f -name 'collection.tsv' -exec bash -c 'create_collection_tsv "$0"' {} \;
cat $OUTPUT_DIRECTORY/temp.tsv | perl -ne 'print unless $seen{$_}++' > $OUTPUT_DIRECTORY/collection.tsv
rm -f $OUTPUT_DIRECTORY/temp.tsv

cp project_in_project.tsv $OUTPUT_DIRECTORY/
cp primary_dcc_contact.tsv $OUTPUT_DIRECTORY/

python3 build_term_tables.py $OUTPUT_DIRECTORY
