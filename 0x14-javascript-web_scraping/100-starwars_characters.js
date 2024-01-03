#!/usr/bin/node
/* Prints all characters of Star Wars movie */

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/';

request(url, (err, response, body) => {
  if (err) console.log(err);
  else {
    const characters = JSON.parse(body).characters;
    for (let i = 0; i < characters.length; i++) {
      request(characters[i], (err, response, body) => {
        if (err) console.log(err);
        else console.log(JSON.parse(body).name);
      });
    }
  }
});
