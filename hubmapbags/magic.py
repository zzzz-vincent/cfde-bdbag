import pandas as pd
from pathlib import Path
from shutil import rmtree
from shutil import move

from . import idnamespace, primary_dcc_contact, biosamples, projects, collections, anatomy, files, biosample_from_subject

def do_it( data_provider, metadata_file ):
    datasets = pd.read_csv( metadata_file )

    for dataset in datasets.iterrows():
        dataset = dataset[1]
        status = dataset['dset_meta.status'].lower()
        assay_type = dataset['dset_meta.data_types'].replace('[','').replace(']','').replace('\'','').lower()
        hubmap_id = dataset['hubmap_id']
        biosample_id = dataset['first_sample_id']
        data_directory = dataset['full_path']
        organ_shortcode = dataset['organ']
        organ_id = dataset['organ_id']

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

        print('Creating biosample.tsv')
        biosamples.create_manifest( biosample_id, data_provider, organ_shortcode )
        move( 'biosample.tsv', output_directory )

        print('Creating project.tsv')
        projects.create_manifest( data_provider )
        move( 'project.tsv', output_directory )

        print('Creating collection.tsv')
        collections.create_manifest( hubmap_id )
        move( 'collection.tsv', output_directory )

        print('Creating anatomy.tsv')
        anatomy.create_manifest( organ_shortcode, organ_id )
        move( 'anatomy.tsv', output_directory )

        print('Creating primary_dcc_contact.tsv')
        primary_dcc_contact.create_manifest( data_provider )
        move( 'primary_dcc_contact.tsv', output_directory )

        print('Creating biosample_from_subject.tsv')
        biosample_from_subject.create_manifest( data_provider )
        move( 'biosample_from_subject.tsv', output_directory )

        print('Creating id_namespace.tsv')
        idnamespace.create_manifest()
        move( 'id_namespace.tsv', output_directory )

        print('Creating file.tsv')
        answer = files.create_manifest( data_provider, assay_type, data_directory )
        if answer:
            move( 'file.tsv', output_directory )

    return True
