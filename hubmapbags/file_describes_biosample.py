import pandas as pd
from pathlib import Path
from shutil import rmtree
import datetime
import time
import os
import pickle
import mimetypes

def _build_dataframe( biosample_id, directory ):
    '''
    Build a dataframe with minimal information for this entity.
    '''

    id_namespace = 'tag:hubmapconsortium.org,2022:'
    headers = ['file_id_namespace', \
               'file_local_id', \
               'biosample_id_namespace', \
               'biosample_local_id']

    temp_file = directory.replace('/','_').replace(' ','_') + '.pkl'
    if Path( temp_file ).exists():
        print('Temporary file ' + temp_file + ' found. Loading df into memory')
        with open( temp_file, 'rb' ) as file:
            df = pickle.load(file)

        df = df.drop(columns=['project_id_namespace', 'project_local_id', \
            'persistent_id', 'creation_time', 'size_in_bytes', \
            'uncompressed_size_in_bytes', 'sha256', 'md5', 'filename', 'dbgap_study_id', \
            'file_format', 'data_type', 'assay_type', 'mime_type', 'sha256', \
            'compression_format','bundle_collection_id_namespace','bundle_collection_local_id'])

        df['biosample_id_namespace']=df['id_namespace']
        df = df.rename(columns={'id_namespace': 'file_id_namespace', \
            'local_id':'file_local_id'}, errors ="raise")
        df['biosample_local_id'] = biosample_id
        df[['file_id_namespace', 'file_local_id', 'biosample_id_namespace', 'biosample_local_id']]
    else:
        df = [] 

    return df

def create_manifest( biosample_id, directory, output_directory ):
    filename = os.path.join( output_directory, 'file_describes_biosample.tsv' )
    temp_file = directory.replace('/','_').replace(' ','_') + '.pkl'
    if not Path(directory).exists() and not Path(temp_file).exists():
        print('Data directory ' + directory + ' does not exist. Temp file was not found either.')
        return False
    else:
        if Path(temp_file).exists():
            print('Temp file ' + temp_file + ' found. Continuing computation.')
        df = _build_dataframe( biosample_id, directory )
        df.to_csv( filename, sep="\t", index=False)
        return True
