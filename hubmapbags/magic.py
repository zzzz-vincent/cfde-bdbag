import pandas as pd
from pathlib import Path
from shutil import rmtree
from shutil import move

from . import biosamples, projects, collections, files

def do_it( data_provider, metadata_file ):
    datasets = pd.read_csv( metadata_file )

    for dataset in datasets.iterrows():
        dataset = dataset[1]
        status = dataset['m.status'].lower()
        assay_type = dataset['m.data_types'].replace('[','').replace(']','').replace('\'','').lower()
        hubmap_id = dataset['hubmap_id']
        data_directory = dataset['m.local_directory_url_path']

        output_directory = assay_type + '-' + status + '-' + dataset['e.uuid']
        p = Path( output_directory )

        if p.exists() and p.is_dir():
            print('Removing existing folder ' + output_directory)
            rmtree(p)
            print('Creating folder ' + output_directory)
            p.mkdir(parents=True, exist_ok=True)
        else:
            print('Creating folder ' + output_directory)
            p.mkdir(parents=True, exist_ok=True)

        biosamples.create_manifest()
        move( 'biosample.tsv', output_directory)
        projects.create_manifest( data_provider )
        move( 'project.tsv', output_directory)
        collections.create_manifest( hubmap_id )
        move( 'collection.tsv', output_directory)
        files.create_manifest( data_provider, data_directory )
        move( 'file.tsv', output_directory)

    return True
