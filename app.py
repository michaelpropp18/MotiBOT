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
    print(body["text"].lower())
    if "yo shimbo" in body["text"].lower():
        print("yes")
        jason = {
  "bot_id"  : "5f28714a19ba9e7da997cc8cfe",
  "text"    : "look what the street kicked up",
}
        res = requests.post('https://api.groupme.com/v3/bots/post', json=jason)
    elif "what’s up shimbo" in body["text"].lower():
        print("yessir")
        jason = {
  "bot_id"  : "5f28714a19ba9e7da997cc8cfe",
  "text"    : "how the fuck is up?",
}
        res = requests.post('https://api.groupme.com/v3/bots/post', json=jason)
    elif "motivate me shimbo" in body["text"].lower():
        print("yeeee")

        x = requests.get('http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en')
        print("h")
        print(x.json())

    return "did something"

if __name__ == '__main__':
    app.run()