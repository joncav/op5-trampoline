#! /usr/bin/python
# Writen for python 2.7
#This file is used for making a single value change on a host in bulk
#In the modify_config.json enter list of hosts one per line

import json
import requests
import urllib

def betterLogging():
    return;

url = "https://your-op5.com/api"
user = ""
pass = ""

config_array = {"key":"value"}
data = []
with open("modify_config.json") as importFile:
    for line in importFile:
        data.append(line)
        hosts = urllib.quote_plus(line.rstrip('\n'))
        r = requests.patch(url + '/config/host/' + hosts.__str__(), data=json.dumps(config_array), verify=False, auth=(user, pass), headers={'content-type': 'application/json'})
        print r.request
        if 'str' in line:
            break

r = requests.get(url + '/config/change/', verify=False, auth=(user, pass))