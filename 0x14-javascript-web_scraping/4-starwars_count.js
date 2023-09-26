#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (!err) {
    const data = JSON.parse(body).results;
    let count = 0;
    data.forEach(film => {
      if (film.character.endsWith('/18/')) count++;
    });
    console.log(count);
  }
});
