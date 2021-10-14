import pandas as pd
from pathlib import Path
import sys

def main( metadata_file ):
    datasets = pd.read_csv( metadata_file )

    table = []
    headers=['HuBMAP ID','Data Directory', 'Status']

    for dataset in datasets.iterrows():
        dataset = dataset[1]
        computing = data_directory.replace('/','_').replace(' ','_') + '.computing'
        done = data_directory.replace('/','_').replace(' ','_') + '.done'
        if Path( computing ).is_file():
            print( 'Removing file ' + computing )
            Path.unlink( computing )

if __name__ == "__main__":
    metadata_file = sys.argv[1]
    main( metadata_file )
