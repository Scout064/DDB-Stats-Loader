# DDB-Stats-Loader
##To-DO

-> Add Button to start collection instead of run at load.

-> Add send to Networked Client Routine for Char Stats

PYTHON:
```
from socket import *
import json
s = socket()
s.bind(('', 80))
s.listen(4)
ns, na = s.accept()

while 1:
    try:
        data = ns.recv(8192)
    except:
        ns.close()
        s.close()
        break

    data = json.loads(data)
    print data
```    
    
        
JavaScript:

```
function callPython()
{
var xmlhttp;
if (window.XMLHttpRequest)
  {// code for IE7+, Firefox, Chrome, Opera, Safari
  xmlhttp=new XMLHttpRequest();
  }
else
  {// code for IE6, IE5
  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
xmlhttp.onreadystatechange=function()
  {
  if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
    document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
    }
  }
xmlhttp.open("GET","Form-data",true);
xmlhttp.send();
}
