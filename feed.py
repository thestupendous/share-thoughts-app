import os
#from pymongo import MongoClient
from flask import Flask, render_template, request
#mongo_host = os.environ.get('MONGOHOST','localhost')
#client = MongoClient(mongo_host,'27017')

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def base():
    # call auth()

    # if not auth() return error, load again

    # if auth() ,
    #   call feed()
    print('*'*30,'printing req \n',request)
    print('\n','printing \n',request.form,'\n\n\n')
    words = request.args['texts']
    return render_template('index2.html',word=words)

if __name__ == '__main__':
    app.run(debug=True,port='5020')
  