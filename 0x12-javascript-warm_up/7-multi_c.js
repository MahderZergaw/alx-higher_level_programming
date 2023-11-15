#!/usr/bin/node
const argument = process.argv.slice(2);
const number = parseInt(argument[0]);
if (Number.isInteger(number)) {
  for (let i = 0; i < number; i++) {
    console.log('C is fun');
  }
} else { console.log('Missing number of occurrences'); }
