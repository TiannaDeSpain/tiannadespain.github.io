
const requestURL = 'https://byui-cit230.github.io/weather/data/towndata.json';

fetch(requestURL)
  .then(function (response) {
    return response.json();
  })
  .then(function (jsonObject) {
    const towns = jsonObject['towns']; 
    for (let i = 0; i < towns.length; i++ ) {
        if(towns[i].name =="Fish Haven" || towns[i].name =="Preston" || towns[i].name =="Soda Springs") {
            let town = document.createElement('div');
            let h2 = document.createElement('h2');
            let motto = document.createElement('h3')
            let yearFounded = document.createElement('p')
            let currentPopulation = document.createElement('p')
            let averageRainfall = document.createElement('p')
            let image = document.createElement('img')

        h2.textContent = towns[i].name + ' ';
        motto.innerHTML =  towns[i].motto;
        yearFounded.innerHTML = "Year Found: " + towns[i].yearFounded;
        currentPopulation.innerHTML = "Current Population: " + towns[i].currentPopulation;
        averageRainfall.innerHTML = "Average Rainfall: " + towns[i].averageRainfall;
    
        image.src = `images/${towns[i].photo}`;
        image.setAttribute('alt', towns[i].name);
        town.setAttribute("class", "city")
        town.appendChild(h2);
        town.appendChild(motto);
        
        town.appendChild(yearFounded);
        town.appendChild(currentPopulation);
        town.appendChild(averageRainfall);
        town.appendChild(image);

        document.querySelector('div.towns').appendChild(town);
        
    }}
});
