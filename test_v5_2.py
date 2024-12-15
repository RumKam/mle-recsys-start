import requests

events_store_url = "http://127.0.0.1:8020"
recommendations_url = "http://127.0.0.1:8000"

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
params = {"user_id": 1291248}

resp = requests.post(events_store_url + "/get", headers=headers, params=params)
if resp.status_code == 200:
    result = resp.json()
else:
    result = None
    print(f"status code: {resp.status_code}")
    
print(result)

resp = requests.post(events_store_url + "/get", 
                     headers=headers, 
                     params={"user_id": 1291248, "k": 3})
print(resp.json()) 

