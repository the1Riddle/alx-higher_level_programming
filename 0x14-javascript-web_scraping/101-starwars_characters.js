#!/usr/bin/node
/* Print all characters of Star wars api
in right order */
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`;

request(url, (err, res, body) => {
  if (err) console.log(err);
  const index = 0;
  const characters = JSON.parse(body).characters;
  printCharcter(characters, index);
});

const printCharcter = function (url, i) {
  request(url[i], (err, res, body) => {
    if (err) console.log(err);
    console.log(JSON.parse(body).name);
    if (++i < url.length) {
      printCharcter(url, i++);
    }
  });
};
