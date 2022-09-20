## Import libraries
import app
import os
import json
import flask
from flask_cors import CORS
import logging
import sys

## define flask/picoweb
app = flask.Flask(__name__)
CORS(app)

@app.route("/json", methods=['GET', 'POST'])
## Get the JSON Data from the chrome extension
def json_post_data():
    if flask.request.method == 'Post':
        request_data = flask.request.get_json()
## create vars
        input_data = [request_data]
## global vars for Player Setup (see @app.route("/config", methods=['GET', 'POST']))
        globals()["Player1"] = {}
        globals()["Player2"] = {}
        globals()["Player3"] = {}
        globals()["Player4"] = {}
        globals()["Player5"] = {}
        globals()["Player6"] = {}
        globals()["Player7"] = {}
        globals()["Player8"] = {}
## next data digestion
## take items from request_data and extract to global var
        for item in input_data:
            new_dict={}
            new_dict['Name']=item.get('ddb_char_array').get('Name')
            new_dict['currentHP']=item.get('ddb_char_array').get('currentHP')
            new_dict['maxHP']=item.get('ddb_char_array').get('maxHP')
            globals()["player_dict"] = [new_dict]
## create unique global var for each name
            PlayerID = new_dict['Name'].replace(" ", "_")
            globals()[f"{PlayerID}"] = new_dict['Name']
## take PlayerID and extract data
        for item in player_dict:
            globals()[f"{PlayerID}_dict"] = {}
            globals()[f"{PlayerID}_dict"]['currentHP']=item.get('currentHP')
            globals()[f"{PlayerID}_dict"]['maxHP']=item.get('maxHP') 
            #print(globals()[f"{PlayerID}_dict"])
        #print(globals())
    else:
        return flask.render_template('error.html')

## Documentation Endpoint
@app.route("/", methods=['GET', 'POST'])
def index():
    if flask.request.method == 'GET':
        return flask.render_template('index.html', output=globals()["player_dict"])
    else:
        return flask.render_template('error.html')

if __name__ == "__main__":
    app.run(debug=True, host='192.168.178.6', port=80)
#######################################################
#######################################################




##abc = {"type":"insecure","id":"1","name":"peter"}
##xyz = abc.copy()
##xyz.pop('type')
##xyz['identity'] = xyz.pop('id')


##abc = {"type":"insecure","id":"1","name":"peter"}
##black_list = {"type"}
##rename ={"id":"identity"}  #use a mapping dictionary in case you want to rename multiple items
##dic = {rename.get(key,key) : val for key ,val in abc.items() if key not in black_list}
##print dic


##Incoming JSON Data from Client: {'ddb_char_array': {'Name': 'Irlibras Stargazer', 'currentHP': '24', 'maxHP': '24'}}