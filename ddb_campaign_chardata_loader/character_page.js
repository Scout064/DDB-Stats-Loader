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
//            const temp_hp = document.querySelector('div.ct-health-summary__hp-group.ct-health-summary__hp-group--temp > div:nth-child(3) > div.ct-health-summary__hp-item-content > div').innerText;
            const name = document.querySelector('h1').innerText;
// log values to console and send to background.js
//            var data_array;
            var json_string = JSON.stringify({[new String('Name')]: name ,[new String('currentHP')]: current_hp ,[new String('maxHP')]: max_hp });
            var data_array = JSON.parse(json_string);
            console.log('Done'),
            console.log('Name' + ": " + name),
            console.log('current HP' + ": " + current_hp),
            console.log('max HP' + ": " + max_hp),
//            console.log('temp HP: ' + temp_hp),
//            data_array.push("Name", ":", name),
//            data_array.push("currentHP", ":", current_hp),
//            data_array.push("maxHP", ":", max_hp),
//            data_array.push('tempHP: ' + temp_hp),
//            console.log(data_array),
            // push URL to backgrund script
            chrome.runtime.sendMessage({message: 'data_array', data: data_array})}
init();
setTimeout(function () {window.location.reload()}, 60000);