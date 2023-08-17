#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const ints = process.argv.slice(2).map(Number);
  const secbig = ints.sort(function (a, b) { return a - b; })[ints.length - 2];
  console.log(secbig);
}
