const hambutton = document.querySelector('.menu');
const mainnav = document.querySelector('.navigation')

hambutton.addEventListener('click', () => {mainnav.classList.toggle('responsive')}, false);

window.onresize = () => {if (window.innerWidth > 760) mainnav.classList.remove('responsive')};

let options = {
    weekday: "long",
    day: "numeric", 
    month: "long",
    year: "numeric"
};

document.getElementById("currentDate").textContent = new Date().toLocaleDateString("en-GB", options);

var today = new Date();
if(today.getDay() == 5){
    document.getElementById("announcment").style.display = "block";
    }