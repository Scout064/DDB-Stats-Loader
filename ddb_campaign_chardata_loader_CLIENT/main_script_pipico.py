## Multi Core Program example
led_red = machine.Pin(0, machine.Pin.OUT)
led_green = machine.Pin(1, machine.Pin.OUT)

sLock = thread.allocate_lock()

def CoreTask():
    while True:
        sLock.acquire()
        print("Enter second Thred")
        sleep(1)
        led_green.high()
        print("Green LED is turned ON")
        sleep(2)
        led_green.low()
        print("Green LED is turned OFF")
        sleep(1)
        print("Exit second Thread")
        sleep(1)
        sLock.release()
thread.start_new_thread(CoreTask, ())

while True:
    sLock.acquire()
    print("Enter main Thread")
    led_red.toggle()
    sleep(0.15)
    print("Red LED toggling...")
    sleep(1)
    print("Exit main Thread")
    sleep(1)
    sLock.release()

#######################################################
#######################################################

## Import libraries
import machine
import _thread as thread
import ujson as json
import picoweb
from time import sleep
import network
import ure as re
import ulogging as logging
import uasyncio as asyncio

## Network Setup 
ssid = '*****'
password = '*******'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
print("Waiting to connect:")
while not wlan.isconnected() and wlan.status() >= 0:
    print(".", end="")   
    time.sleep(1)
print("")
print(wlan.ifconfig())
## define IFconfig var with ifconfig array
IFconfig = wlan.ifconfig()
## take first Value of array
IPaddress = [IFconfig[0]]


## define flask/picoweb
def index(req, resp):
    method = req.method
    print("Method was:" + method)
    yield from picoweb.start_response(resp)
    yield from resp.awrite("Welcome to the Char Data API running on PiPico W and picoweb!")
    
def json(req, resp):
    method = req.method
    print("Method was:" + method)
    
    if req.method == "POST":
        size = int(req.headers[b"Content-Length"])
        print("Size: ", size)
        yield from req.read_form_data()
    else:
        req.parse_qs()
        
yield from picoweb.start_response(resp)
yield from resp.awrite("HTTP/1.0 200 OK\r\n")
yield from resp.awrite("Content-Type: application/json\r\n")
yield from resp.awrite("\r\n")

print(req.headers)
print(req.form)
char_data_import = req.form
    
ROUTES = [
            ("/", index),
            ("/json", json)
         ]

logging.basicConfig(level=logging.INFO)         
app = picoweb.WebApp(Char_Data_API, ROUTES)
app.run(debug=2, port = 80, host = IPaddress)
    
## Grab Posted Data from Chrome extension and convert to python dict via JSON
json_convert_data = json.loads(char_data_import)
python_convert_data = json.dumps(json_convert_data)
char_data = python_convert_data

## Check converted data by printing the dict
print(char_data)

#######################################################
#######################################################

        
        
        
        
        
        
        
        
        
## EXAMPLE CODES
#######################################################
#######################################################
def index(req, resp):
    method = req.method
    print("Method was:" + method)
    yield from picoweb.start_response(resp)
    yield from resp.awrite("Hello world from picoweb running on the ESP32")

def batteryslave(req, resp):
    method = req.method
    print("Method was:" + method)

    if req.method == "POST":
        size = int(req.headers[b"Content-Length"])
        print("Size: ", size)
        yield from req.read_form_data()
    else:
        req.parse_qs()

    yield from picoweb.start_response(resp)
    yield from resp.awrite("OK")
    yield from resp.awrite("\r\n")

    print(req.headers)

ROUTES = [
            ("/", index),
            ("/batteryslave", batteryslave)
         ]
         
app = picoweb.WebApp(__name__, ROUTES)
app.run(debug=2, port = 80, host = "192.168.42.192")
#######################################################
#######################################################
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    return render_template('form.html')

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    return render_template('greeting.html', say=request.form['say'], to=request.form['to'])

if __name__ == "__main__":
    app.run()
#######################################################
#######################################################
#
# This is a picoweb example showing a centralized web page route
# specification (classical Django style).
#
import ure as re
import picoweb


def index(req, resp):
    # You can construct an HTTP response completely yourself, having
    # a full control of headers sent...
    yield from resp.awrite("HTTP/1.0 200 OK\r\n")
    yield from resp.awrite("Content-Type: text/html\r\n")
    yield from resp.awrite("\r\n")
    yield from resp.awrite("I can show you a table of <a href='squares'>squares</a>.<br/>")
    yield from resp.awrite("Or my <a href='file'>source</a>.")


def squares(req, resp):
    # Or can use a convenience function start_response() (see its source for
    # extra params it takes).
    yield from picoweb.start_response(resp)
    yield from app.render_template(resp, "squares.tpl", (req,))


def hello(req, resp):
    yield from picoweb.start_response(resp)
    # Here's how you extract matched groups from a regex URI match
    yield from resp.awrite("Hello " + req.url_match.group(1))


ROUTES = [
    # You can specify exact URI string matches...
    ("/", index),
    ("/squares", squares),
    ("/file", lambda req, resp: (yield from app.sendfile(resp, "example_webapp.py"))),
    # ... or match using a regex, the match result available as req.url_match
    # for match group extraction in your view.
    (re.compile("^/iam/(.+)"), hello),
]


import ulogging as logging
logging.basicConfig(level=logging.INFO)
#logging.basicConfig(level=logging.DEBUG)

app = picoweb.WebApp(__name__, ROUTES)
# debug values:
# -1 disable all logging
# 0 (False) normal logging: requests and errors
# 1 (True) debug logging
# 2 extra debug logging
app.run(debug=1)
#######################################################
#######################################################  