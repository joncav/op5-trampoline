#! /usr/bin/python
# Writen for python 2.7
# This script is written to bulk delete hosts from op5

import json
import requests

url = "https://your-op5.com/api"
user = "user"
pass = "pass"
data = []
with open("addParents.json") as importFile:
    for line in importFile:
        data = json.loads(line)
        parentOnly = '{"parents":"' + data['parents'] + '"}'
        r = requests.patch(url + '/config/host/' + data['host_name'] , data=parentOnly, verify=False, auth=(user, pass), headers={'content-type': 'application/json'})
        print r.text