import pandas as pd
from pathlib import Path
from shutil import rmtree

def _build_dataframe( biosample_id, subject_id ):
    '''
    Build a dataframe with minimal information for this entity.
    '''

    id_namespace = 'tag:hubmapconsortium.org,2021:'
    headers = ['biosample_id_namespace', 'biosample_local_id', 'subject_id_namespace', 'subject_local_id']
    df = pd.DataFrame(columns=headers)
    df = df.append({'biosample_id_namespace':id_namespace, \
                     'biosample_local_id':biosample_id, \
                     'subject_id_namespace':id_namespace, \
                     'subject_local_id':subject_id}, ignore_index=True)

    return df

def create_manifest( biosample_id, subject_id ):
    filename = 'biosample_from_subject.tsv'
    df = _build_dataframe( biosample_id, subject_id )
    df.to_csv( filename, sep="\t", index=False)

    return True
