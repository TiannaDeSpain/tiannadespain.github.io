
$.getJSON("https://tiannadespain.github.io/finalproject/data/rentals.json", function(json) {
    console.log(json); 
  var data = json;
  data.forEach(tablerow);

  function tablerow(item) {
    let table = document.getElementById("rentalsTable")
    let tr = document.createElement("tr")
    let RentalType = document.createElement('td');
    let MaxPersons = document.createElement('td');
    let ReservationsHalf = document.createElement('td');
    let ReservationsWhole = document.createElement('td');
    let WalkHalf = document.createElement('td');
    let WalkWhole = document.createElement('td');

    RentalType.innerHTML =  item.RentalType;
    MaxPersons.innerHTML =  item.MaxPersons;
    ReservationsHalf.innerHTML =  item.ReservationsHalf;
    ReservationsWhole.innerHTML =  item.ReservationsWhole;
    WalkHalf.innerHTML =  item.WalkHalf;
    WalkWhole.innerHTML = item.WalkWhole;

    tr.appendChild(RentalType);
    tr.appendChild(MaxPersons);
    tr.appendChild(ReservationsHalf);
    tr.appendChild(ReservationsWhole);
    tr.appendChild(WalkHalf);
    tr.appendChild(WalkWhole);

    table.appendChild(tr)

    let link = document.getElementById(item.id)

    let text = link.textContent
    text = text + " " + item.ReservationsHalf + "!"
    link.textContent = text

   
  }
});