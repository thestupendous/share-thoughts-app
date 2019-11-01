from pymongo import MongoClient
client = MongoClient('192.168.99.100:31001')
print('connected',client)
dbs = client.newdb
coll = dbs.newcoll

coll.insert_one({"a":"b"})
p = coll.find()
print('find ',p)
for i in p:
    print(i)