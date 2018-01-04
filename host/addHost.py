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
