#!/bin/bash

set -x

DATA=$1

OUTPUT_DIRECTORY='cfde-submission'-$(date +"%Y%m%d")
if [ -d $OUTPUT_DIRECTORY ]; then
	rm -rf $OUTPUT_DIRECTORY
fi
mkdir $OUTPUT_DIRECTORY

function create_subject_tsv(){
        FILE=$1
        OUTPUT_DIRECTORY='cfde-submission'-$(date +"%Y%m%d")
        if [ ! -f $OUTPUT_DIRECTORY/subject.tsv ]; then
                head -n1 $FILE > $OUTPUT_DIRECTORY/subject.tsv
        fi

        tail -n +2 $FILE >> $OUTPUT_DIRECTORY/subject.tsv
}

function create_subject_in_collection_tsv(){
        FILE=$1
        OUTPUT_DIRECTORY='cfde-submission'-$(date +"%Y%m%d")
        if [ ! -f $OUTPUT_DIRECTORY/subject_in_collection.tsv ]; then
                head -n1 $FILE > $OUTPUT_DIRECTORY/subject_in_collection.tsv
        fi

        tail -n +2 $FILE >> $OUTPUT_DIRECTORY/subject_in_collection.tsv
}

function create_file_in_collection_tsv(){
       	FILE=$1
        OUTPUT_DIRECTORY='cfde-submission'-$(date +"%Y%m%d")
       	if [ ! -f $OUTPUT_DIRECTORY/file_in_collection.tsv ]; then
               	head -n1 $FILE > $OUTPUT_DIRECTORY/file_in_collection.tsv
        fi

        tail -n +2 $FILE >> $OUTPUT_DIRECTORY/file_in_collection.tsv
}

function create_file_tsv(){
	FILE=$1
        OUTPUT_DIRECTORY='cfde-submission'-$(date +"%Y%m%d")
	if [ ! -f $OUTPUT_DIRECTORY/file.tsv ]; then
		head -n1 $FILE > $OUTPUT_DIRECTORY/file.tsv
	fi

	tail -n +2 $FILE >> $OUTPUT_DIRECTORY/file.tsv
}

function create_files_in_collection_tsv(){
        FILE=$1
        OUTPUT_DIRECTORY='cfde-submission'-$(date +"%Y%m%d")
        if [ ! -f $OUTPUT_DIRECTORY/files_in_collection.tsv ]; then
                head -n1 $FILE > $OUTPUT_DIRECTORY/files_in_collection.tsv
        fi

        tail -n +2 $FILE >> $OUTPUT_DIRECTORY/files_in_collection.tsv
}

function create_biosample_tsv(){
	FILE=$1
        OUTPUT_DIRECTORY='cfde-submission'-$(date +"%Y%m%d")
	if [ ! -f $OUTPUT_DIRECTORY/biosample.tsv ]; then
		head -n1 $FILE > $OUTPUT_DIRECTORY/biosample.tsv
	fi

	tail -n +2 $FILE >> $OUTPUT_DIRECTORY/biosample.tsv
}

function create_file_describes_biosample_tsv(){
        FILE=$1
        OUTPUT_DIRECTORY='cfde-submission'-$(date +"%Y%m%d")
        if [ ! -f $OUTPUT_DIRECTORY/file_describes_biosample.tsv ]; then
                head -n1 $FILE > $OUTPUT_DIRECTORY/file_describes_biosample.tsv
        fi

        tail -n +2 $FILE >> $OUTPUT_DIRECTORY/file_describes_biosample.tsv
}

function create_biosample_in_collection_tsv(){
        FILE=$1
        OUTPUT_DIRECTORY='cfde-submission'-$(date +"%Y%m%d")
        if [ ! -f $OUTPUT_DIRECTORY/biosample_in_collection.tsv ]; then
                head -n1 $FILE > $OUTPUT_DIRECTORY/biosample_in_collection.tsv
        fi

        tail -n +2 $FILE >> $OUTPUT_DIRECTORY/biosample_in_collection.tsv
}

function create_biosample_from_subject_tsv(){
        FILE=$1
        OUTPUT_DIRECTORY='cfde-submission'-$(date +"%Y%m%d")
        if [ ! -f $OUTPUT_DIRECTORY/biosample_from_subject.tsv ]; then
                head -n1 $FILE > $OUTPUT_DIRECTORY/biosample_from_subject.tsv
        fi

	tail -n +2 $FILE >> $OUTPUT_DIRECTORY/biosample_from_subject.tsv
}

function create_collection_defined_by_project_tsv(){
        FILE=$1
        OUTPUT_DIRECTORY='cfde-submission'-$(date +"%Y%m%d")
        if [ ! -f $OUTPUT_DIRECTORY/collection_defined_by_project.tsv ]; then
                head -n1 $FILE > $OUTPUT_DIRECTORY/collection_defined_by_project.tsv
        fi

	tail -n +2 $FILE >> $OUTPUT_DIRECTORY/collection_defined_by_project.tsv
}

