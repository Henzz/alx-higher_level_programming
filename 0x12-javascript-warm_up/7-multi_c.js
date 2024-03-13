#!/usr/bin/node
const { argv } = require('node:process');

let arg1;
let i = 0;
argv.forEach((val, index) => { i++; });
if (i < 3) {
  console.log('Missing number of occurrences');
} else {
  argv.forEach((val, index) => {
    if (index === 2) {
      arg1 = parseInt(val);
      if (!isNaN(arg1) && arg1 > 0) {
        while (arg1) {
          console.log('C is fun');
          arg1--;
        }
      }
    }
  });
}
