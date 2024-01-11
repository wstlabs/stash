import csv
import sys
import simplejson as json
import requests

url = 'https://api.yelp.com/v3/businesses/search?sort_by=best_match&latitude=40.735556&longitude=-73.990556&limit=20' 
token = 'blahblah'
headerdict = {'Authorization': f"Bearer {token}",  'Accept': 'application/json'}

resp = requests.get(url, headers=headerdict)
print("status = ", resp.status_code)
print(resp.headers)
if resp.status_code != 200:
    print(resp.text)
    sys.exit(1)

data = resp.json()
print("type = ", type(data))
print(list(data.keys()))
# print(json.dumps(data, indent=4))
businesses = data['businesses']

def save_records(filename, reclist):
    header = ['id', 'alias', 'name', 'review_count', 'rating', 'phone']
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for r in reclist:
            values = [r[k] for k in header]
            writer.writerow(values)

save_records("output.csv", businesses)

