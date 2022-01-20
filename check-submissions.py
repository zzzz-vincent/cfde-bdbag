import os
import subprocess
import unittest
import os
from argparse import ArgumentParser
from tabulate import tabulate
from os import path

def _pretty_print( text ):
	table = [[text]]
	output = tabulate(table, tablefmt='grid')
	print(output)

def _get_number_of_files( directory ):
	return len([name for name in os.listdir( directory ) if os.path.isfile(os.path.join( directory, name))])

def _count_number_of_lines( filename ):
	'''
	Helper function that calculates the number of lines in a file.
	'''

	answer = sum(1 for line in open(filename))
	return answer

def _count_number_of_project( directory ):
	'''
	Helper function that counts the number of collections in all collection related manifests and returns true if they match.
	'''

	data = {}
	data['file.tsv']=_count_number_of_lines( directory + 'file.tsv')
	data['file_describes_biosample.tsv']=_count_number_of_lines( directory + 'file_describes_biosample.tsv')
	data['file_describes_subject.tsv']=_count_number_of_lines( directory + 'file_describes_subject.tsv')
	data['file_in_collection.tsv']=_count_number_of_lines( directory + 'file_in_collection.tsv')

	expected_value = next(iter(data.values()))
	answer = all(value == expected_value for value in data.values())
	return answer

def _count_number_of_files( directory ):
	'''
	Helper function that counts the number of collections in all collection related manifests and returns true if they match.
	'''

	data = {}
	data['file.tsv']=_count_number_of_lines( directory + 'file.tsv')
	data['file_describes_biosample.tsv']=_count_number_of_lines( directory + 'file_describes_biosample.tsv')
	data['file_describes_subject.tsv']=_count_number_of_lines( directory + 'file_describes_subject.tsv')
	data['file_in_collection.tsv']=_count_number_of_lines( directory + 'file_in_collection.tsv')

	expected_value = next(iter(data.values()))
	answer = all(value == expected_value for value in data.values())
	return answer

def _count_number_of_collections( directory ):
	'''
	Helper function that counts the number of collections in all collection related manifests and returns true if they match.
	'''

	data = {}
	data['biosample_in_collection.tsv']=_count_number_of_lines( directory + 'biosample_in_collection.tsv')
	data['subject_in_collection.tsv']=_count_number_of_lines( directory + 'subject_in_collection.tsv')
	data['collection.tsv']=_count_number_of_lines( directory + 'collection.tsv')
	data['collection_defined_by_project.tsv']=_count_number_of_lines( directory + 'collection_defined_by_project.tsv')

	expected_value = next(iter(data.values()))
	answer = all(value == expected_value for value in data.values())
	return answer

def _pretty_print_number_of_files( directory ):
	'''
	'''
	table = [['file_describes_biosample.tsv',_count_number_of_lines( directory + 'file_describes_biosample.tsv')],['file_in_collection.tsv',_count_number_of_lines( directory + 'file_in_collection.tsv')],['file_describes_subject.tsv',_count_number_of_lines( directory + 'file_describes_subject.tsv')],['file.tsv',_count_number_of_lines( directory + 'file.tsv')]]
	output = tabulate(table, tablefmt='grid')
	print(output + '\n')

def _pretty_print_number_of_collections( directory ):
	'''
	'''
	table = [['biosample_in_collection.tsv',_count_number_of_lines( directory + 'biosample_in_collection.tsv')],['subject_in_collection.tsv',_count_number_of_lines( directory + 'subject_in_collection.tsv')],['collection.tsv',_count_number_of_lines( directory + 'collection.tsv')],['collection_defined_by_project.tsv',_count_number_of_lines( directory + 'collection_defined_by_project.tsv')]]
	output = tabulate(table, tablefmt='grid')
	print(output + '\n')

parser = ArgumentParser()
parser.add_argument( '-d', '--directory', dest='directory', default=None, help='Directory')
parser.add_argument( '--debug', dest='debug', default=False, help='Debug')
results = parser.parse_args()
directory = results.directory
debug = results.debug

if _count_number_of_files( directory ):
	_pretty_print('Valid submission')
	print('The number of files is the same in each manifest')
	_pretty_print_number_of_files( directory )
else:
	_pretty_print('Invalid submission')
	print('The number of files is different in each manifest')
	_pretty_print_number_of_files( directory )

if _count_number_of_collections( directory ):
	print('The number of collections is the same in each manifest')
	_pretty_print_number_of_collections( directory )
else:
	print('The number of collections is different in each manifest')
	_pretty_print_number_of_collections( directory )

if _get_number_of_files( directory ) != 23:
	print('Expected number of files is 23. Number of files found is ' + str(_get_number_of_files( directory )) + '.\n')

	if not path.isfile( directory + 'C2M2_datapackage.json' ):
		print('File ' + str(directory) + 'C2M2_datapackage.json was expected to exist, and it does not.\n')
