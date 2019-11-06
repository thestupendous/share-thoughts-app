from pymongo import MongoClient

conn = MongoClient('localhost:27017')

a=conn['share']['auths'].find()

for i in a:
    print(i['data']['uid'])
a=conn['share']['auths'].find()

x = list(a)
print(x)
for i in x[0].keys():
    print(i,x[0][i],sep='  -> ')
print(x[0]['data']['uid'])
print(type(x[0]['_id']))