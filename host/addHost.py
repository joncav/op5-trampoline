#! /usr/bin/python
#Writen for python 2.7
#This script is used for adding hosts, through line seperated json of host paramaters

import json
import requests


url = "https://your-op5.com/api"
user = "user"
pass = "pass"
data = []
with open("addHost.json") as importFile:
   for line in importFile:
       data.append(json.loads(line))
       r = requests.post(url + '/config/host/', data=line, verify=False, auth=(user, pass), headers={'content-type': 'application/json'})
       print r.request
       print r.text
       if 'str' in line:
          break

