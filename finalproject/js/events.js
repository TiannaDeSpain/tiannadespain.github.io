
const requestURL = 'https://byui-cit230.github.io/weather/data/towndata.json';

fetch(requestURL)
  .then(function (response) {
    return response.json();
  })
  .then(function (jsonObject) {
    const events = jsonObject['towns']; 
    let list = document.createElement('ul');
    var name = document.getElementById('title');
    let title = document.createElement('h3');
    let temp
    let div =  document.getElementById("events");


    for (let i = 0; i < events.length; i++ ) {
        // debugger
        if (events[i].name == name.textContent){
            for (let j=0; j<events[i].events.length; j++){
                title.textContent = events[i].name + ' Upcoming Events:'
                temp = document.createElement("li")
                temp.textContent = events[i].events[j]
                list.appendChild(temp)
            }
        }
           }
           div.appendChild(title);
           div.appendChild(list); 
}
);
