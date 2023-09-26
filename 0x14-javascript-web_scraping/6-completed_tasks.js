#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const done = {};
    const tasks = JSON.parse(body);
    for (const t in tasks) {
      if (t.done) {
        if (!done[t.userId]) {
          done[t.userId] = 1;
        } else {
          done[t.userId]++;
        }
      }
    }
    console.log(done);
  }
});
