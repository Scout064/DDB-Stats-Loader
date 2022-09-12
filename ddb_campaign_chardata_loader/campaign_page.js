/*eslint-env es6*/
// Run on Tab load, wait 10 Seconds, then start grabbing urls and data off the Site
setTimeout(() => { 
// define css selector for active character urls
    var urls = document.querySelectorAll(
        '.ddb-campaigns-detail-body-listing-active a.ddb-campaigns-character-card-footer-links-item-view'
        );
// create empty array
    var url_array = [];
// define loop
    for (url in urls) {
// Put the urls in the array and inform console
        url_array.push(urls[url].href);
        }
    console.log ('done loading urls');
// Clean Array, remove undefined vales and inform console
    console.log('cleaning array!')
    url_array = url_array.filter(function( element ) {
        return element !== undefined;
        });
    console.log('array cleaned!');
    console.log('loading characters!');
// push URL to backgrund script
    chrome.runtime.sendMessage({message: 'url_array', data: url_array});
// define function to iterate url_array and get character urls
    function grabCharData () {
// iterate url_array, pass on urls and digest as hidden iFrame
    for (var url_array_iterate of url_array){
            console.log(url_array_iterate);
            console.log('opening url and grabbing data!');
            function createNodeContainer(){ // create the new div
                var makeIframe = document.createElement("iframe");
                    makeIframe.setAttribute("src", url_array_iterate);
                    makeIframe.setAttribute("scrolling", "no");
                    makeIframe.setAttribute("id", "iframe");
                    makeIframe.style.overflow = "hidden";
                    makeIframe.style.border = "0pt";
                    makeIframe.style.border = "none";
                    makeIframe.style.position = "absolute";
                    makeIframe.style.width = "1024px";
                var makediv = document.createElement("div");
                    makediv.style.height = "0px";
                    makediv.style.width = "0px";
                    makediv.style.position = "relative";
                    makediv.style.overflow = "hidden";
                makediv.appendChild(makeIframe);
                document.body.appendChild(makediv);
                }
                createNodeContainer();
            } 
        }
    grabCharData();
}, 10000);

