## Import libraries
import machine
import _thread
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
from extract import json_extract
import os

##Set CPU clock speed to 133MHz (max. on std. voltage) if not set
if machine.freq() != 133000000:
    print('Checking CPU speed!')
    sleep(1)
    print('Maximizing CPU speed!')
    machine.freq(133000000)
    print('CPU clock changed to 133MHz!')
    sleep(1)
    print('current CPU speed:')
    print(machine.freq(),'Hz')
    sleep(2)
else:
    print('CPU speed already maxed!')
    print('current CPU speed:')
    print(machine.freq(),'Hz')
    print('Continue to Boot!')
    sleep(2)

## Network Setup 
ssid = '*********'
password = '********'
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
    
## delete old version of playerID.json and create empty
os.remove("playerID.json")
file = open('playerID.json', 'w')
file.close()

## Set up Multicore Workflow
## Define semaphore lock
sLock = _thread.allocate_lock()

## Define second Thread
def CoreTask():
    while True:
        ## Acquire semaphore lock
        sLock.acquire()
        ## Execute some code
        print('Enter second Thread!')
        
        sleep(10)
        print('Exit second Thread!')
        ## Release semaphore lock
        sLock.release()
## Restart Thread
_thread.start_new_thread(CoreTask, ())

## Define main thread
while True:
    ## Acquire semaphore lock
    sLock.acquire()
    print('Enter main Thread!')

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
            ##print("DATA RECEIVED")##
            ##print(request_data)##
            ##method = req.method##
            ##print("Method was:" + method)##
            ##print("Writing Data to DB!")##
        else:
            yield from picoweb.start_response(resp, content_type = "text/html")
            yield from app.render_template(resp, status="500", 'error.html')
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
            yield from app.render_template(resp, status="500", 'error.html') 
    
    ## Configuration Endpoint
    @app.route("/config")
    def config(req, resp):
        if req.method == 'GET':
            load_db = open('db.json', 'r')
            get_data = json.load(load_db)
            player_names = json_extract(get_data, 'Name')
            playerID = {'Name':player_names}
            #playerConf = {"Player1":player_names, "Player2":player_names, "Player3":player_names, "Player4":player_names, "Player5":player_names, "Player6":player_names, "Player7":player_names, "Player8":player_names}
            for i in range(0, 8):
                locals()[f"Player{i}"] = name
                playerConf = {"Player_ID{i}":locals()[f"Player{i}"]}
            for i in player_names:
                file = open('playerID.json', "a")
                file.write(json.dumps('{'Name':i},'))
                file.close()
            yield from picoweb.start_response(resp, content_type = "text/html")
            yield from app.render_template(resp, 'config.html', (playerConf,))
        else:
            yield from picoweb.start_response(resp, content_type = "text/html")
            yield from app.render_template(resp, status="500", 'error.html')

    logging.basicConfig(level=logging.DEBUG)
    app.run(debug=2, port = 80, host = IPaddress)
    
    ## Release semaphore lock
    print('Exit main Thread!')
    sLock.release()
