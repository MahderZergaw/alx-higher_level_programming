#!/usr/bin/node
const argument = process.argv.slice(2);
const number = parseInt(argument[0]);
if (Number.isInteger(number)) { console.log('My number: ', number); } else { console.log('Not a number'); }
