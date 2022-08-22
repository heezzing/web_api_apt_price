from pymongo import MongoClient


URI = f'mongodb+srv://heezzing:djaakdi2382!@cluster0.fuvxy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

client = MongoClient(URI)

print(client)

DATABASE = 'myFirstDatabase'

db = client[DATABASE]

coll = db['APT']

import json

with open('apt_data.json') as f :
    coll.insert_many(json.load(f))
