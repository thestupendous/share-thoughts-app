from pymongo import MongoClient

cli = MongoClient('localhost:27017')
dbs = cli.share
coll = dbs.auths 


for i in coll.find({'username':'cloris'}):
    print (i)
#d = dict(coll.find({'username':'cloris'}))

#print(d)