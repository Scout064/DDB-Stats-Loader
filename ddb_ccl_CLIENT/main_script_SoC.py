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
output = None

#logging.basicConfig(level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.route("/json", methods=['GET', 'POST'])
def json_post_data():
    if flask.request.method == 'Post':
        request_data = flask.request.get_json()
## next data digestion
        players = None
#        json_data_import = json.dumps(request_data)
        print(json.dumps(request_data))
        sys.stdout.flush() 

        merged_json = {}
        for key,value in json_data.items():
            merged_json[key] = value
            print(merged_json)
            sys.stdout.flush()

    else:
        return flask.render_template('error.html')

@app.route("/", methods=['GET', 'POST'])
def index():
    if flask.request.method == 'GET':
        return flask.render_template('index.html', output="CONSOLE OFFLINE!")
    else:
        return flask.render_template('error.html')

if __name__ == "__main__":
    app.run(debug=True, host='192.168.178.7', port=80)
#######################################################
#######################################################




