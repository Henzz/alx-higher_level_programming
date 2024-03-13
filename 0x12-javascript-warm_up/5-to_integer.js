#!/usr/bin/node
const { argv } = require('node:process');

let arg1;
argv.forEach((val, index) => {
  if (index === 2) {
    arg1 = parseInt(val);
    if (!isNaN(arg1)) {
      console.log(`My number: ${arg1}`);
    } else {
      console.log('Not a number');
    }
  }
});
