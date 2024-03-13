#!/usr/bin/node
const { argv } = require('node:process');

let largest = 0;
let secondLargest = 0;
let i = 0;
argv.forEach((val, index) => { i++; });

if (i > 3) {
  argv.forEach((val, index) => {
    if (index >= 2) {
      if (val > largest) {
        secondLargest = largest;
        largest = val;
      } else if (val < largest && val > secondLargest) {
        secondLargest = val;
      }
    }
  });
}
console.log(parseInt(secondLargest));
