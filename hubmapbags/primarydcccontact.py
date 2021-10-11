import pandas as pd
from pathlib import Path
from shutil import rmtree

def _build_dataframe( data_provider ):
    '''
    Build a dataframe with minimal information for this entity.
    '''

    headers = ['contact_email', 'contact_name', 'project_id_namespace', 'project_local_id', 'dcc_abbreviation', 'dcc_name', 'dcc_description', 'dcc_url'] 
    df = pd.DataFrame(columns=headers)
    df = df.append({'contact_email':'cfde-submissions@hubmapconsortium.org',\
            'contact_name':'Ivan Cao-Berg',\
            'project_id_namespace':'tag:hubmapconsortium.org,2021:',\
            'project_local_id':data_provider,\
            'dcc_abbreviation':'HuBMAP',\
            'dcc_name':'HuBMAP',\
            'dcc_description':'Human BioMolecular Atlas Program',\
            'dcc_url':'http://portal.hubmapconsortium.org'}, ignore_index=True)

    return df

def create_manifest( data_provider ):
    filename = 'primary_dcc_contact.tsv'
    df = _build_dataframe( data_provider )
    df.to_csv( filename, sep="\t", index=False)

    return True
