#!/usr/bin/node
function add (a, b) {
  const addit = a + b;
  console.log(addit);
}
add(Number(process.argv[2]), Number(process.argv[3]));
