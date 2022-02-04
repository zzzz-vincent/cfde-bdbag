import json
import logging

import requests
import pandas
from pandas import read_csv
from requests.auth import HTTPBasicAuth


def search_id(authorization):
    url = "https://entity.api.hubmapconsortium.org/entities/"
    token = "Ag7dvdyQGVWqzGMvD8kjDev85DDVWWen48JEe9yEW9zV5Gw3njFWC1nmO2ejY5rvEqoBoGOP1vVze6FzjD1n5FBVd8"
    authorization = "Bearer " + authorization
    my_headers = {
        "accept": "application/json",
        "Authorization": authorization
    }

    data = read_csv('hubmap_id.csv')
    row = data.iloc[:, 0]
    # single_test = "HBM358.KDDT.729"
    # response2 = requests.get(url + single_test, headers=my_headers)
    with open('entities_search_result.json', 'w') as json_file:
        for hubmap_id in row:
            print("processing "+ hubmap_id +"...")
            response = requests.get(url + hubmap_id, headers=my_headers)
            data_json = response.json()
            logging.info("result of " + hubmap_id + ":")
            logging.info(data_json)
            json_file.write("result of " + hubmap_id + ":")
            json.dump(data_json, json_file)
            json_file.write('\n')
        print("done ")


token = "Ag7dvdyQGVWqzGMvD8kjDev85DDVWWen48JEe9yEW9zV5Gw3njFWC1nmO2ejY5rvEqoBoGOP1vVze6FzjD1n5FBVd8"
search_id(token)
