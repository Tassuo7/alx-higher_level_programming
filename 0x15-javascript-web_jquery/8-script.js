$(document).ready(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.get(url, function (data) {
    data.results.forEach(function (movie) {
      const lis = $('<li>').text(movie.title);
      $('UL#list_movies').append(lis);
    });
  });
});
