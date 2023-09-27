#!/usr/bin/node
const request = require('request');
const mid = process.argv[2];
const swapi = 'https://swapi-api.hbtn.io/api/films/';

request.get(swapi + mid, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const caract = JSON.parse(body).characters;
  for (const c of caract) {
    request.get(c, function (err, response, body) {
      if (err) {
        console.log(err);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
