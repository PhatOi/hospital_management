let action_form_btns = document.querySelectorAll('.btn-action_form');
let action_form_submit_btn = NaN;
let action_form_cancel_btn = NaN;
let action_form_container = document.querySelector('.action_form .action_form-container')
let action_form = document.querySelector('.action_form')

// ------------------------------------------------------------------------
// ACTION FORM
function removeClass(form, className) {
    form.classList.remove(className)
}

function inputTypeCheck(th) {
    if(th.innerHTML == "Hạn sử dụng" || th.innerHTML == "Thời gian")
        return 'type=date'
    else if(th.innerHTML == "Số lượng") 
        return 'type=number'
    else return 'type=text'
}

function inProccess(th) {
    if(th.innerHTML == "Tiến trình")
        return '<span style="width:1%; display:inline-block">%</span>'
    else return ''
}

function format_action_form(action_form_btn) {
    // Take header
    const title = document.querySelector('.action_form .card-title');
    title.innerHTML = action_form_btn.innerText;

    // Select th tag needed
    let ths;
    switch (action_form_btn.innerText) {
        case "Thêm nhân viên":
            ths = document.querySelectorAll('#staffList table th')
            break;
        
        case "Thêm bệnh nhân":
            ths = document.querySelectorAll('#patientList table th')
            break;

        case "Thêm loại thuốc":
            ths = document.querySelectorAll('#pillList table th')
            break;

        case "Thêm thiết bị":
            ths = document.querySelectorAll('#equipmentList table th')
            break;
        
        default:
            break;
    }

    // Format form
    const action_form_sample = document.querySelector('.action_form .forms-sample');

    action_form_sample.innerHTML = "";

    for(const th of ths) 
        if(th.innerHTML == 'Tên bệnh nhân' || th.innerHTML == 'Tên nhân viên') {
            action_form_sample.innerHTML += `
            <div class="form-group">
                <label for="name">${th.innerHTML}</label>
                <input type="text" class="form-control" id="action_form-name" required autocomplete="off">
                <label for="job">Nghề nghiệp</label>
                <input type="text" class="form-control" id="action_form-name" required autocomplete="off">
            </div>
            `
        }
        else if(th.innerHTML == "Tiến trình") {
            action_form_sample.innerHTML += `
            <div class="form-group">
                <label for="name" class="d-block">${th.innerHTML}</label>
                <input type="number" class="form-control" id="action_form-name" style="width:98%; display: inline-block" required autocomplete="off">
                ${inProccess(th)}
            </div>
            `
        }
        else if(th.innerText != "") {
            action_form_sample.innerHTML += `
            <div class="form-group">
                <label for="name">${th.innerHTML}</label>
                <input ${inputTypeCheck(th)} class="form-control" id="action_form-name" required autocomplete="off">
            </div>
            `
        } 

    action_form_sample.innerHTML += `
        <button type="submit" class="btn btn-action_form-submit btn-submit btn-primary me-2">Submit</button>
        <button class="btn btn-action_form-cancel btn-light">Cancel</button>
    `

    return;
}

function proccessType(value) {
    if(value < 30) return 'danger'
    else if(value < 70) return 'warning'
    else return 'success'
}

function dateConvert(input) {
    let arrDate = input.split('-');
    return `${arrDate[2]}/${arrDate[1]}/${arrDate[0]}`
}

function addRow(inputs, listType) {
    let row;
    
    for(const input of inputs) console.log(input.value);

    switch (listType) {
        case "Thêm nhân viên":
            row = document.querySelector('#staffList table tbody')
            row.innerHTML += `
            <tr>
                <td>
                    <div class="delete_btn form-check form-check-flat mt-0 h2">
                        <i class="mdi mdi-delete" title="Delete"></i>
                    </div>
                </td>
                <td>
                    <div class="d-flex ">
                        <img src="images/faces/face1.jpg" alt="">
                        <div>
                        <h6>${inputs[0].value}</h6>
                        <p>${inputs[1].value}</p>
                        </div>
                    </div>
                </td>
                <td>
                    ${inputs[2].value}
                </td>
                <td>
                    ${inputs[3].value}
                </td>
                <td>
                    ${inputs[4].value}
                </td>
                <td>
                    <div>
                        <div class="d-flex justify-content-between align-items-center mb-1 max-width-progress-wrap">
                            <p class="text-${proccessType(Number(inputs[5].value))}">${inputs[5].value}%</p>
                            <p>85/162</p>
                        </div>
                        <div class="progress progress-md">
                            <div class="progress-bar bg-${proccessType(Number(inputs[5].value))}" role="progressbar" style="width:${inputs[5].value}%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
                        </div>
                    </div>
                </td>
                <td><div class="badge badge-opacity-warning">${inputs[6].value}</div></td>
            </tr>
            `
            break;
    
        case "Thêm bệnh nhân":
            row = document.querySelector('#patientList table tbody')
            row.innerHTML += `
            <tr>
                <td>
                    <div class="delete_btn form-check form-check-flat mt-0 h2">
                        <i class="mdi mdi-delete" title="Delete"></i>
                    </div>
                </td>
                <td>
                    <div class="d-flex ">
                        <img src="images/faces/face1.jpg" alt="">
                        <div>
                            <h6>${inputs[0].value}</h6>
                            <p>${inputs[1].value}</p>
                        </div>
                    </div>
                </td>
                <td>
                    ${inputs[2].value}
                </td>
                <td>
                    ${inputs[3].value}
                </td>
                <td>
                    <div>
                        <div class="d-flex justify-content-between align-items-center mb-1 max-width-progress-wrap">
                            <p class="text-${proccessType(Number(inputs[4].value))}">${inputs[4].value}%</p>
                            <p>85/162</p>
                        </div>
                        <div class="progress progress-md">
                            <div class="progress-bar bg-${proccessType(Number(inputs[4].value))}" role="progressbar" style="width: ${inputs[4].value}%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
                        </div>
                    </div>
                </td>
                <td>
                    ${inputs[5].value}
                </td>
            </tr>
            `
            break;

        case "Thêm loại thuốc":
            row = document.querySelector('#pillList table tbody')
            row.innerHTML += `
            <tr>
                <td>
                    <div class="delete_btn form-check form-check-flat mt-0 h2">
                        <i class="mdi mdi-delete" title="Delete"></i>
                    </div>
                </td>
                <td>
                    ${inputs[0].value}
                </td>
                <td>
                    ${inputs[1].value}
                </td>
                <td>
                    ${inputs[2].value}
                </td>
                <td>
                    ${dateConvert(inputs[3].value)}
                </td>
            </tr>
            `
            break;

        case "Thêm thiết bị":
            row = document.querySelector('#equipmentList table tbody')
            row.innerHTML += `
            <tr>
                <td>
                    <div class="delete_btn form-check form-check-flat mt-0 h2">
                        <i class="mdi mdi-delete" title="Delete"></i>
                    </div>
                </td>
                <td>
                    <div class="badge badge-opacity-success">${inputs[0].value}</div>
                </td>
                <td>
                    ${inputs[1].value}
                </td>
                <td>
                    ${inputs[2].value}
                </td>
                <td>
                    ${dateConvert(inputs[3].value)}
                </td>
            </tr>
            `
            break;
        
        default:
            break;
    }
}

