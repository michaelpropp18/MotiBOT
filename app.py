import os
from flask import Flask
from requests.api import request


app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def hello():
    return "Hello World!"


@app.route('/callback', methods = ['POST'])
def hello_name():
    print(request)
    return "did something"

if __name__ == '__main__':
    app.run()