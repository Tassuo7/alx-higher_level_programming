#!/usr/bin/node
const argpas = process.argv.length;
if (argpas === 2) {
	  console.log('No argument');
} else if (argpas === 3) {
	  console.log('Argument found');
} else {
	  console.log('Arguments found');
}
