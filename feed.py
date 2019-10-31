import os
#from pymongo import MongoClient
from flask import Flask, render_template, request, redirect
#mongo_host = os.environ.get('MONGOHOST','localhost')
#client = MongoClient(mongo_host,'27017')

app = Flask(__name__)
@app.route('/')
def delete_route():
    return redirect('/feed')

@app.route('/feed/post',methods=['GET','POST'])
def post_status():
    uid = request.form['uid']
    status = request.form['status']

    print('\n\n','uid and status ',uid,status,sep='  ',end='\n\n')
    return redirect('/feed')

    # -- make db call to update posts collection to add new entry for 
    #    corresponding uid and suitable post

@app.route('/feed',methods=['GET','POST'])
def base():
    # expecting userid as post request
    uid = '1'
    return render_template('feed.html',uid=uid)

if __name__ == '__main__':
    app.run(debug=True,port='5020')
  