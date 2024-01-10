document.addEventListener('DOMContentLoaded', function() {
  const btnTranslate = document.querySelector('input#btn_translate');
  const languageCodeInput = document.querySelector('input#language_code');

  btnTranslate.addEventListener('click', translate);
  languageCodeInput.addEventListener('focus', function() {
    this.addEventListener('keydown', function(e) {
      if (e.keyCode === 13) {
        translate();
      }
    });
  });
});

function translate() {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  const languageCodeInput = document.querySelector('input#language_code');
  const helloDiv = document.querySelector('div#hello');

  fetch(url + new URLSearchParams({ lang: languageCodeInput.value }))
    .then(response => response.json())
    .then(data => helloDiv.innerHTML = data.hello);
}
