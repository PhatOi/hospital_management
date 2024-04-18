// ------------------------------------------------------------------------
// Auto slide 

const prev_btn = document.querySelector('.bttn-prev');
const next_btn = document.querySelector('.bttn-next');

prev_btn.addEventListener("click", () => {
    let lists = document.querySelectorAll('.slide-item');
    document.querySelector('.slide-container').appendChild(lists[0]);
});

next_btn.addEventListener("click", () => {
    let lists = document.querySelectorAll('.slide-item');
    document.querySelector('.slide-container').prepend(lists[lists.length - 1]);
});

setInterval(() => {
    let lists = document.querySelectorAll('.slide-item');
    document.querySelector('.slide-container').appendChild(lists[0]);
}, 5000)