/*eslint-env es6*/
//background script is always running unless extension is disabled
// add listener for URL array
chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse){
    var ddb_urls_array = [];
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
    var ddb_char_array = [];
    // define function to get character urls
    function requestCharData () {
// if valid data received, print to console and
// parse received data to variable
    if (request.message == 'data_array' ) {
        ddb_char_array = request.data;
        console.log('received char data! ' + '... ' + 'printing to console!');
        console.log(ddb_char_array);}
    else {
        console.log('NO CHARACTER DATA RECEIVED!');}
        }
    setInterval(requestCharData, 10000);
    });