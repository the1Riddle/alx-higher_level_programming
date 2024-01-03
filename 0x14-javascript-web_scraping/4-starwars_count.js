#!/usr/bin/node
/* Display the number of movie the character
Wedge Antilles is present */

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (err, response, body) => {
  if (err) console.log(err);
  else {
    let count = 0;
    const results = JSON.parse(body).results;
    for (let i = 0; i < results.length; i++) {
      const characters = results[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].search('18') > 0) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
