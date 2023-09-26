#!/usr/bin/node
const fs = require('fs');
const fpath = process.argv[2];
fs.readFile(fpath, 'utf8', function (err_obj, fcont) {
  console.log(err_obj || fcont);
});
