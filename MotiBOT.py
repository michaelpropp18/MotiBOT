print("hello world")

import requests
import json


x = requests.get('http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en')
j = x.json()
msg = []
print('Motivational quote of the day: "' + j['quoteText'] + '" -' + j["quoteAuthor"])


