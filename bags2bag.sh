#!/bin/bash

set -x

DATA=$1

OUTPUT_DIRECTORY='cfde-bdbag'-$(date +"%Y%m%d")
if [ -d $OUTPUT_DIRECTORY ]; then
	rm -rf $OUTPUT_DIRECTORY
fi
mkdir $OUTPUT_DIRECTORY

function create_subject_tsv(){
        FILE=$1
        OUTPUT_DIRECTORY='cfde-bdbag'-$(date +"%Y%m%d")
        if [ ! -f $OUTPUT_DIRECTORY/subject.tsv ]; then
                head -n1 $FILE > $OUTPUT_DIRECTORY/subject.tsv
        fi

        tail -n +2 $FILE >> $OUTPUT_DIRECTORY/subject.tsv
}

function create_subject_in_collection_tsv(){
        FILE=$1
        OUTPUT_DIRECTORY='cfde-bdbag'-$(date +"%Y%m%d")
        if [ ! -f $OUTPUT_DIRECTORY/subject_in_collection.tsv ]; then
                head -n1 $FILE > $OUTPUT_DIRECTORY/subject_in_collection.tsv
        fi

        tail -n +2 $FILE >> $OUTPUT_DIRECTORY/subject_in_collection.tsv
}

function create_file_in_collection_tsv(){
       	FILE=$1
        OUTPUT_DIRECTORY='cfde-bdbag'-$(date +"%Y%m%d")
       	if [ ! -f $OUTPUT_DIRECTORY/file_in_collection.tsv ]; then
               	head -n1 $FILE > $OUTPUT_DIRECTORY/file_in_collection.tsv
        fi

        tail -n +2 $FILE >> $OUTPUT_DIRECTORY/file_in_collection.tsv
}

function create_file_tsv(){
	FILE=$1
        OUTPUT_DIRECTORY='cfde-bdbag'-$(date +"%Y%m%d")
	if [ ! -f $OUTPUT_DIRECTORY/file.tsv ]; then
		head -n1 $FILE > $OUTPUT_DIRECTORY/file.tsv
	fi

	tail -n +2 $FILE >> $OUTPUT_DIRECTORY/file.tsv
}

function create_file_in_collection_tsv(){
        FILE=$1
        OUTPUT_DIRECTORY='cfde-bdbag'-$(date +"%Y%m%d")
        if [ ! -f $OUTPUT_DIRECTORY/files_in_collection.tsv ]; then
                head -n1 $FILE > $OUTPUT_DIRECTORY/files_in_collection.tsv
        fi

        tail -n +2 $FILE >> $OUTPUT_DIRECTORY/files_in_collection.tsv
}

function create_biosample_tsv(){
	FILE=$1
        OUTPUT_DIRECTORY='cfde-bdbag'-$(date +"%Y%m%d")
	if [ ! -f $OUTPUT_DIRECTORY/biosample.tsv ]; then
		head -n1 $FILE > $OUTPUT_DIRECTORY/biosample.tsv
	fi

	tail -n +2 $FILE >> $OUTPUT_DIRECTORY/biosample.tsv
}

function create_file_describes_biosample_tsv(){
        FILE=$1
        OUTPUT_DIRECTORY='cfde-bdbag'-$(date +"%Y%m%d")
        if [ ! -f $OUTPUT_DIRECTORY/file_describes_biosample.tsv ]; then
                head -n1 $FILE > $OUTPUT_DIRECTORY/file_describes_biosample.tsv
        fi

        tail -n +2 $FILE >> $OUTPUT_DIRECTORY/file_describes_biosample.tsv
}

function create_biosample_in_collection_tsv(){
        FILE=$1
        OUTPUT_DIRECTORY='cfde-bdbag'-$(date +"%Y%m%d")
        if [ ! -f $OUTPUT_DIRECTORY/biosample_in_collection.tsv ]; then
                head -n1 $FILE > $OUTPUT_DIRECTORY/biosample_in_collection.tsv
        fi

        tail -n +2 $FILE >> $OUTPUT_DIRECTORY/biosample_in_collection.tsv
}

function create_biosample_from_subject_tsv(){
        FILE=$1
        OUTPUT_DIRECTORY='cfde-bdbag'-$(date +"%Y%m%d")
        if [ ! -f $OUTPUT_DIRECTORY/biosample_from_subject.tsv ]; then
                head -n1 $FILE > $OUTPUT_DIRECTORY/biosample_from_subject.tsv
        fi

	tail -n +2 $FILE >> $OUTPUT_DIRECTORY/biosample_from_subject.tsv
}

function create_collection_defined_by_project_tsv(){
        FILE=$1
        OUTPUT_DIRECTORY='cfde-bdbag'-$(date +"%Y%m%d")
        if [ ! -f $OUTPUT_DIRECTORY/collection_defined_by_project.tsv ]; then
                head -n1 $FILE > $OUTPUT_DIRECTORY/collection_defined_by_project.tsv
        fi

	tail -n +2 $FILE >> $OUTPUT_DIRECTORY/collection_defined_by_project.tsv
}

function create_file_describes_subject_tsv(){
        FILE=$1
        OUTPUT_DIRECTORY='cfde-bdbag'-$(date +"%Y%m%d")
        if [ ! -f $OUTPUT_DIRECTORY/file_describes_subject.tsv ]; then
                head -n1 $FILE > $OUTPUT_DIRECTORY/file_describes_subject.tsv
        fi

	tail -n +2 $FILE >> $OUTPUT_DIRECTORY/file_describes_subject.tsv
}

