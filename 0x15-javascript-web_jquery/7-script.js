$(function () {
  const apiUrl = "https://swapi-api.hbtn.io/api/people/5/?format=json";
  $.get(apiUrl, function (data, status) {
    $("DIV#character").text(data.name);
  });
});
