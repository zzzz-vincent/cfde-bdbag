import pandas as pd
from pathlib import Path
from shutil import rmtree

def _build_dataframe():
    '''
    Build a dataframe with minimal information for this entity.
    '''

    id_namespace = 'HuBMAP'
    headers = ['id_namespace', 'local_id', 'project_id_namespace', 'project_local_id', 'persisten_id', 'creation_time', 'anatomy']
    df = pd.DataFrame(columns=headers)

    return df

def create_manifest():
    filename = 'biosample.tsv'
    df = _build_dataframe( data_provider )
    df.to_csv( filename, sep="\t", index=False)

    return True
