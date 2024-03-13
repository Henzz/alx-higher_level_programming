#!/usr/bin/node
const { argv } = require('node:process');

let j;
let i = 0;
let str = '';
argv.forEach((val, index) => { i++; });
if (i < 3) {
  console.log('Missing size');
} else {
  argv.forEach((val, index) => {
    if (index === 2) {
      j = parseInt(val);
      i = 0;
      if (!isNaN(j)) {
        if (j > 0) {
          while (j) {
            while (i < parseInt(val)) {
              str += 'X';
              i++;
            }
            console.log(str);
            str = '';
            i = 0;
            j--;
          }
        }
      } else {
        console.log('Missing size');
      }
    }
  });
}
