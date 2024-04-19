const feedback_form_addBtn = document.querySelector('.feedback')
const feedback_form_submitBtn = document.querySelector('.btn-feedback_form-submit');
const feedback_form_cancelBtn = document.querySelector('.btn-feedback_form-cancel');
const feedback_form = document.querySelector('.feedback_form');
const feedback_form_container = document.querySelector('.feedback_form .feedback_form-container');

function removeClass(feedback_form, className) {
    feedback_form.classList.remove(className)
}

feedback_form_addBtn.addEventListener('click', () => {
    feedback_form.classList.add('d-block')
})

feedback_form_cancelBtn.addEventListener('click', () => {
    removeClass(feedback_form, 'd-block')
})

feedback_form.addEventListener('click', () => {
    removeClass(feedback_form, 'd-block')
})

feedback_form_container.addEventListener('click', (event) => {
    event.stopPropagation();
})

feedback_form_submitBtn.addEventListener('click', (event) => {
    let inputList = document.querySelectorAll('.feedback_form input');
    let counter = 0;
    
    for(const input of inputList) {

        if(input.value != "") {
            counter++;
        }
    }
    
    if(counter == inputList.length) {
        event.preventDefault();
        removeClass(feedback_form, 'd-block')
    }


})
