import requests
import json

#Set common config in one place
host = "https://your-op5.com/api"
user = "user"
password = "pass"

#To set the number of hosts to add before saving the config
save_limit = 5

#set number of hosts you want to create
create_hosts_num = 150

def checkHostCount ():
    global host_count
    #the save variable is to know when we have saved because if we never reach the save_limit we need to save early (not done yet)
    global save
    #be sure the host_count variable is set, and reduce it so we know when we have reached zero and should save
    try:
        host_count
    except NameError:
        host_count = 0
        save = 0
    if save_limit - host_count == 0:
        save = 1
        host_count = 0
    return;

for x in range(0, create_hosts_num):
    #controlling the save based on count so that we can pause before things break (not done yet)
    checkHostCount()
    host_count = host_count + 1

    #increment the host count
    next_host = "test_host_" + str(x)

    #set the data for adding hosts and make the request
    data = {
        "file_id": "etc/hosts.cfg",
        "host_name": next_host,
        "max_check_attempts": "5",
        "notification_interval": "20",
        "notification_options": "10",
        "notification_period": "24x7",
        "template": "default-host-template"
    }
    r = requests.post('https://' + host + '/api/config/host', data=json.dumps(data),
                      auth=(user, password), headers={'content-type': 'application/json'}, verify=False)

    #print request output so we know about any problems
    print(r.url)
    print(r.text)
    print (r)