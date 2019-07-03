import requests
import json


def create_index(index_name):
    r = requests.put(str("http://localhost:9200/" + index_name))
    return r.status_code, r.reason


# print(create_index("schools"))


def add_data_to_index(index, type, id, data):
    """
    :param index: string of existing index name
    :param type: type of data, it can be anything such as chair, ball, school,...
    :param id: id of data, it must be unique

    :param data: json of data
    for example: {"name":"some name", "description":"some description", "tags":["Senior Secondary", "beautiful campus"]}
    :return: requests status code and reason for it
    """
    r = requests.post(str("http://localhost:9200/" + index + "/" + type + "/" + id), data=data)
    return r.status_code, r.reason


data = {"name": "Central School", "description": "CBSE Affiliation", "street": "Nagan",
        "city": "paprola", "state": "HP", "zip": "176115", "location": [31.8955385, 76.8380405],
        "fees": 2000, "tags": ["Senior Secondary", "beautiful campus"], "rating": "3.5"}
print(add_data_to_index("schools", "school", "1", json.dumps(data)))

# r = requests.post("http://localhost:9200/schools/school", data={'number': 12524, 'type': 'issue', 'action': 'show'})
# print(r.status_code, r.reason)
