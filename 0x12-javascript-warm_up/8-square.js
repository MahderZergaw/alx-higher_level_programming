#!/usr/bin/node

const arg = process.argv[2];
const squareSize = parseInt(arg, 10);
const str = 'X';

if (Number.isInteger(squareSize)) {
  let row = 0;
  while (row < squareSize) {
    let col = 0;
    let squareCharacter = '';
    while (col < squareSize) {
      squareCharacter += str + '';
      col++;
    }
    console.log(squareCharacter);
    row++;
  }
} else {
  console.log('Missing size');
}
