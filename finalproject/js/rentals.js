const requestURL = 'https://github.com/TiannaDeSpain/finalwebsitewdd230/blob/master/js/rentals.json';

fetch(requestURL)
  .then(function (response) {
    return response.json();
  })