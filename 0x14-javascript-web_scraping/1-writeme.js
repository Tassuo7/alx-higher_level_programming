#!/usr/bin/node
const fs = require('fs');
const fpath = process.argv[2];
const stw = process.argv[3];
fs.writeFile(fpath, stw, err => {
  if (err) console.log(err);
});
