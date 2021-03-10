import pandas as pd
from pathlib import Path
from shutil import rmtree

# Collections
def build_dataframe( hubmap_id ):
    id_namespace = 'HuBMAP'
    df = pd.DataFrame(columns=headers)
    df = df.append({'id_namespace':id_namespace, 'local_id':hubmap_id, 'name':hubmap_id}, ignore_index=True)
   
    return df

def create_manifest( data_provider ):
    filename = 'collection.tsv'
    df = build_dataframe( data_provider )
    df.to_csv( filename, sep="\t", index=False)
    
    return True

