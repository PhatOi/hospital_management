const btns = document.querySelectorAll('.personal_form-btn');
const inputs = document.querySelectorAll('.input-infor');
const selects = document.querySelectorAll('.select-infor');

for(const bttn of btns) {
    bttn.addEventListener('click',toogleBttn);
}

function toogleBttn () {
    for(const bttn of btns) {
        bttn.classList.toggle('d-none');
    }

    for(const input of inputs) {
        if(input.hasAttribute('disabled')) {
            input.removeAttribute('disabled');
        }
        else {
            input.setAttribute('disabled', 'true');
        }
    }

    for(const select of selects) {
        if(select.style.backgroundColor == "rgb(255, 255, 255)") select.style.backgroundColor = "rgb(233 236 239)";
        else select.style.backgroundColor = "rgb(255, 255, 255)"
    }
}
