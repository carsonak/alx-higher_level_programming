#!/usr/bin/node
const nums = process.argv.slice(2).map((n) => parseInt(n));
let biggest = nums.length > 1 ? nums[0] : 0;
let secondBiggest = biggest;
if (nums.length > 1) {
  nums.forEach((n) => {
    if (n > biggest) {
      secondBiggest = biggest;
      biggest = n;
    }
    if ((secondBiggest >= biggest || secondBiggest < n) && n < biggest) {
      secondBiggest = n;
    }
  });
}
console.log(secondBiggest);
