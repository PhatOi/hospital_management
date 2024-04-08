const bttns = document.querySelectorAll('.bttn');
const inputs = document.querySelectorAll('input');

for(const bttn of bttns) {
    bttn.addEventListener('click',toogleBttn);
}

function toogleBttn () {
    for(const bttn of bttns) {
        bttn.classList.toggle('display-none');
    }

    for(const input of inputs) {
        if(input.hasAttribute('disabled')) {
            input.removeAttribute('disabled');
            input.style.outline = "1px solid #000";
        }
        else {
            input.setAttribute('disabled', 'true');
            input.style.outline = "1px solid #fff";
        }
    }
}