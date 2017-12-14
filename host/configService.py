#! /usr/bin/python
# Writen for python 2.7
# This script is written to bulk delete hosts from op5

import json
import requests

#Update with your OP5 Monitor hostname or IP, and credentials with API access
url = "https://your-op5.com/api"
user = "user"
password = "pass"
data = []
with open("configServiceItem.json") as importFile:
    for line in importFile:
        data = json.loads(line)
        #Update config items below with the specific data for the patch
        configItem = '{"servicegroups":"' + data['servicegroups'] + '"}'
        r = requests.patch(url + '/config/service/' + data['host_name'] + ';' + data['service_description'] , data=configItem, verify=False, auth=(user, password), headers={'content-type': 'application/json'})
        #For troubleshooting uncomment below to see the changes you're submitting
        #print r.url
        #print r.request
        #Uncomment the below line if you want to also save changes within config during process
        #requests.get(url + '/api/config/change/', verify=False, auth=(user, password), headers={'content-type': 'application/json'})