import logging

import pandas as pd
from pathlib import Path
from shutil import rmtree

def __get_name( organ ):
    '''
    For full list, visit
    https://github.com/hubmapconsortium/search-api/blob/test-release/src/search-schema/data/definitions/enums/organ_types.yaml
    '''

    organs = {}
    organs['SI'] = 'Small intestine'
    organs['LI'] = 'Large intestine'
    organs['LK'] = 'Left kidney'
    organs['RK'] = 'Right kidney'
    organs['SP'] = 'Spleen'

    return organs[organ]

def __get_organ_from_uberon( organ ):
    '''
    For full list, visit
    https://github.com/hubmapconsortium/search-api/blob/test-release/src/search-schema/data/definitions/enums/organ_types.yaml
    '''
   
    logging.info('Organ is ' + organ )
    organs = {}
    organs['SI'] = 'UBERON:0002108' #small intestine
    organs['LI'] = 'UBERON:0000059' #large intestine
    organs['LK'] = 'UBERON:0004538' #left kidney
    organs['RK'] = 'UBERON:0004539' #right kidney
    organs['SP'] = 'UBERON:0002106' #spleen

    return organs[organ]

def _build_dataframe( organ_shortcode, organ_id ):
    '''
    Build a dataframe with minimal information for this entity.
    '''

    id_namespace = 'tag:hubmapconsortium.org,2021:'
    headers = ['id', 'name', 'description']
    df = pd.DataFrame(columns=headers)
    df = df.append({'id':__get_organ_from_uberon(organ_shortcode), \
           'name':organ_id, \
           'description':__get_name(organ_shortcode)}, ignore_index=True)

    return df

def create_manifest( organ_shortcode, organ_id ):
    filename = 'anatomy.tsv'
    df = _build_dataframe( organ_shortcode, organ_id )
    df.to_csv( filename, sep="\t", index=False)

    return True
