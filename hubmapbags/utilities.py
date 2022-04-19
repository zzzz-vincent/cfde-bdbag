import sys
import pandas

def add_empty_duuid_column( file ):
	duuid=file.split('_')[-1].split('.')[0]
	print(file)

	df = pandas.read_pickle( file )
	df['duuid']=duuid
	df.to_pickle(file)

def add_empty_dbgap_study_id_column( file ):
	duuid=file.split('_')[-1].split('.')[0]
	print(file)

	df = pandas.read_pickle( file )
	df['dbgap_study_id']=None
	df.to_pickle(file)

