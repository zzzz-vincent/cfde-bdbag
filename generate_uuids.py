import sys
import pandas
import os
import json
import time
import requests

file = str(sys.argv[1])
print(file)

TOKEN = os.getenv('TOKEN')
duuid=file.split('_')[-1].split('.')[0]

if not TOKEN:
	print('TOKEN not set. Exiting script.')
	sys.exit()

df = pandas.read_pickle( file )

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
			print('Request response. Not populating data frame.')
			print(j['message'])
			sys.exit()
		else:
			for datum in j:
				df.loc[df['local_id'].str.contains(datum['file_path']),'hubmap_uuid']=datum['uuid']
  
			df.to_pickle(file)
			with open(file.replace('pkl','json'),'w') as outfile:
				json.dump(j, outfile, indent=4)
	else:
		print('HuBMAP uuid column is populated. Skipping generation.')
else:
	print('Data frame has ' + str(len(df)) + ' items. Partitioning into smaller chunks.')
	n = 1000  #chunk row size
	dfs = [df[i:i+n] for i in range(0,df.shape[0],n)]
	
	counter = 0
	for frame in dfs:
		counter=counter+1
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
			print('Generating uuids')
			r = requests.post(URL, params=params, headers=headers, data=json.dumps(payload), allow_redirects=True, timeout=120)
			j = json.loads(r.text)
			time.sleep(5)

			if 'message' in j:
				print('Request response. Not populating data frame.')
				print(j['message'])
				sys.exit()
			else:
				for datum in j:
					df.loc[df['local_id'].str.contains(datum['file_path']),'hubmap_uuid']=datum['uuid']

				print('Saving all results to disk.')
				df.to_pickle(file)
				with open(file.replace('pkl','json'),'w') as outfile:
					json.dump(j, outfile, indent=4)
		else:
			print('HuBMAP uuid chunk is populated. Skipping recomputation.')



