import requests
import json

URL = "https://www.submarinecablemap.com/api/v3/cable/2africa.json"
resp = requests.get(URL)
data = resp.json()

print(json.dumps(data.get("landing_points", []), indent=2))
