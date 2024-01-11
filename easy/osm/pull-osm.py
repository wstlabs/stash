import csv
import sys
import simplejson as json
import requests

url = 'https://photon.komoot.io/api/?q=1000+5th+Avenue,New+York,NY'
headerdict = {'Accept': 'application/json'}

resp = requests.get(url)
print("status = ", resp.status_code)
print(resp.headers)
if resp.status_code != 200:
    print(resp.text)
    sys.exit(1)

data = resp.json()
print("type = ", type(data))
print(list(data.keys()))
print(json.dumps(data, indent=4))

