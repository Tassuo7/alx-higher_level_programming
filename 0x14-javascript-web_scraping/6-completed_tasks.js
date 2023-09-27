#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, function (err, response, body) {
  if (err) console.log(error);
  else if (response.statusCode === 200) {
    const done = {};
    for (let i = 0; i < JSON.parse(body).length; i++) {
      const task = JSON.parse(body)[i];
      if (task.userId in done && task.completed) {
        done[task.userId] += 1;
      } else if (!(task.userId in done) && task.completed) {
        done[task.userId] = 1;
      }
    }
    console.log(done);
  }
});
