import requests



r = requests.post("http://localhost:9200/schools/school", data={'number': 12524, 'type': 'issue', 'action': 'show'})
print(r.status_code, r.reason)
