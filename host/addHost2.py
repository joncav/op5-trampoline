#! /usr/bin/python
#Writen for python 2.7
#This script includes bypassing of the noisy ssl auth warning, and also single host addition in data variable
#Not completed yet

import json
import requests
import logging

try:
    import http.client as http_client
except ImportError:
    import httplib as http_client
http_client.HTTPConnection.debuglevel = 1

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

url = "https://your-op5.com/api"
user = "user"
password = "pass"
#with open('addHost2.json') as importFile:
#   for line in importFile
#       data = line

#      if 'str' in line:
#         break


data = {}

r = requests.post(url + '/config/host/', data=json.dumps(data), verify=False, auth=(user, password), headers={'content-type': 'application/json'})
print r.text
