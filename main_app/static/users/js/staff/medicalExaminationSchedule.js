const date_form_addBtn = document.querySelector('.btn-add-date_form');
const date_form_submitBtn = document.querySelector('.btn-date_form-submit');
const date_form_cancelBtn = document.querySelector('.btn-date_form-cancel');
const date_form = document.querySelector('.date_form');
const date_form_container = document.querySelector('.date_form .date_form-container');

function removeClass(form, className) {
    form.classList.remove(className)
}

date_form_addBtn.addEventListener('click', () => {
    date_form.classList.add('d-block')
})

date_form_cancelBtn.addEventListener('click', () => {
    removeClass(date_form, 'd-block')
})

date_form.addEventListener('click', () => {
    removeClass(date_form, 'd-block')
})

date_form_container.addEventListener('click', (event) => {
    event.stopPropagation();
})

date_form_submitBtn.addEventListener('click', (event) => {
    let inputList = document.querySelectorAll('.date_form input');
    let counter = 0;
    
    for(const input of inputList) {

        if(input.value != "") {
            counter++;
        }
    }
    
    if(counter == inputList.length) {
        event.preventDefault();
        
        let date = document.getElementById('date_form-date');
        let arrDate = date.value.split('/');
        console.log(arrDate);

        let content = document.getElementById('date_form-content');
        let location = document.getElementById('date_form-location');
        let doctor_name = document.getElementById('date_form-name');

        let table = document.querySelector('.table tbody');
        table.innerHTML += `
        <tr>
            <td>
                ${arrDate[1]}/${arrDate[0]}/${arrDate[2]}
            </td>
            <td>
                ${content.value}
            </td>
            <td>
                ${location.value}
            </td>
            <td>
                ${doctor_name.value}
            </td>
        </tr>
        `;
        removeClass(date_form, 'd-block');
    }


})