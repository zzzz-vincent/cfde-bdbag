import pandas as pd
from pathlib import Path
from shutil import rmtree
import datetime
import time
import os
import mimetypes
import pickle

def __get_filename( file ):
    '''
    Helper function that returns a valid filename representation
    '''

    return file.name.replace(' ', '%20')

def _get_list_of_files( directory ):
    '''
    Helper function that returns the EDAM Ontology code for the file data type.
    '''

    return Path(directory).glob('**/*')

def _build_dataframe( donor_id, directory ):
    '''
    Build a dataframe with minimal information for this entity.
    '''

    id_namespace = 'tag:hubmapconsortium.org,2021:'
    headers = ['file_id_namespace', \
                'file_local_id', \
                'subject_id_namespace', \
                'subject_local_id']

    temp_file = directory.replace('/','_').replace(' ','_') + '.pkl'
    if Path( temp_file ).exists():
        print('Temporary file ' + temp_file + ' found. Loading df into memory')
        with open( temp_file, 'rb' ) as file:
            df = pickle.load(file)

        df = df.drop(columns=['project_id_namespace', 'project_local_id', \
            'persistent_id', 'creation_time', 'size_in_bytes', \
            'uncompressed_size_in_bytes', 'sha256', 'md5', 'filename', \
            'file_format', 'data_type', 'assay_type', 'mime_type', 'sha256'])

        df['subject_id_namespace']=df['id_namespace']
        df = df.rename(columns={'id_namespace': 'file_id_namespace', \
            'local_id':'file_local_id'}, errors ="raise")
        df['subject_local_id'] = donor_id
        df[['file_id_namespace', 'file_local_id', 'subject_id_namespace', 'subject_local_id']]
    else:
        df = pd.DataFrame(columns=headers)

        p = Path(directory).glob('**/*')
        print('Finding all files in directory ' + str(directory))

        for file in p:
            if file.is_file():
                print('Processing ' + str(file) )
                if str(file).find('drv_') < 0 or str(file).find('processed') < 0:
                    df = df.append({'file_id_namespace':id_namespace, \
                        'file_local_id':str(file).replace(' ','%20'), \
                        'subject_id_namespace':id_namespace, \
                        'subject_local_id':donor_id}, ignore_index=True)

    return df

def create_manifest( donor_id, directory ):
    '''
    Helper function that creates the TSV file
    '''
    
    filename = 'file_describes_subject.tsv'
    if not Path(directory).exists():
        print('Data directory ' + directory + ' does not exist')
        return False
    else:
        df = _build_dataframe( donor_id, directory )
        df.to_csv( filename, sep="\t", index=False)
        return True
