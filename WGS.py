#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from pathlib import Path
from shutil import rmtree

metadata_file = 'published-WGS-datasets-3-8-2021.csv'
datasets = pd.read_csv( metadata_file )

for dataset in datasets.iterrows():
    directory = dataset[1]['e.uuid']
    p = Path( directory )
    
    if p.exists() and p.is_dir():
        print('Removing existing folder ' + directory)
        rmtree(p)
        print('Creating folder' + directory)
        p.mkdir(parents=True, exist_ok=True)
    else:
        print('Creating folder' + directory)
        p.mkdir(parents=True, exist_ok=True)


# # Biosample

# In[ ]:


headers = ['id_namespace', 'local_id', 'project_id_namespace', 'project_local_id', 'persisten_id', 'creation_time', 'anatomy']

df = pd.DataFrame(columns=headers)

filename = 'biosample.tsv'
for dataset in datasets.iterrows():
    directory = dataset[1]['e.uuid']
    df.to_csv(directory+'/'+filename, sep="\t", index=False)


# # Project

# In[ ]:


id_namespace = 'HuBMAP'
local_id = 'University of Florida TMC'

headers = ['id_namespace', 'local_id', 'persistent_id', 'creation_time', 'abbreviation', 'name', 'description']
df = pd.DataFrame(columns=headers)
df = df.append({'id_namespace':id_namespace, 'local_id':local_id, 'name':local_id}, ignore_index=True)

filename = 'project.tsv'
for dataset in datasets.iterrows():
    directory = dataset[1]['e.uuid']
    df.to_csv(directory+'/'+filename, sep="\t", index=False)


# # Collections

# In[ ]:


id_namespace = 'HuBMAP'

headers = ['id_namespace', 'local_id', 'persistent_id', 'creation_time', 'abbreviation', 'name', 'description']
df = pd.DataFrame(columns=headers)

filename = 'collection.tsv'
for dataset in datasets.iterrows():
    directory = dataset[1]['e.uuid']
    local_id = dataset[1]['hubmap_id']
    name = dataset[1]['hubmap_id']
    
    df = pd.DataFrame(columns=headers)
    df = df.append({'id_namespace':id_namespace, 'local_id':local_id, 'name':local_id}, ignore_index=True)

    df.to_csv(directory+'/'+filename, sep="\t", index=False)


# # Files

# In[ ]:


id_namespace = 'HuBMAP'

headers = ['id_namespace', 'local_id', 'project_id', 'persisten_id', 'creation_time', 'size_in_bytes', 'uncompressed_size_in_bytes', 'sha256','md5','filename','file_format', 'data_type', 'assay_type','mime_type']
df = pd.DataFrame(columns=headers)

filename = 'file.tsv'
for dataset in datasets.iterrows():
    directory = dataset[1]['e.uuid']
    data_directory = Path(dataset[1]['m.local_directory_url_path'])
    
    if not data_directory.exists():
        print('Data directory does not exist')
        
    df.to_csv(directory+'/'+filename, sep="\t", index=False)


# In[ ]:




