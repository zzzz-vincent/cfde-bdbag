import pandas as pd
from pathlib import Path
from shutil import rmtree

def _build_dataframe( data_provider ):
    '''
    Build a dataframe with minimal information for this entity.
    '''

    id_namespace = 'HuBMAP'
    headers = ['id_namespace', 'local_id', 'persistent_id', 'creation_time', 'abbreviation', 'name', 'description']
    df = pd.DataFrame(columns=headers)
    df = df.append({'id_namespace':id_namespace, 'local_id':data_provider, 'name':data_provider}, ignore_index=True)

    return df

def create_manifest( data_provider ):
    filename = 'project.tsv'
    df = _build_dataframe( data_provider )
    df.to_csv( filename, sep="\t", index=False)

    return True
