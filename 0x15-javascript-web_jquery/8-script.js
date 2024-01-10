$(function () {
  const apiUrl = "https://swapi-api.hbtn.io/api/films/?format=json";
  $.get(apiUrl, function (data) {
    const titles = data.results;
    for (let i = 0; i < titles.length; i++) {
      $("UL#list_movies").append("<li>" + titles[i].title + "</li>");
    }
  });
});
