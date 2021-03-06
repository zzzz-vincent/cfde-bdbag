import sys
import pandas
import os
import json
import time
import requests
from argparse import ArgumentParser

def generate( file, debug=True ):
	'''
	Main function that generates UUIDs using the uuid-api.
	'''

	if debug:
		print('Processing ' + file + '.')

	# icaoberg since neither the hubmap id nor the uuid are save in the dataframe
	# extract it from the filename
	duuid=file.split('_')[-1].split('.')[0]

	TOKEN = os.getenv('TOKEN')
	if not TOKEN:
		if debug:
			print('TOKEN not set. Exiting script.')
		return False

	try:
		df = pandas.read_pickle( file )
	except:
		if debug:
			print('Unable to load pickle file ' + file + '. Exiting script.' )
		return False

	# Making a POST requesit¬
	URL='https://uuid-api.dev.hubmapconsortium.org/hmuuid/'
	headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0','Authorization':'Bearer '+TOKEN, 'Content-Type':'application/json'}

	if len(df) <= 1000:
		if df['hubmap_uuid'].isnull().all():
			file_info = []
			for datum in df.iterrows():
				datum = datum[1]
				filename = datum['local_id'][datum['local_id'].find(duuid)+len(duuid)+1:]
				file_info.append({'path':filename, \
					'size':datum['size_in_bytes'], \
					'checksum':datum['sha256'], \
				'base_dir':'DATA_UPLOAD'})

			payload = {}
			payload['parent_ids']=[duuid]
			payload['entity_type']='FILE'
			payload['file_info']=file_info
			params = {'entity_count':len(file_info)}

			r = requests.post(URL, params=params, headers=headers, data=json.dumps(payload), allow_redirects=True, timeout=120)
			j = json.loads(r.text)

			if 'message' in j:
				if debug:
					print('Request response. Not populating data frame and exiting script.')
				print(j['message'])
			return False
			else:
				for datum in j:
					df.loc[df['local_id'].str.contains(datum['file_path']),'hubmap_uuid']=datum['uuid']
  
				if debug:
					print('Updating pickle file ' + file + ' with the request response.')

				df.to_pickle(file)
				with open(file.replace('pkl','json'),'w') as outfile:
					json.dump(j, outfile, indent=4)
		else:
			if debug:
				print('HuBMAP uuid column is populated. Skipping generation.')
	else:
		if debug:
			print('Data frame has ' + str(len(df)) + ' items. Partitioning into smaller chunks.')

		n = 1000  #chunk row size
		dfs = [df[i:i+n] for i in range(0,df.shape[0],n)]
	
		counter = 0
		for frame in dfs:
			counter=counter+1
			if debug:
				print('Computing uuids on partition ' + str(counter) + ' of ' + str(len(dfs)) + '.')

			file_info = []
			for datum in frame.iterrows():
				datum = datum[1]
				filename = datum['local_id'][datum['local_id'].find(duuid)+len(duuid)+1:]
				file_info.append({'path':filename, \
					'size':datum['size_in_bytes'], \
					'checksum':datum['sha256'], \
				'base_dir':'DATA_UPLOAD'})

			payload = {}
			payload['parent_ids']=[duuid]
			payload['entity_type']='FILE'
			payload['file_info']=file_info
			params = {'entity_count':len(file_info)}

			if frame['hubmap_uuid'].isnull().all():
				if debug:
					print('Generating uuids')

				r = requests.post(URL, params=params, headers=headers, data=json.dumps(payload), allow_redirects=True, timeout=120)
				j = json.loads(r.text)
				time.sleep(5)

				if 'message' in j:
					if debug:
						print('Request response. Not populating data frame.')
					print(j['message'])
					return False
				else:
					for datum in j:
						df.loc[df['local_id'].str.contains(datum['file_path']),'hubmap_uuid']=datum['uuid']

					if debug:
						print('Updating pickle file ' + file + ' with the results of this chunk.')
					df.to_pickle(file)
			else:
				if debug:
					print('HuBMAP uuid chunk is populated. Skipping recomputation.')
