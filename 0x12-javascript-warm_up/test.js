const rows = 3;
const columns = 3;

// Use nested for loops to generate the pattern
for (let i = 0; i < rows; i++) {
  let row = '';
  for (let j = 0; j < columns; j++) {
    row += 'X';
  }
  console.log(row);
}
