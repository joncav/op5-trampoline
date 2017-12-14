#! /usr/bin/python
# Writen for python 2.7
# This script is written to bulk delete hosts from op5

import json
import requests
import logging
import urllib

url = "https://your-op5.com/api"
user = ""
password = ""
data = []
with open("delhost.json") as importFile:
    for line in importFile:
        # data.append(json.loads(line))
        data.append(line)
        #print(line)
        hosts = urllib.quote_plus(line.rstrip('\n'))
        #print(hosts)
        r = requests.delete(url + '/config/host/' + hosts.__str__(), verify=False, auth=(user, password))
        print r.text
        print r.url
        print r.request
        if 'str' in line:
            break
