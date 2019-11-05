import os
#from pymongo import MongoClient
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
#mongo_host = os.environ.get('MONGOHOST','localhost')
#client = MongoClient(mongo_host,'27017')

app = Flask(__name__)
@app.route('/',methods=['GET','POST','PUT','PATCH','DELETE'])
def delete_route():
    print("entered")
    #authenticate
    #load feed
    print("\n\n*****\n\n")
    a=request
    a = request.files
    print('p')
    print("**json",request.json,'\n\n')
    print('printing [',a,']****\n',sep='')

@app.route('/feed/post',methods=['GET','POST'])
def post_status(uid):
    uid = request.form['uid']
    status = request.form['status']
    #needs to have userId
    print('\n\n','uid and status ',uid,status,sep='  ',end='\n\n')
    return redirect('/feed')

    # -- make db call to update posts collection to add new entry for 
    #    corresponding uid and suitable post

@app.route('/feed',methods=['GET','POST'])
def base(uid=None):
    # expecting userid as post request
    client = MongoClient('localhost:27017')
    data = []
    dbs = client.share ; col = dbs.posts
    for rows in col.find():
       data.append(rows)
       #print('',data,'',sep='\n\n')
    return render_template('feed.html',feed_data=data,uid=uid)

if __name__ == '__main__':
    app.run(debug=True,port='5010')
  