
var high = document.getElementById("high")
var current = document.getElementById("current")
var humid = document.getElementById("humid")
var speed = document.getElementById("speed")

var fiveday = document.getElementById("fiveday")
var fourday = document.getElementById("fourday")
var threeday = document.getElementById("threeday")
var twoday = document.getElementById("twoday")
var oneday = document.getElementById("oneday")

var oneimg = document.getElementById("oneimg")
var twoimg = document.getElementById("twoimg")
var threeimg = document.getElementById("threeimg")
var fourimg = document.getElementById("fourimg")
var fiveimg = document.getElementById("fiveimg")

var onespan = document.getElementById("onespan")
var twospan = document.getElementById("twospan")
var threespan = document.getElementById("threespan")
var fourspan = document.getElementById("fourspan")
var fivespan = document.getElementById("fivespan")

const apiURL = "https://api.openweathermap.org/data/2.5/weather?id=5607916&appid=64286fe075e1c1e85b00043631a855cb&units=imperial";
fetch(apiURL)
  .then((response) => response.json())
  .then((jsObject) => {
    console.log(jsObject);
    high.innerHTML = Math.round(jsObject.main.temp_max)
    current.innerHTML = jsObject.weather[0].main
    humid.innerHTML = jsObject.main.humidity
    speed.innerHTML = Math.round(jsObject.wind.speed)
  });
const apiURL2 = "https://api.openweathermap.org/data/2.5/forecast?id=5607916&appid=64286fe075e1c1e85b00043631a855cb&units=imperial";
fetch(apiURL2)
  .then((response) => response.json())
  .then((jsObject) => {
    console.log(jsObject);
    var list = jsObject.list.filter(x => x.dt_txt.includes("18:00:00"))
    date = new Date(list[0].dt_txt)
    oneday.innerHTML = dayAsString(date.getDay());
    onespan.innerHTML = Math.round(jsObject.list[0].main.temp_max)
    oneimg.setAttribute('src', 'https://api.openweathermap.org/img/w/' + list[0].weather[0].icon + '.png');
    twoday.innerHTML = dayAsString(date.getDay()+1);
    twospan.innerHTML = Math.round(jsObject.list[1].main.temp_max)
    twoimg.setAttribute('src', 'https://api.openweathermap.org/img/w/' + list[1].weather[0].icon + '.png');
    threeday.innerHTML = dayAsString(date.getDay()+2);
    threespan.innerHTML = Math.round(jsObject.list[2].main.temp_max)
    threeimg.setAttribute('src', 'https://api.openweathermap.org/img/w/' + list[2].weather[0].icon + '.png');
    fourday.innerHTML = dayAsString(date.getDay()+3);
    fourspan.innerHTML = Math.round(jsObject.list[3].main.temp_max)
    fourimg.setAttribute('src', 'https://api.openweathermap.org/img/w/' + list[3].weather[0].icon + '.png');
    fiveday.innerHTML = dayAsString(date.getDay()+4);
    fivespan.innerHTML = Math.round(jsObject.list[4].main.temp_max)
    fiveimg.setAttribute('src', 'https://api.openweathermap.org/img/w/' + list[4].weather[0].icon + '.png'); 
  });

  function dayAsString(dayIndex){
    var weekdays = new Array(7);
    weekdays[0] = "Sunday";
    weekdays[1] = "Monday";
    weekdays[2] = "Tuesday";
    weekdays[3] = "Wednesday";
    weekdays[4] = "Thursday";
    weekdays[5] = "Friday";
    weekdays[6] = "Saturday";
    return weekdays[dayIndex];
  }


