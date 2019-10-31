import os
from pymongo import MongoClient
from flask import Flask, render_template
mongo_host = os.environ.get('MONGOHOST','localhost')
client = MongoClient(mongo_host,27017)

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def base():
    # call auth()

    # if not auth() return error, load again

    # if auth() ,
    #   call feed()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,port='5010')
  