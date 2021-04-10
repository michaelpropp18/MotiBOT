import os
from flask import Flask
from flask import request
import requests


app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def hello():
    return "Hello World!"


@app.route('/callback', methods = ['POST'])
def hello_name():
    print(request.get_json(), type(request))
    body = request.get_json()
    if "yo shimbo" in body["text"]:
        print("yes")
        jason = {
  "bot_id"  : "5f28714a19ba9e7da997cc8cfe",
  "text"    : "look what the street kicked up",
}
        res = requests.post('https://api.groupme.com/v3/bots/post', json=jason)
        

    return "did something"

if __name__ == '__main__':
    app.run()