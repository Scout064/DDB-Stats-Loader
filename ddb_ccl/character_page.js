/*eslint-env es6*/
let timerId;

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

// grab current and max HP from Character
function getHP() {
  const current_hp = document.querySelector('div.ct-health-summary__hp-group.ct-health-summary__hp-group--primary > div:nth-child(1) > div.ct-health-summary__hp-item-content > div').innerText;
  const max_hp = document.querySelector('div.ct-health-summary__hp-group.ct-health-summary__hp-group--primary > div:nth-child(3) > div.ct-health-summary__hp-item-content > div').innerText;
  const name = document.querySelector('h1').innerText;
  return {
    name,
    current_hp,
    max_hp
  };
}

// log values to console and send to background.js
function sendHP() {
  const hp = getHP();
  const data_array = {
    Name: hp.name,
    currentHP: hp.current_hp,
    maxHP: hp.max_hp
  };
  console.log('Name' + ": " + hp.name);
  console.log('current HP' + ": " + hp.current_hp);
  console.log('max HP' + ": " + hp.max_hp);
  // push data to background script
  chrome.runtime.sendMessage({ message: 'data_array', data: data_array });
}

// initialize the script
async function init() {
  await waitForLoading();
  sendHP();
}

// add start/stop button to page
function addStartStopButton() {
  const button = document.createElement('button');
  button.textContent = 'Start';
  button.style.position = 'fixed';
  button.style.top = '10px';
  button.style.right = '10px';
  button.style.zIndex = '9999';
  button.addEventListener('click', () => {
    if (button.textContent === 'Start') {
      init();
      timerId = setInterval(() => {
        init();
      }, 60000);
      button.textContent = 'Stop';
    } else {
      clearInterval(timerId);
      button.textContent = 'Start';
    }
  });
  document.body.appendChild(button);
}

addStartStopButton();
