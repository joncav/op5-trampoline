import requests

#set common config in one place
hostname = "123.123.123.123"
username = "admin"
password = "password"
license_file = "license-name.lic"

#upload the license to the server
response = requests.put(
	'https://' + hostname + '/api/beta/license/data',
	auth=(username, password), verify=False,
	data=open(license_file, 'rb').read(),
	headers={
		'content-type': 'application/octet-stream',
		'accept': 'application/json'
	}
)
#message to know if we succeeded
print(response.text)