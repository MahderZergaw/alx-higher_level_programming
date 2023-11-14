#!/usr/bin/node
const argument = process.argv.slice(2);
if (argument[0] === undefined) {
  console.log('No argument');
} else {
  console.log(argument[0]);
}
