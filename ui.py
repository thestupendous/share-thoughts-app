import os
from pymongo import MongoClient
from flask import Flask , render_template, redirect, request
import requests

ui_host = os.environ.get('UIHOST','localhost')
auth_host = os.environ.get('AUTHHOST','localhost')
feed_host = os.environ.get('FEEDHOST','localhost')
user_host = os.environ.get('USERHOST','localhost')
db_host = os.environ.get('DBHOST','localhost')

app = Flask(__name__)

@app.route('/auth',methods=['GET','POST','PUT','PATCH','DELETE'])
def auth1():
    
    return render_template('auth.html')
@app.route('/reqdata',methods=['GET','POST','PUT','PATCH','DELETE'])
def call_auth():
    auth_data = { "username":request.form['username'], "password":request.form['password']}
    uid = requests.post('http://0.0.0.0:5002',json=auth_data)
    print('*'*15, '[',uid,'*]','*'*15)
    return "you've been authenticated and reached UI page again."


@app.route('/authfail',methods=['GET','POST','PUT','PATCH','DELETE'])
def auth_fail_():
    print('auth failed')
    return "<h1> auth failed !!</h1>"

@app.route('/authres',methods=['GET','POST','PUT','PATCH','DELETE'])
def auth_success():
    print('returned with success')


@app.route('/feed',methods=['GET','POST','PUT','PATCH','DELETE'])
def feeds():
    return "<h1>***here goes feed</h2>"

@app.route('/',methods=['GET','POST','PUT','PATCH','DELETE'])
def home():
    
    return redirect('/auth')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port='5001')