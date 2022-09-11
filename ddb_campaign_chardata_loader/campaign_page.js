/*eslint-env es6*/
// Run on Tab load, wait 5 Seconds, then grab urls off the Site
setTimeout(() => { 
// define css selector for active character urls
    var urls = document.querySelectorAll(
        '.ddb-campaigns-detail-body-listing-active a.ddb-campaigns-character-card-footer-links-item-view'
        );
// create empty array
    const url_array = [];
// define loop
    for (url in urls) {
// Put the urls in the array and inform console
        url_array.push(urls[url].href);
        }
    console.log ('done loading urls');
    console.log(url_array);
// push URL to backgrund script
    chrome.runtime.sendMessage({message: 'url_array', data: url_array});
// define function to iterate url_array and get character urls
    function grabCharData () {
            url_array.forEach(item => {
            console.log(url_array);
// pass on url and digest as hidden iFrame
            console.log('opening url and grabbing data!');
            (function(){
                var i = document.createElement('iframe');
                i.style.display = 'flex';
                i.onload = function() { i.parentNode.removeChild(i); };
                i.src = url_array;
                document.body.appendChild(i);
                })();
            })
        }
    setInterval(grabCharData, 60000);
    }, 10000);