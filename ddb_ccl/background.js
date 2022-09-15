/*eslint-env es6*/
//background script is always running unless extension is disabled
// define global variabels
var ddb_url_array = [];
var ddb_char_array;
var client_ip = [];
// load client_ip from Storage and check if set
chrome.storage.local.get(['clientIP'], function(result) {
client_ip = result.clientIP;
// if not set open options.html
if (typeof client_ip === 'undefined'){
    console.log('Opening options.html, please set client IP!');
    chrome.runtime.openOptionsPage();}
else {
    console.log('Client IP in options.html set, nothing to do!');}
})
// define function to create json dict and send via fetch()
function sendCharData() {
    fetch('http://' + client_ip + '/json', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ddb_char_array})
    });
console.log('printing Json format String!')
console.log(JSON.stringify({ddb_char_array}));
        };
// add listener for URL array
chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse){
// if valid data received, print to console and
// parse received data to variable
    if (request.message == 'url_array' ) {
        ddb_url_array = request.data;
        console.log('received url data! ' + '... ' + 'printing to console!');
        console.log(ddb_url_array);}
    else {
        console.log('NO URL DATA RECEIVED!');}
    });
// add listener for character array
chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse){
// check if client IP is loaded
    if (typeof client_ip !== 'undefinded'){
        console.log('Already loaded client IP');
        console.log('Client IP: ' + client_ip);
        requestCharData();
        console.log('sending char data to client!');
        sendCharData();}
    else {
// get client IP from storage
        chrome.storage.local.get(['clientIP'], function(result) {
        client_ip = result.clientIP;
        console.log('Loading client IP!');
        console.log('Client IP: ' + client_ip);
        requestCharData();
        console.log('sending char data to client!');
        sendCharData();})}
// define function to get character urls
    function requestCharData () {        
// if valid data received, print to console and
// parse received data to variable
    if (request.message == 'data_array') {
        ddb_char_array = request.data;
        console.log('received char data! ' + '... ' + 'printing to console!');
        console.log(ddb_char_array);}
    else {
        console.log('NO CHARACTER DATA RECEIVED!');
        }
    };
});