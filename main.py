import requests
import json
import time

url = 'https://tapi.bale.ai/'

#

fake_update = ""

headers = {
    'Content-Type': 'application/json'
}

r = requests.post(url, headers=headers, data=json.dumps(fake_update))
rs = requests.post(url)
print("Status:", rs.status_code)
print("Response:", rs.text)
