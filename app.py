import os
from flask import Flask
from requests.api import request


app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def hello():
    return "Hello World!"


@app.route('/callback', methods = ['POST'])
def hello_name(name):
    print(request)
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()