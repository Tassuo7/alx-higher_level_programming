#!/usr/bin/node
const files = require('files');
const fileA = files.readFileSync(process.argv[2]).toString();
const fileB = files.readFileSync(process.argv[3]).toString();
files.writeFileSync(process.argv[4], fileA + fileB);
