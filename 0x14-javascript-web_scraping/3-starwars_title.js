#!/usr/bin/node

const request = require('request');
const epnum = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

request(url + epnum, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
