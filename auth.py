import os
from pymongo import MongoClient
from flask import Flask, render_template, request, redirect
import requests
app = Flask(__name__)

ui_host = os.environ.get('UIHOST','localhost')
auth_host = os.environ.get('AUTHHOST','localhost')
feed_host = os.environ.get('FEEDHOST','localhost')
user_host = os.environ.get('USERHOST','localhost')
db_host = os.environ.get('DBHOST','localhost')


@app.route('/',methods=['GET','POST','PUT','PATCH','DELETE'])
def auth():
    print('inside auth/\n----> request ',request.json)
    user = request.json['username']
    password = request.json['password']
    cli = MongoClient('0.0.0.0:27017')
    dbs = cli.share
    coll = dbs.auths
    a = {'uid':'None'}
    for i in coll.find({'username':user}):
        if password == i['data']['password']:
            print("password matched")
            #return i['data']['uid']
            a={'uid':str(i['data']['uid'])}
            requests.post('http://0.0.0.0:5001/authres',json=a)
            a=str(a)
            return '%s'%a
    print('user not found')
    requests.post('http://0.0.0.0:5001/authfail',json=a)
    return 'incorrect password'


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port='5002')