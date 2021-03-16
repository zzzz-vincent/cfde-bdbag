import pandas as pd
from pathlib import Path
from shutil import rmtree

def __get_organ_from_uberon( organ ):
    '''
    For full list, visit
    https://github.com/hubmapconsortium/search-api/blob/test-release/src/search-schema/data/definitions/enums/organ_types.yaml
    '''
   
    organs = {}
    organs['SI'] = 'UBERON:0002108' #small intestine
    organs['LI'] = 'UBERON:0000059' #large intestine
    organs['LK'] = 'UBERON:0004538' #left kidney
    organs['RK'] = 'UBERON:0004539' #right kidney
    organs['SP'] = 'UBERON:0002106' #spleen    
 
    return organs[organ]

def _build_dataframe( biosample_id, data_provider, organ ):
    '''
    Build a dataframe with minimal information for this entity.
    '''

    id_namespace = 'HuBMAP'
    headers = ['id_namespace', 'local_id', 'project_id_namespace', 'project_local_id', 'persisten_id', 'creation_time', 'anatomy']
    df = pd.DataFrame(columns=headers)
    df = df.append({'id_namespace':id_namespace, \
       'local_id':biosample_id, \
       'project_id_namespace':id_namespace, \
       'project_local_id':data_provider, \
       'anatomy': __get_organ_from_uberon(organ)}, ignore_index=True)

    return df

def create_manifest( biosample_id, data_provider, organ ):
    filename = 'biosample.tsv'
    df = _build_dataframe( biosample_id, data_provider, organ )
    df.to_csv( filename, sep="\t", index=False)

    return True