function create_file_describes_subject_tsv(){
        FILE=$1
        OUTPUT_DIRECTORY='cfde-submission'-$(date +"%Y%m%d")
        if [ ! -f $OUTPUT_DIRECTORY/file_describes_subject.tsv ]; then
                head -n1 $FILE > $OUTPUT_DIRECTORY/file_describes_subject.tsv
        fi

	tail -n +2 $FILE >> $OUTPUT_DIRECTORY/file_describes_subject.tsv
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
export -f create_subject_tsv
export -f create_project_tsv
export -f create_collection_tsv
export -f create_biosample_tsv
export -f create_files_in_collection_tsv
export -f create_biosample_in_collection_tsv
export -f create_subject_in_collection_tsv
export -f create_file_in_collection_tsv
export -f create_file_describes_biosample_tsv
export -f create_file_describes_subject_tsv
export -f create_biosample_from_subject_tsv
export -f create_collection_defined_by_project_tsv

find $DATA -type f -name 'file.tsv' -exec bash -c 'create_file_tsv "$0"' {} \;

find $DATA -type f -name 'subject_in_collection.tsv' -exec bash -c 'create_subject_in_collection_tsv "$0"' {} \;

find $DATA -type f -name 'biosample_in_collection.tsv' -exec bash -c 'create_biosample_in_collection_tsv "$0"' {} \;
cat $OUTPUT_DIRECTORY/biosample_in_collection.tsv | perl -ne 'print unless $seen{$_}++' > $OUTPUT_DIRECTORY/temp.tsv
mv $OUTPUT_DIRECTORY/temp.tsv $OUTPUT_DIRECTORY/biosample_in_collection.tsv
rm -f $OUTPUT_DIRECTORY/temp.tsv

find $DATA -type f -name 'file_describes_biosample.tsv' -exec bash -c 'create_file_describes_biosample_tsv "$0"' {} \;
cat $OUTPUT_DIRECTORY/file_describes_biosample.tsv | perl -ne 'print unless $seen{$_}++' > $OUTPUT_DIRECTORY/temp.tsv
mv $OUTPUT_DIRECTORY/temp.tsv $OUTPUT_DIRECTORY/file_describes_biosample.tsv
rm -f $OUTPUT_DIRECTORY/temp.tsv

find $DATA -type f -name 'file_in_collection.tsv' -exec bash -c 'create_file_in_collection_tsv "$0"' {} \;
cat $OUTPUT_DIRECTORY/file_in_collection.tsv | perl -ne 'print unless $seen{$_}++' > $OUTPUT_DIRECTORY/temp.tsv
mv $OUTPUT_DIRECTORY/temp.tsv $OUTPUT_DIRECTORY/file_in_collection.tsv
rm -f $OUTPUT_DIRECTORY/temp.tsv

find $DATA -type f -name 'files_in_collection.tsv' -exec bash -c 'create_files_in_collection_tsv "$0"' {} \;

find $DATA -type f -name 'project.tsv' -exec bash -c 'create_project_tsv "$0"' {} \;
cat $OUTPUT_DIRECTORY/temp.tsv | perl -ne 'print unless $seen{$_}++' > $OUTPUT_DIRECTORY/project.tsv
rm -f $OUTPUT_DIRECTORY/temp.tsv

find $DATA -type f -name 'collection.tsv' -exec bash -c 'create_collection_tsv "$0"' {} \;
cat $OUTPUT_DIRECTORY/temp.tsv | perl -ne 'print unless $seen{$_}++' > $OUTPUT_DIRECTORY/collection.tsv
rm -f $OUTPUT_DIRECTORY/temp.tsv

find $DATA -type f -name 'subject.tsv' -exec bash -c 'create_subject_tsv "$0"' {} \;
cat $OUTPUT_DIRECTORY/subject.tsv | perl -ne 'print unless $seen{$_}++' > $OUTPUT_DIRECTORY/temp.tsv
mv $OUTPUT_DIRECTORY/temp.tsv $OUTPUT_DIRECTORY/subject.tsv
rm -f $OUTPUT_DIRECTORY/temp.tsv

find $DATA -type f -name 'biosample.tsv' -exec bash -c 'create_biosample_tsv "$0"' {} \;
cat $OUTPUT_DIRECTORY/biosample.tsv | perl -ne 'print unless $seen{$_}++' > $OUTPUT_DIRECTORY/temp.tsv
mv $OUTPUT_DIRECTORY/temp.tsv $OUTPUT_DIRECTORY/biosample.tsv
rm -f $OUTPUT_DIRECTORY/temp.tsv

find $DATA -type f -name 'biosample_from_subject.tsv' -exec bash -c 'create_biosample_from_subject_tsv "$0"' {} \;
cat $OUTPUT_DIRECTORY/biosample_from_subject.tsv | perl -ne 'print unless $seen{$_}++' > $OUTPUT_DIRECTORY/temp.tsv
mv $OUTPUT_DIRECTORY/temp.tsv $OUTPUT_DIRECTORY/biosample_from_subject.tsv
rm -f $OUTPUT_DIRECTORY/temp.tsv

find $DATA -type f -name 'file_describes_subject.tsv' -exec bash -c 'create_file_describes_subject_tsv "$0"' {} \;
cat $OUTPUT_DIRECTORY/file_describes_subject.tsv | perl -ne 'print unless $seen{$_}++' > $OUTPUT_DIRECTORY/temp.tsv
mv $OUTPUT_DIRECTORY/temp.tsv $OUTPUT_DIRECTORY/file_describes_subject.tsv
rm -f $OUTPUT_DIRECTORY/temp.tsv

find $DATA -type f -name 'collection_defined_by_project.tsv' -exec bash -c 'create_collection_defined_by_project_tsv "$0"' {} \;
cat $OUTPUT_DIRECTORY/collection_defined_by_project.tsv | perl -ne 'print unless $seen{$_}++' > $OUTPUT_DIRECTORY/temp.tsv
mv $OUTPUT_DIRECTORY/temp.tsv $OUTPUT_DIRECTORY/collection_defined_by_project.tsv
rm -f $OUTPUT_DIRECTORY/temp.tsv

cp project_in_project.tsv $OUTPUT_DIRECTORY/
cp primary_dcc_contact.tsv $OUTPUT_DIRECTORY/
