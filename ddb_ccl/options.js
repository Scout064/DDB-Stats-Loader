/*eslint-env es6*/
function save_options() {
  var ipAddress = document.getElementById('ipaddress').value;
  chrome.storage.local.set({clientIP: ipAddress}, function() {
    var status = document.getElementById('status');
    status.textContent = 'Options saved.';
    setTimeout(function() {
      status.textContent = '';
    }, 750);
  });
}

function restore_options() {
    chrome.storage.local.get(['clientIP'], function(result) {
        if(result.clientIP != undefined) {document.getElementById('ip').innerText = result.clientIP;}
          });                             
        }
document.addEventListener('DOMContentLoaded', restore_options);
document.getElementById('save').addEventListener('click', save_options);