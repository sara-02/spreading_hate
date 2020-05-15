# requirements
flask, networkx, ndblib
# Running the API
`python3 api.py`
```python
import requests
json_={}
json_["infected_node"]=["94152234"] # put a different user_id here
print(json.dumps(json_))
r = requests.post(url="http://localhost:8091/api/predict_single_iter", data=json.dumps(json_),  headers={'Content-Type': 'application/json', 'Accept': 'application/json'})
print(r.text)
```