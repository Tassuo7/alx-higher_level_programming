#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (!err) {
    const data = JSON.parse(body).results;
    console.log(data.reduce((count, film) => {
      return film.characters.find((character) => character.endsWith('/18/'))
        ? count++
        : count;
    }, 0));
  }
});
