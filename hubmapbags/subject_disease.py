import pandas as pd
import os

def _build_dataframe():
    '''
    Build a dataframe with minimal information for this entity.
    '''

    headers = ['subject_id_namespace', \
               'subject_local_id', \
               'disease']

    df = pd.DataFrame( columns = headers )

    return df

def create_manifest( output_directory ):
    filename = os.path.join( output_directory, 'subject_disease.tsv' )
    df = _build_dataframe()
    df.to_csv( filename, sep="\t", index=False)
    
    return True
