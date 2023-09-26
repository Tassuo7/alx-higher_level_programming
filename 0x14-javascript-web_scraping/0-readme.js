#!/usr/bin/node
const fs = require('fs');
const fpath = process.argv[2];
fs.readFile(fpath, 'utf8', function (err, fcont) {
  console.log(err || fcont);
});
