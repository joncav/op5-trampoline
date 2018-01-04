#! /usr/bin/python
#Writen for python 2.7
#This script is used for adding hosts, through line seperated json of host paramaters

import json
import requests
import logging

url = "https://your-op5.com/api"
user = "user"
password = "pass"
save_check = 0

logging.basicConfig(filename="requests.log", level=logging.INFO)
logger = logging.getLogger('jsonrequests')

data = []
with open("addHost.json") as importFile:
    for line in importFile:
        data.append(json.loads(line))
        print(i['file_id'])
        break
        #r = requests.post(url + '/config/host/', data=line, verify=False, auth=(user, password), headers={'content-type': 'application/json'})
        #logger.info('%s', r.headers)
        #logger.info('%s', r.request)
        #logger.info('%s', r.text)

        #if save_check < 10:
        #    save_check += 1
        #else:
        #    logger.info('%s', "Saved")
        #    r = requests.post(url + '/config/change', data=line, verify=False, auth=(user, password))
        #    save_check = 0

        #if 'str' in line:
        #    break
