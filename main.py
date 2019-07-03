from elasticsearch import Elasticsearch


class IndexHandler:
    def __init__(self, elasticsearch, index_name):
        self.elasticsearch = elasticsearch
        self.index_name = index_name
        self.types = []

    def bulk_indexer(self, type_name, objs):
        typ = [element for element in self.types if element['type'] == type_name]
        if not typ:
            typ = {'type': type_name, 'last_added_object': -1}
            self.types.append(typ)
        for obj in objs:
            typ['last_added_object'] += 1
            res = es.index(index=self.index_name, doc_type=typ['type'], id=typ['last_added_object'], body=obj)
            if res['result'] != 'created':
                print("ERROR for object: ", obj)
                print(res['result'])

    def bulk_show(self, type_name, begin, end):
        typ = [element for element in self.types if element['type'] == type_name]
        if not typ:
            print("Type Name Does Not Exist")
            return
        for i in range(begin, end + 1):
            res = es.get(index=self.index_name, doc_type=type_name, id=i)
            print(res)


es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
e1 = {
    "first_name": "nitin",
    "last_name": "panwar",
    "age": 27,
    "about": "Love to play cricket",
    "interests": ['sports', 'music'],
}
e2 = {
    "first_name": "Jane",
    "last_name": "Smith",
    "age": 32,
    "about": "I like to collect rock albums",
    "interests": ["music"]
}
e3 = {
    "first_name": "Douglas",
    "last_name": "Fir",
    "age": 35,
    "about": "I like to build cabinets",
    "interests": ["forestry"]
}

ih = IndexHandler(es, 'table')
ih.bulk_indexer("employees", [e1, e2, e3])
ih.bulk_show("employees", 0, 2)
