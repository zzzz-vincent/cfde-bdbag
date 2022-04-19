import pandas as pd
from pathlib import Path
from shutil import rmtree
from shutil import move
from os import remove
import logging
import glob
import os.path
import shutil
from os import listdir
from os.path import isfile, join, exists

from . import collection_anatomy, collection_compound, \
              biosample_substance, biosample_gene, assay_type, \
              biosample_disease, anatomy, \
              file_describes_collection, project_in_project, \
              file_describes_biosample, file_describes_subject, \
              biosample_from_subject, subject, \
              subject_in_collection, ncbi_taxonomy, \
              id_namespace, biosample_in_collection, \
              file_in_collection, primary_dcc_contact, \
              biosample, projects, \
              collection, anatomy, \
              file as files, collection_defined_by_project, \
              collection_disease, collection_gene, \
              collection_phenotype, collection_protein, \
              collection_substance, collection_taxonomy, \
              collection_in_collection, subject_disease, \
              subject_phenotype, subject_race, \
              subject_role_taxonomy, subject_substance, \
              file_format

def __get_number_of_files( output_directory ):
    return len([name for name in os.listdir( output_directory ) if os.path.isfile( os.path.join( output_directory, name ))])

def do_it( metadata_file, dbgap_study_id='' ):
    datasets = pd.read_csv( metadata_file, sep='\t' )
    print( 'Number of datasets found is ' + str(datasets.shape[0]) )

    for dataset in datasets.iterrows():
        dataset = dataset[1]
        status = dataset['ds.status'].lower()
        data_type = dataset['ds.data_types'].replace('[','').replace(']','').replace('\'','').lower()
        data_provider = dataset['ds.group_name']
        hubmap_id = dataset['ds.hubmap_id']
        biosample_id = dataset['first_sample_id']
        data_directory = dataset['full_path']
        print('Preparing bag for dataset ' + data_directory )
        computing = data_directory.replace('/','_').replace(' ','_') + '.computing'
        done = '.' + data_directory.replace('/','_').replace(' ','_') + '.done'
        broken = '.' + data_directory.replace('/','_').replace(' ','_') + '.broken'
        organ_shortcode = dataset['organ_type']
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

            output_directory = data_type + '-' + status + '-' + dataset['dataset_uuid']
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
            biosample.create_manifest( biosample_id, data_provider, organ_shortcode, output_directory )

            print('Making file.tsv')
            answer = files.create_manifest( data_provider, data_type, dbgap_study_id, data_directory, output_directory )

            print('Making biosample_in_collection.tsv')
            biosample_in_collection.create_manifest( biosample_id, hubmap_id, output_directory )

            print('Making project.tsv')
            projects.create_manifest( data_provider, output_directory )

            print('Making project_in_project.tsv')
            project_in_project.create_manifest( data_provider, output_directory )

            print('Making biosample_from_subject.tsv')
            biosample_from_subject.create_manifest( biosample_id, donor_id, output_directory )

            print('Making ncbi_taxonomy.tsv')
            ncbi_taxonomy.create_manifest( output_directory )

            print('Making collection.tsv')
            collection.create_manifest( hubmap_id, output_directory )

            print('Making collection_defined_by_project.tsv')
            collection_defined_by_project.create_manifest( hubmap_id, data_provider, output_directory )

            print('Making file_describes_collection.tsv')
            file_describes_collection.create_manifest( hubmap_id, data_directory, output_directory )

            print('Making dcc.tsv')
            primary_dcc_contact.create_manifest( output_directory )        

            print('Making id_namespace.tsv')
            id_namespace.create_manifest( output_directory )

            print('Making subject.tsv')
            subject.create_manifest( data_provider, donor_id, output_directory )

            print('Making subject_in_collection.tsv')
            subject_in_collection.create_manifest( donor_id, hubmap_id, output_directory )

            print('Making file_in_collection.tsv')
            answer = file_in_collection.create_manifest( hubmap_id, data_directory, output_directory )

            print('Creating empty files')
            file_describes_subject.create_manifest( output_directory )
            file_describes_biosample.create_manifest( output_directory )
            anatomy.create_manifest( output_directory )
            assay_type.create_manifest( output_directory )
            biosample_disease.create_manifest( output_directory )
            biosample_gene.create_manifest( output_directory )
            biosample_substance.create_manifest( output_directory )
            collection_anatomy.create_manifest( output_directory )
            collection_compound.create_manifest( output_directory )
            collection_disease.create_manifest( output_directory )
            collection_gene.create_manifest( output_directory )
            collection_in_collection.create_manifest( output_directory )
            collection_phenotype.create_manifest( output_directory )
            collection_protein.create_manifest( output_directory )
            collection_substance.create_manifest( output_directory )
            collection_taxonomy.create_manifest( output_directory )
            assay_type.create_manifest( output_directory )
            file_format.create_manifest( output_directory )
            ncbi_taxonomy.create_manifest( output_directory )
            subject_disease.create_manifest( output_directory )
            subject_phenotype.create_manifest( output_directory )
            subject_race.create_manifest( output_directory )
            subject_role_taxonomy.create_manifest( output_directory )
            subject_substance.create_manifest( output_directory )
            file_format.create_manifest( output_directory )

            print('Removing checkpoint ' + computing )
            remove(computing)

            # Copy empty files
            empty_files = 'empty'
            efiles = [f for f in listdir(empty_files) if isfile(join(empty_files, f))]

            for file in efiles:
                if not exists(join(output_directory,file)):
                    shutil.copy(join(empty_files,file), output_directory)

            print('Creating final checkpoint ' + done )
            if __get_number_of_files( output_directory ):
                with open(done, 'w') as file:
                   pass
            else:
                print('Wrong number of output files. Labelling dataset as broken.')
                with open(broken, 'w') as file:
                   pass

    return True
