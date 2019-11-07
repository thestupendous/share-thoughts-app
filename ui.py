import os
from pymongo import MongoClient
from flask import Flask , render_template, redirect, request, url_for
import requests,json

ui_host = os.environ.get('UIHOST','localhost')
auth_host = os.environ.get('AUTHHOST','localhost')
feed_host = os.environ.get('FEEDHOST','localhost')
user_host = os.environ.get('USERHOST','localhost')
db_host = os.environ.get('DBHOST','localhost')

app = Flask(__name__)

@app.route('/auth',methods=['GET','POST','PUT','PATCH','DELETE'])
def auth1():
    print('inside ui/auth')
    if request.method == 'GET':
       return render_template('auth.html',failed=False)
    if request.method == 'POST':
       return render_template('auth.html',failed=True)

@app.route('/reqdata',methods=['GET','POST','PUT','PATCH','DELETE'])
def call_auth():
    print('inside ui/reqdata')
    auth_data = { "username":request.form['username'], "password":request.form['password']}
    response = requests.post('http://0.0.0.0:5002',json=auth_data)
    print('*'*15, '[',uid.text,'*]','*'*15)
    dictresponse=json.loads(response.text)
    print("\n+"*5,type(dictresponse),'\n+'*5)
    if dictresponse['failed'] == True:
        # return 'authentication failed! inside ui call auth'
        return redirect('/auth',code=307)
        
    else:
        # return 'successfully authenticated, ready for feeds page'
        requests.post('http:0.0.0.0:5003',json=dictresponse)

# @app.route('/authfail',methods=['GET','POST','PUT','PATCH','DELETE'])
# def auth_fail_():
#     print('inside ui/authfail\nauth failed')
#     return "<h1> auth failed !!</h1>"

# @app.route('/authres',methods=['GET','POST','PUT','PATCH','DELETE'])
# def auth_success():
#     print('inside ui/authres\nauth success')
#     print(request.data)
#     return "auth success"


@app.route('/feed',methods=['GET','POST','PUT','PATCH','DELETE'])
def feeds():
    print('inside ui/feed')
    return "<h1>***here goes feed</h2>"

@app.route('/',methods=['GET','POST','PUT','PATCH','DELETE'])
def home():
    print('inside ui/')
    return redirect('/auth')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port='5001')