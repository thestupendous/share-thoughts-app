import os
#from pymongo import MongoClient
from flask import Flask, render_template, request, redirect
#mongo_host = os.environ.get('MONGOHOST','localhost')
#client = MongoClient(mongo_host,'27017')

app = Flask(__name__)
@app.route('/')
def delete_route():
    return redirect('/user')

@app.route('/user',methods=['GET','POST'])
def base():
    # expecting userid as post request
    uid = '1'
    return render_template('user.html',uid=uid)

if __name__ == '__main__':
    app.run(debug=True,port='5030')
  