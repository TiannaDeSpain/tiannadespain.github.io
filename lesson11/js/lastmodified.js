document.getElementById('lastmodified').innerHTML = `Last Updated: ${document.lastModified}`;
document.getElementById('year').innerHTML = `&copy; ${new Date().getFullYear()}`;


let options = {
    weekday: "long",
    day: "numeric", 
    month: "long",
    year: "numeric"
};

document.getElementById("currentDate").textContent = new Date().toLocaleDateString("en-GB", options);
document.getElementById("currentYear").innerHTML = "&copy; " + new Date().getFullYear();