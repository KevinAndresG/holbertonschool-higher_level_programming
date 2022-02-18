$(document).ready(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    // const bod = JSON.parse(data);
    for (i in data.results) {
      for (j in data.results[i]) {
        if (j === "title") {
          $('#list_movies').append('<li>' + data.results[i][j]);
        }
      }
    }
  });
});