function create_collection_tsv(){
	FILE=$1
        OUTPUT_DIRECTORY='cfde-bdbag'-$(date +"%Y%m%d")
	if [ ! -f $OUTPUT_DIRECTORY/collection.tsv ]; then
		head -n1 $FILE > $OUTPUT_DIRECTORY/collection.tsv
	fi

	tail -n +2 $FILE >> $OUTPUT_DIRECTORY/collection.tsv
}

function create_project_tsv(){
	FILE=$1
        OUTPUT_DIRECTORY='cfde-bdbag'-$(date +"%Y%m%d")
	
	if [ ! -f $OUTPUT_DIRECTORY/project.tsv ]; then
	        #cp project.tsv $OUTPUT_DIRECTORY/project.tsv
		head -n1 $FILE > $OUTPUT_DIRECTORY/project.tsv
	fi

	tail -n +2 $FILE >> $OUTPUT_DIRECTORY/project.tsv
}

function create_project_in_project_tsv(){
	FILE=$1
        OUTPUT_DIRECTORY='cfde-bdbag'-$(date +"%Y%m%d")
	
	if [ ! -f $OUTPUT_DIRECTORY/project_in_project.tsv ]; then
	        #cp project_in_project.tsv $OUTPUT_DIRECTORY/project_in_project.tsv
		head -n1 $FILE > $OUTPUT_DIRECTORY/project_in_project.tsv
	fi

	tail -n +2 $FILE >> $OUTPUT_DIRECTORY/project_in_project.tsv
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
export -f create_project_in_project_tsv

find $DATA -type f -name 'file.tsv' -exec bash -c 'create_file_tsv "$0"' {} \;
find $DATA -type f -name 'file_describes_biosample.tsv' -exec bash -c 'create_file_describes_biosample_tsv "$0"' {} \;
find $DATA -type f -name 'file_in_collection.tsv' -exec bash -c 'create_file_in_collection_tsv "$0"' {} \;
find $DATA -type f -name 'file_describes_subject.tsv' -exec bash -c 'create_file_describes_subject_tsv "$0"' {} \;

find $DATA -type f -name 'subject.tsv' -exec bash -c 'create_subject_tsv "$0"' {} \;
cat $OUTPUT_DIRECTORY/subject.tsv | uniq > /tmp/temp.tsv && mv /tmp/temp.tsv $OUTPUT_DIRECTORY/subject.tsv
find $DATA -type f -name 'subject_in_collection.tsv' -exec bash -c 'create_subject_in_collection_tsv "$0"' {} \;
cat $OUTPUT_DIRECTORY/subject_in_collection.tsv | uniq > /tmp/temp.tsv && mv /tmp/temp.tsv $OUTPUT_DIRECTORY/subject_in_collection.tsv

find $DATA -type f -name 'biosample_in_collection.tsv' -exec bash -c 'create_biosample_in_collection_tsv "$0"' {} \;
cat $OUTPUT_DIRECTORY/biosample_in_collection.tsv | uniq > /tmp/temp.tsv && mv /tmp/temp.tsv $OUTPUT_DIRECTORY/biosample_in_collection.tsv
find $DATA -type f -name 'biosample.tsv' -exec bash -c 'create_biosample_tsv "$0"' {} \;
cat $OUTPUT_DIRECTORY/biosample.tsv | sort | uniq > /tmp/temp.tsv && mv /tmp/temp.tsv $OUTPUT_DIRECTORY/biosample.tsv
find $DATA -type f -name 'biosample_from_subject.tsv' -exec bash -c 'create_biosample_from_subject_tsv "$0"' {} \;
cat $OUTPUT_DIRECTORY/biosample_from_subject.tsv | uniq > /tmp/temp.tsv && mv /tmp/temp.tsv $OUTPUT_DIRECTORY/biosample_from_subject.tsv

find $DATA -type f -name 'project.tsv' -exec bash -c 'create_project_tsv "$0"' {} \;
cat $OUTPUT_DIRECTORY/project.tsv | uniq > /tmp/temp.tsv && mv /tmp/temp.tsv $OUTPUT_DIRECTORY/project.tsv
find $DATA -type f -name 'project_in_project.tsv' -exec bash -c 'create_project_in_project_tsv "$0"' {} \;
cat $OUTPUT_DIRECTORY/project_in_project.tsv | sort | uniq > /tmp/temp.tsv && mv /tmp/temp.tsv $OUTPUT_DIRECTORY/project_in_project.tsv

find $DATA -type f -name 'collection.tsv' -exec bash -c 'create_collection_tsv "$0"' {} \;
cat $OUTPUT_DIRECTORY/collection.tsv | uniq > /tmp/temp.tsv && mv /tmp/temp.tsv $OUTPUT_DIRECTORY/collection.tsv
find $DATA -type f -name 'collection_defined_by_project.tsv' -exec bash -c 'create_collection_defined_by_project_tsv "$0"' {} \;

find $DATA -type f -name "dcc.tsv" -exec cp {} $OUTPUT_DIRECTORY/ \;

bash ./copy_empty_files.sh $OUTPUT_DIRECTORY

find $DATA -type f -name "*.tsv" -exec sed -i 's/hubmapconsortium.org,2021/hubmapconsortium.org,2022/g' {} \;

