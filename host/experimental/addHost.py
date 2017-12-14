#! /usr/bin/python
#Writen for python 2.7
#This script is used for adding hosts, through line seperated json of host paramaters

import json
import requests


url = "https://your-op5.com/api"
user = "user"
password = "pass"
data = []

host_count = 100
for i in range(host_count, 0, -1):
    with open("addHost.json") as importFile:
        for line in importFile:
            data.append(json.loads(line))
            r = requests.post(url + '/config/host/', data=line, verify=False, auth=(user, password),
                              headers={'content-type': 'application/json'})
    if i == 50:
        r = requests.get(url + '/config/change/', verify=False, auth=(user, password))
        elif i == host_count:
        print('Done adding hosts')
