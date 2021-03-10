import pandas as pd
from pathlib import Path
from shutil import rmtree

def _build_dataframe( hubmap_id ):
    '''
    Build a dataframe with minimal information for this entity.
    '''

    id_namespace = 'HuBMAP'
    df = pd.DataFrame(columns=headers)
    df = df.append({'id_namespace':id_namespace, 'local_id':hubmap_id, 'name':hubmap_id}, ignore_index=True)

    return df

def create_manifest( hubmap_id ):
    filename = 'collection.tsv'
    df = _build_dataframe( data_provider )
    df.to_csv( filename, sep="\t", index=False)

    return True
