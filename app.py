import os
from flask import Flask
from flask import request
import requests
import random


app = Flask(__name__)

def roundtable():
    x = []
    topics = ['x-rays','Asia','World War 1','bread','Napoleon','cheese','Central America','magicians','potatoes','diving','volleyball','army','prisons','money','tigers','rugby','zebras','skull','execution','mules','golf','basketball','donkeys','criminals','rhinoceros','wrestling','coins','pigeons','giants','goats','blacksmiths','shipwrecks','sheep','Disney movies','tattoos','sailing','funerals','Boy Scouts','cocoa','bears','leather','weaving','matches','medicine','lighthouses','movie theaters','sharks','North Africa','ostriches','socialism','cards','airplanes','fencing','toads','birds','spiritism','insects','apes','boxing','cats','vanilla','cactus','shoes','playing cards','music','engineering','cigarettes','ferry boats','coffin','swings','astronomy','frogs','hockey','elephants','spinning','cobblers','Africa','rice','carousels','vaccines','muppets','beekeeping','dance','milk','amusement parks','buffaloes','parachuting','stadiums','water skiing','crocodiles','salt','Americans','coffee','gypsies','justice','cemetery','alligators','airports','seesaws','slavery','nurses','sports','rabbits','chess','athletics','caves','games','lions','hotels','windmills','post office','archery','diamond','artists','tanning','telephone','meteorology','communism','railroads','lighters','laundry','coal','pigs','Olympic games','shells','newspapers','skating','hurricanes','sugar','death','printing','paper boys','monkeys','smoking','submarines','pipe organs','wood','gold','Red Cross','mining','banana','hippopotamus','banking','giraffes','disasters','veterinarians','drugstores','dogs','South America','Europe','tennis','camels','agriculture','volcanoes','fishing','breweries','books','pilots','spas','mummies','shipping','horses','dolphins','hammocks','postcards','tobacco','sewing machines','Native Americans','motherhood','balloons','bohemians','bats','murderers','bananas','gorillas','cycling','jewelry','Salvation Army','pipes','journalism','barbers','snakes','Buddhism','baseball','motorcycles','accordions','dentistry','masonry','vegetables','farmers markets','radio','football','pottery','politics','turtles','shovels','circus','police','flood','billiards','earthquake','cricket','seashells','typewriter','marionettes','oil','hunting','royalty','bridges','radiology','cotton','military','gymnastics','canoes','whales','foxes','carpentry','bakeries','clowns','pineapple','soccer','zeppelins','crime','firemen','fortune tellers','pharmacy','pork','mountaineering','typewriters','cows','boats','puppets']
    while len(x) < 10:
        random_topic = topics[random.randint(0,len(topics))]
        x = requests.get('https://api.datamuse.com/words?rel_jjb=' + random_topic)
        x = x.json()
    topics = []
    i = 0
    while len(topics) < 3:
        if x[i]['word'] not in ['many', 'other', 'various']:
            topics.append(x[i]['word'])
        i += 1
    return ("Hey guys, we will be holding a roundtable discussion about " + random_topic + "." + " We will be discussing " + topics[0] + " " + random_topic + ", " + topics[1] + " " + random_topic + ", and " + topics[2] + " " + random_topic + ".")

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
        body = x.json()
        jason = {
  "bot_id"  : "5f28714a19ba9e7da997cc8cfe",
  "text"    : body["quoteText"],
}
        res = requests.post('https://api.groupme.com/v3/bots/post', json=jason)
    elif ("round table" in body["text"].lower() or "roundtable" in body["text"].lower()) and body["sender_id"] != "bot":
        print("yeeee")
        text = roundtable()
        print("h")
        jason = {
  "bot_id"  : "5f28714a19ba9e7da997cc8cfe",
  "text"    : text,
}
        res = requests.post('https://api.groupme.com/v3/bots/post', json=jason)


    return "did something"

if __name__ == '__main__':
    app.run()