function cancel_btn() {
    action_form_cancel_btn.addEventListener('click', (event) => {
        event.preventDefault();
        removeClass(action_form, 'd-block')
    })
}

function sumbit_btn(action_form_btn) {
    action_form_submit_btn.addEventListener('click', (event) => {
        let inputList = document.querySelectorAll('.action_form input');
        let counter = 0;
        
        for(const input of inputList) {
    
            if(input.value != "") {
                counter++;
            }
        }

        if(counter == inputList.length) {
            event.preventDefault();
            
            addRow(inputList, action_form_btn.innerText)

            delete_form_delete_btns = document.querySelectorAll('.delete_btn');

            clickListen(delete_form_delete_btns);

            removeClass(action_form, 'd-block')
        }
    })
}

for(const action_form_btn of action_form_btns) {
    action_form_btn.addEventListener('click', () => {
        action_form.classList.add('d-block');

        format_action_form(action_form_btn);

        // Select btn and add event listener
        action_form_submit_btn = document.querySelector('.btn-action_form-submit');
        action_form_cancel_btn = document.querySelector('.btn-action_form-cancel');

        cancel_btn();

        sumbit_btn(action_form_btn)
    })
}

action_form.addEventListener('click', () => {
    removeClass(action_form, 'd-block')
})

action_form_container.addEventListener('click', (event) => {
    event.stopPropagation();
})


// -----------------------------------------------------------------------------
// Delete object

let delete_form_delete_btns = document.querySelectorAll('.delete_btn');
let delete_form_submit_btn = NaN;
let delete_form_cancel_btn = NaN;
const delete_form = document.querySelector('.delete_form');
const delete_form_container = document.querySelector('.delete_form .delete_form-container');
const delete_form_sample = document.querySelector('.delete_form .forms-sample')
const prev_delete_form_sample = delete_form_sample.innerHTML;

function delete_form_reset() {
    delete_form.classList.remove('d-block')

    delete_form_sample.innerHTML = prev_delete_form_sample;
}

function printHTML(node) {
    return node.innerHTML;
}

function clickListen(delete_form_delete_btns) {
    for(const delete_btn of delete_form_delete_btns) {
        delete_form_delete_btns = document.querySelectorAll('.delete_btn');
    
        delete_btn.addEventListener('click', () => {
    
            console.log(delete_form_delete_btns);
            delete_form.classList.add('d-block');
    
            const tr = delete_btn.parentElement.parentElement;
            const thead = tr.parentElement.previousElementSibling;
            const tdList = tr.children;
    
            delete_form_sample.innerHTML = `
            <div class="table-responsive my-2 border-top border-bottom"> 
                <table class="table select-table">
                    <thead>
                        ${printHTML(thead)}
                    </thead>
                    <tbody>
                        <tr>
                            ${printHTML(tr)}
                        </tr>
                    </tbody>
                </table>
            </div>
            ` + delete_form_sample.innerHTML;
    
            delete_form_submit_btn = document.querySelector('.btn-delete_form-submit');
            delete_form_cancel_btn = document.querySelector('.btn-delete_form-cancel');
    
            delete_form_cancel_btn.addEventListener('click', () => {
                delete_form_reset();
            })
    
            delete_form_submit_btn.addEventListener('click', () => {
                tr.remove();
    
                delete_form_reset();
            })
        })
    }
}

clickListen(delete_form_delete_btns);

delete_form.addEventListener('click', () => {
    delete_form_reset();
})

delete_form_container.addEventListener('click', (e) => {
    e.stopPropagation();
})