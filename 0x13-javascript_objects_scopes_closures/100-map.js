#!/usr/bin/node
const data = require('./100-data.js');
const listdt = data.list
console.log(listdt);
console.log(listdt.map((item, index) => item * index));
