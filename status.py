#!/hive/packages/anaconda/Anaconda3-2019.10/bin/python3

import pandas as pd
from itertools import chain
from pathlib import Path
import sys
from tabulate import tabulate

def main( metadata_file ):
    datasets = pd.read_csv( metadata_file )

    table = []
    headers=['HuBMAP ID','Data Directory', 'Status']

    for dataset in datasets.iterrows():
        dataset = dataset[1]
        hubmap_id = dataset['dataset_uuid']
        data_directory = dataset['full_path']
        computing = data_directory.replace('/','_').replace(' ','_') + '.computing'
        done = data_directory.replace('/','_').replace(' ','_') + '.done'

        if Path( computing ).exists():
            status = 'COMPUTING'
        elif Path( done ).exists():
            status = 'DONE'
        else:
            status = ''

        table.append([str(hubmap_id), data_directory[0:25]+'...', status])

    print( metadata_file + '\n' )
    print( tabulate(table, headers) )
    print( '\n' )

if __name__ == "__main__":
    metadata_file = sys.argv[1]
    main( metadata_file )
