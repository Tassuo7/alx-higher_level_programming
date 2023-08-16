#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const numb = Number(process.argv[2]);
  for (let i = 0; i < numb; i++) {
    console.log('X'.repeat(numb));
  }
}
