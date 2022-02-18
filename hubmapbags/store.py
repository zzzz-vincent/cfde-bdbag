# decouple to seperate file
import pickle
import sqlite3
from datetime import datetime
from pathlib import Path


def get_uuid():
    return ""


def store(tempfile):
    # check env has token

    # build SQLlite DB
    db_name = datetime.now().strftime("%Y%m%d%H%M") + ".db"

    # check if local db exist
    if Path(db_name).exists():
        print('local db: ' + db_name + " exist, skip computing")
        return

    # build local db
    connection = sqlite3.connect(db_name + '.db')
    cursor = connection.cursor()
    print('local db: ' + db_name + " connected")

    # check if same rule apply for entries
    # avoid adding record if exist, skip if found
    cursor.execute('''CREATE TABLE IF NOT EXISTS hubmap
                   (uuid text,
                   id_namespace text,
                   local_id text,
                   project_id_namespace text,
                   project_local_id text,
                   persistent_id text,
                   creation_time text,
                   size_in_bytes text,
                   uncompressed_size_in_bytes text,
                   sha256 text,
                   md5 text,
                   filename text,
                   file_format text,
                   data_type text,
                   assay_type text,
                   mime_type text,
                   bundle_collection_id_namespace text,
                   bundle_collection_local_id text,
                   compression_format text)''')

    # read pickle

    with (open(tempfile, "rb")) as openfile:
        while True:
            try:
                pickle_load = pickle.load(openfile)
                for row in pickle_load.interrows():
                    uuid = get_uuid()
                    sql = ''' INSERT INTO hubmap(uuid,id_namespace,local_id,project_id_namespace,project_local_id,persistent_id,creation_time,size_in_bytes,uncompressed_size_in_bytes,sha256,md5, filename, file_format, data_type, assay_type, mime_type, bundle_collection_id_namespace, bundle_collection_local_id, compression_format)
		VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''
                    cursor.execute(sql, row)
            except EOFError:
                break

    # DB closed
    connection.commit()
    connection.close()


def add_record(conn, record):
    """
	Create a new record
	:param conn:
	:param task:
 	:return:
 	"""

    sql = ''' INSERT INTO data(date,UUID,full_path,file,file_size,MD5sum,MD5sum_running_time,SHA256sum,SHA256sum_running_time,XXH128sum,XXH128sum_running_time)
		VALUES(?,?,?,?,?,?,?,?,?,?,?) '''
    cursor = conn.cursor()
    cursor.execute(sql, record)
    conn.commit()

    return cursor.lastrowid
