/*eslint-env es6*/
// define waiting function for Char Sheet loading
            async function waitForLoading() {
            if (!document.querySelector('.ct-character-header-info') || document.querySelector('.ct-loading-blocker')) {
                return new Promise((r) =>
                    setTimeout(() => {
                        r(waitForLoading());
                    }, 200)
                );
            }
            return Promise.resolve();
            }
// init waiting function
            async function init(){
            await waitForLoading();
// grab current and max HP from Character
            const current_hp = document.querySelector('div.ct-health-summary__hp-group.ct-health-summary__hp-group--primary > div:nth-child(1) > div.ct-health-summary__hp-item-content > div').innerText;
            const max_hp = document.querySelector('div.ct-health-summary__hp-group.ct-health-summary__hp-group--primary > div:nth-child(3) > div.ct-health-summary__hp-item-content > div').innerText;
            const name = document.querySelector('h1').innerText;
// log values to console and send to background.js
            const data_array = [];
            console.log('Done'),
            console.log('Name: ' + name),
            console.log('current HP: ' + current_hp),
            console.log('max HP: ' + max_hp),
            data_array.push('Name: ' + name),
            data_array.push('current HP: ' + current_hp),
            data_array.push('max HP: ' + max_hp),
            // push URL to backgrund script
            chrome.runtime.sendMessage({message: 'data_array', data: data_array})}
init();
setTimeout(function () {window.location.reload()}, 60000);