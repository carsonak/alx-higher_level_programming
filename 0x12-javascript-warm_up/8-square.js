#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (!size || size < 0) {
  process.exit();
}
let filler = '';
for (let i = 0; i < size; i++) {
  filler += 'X';
}
for (let i = 0; i < size; i++) {
  console.log(filler);
}
