import xmltodict
import json

o = xmltodict.parse('<e> <a>text</a> <a>text</a> </e>')
print(json.dumps(o))
