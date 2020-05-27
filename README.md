# requirements
flask, networkx, ndblib
# Running the API
`python3 api.py`
```python
import requests
json_={}
json_["infected_nodes"]=["94152234"] # put a different user_id here
json_["max_iter"]=9
print(json.dumps(json_))
r = requests.post(url="http://localhost:8091/api/infect_predict", data=json.dumps(json_),  headers={'Content-Type': 'application/json', 'Accept': 'application/json'})
print(r.text)
```
