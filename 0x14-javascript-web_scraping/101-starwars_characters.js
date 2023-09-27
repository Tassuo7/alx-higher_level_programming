#!/usr/bin/node
const request = require('request');
const mid = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
request(url + mid, function (err, response, body) {
  if (!err) {
    const charact = JSON.parse(body).characters;
    printCharacters(charact, 0);
  }
});

function printCharacters (charact, i) {
  request(charact[i], function (err, response, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (i + 1 < charact.length) {
        printCharacters(charact, i + 1);
      }
    }
  });
}
