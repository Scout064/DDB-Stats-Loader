## Import libraries
import machine
import _thread as thread
import json
import picoweb
from time import sleep
import network
import ure as re
import ulogging as logging
import uasyncio
from tinydb import TinyDB, Query
import utemplate
import neopixel

## Network Setup 
#ssid = 'IOT'
#password = 'T79brWDLcZp3LVrw'
ssid = 'zyxelemea'
password = 'ZyxelEMEA20!'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
print("Waiting to connect:")
while not wlan.isconnected() and wlan.status() >= 0:
    print(".", end="")   
    sleep(5)
print("")
print(wlan.ifconfig())
## define IFconfig var with ifconfig array
IFconfig = wlan.ifconfig()
## take first Value of array
IPaddress = IFconfig[0]

##Set up Database
db = TinyDB('db.json')
## check if db empty, if not: clear all data
if db.all() != []:
    db.truncate()

## define picoweb/picoweb
app = picoweb.WebApp(__name__)

@app.route("/json")
## Get the JSON Data from the chrome extension
def json_post_data(req, resp):
    if req.method == 'OPTIONS':
        headers = {"Access-Control-Allow-Methods": "POST, GET", "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "Access-Control-Allow-Methods, Access-Control-Allow-Origin, Origin, Accept, Content-Type"}
        yield from picoweb.start_response(resp, status="200", headers=headers)
        method = req.method
        ##DEBUG OPTIONS##
        ##print("CORS HEADER RECEIVED")##
        ##print("Method was:" + method)##
    elif req.method == 'POST':
        ##create vars
        size = int(req.headers[b"Content-Length"])
        read_request = yield from req.reader.readexactly(size)
        request_data = json.loads(read_request)
        headers_json = {'Content-Type': 'application/json', 'Accept': "application/json", "Access-Control-Allow-Methods": "POST, GET", "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "Access-Control-Allow-Methods, Access-Control-Allow-Origin, Origin, Accept, Content-Type"}
        ## next data digestion
        yield from picoweb.start_response(resp, content_type="application/json; charset=utf-8", status="200", headers=headers_json)
        db.insert(request_data)
        ##DEBUG OPTIONS##
        print("DATA RECEIVED")##
        print(request_data)##
        method = req.method##
        print("Method was:" + method)##
        print("Writing Data to DB!")##
    else:
        yield from picoweb.start_response(resp, content_type = "text/html")
        yield from app.render_template(resp, 'error.html')
        ##DEBUG OPTIONS##
        ##print("ERROR! NOT A VALID REQUEST!")##
        ##method = req.method##
        ##print("Method was:" + method)##

## Documentation Endpoint
@app.route("/")
def index(req, resp):
    if req.method == 'GET':
        yield from picoweb.start_response(resp, content_type = "text/html")
        yield from app.render_template(resp, 'index.html')
    else:
        yield from picoweb.start_response(resp, content_type = "text/html")
        yield from app.render_template(resp, 'error.html')
    
## Configuration Endpoint
@app.route("/config")
def config(req, resp):
    if req.method == 'GET':
        yield from picoweb.start_response(resp, content_type = "text/html")
        yield from app.render_template(resp, 'config.html')
    else:
        yield from picoweb.start_response(resp, content_type = "text/html")
        yield from app.render_template('error.html')

logging.basicConfig(level=logging.DEBUG)
app.run(debug=2, port = 80, host = IPaddress)

