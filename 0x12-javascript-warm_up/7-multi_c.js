#!/usr/bin/node
let reps = parseInt(process.argv[2]);
if (!reps) {
  console.log('Missing number of occurrences');
  process.exit();
}
while (reps-- > 0) {
  console.log('C is fun');
}
