import pandas as pd
from pathlib import Path
from shutil import rmtree
from shutil import move
from os import remove
import pickle
import sqlite3

from . import file_describes_biosample, file_describes_subject, biosample_from_subject, subject, subject_in_collection, ncbi_taxonomy, idnamespace, biosample_in_collection, files_in_collection, primarydcccontact, biosamples, projects, collections, anatomy, files, collection_defined_by_project

def do_it( metadata_file ):
    datasets = pd.read_csv( metadata_file )
    print( 'Number of datasets found is ' + str(datasets.shape[0]) )

    for dataset in datasets.iterrows():
        dataset = dataset[1]
        status = dataset['dset.status'].lower()
        assay_type = dataset['dset.data_types'].replace('[','').replace(']','').replace('\'','').lower()
        data_provider = dataset['ds.group_name']
        hubmap_id = dataset['hubmap_id']
        biosample_id = dataset['first_sample_id']
        data_directory = dataset['full_path']
        print('Preparing bag for dataset ' + data_directory )
        computing = data_directory.replace('/','_').replace(' ','_') + '.computing'
        done = data_directory.replace('/','_').replace(' ','_') + '.done'
        organ_shortcode = dataset['organ']
        organ_id = dataset['organ_id']
        donor_id = dataset['donor_id']

        if Path(done).exists():
            print('Checkpoint found. Avoiding computation. To re-compute erase file ' + done)
        elif Path(computing).exists():
            print('Checkpoint found. Avoiding computation since another process is building this bag.')
        else:
            with open(computing, 'w') as file:
                pass

            print('Creating checkpoint ' + computing)

            if status == 'new':
                print('Dataset is not published. Aborting computation.')

            output_directory = assay_type + '-' + status + '-' + dataset['dataset_uuid']
            p = Path( output_directory )

            if p.exists() and p.is_dir():
                print('Removing existing folder ' + output_directory)
                rmtree(p)
                print('Creating folder ' + output_directory)
                p.mkdir(parents=True, exist_ok=True)
            else:
                print('Creating folder ' + output_directory)
                p.mkdir(parents=True, exist_ok=True)

            print('Making biosample.tsv')
            biosamples.create_manifest( biosample_id, data_provider, organ_shortcode )
            move( 'biosample.tsv', output_directory )

            print('Making file.tsv')
            answer = files.create_manifest( data_provider, assay_type, data_directory )
            if answer:
                move( 'file.tsv', output_directory )

            print('Making biosample_in_collection.tsv')
            biosample_in_collection.create_manifest( biosample_id, hubmap_id )
            move( 'biosample_in_collection.tsv', output_directory )

            print('Making project.tsv')
            projects.create_manifest( data_provider )
            move( 'project.tsv', output_directory )

            print('Making biosample_from_subject.tsv')
            biosample_from_subject.create_manifest( biosample_id, donor_id )
            move( 'biosample_from_subject.tsv', output_directory )

            print('Making ncbi_taxonomy.tsv')
            ncbi_taxonomy.create_manifest()
            move( 'ncbi_taxonomy.tsv', output_directory )

            print('Making collection.tsv')
            collections.create_manifest( hubmap_id )
            move( 'collection.tsv', output_directory )

            print('Making collection_defined_by_project.tsv')
            collection_defined_by_project.create_manifest( hubmap_id, data_provider )
            move( 'collection_defined_by_project.tsv', output_directory )

            print('Making file_describes_subject.tsv')
            file_describes_subject.create_manifest( donor_id, data_directory )
            move( 'file_describes_subject.tsv', output_directory )

            print('Making dcc.tsv')
            primarydcccontact.create_manifest( data_provider )
            move( 'dcc.tsv', output_directory )

            print('Making id_namespace.tsv')
            idnamespace.create_manifest()
            move( 'id_namespace.tsv', output_directory )

            print('Making subject.tsv')
            subject.create_manifest( data_provider, donor_id )
            move( 'subject.tsv', output_directory )

            print('Making file_describes_biosample.tsv')
            file_describes_biosample.create_manifest( biosample_id, data_directory )
            move( 'file_describes_biosample.tsv', output_directory )

            print('Making subject_in_collection.tsv')
            subject_in_collection.create_manifest( donor_id, hubmap_id )
            move( 'subject_in_collection.tsv', output_directory )

            print('Making files_in_collection.tsv')
            answer = files_in_collection.create_manifest( hubmap_id, data_directory )
            move( 'file_in_collection.tsv', output_directory )

            print('Removing checkpoint ' + computing )
            remove(computing)

            print('Creating final checkpoint ' + done )
            with open(done, 'w') as file:
                pass

    return True
def store():
    # build SQLlite DB
    connection = sqlite3.connect('HubMAP.db')
    cursor = connection.cursor()

    # read pickle
    data = pickle.load("")

    # DB closed
    connection.commit()
    connection.close()
