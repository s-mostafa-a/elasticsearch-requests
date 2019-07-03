import xmltodict
import json
from json2table import convert as j2tconvert


def xml_to_json(string):
    o = xmltodict.parse(string)
    return json.dumps(o)


def json_to_table(json_obj):
    build_direction = "LEFT_TO_RIGHT"
    table_attributes = {"style": "width:100%"}
    html = j2tconvert(json_obj, build_direction=build_direction, table_attributes=table_attributes)
    print(html)


# print(xml_to_json('<e> <a>text</a> <a>text</a> </e>'))
print(json_to_table(
    {"menu": {
        "id": "file",
        "value": "File",
        "menuitem": [
            {"value": "New", "onclick": "CreateNewDoc()"},
            {"value": "Open", "onclick": "OpenDoc()"},
            {"value": "Close", "onclick": "CloseDoc()"}
        ]
    }
    }
))
