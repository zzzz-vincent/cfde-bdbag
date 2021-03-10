import pandas as pd
from pathlib import Path
from shutil import rmtree
import datetime
import time
import os
import mimetypes

def __get_filename( file ):
    return file.name

def __get_file_extension( file ):
    return file.suffix

def __get_file_size( file ):
    return file.stat().st_size

def __get_file_creation_date( file ):
    t = os.path.getmtime(str(file))
    return str(datetime.datetime.fromtimestamp(t))

def __get_file_format( file ):
    extension = get_file_extension( file )
    return extension

def __get_data_type( file ):
    extension = get_file_extension( file )
    return extension

def __get_mime_type( file ):
    return mimetypes.MimeTypes().guess_type(str(file))[0]

def _build_dataframe( project_id, directory ):
    '''
    Build a dataframe with minimal information for this entity.
    '''

    id_namespace = 'HuBMAP'
    headers = ['id_namespace', \
               'local_id', \
               'project_id', \
               'persisten_id', \
               'creation_time', \
               'size_in_bytes', \
               'uncompressed_size_in_bytes', \
               'sha256', \
               'md5', \
               'filename', \
               'file_format', \
               'data_type', \
               'assay_type', \
               'mime_type']

    df = pd.DataFrame(columns=headers)

    p = Path(directory).glob('**/*')
    files = [x for x in p if x.is_file()]

    for file in files:
        df = df.append({'id_namespace':id_namespace, \
                        'local_id':file, \
                        'project_id':project_id, \
                        'creation_time':__get_file_creation_date(file), \
                        'size_in_bytes':__get_file_size(file), \
                        'filename':__get_filename(file), \
                        'file_format':__get_file_format(file), \
                        'data_type':__get_data_type(file), \
                        'assay_type':'Whole Genome Sequence', \
                        'mime_type':__get_mime_type(file)}, ignore_index=True)

    return df

def create_manifest( project_id, directory ):
    filename = 'file.tsv'
    if not directory.exists():
        print('Data directory does not exist')
        return False
    else:
        df = _build_dataframe( project_id, directory )
        df.to_csv( filename, sep="\t", index=False)
        return True
