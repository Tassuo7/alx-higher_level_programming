#!/usr/bin/node
let logs = 0;
exports.logMe = function (item) {
  console.log(logs + ': ' + item);
  logs++;
};
