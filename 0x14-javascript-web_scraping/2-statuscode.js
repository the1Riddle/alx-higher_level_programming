#!/usr/bin/node
/* Displays the status code of a GET request */

const request = require('request');
const url = process.argv[2];

request(url, (err, response) => {
  if (err) console.log(err);
  else console.log('code:', response.statusCode);
});
