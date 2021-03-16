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
    extension = __get_file_extension( file )
    return extension

def __get_data_type( file ):
    extension = __get_file_extension( file )
    print( 'File extension is ' + extension )

    formats = {}
    formats['.tsv'] = 'data:2526' #tsv 
    formats['.tif'] = 'data:2968' #tiff
    formats['.tiff'] = 'data:2968' #tiff
    formats['.png'] = 'data:2968' #png
    formats['.jpg'] = 'data:2968' #jpg
    formats['.ome.tiff'] = 'data:2968' #ome.tiff
    formats['.fastq'] = 'data:2044' #txt
    formats['.txt'] = 'data:2526' #txt
    formats['.xml'] = 'data:2526' #xml
    formats['.czi'] = 'data:2968' #czi
    formats['.gz'] = 'data:2044' #gz
    formats[''] = '' #other

    return formats[extension]

def __get_mime_type( file ):
    return mimetypes.MimeTypes().guess_type(str(file))[0]

def __get_file_format( file ):
    extension = __get_file_extension( file )
    print( 'File extension is ' + extension )

    formats = {}
    formats['.tsv'] = 'format:2330' #tsv 
    formats['.tif'] = 'format:3547' #tiff
    formats['.tiff'] = 'format:3547' #tiff
    formats['.png'] = 'format:3547' #png
    formats['.jpg'] = 'format:3547' #jpg
    formats['.ome.tiff'] = 'format:3547' #ome.tiff
    formats['.fastq'] = 'format:2330' #txt
    formats['.txt'] = 'format:2330' #txt
    formats['.xml'] = 'format:2332' #xml
    formats['.czi'] = 'format:3547' #czi
    formats['.gz'] = 'format:3989' #gz
    formats[''] = 'format:2330' #gz

    return formats[extension]

def __get_assay_type_from_obi(assay_type):
   
    print('Assay type is ' + assay_type ) 
    assay = {}
    assay['af'] = 'CHMO:0000087' #AF
    assay['atacseq-bulk'] = 'OBI:0002039' #Bulk ATAC-seq
    assay['bulk-rna'] = 'OBI:0001271' #Bulk RNA-seq
    assay[''] = 'OBI:0002631' #scRNA-seq
    assay[''] = 'OBI:0002764' #scATACseq
    assay['snatacseq'] = 'OBI:0002762' #snATAC-seq
    assay['wgs'] = 'OBI:0002117' #WGS
    
    return assay[assay_type]

def _build_dataframe( project_id, assay_type, directory ):
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
        print('Processing ' + str(file) )
        df = df.append({'id_namespace':id_namespace, \
                        'local_id':file, \
                        'project_id':project_id, \
                        'creation_time':__get_file_creation_date(file), \
                        'size_in_bytes':__get_file_size(file), \
                        'filename':__get_filename(file), \
                        'file_format':__get_file_format(file), \
                        'data_type':__get_data_type(file), \
                        'assay_type':__get_assay_type_from_obi(assay_type), \
                        'mime_type':__get_mime_type(file)}, ignore_index=True)

    return df

def create_manifest( project_id, assay_type, directory ):
    filename = 'file.tsv'
    if not Path(directory).exists():
        print('Data directory ' + directory + ' does not exist')
        return False
    else:
        df = _build_dataframe( project_id, assay_type, directory )
        df.to_csv( filename, sep="\t", index=False)
        return True
