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
var today = new Date();
if(today.getDay() == 4){
    document.getElementById("fhAnnouncment").style.display = "block";
    }
var today = new Date();
if(today.getDay() == 0){
    document.getElementById("ssAnnouncment").style.display = "block";
    }


imagesToLoad = document.querySelectorAll("img[data-src]");
imgOptions = {
    threshold: 1,
    rootMargin: "0px 0px 100px 0px"
};

    loadImages = (image) => {
    image.setAttribute('src', image.getAttribute('data-src'));
    image.onload = () => {
        image.removeAttribute('data-src');};
};
if('IntersectionObserver' in window) {
    const imgObserver = new IntersectionObserver((items, observer) => {
        items.forEach((item) => {
            if(item.isIntersecting) {
                loadImages(item.target);
                imgObserver.unobserve(item.target);
            }
        });
    }, imgOptions );

imagesToLoad.forEach((img) => {
    imgObserver.observe(img);
});
} 
else {
imagesToLoad.forEach((img) => {
    loadImages(img);
});
}
