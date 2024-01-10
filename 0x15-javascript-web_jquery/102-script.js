document.addEventListener('DOMContentLoaded', function() {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  const btnTranslate = document.querySelector('input#btn_translate');
  const languageCodeInput = document.querySelector('input#language_code');
  const helloDiv = document.querySelector('div#hello');

  btnTranslate.addEventListener('click', function() {
    const lang = languageCodeInput.value;
    fetch(url + new URLSearchParams({ lang }))
      .then(response => response.json())
      .then(data => helloDiv.innerHTML = data.hello);
  });
});
