import pandas as pd
from pathlib import Path
from shutil import rmtree

# Biosamples
def build_dataframe():
    id_namespace = 'HuBMAP'
    headers = ['id_namespace', 'local_id', 'project_id_namespace', 'project_local_id', 'persisten_id', 'creation_time', 'anatomy']
    df = pd.DataFrame(columns=headers)

    return df

def create_manifest():
    filename = 'biosample.tsv'
    df = build_dataframe( data_provider )
    df.to_csv( filename, sep="\t", index=False)
    
    return True

