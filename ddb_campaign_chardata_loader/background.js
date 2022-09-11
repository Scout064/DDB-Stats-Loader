/*eslint-env es6*/
//background script is always running unless extension is disabled
// add listener for URL array
chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse){
    var ddb_url_array = [];
// if valid data received, print to console and
// parse received data to variable
//    if (ddb_char_array != 'undefined' ) {
    if (request.message == 'url_array' ) {
        ddb_url_array = request.data;
        console.log('received url data! ' + '... ' + 'printing to console!');
        console.log(ddb_url_array);}
    else {
        console.log('NO URL DATA RECEIVED!');}
    });