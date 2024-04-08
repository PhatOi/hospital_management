
document.querySelector('.next').onclick = function(){
    let lists = document.querySelectorAll('.month');
    document.querySelector('.months ul').appendChild(lists[0]);
}

document.querySelector('.prev').onclick = function(){
    let lists = document.querySelectorAll('.month');
    document.querySelector('.months ul').prepend(lists[lists.length - 1]);
}

var date = new Date();
var days = document.querySelectorAll('.day');

for(const day of days) {
   if(day.innerHTML == date.getDate()) day.innerHTML = `<span class="active">${day.innerHTML}</span>`;
}
console.log(date.getDate());