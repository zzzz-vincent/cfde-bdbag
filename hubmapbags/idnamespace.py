import pandas as pd
from pathlib import Path
from shutil import rmtree

def _build_dataframe():
    '''
    Build a dataframe with minimal information for this entity.
    '''

    id_namespace = 'HuBMAP'
    headers = ['id', 'abbreviation', 'name', 'description']
    df = pd.DataFrame(columns=headers)
    df = df.append({'id':'HuBMAP', \
           'abbreviation':'HuBMAP', \
           'name':'HuBMAP', \
           'description':'Human BioMolecular Atlas Program'}, ignore_index=True)

    return df

def create_manifest():
    filename = 'id_namespace.tsv'
    df = _build_dataframe()
    df.to_csv( filename, sep="\t", index=False)

    return True
