#!/usr/bin/node

const request = require('request');
const ep_num = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

request(url + ep_num, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
