#! /usr/bin/python
#Writen for python 2.7
#This script is used for adding hosts, through line seperated json of host paramaters

import json
import requests
import logging

url = "https://your-op5.com/api"
user = "user"
password = "pass"

log_format = '%(asctime)::%(messagae)s'
logging.basicConfig(format=log_format)
logger = logging.getLogger('jsonrequests')

data = []
with open("addHost.json") as importFile:
   for line in importFile:
       data.append(json.loads(line))
       r = requests.post(url + '/config/host/', data=line, verify=False, auth=(user, password), headers={'content-type': 'application/json'})
       logger.info('%s', r.request)
       logger.info('%s', r.text)
       #print r.request
       #print r.text
       if 'str' in line:
          break
