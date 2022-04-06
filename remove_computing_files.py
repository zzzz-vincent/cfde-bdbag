import pandas as pd
from pathlib import Path
import sys

def main( metadata_file ):
    datasets = pd.read_csv( metadata_file )

    for dataset in datasets.iterrows():
        dataset = dataset[1]
        data_directory = dataset['full_path']
        computing = data_directory.replace('/','_').replace(' ','_') + '.computing'
        done = data_directory.replace('/','_').replace(' ','_') + '.done'
        if Path( computing ).is_file():
            print( 'Removing file ' + computing )
            Path( computing ).unlink()

if __name__ == "__main__":
    metadata_file = sys.argv[1]
    main( metadata_file )
