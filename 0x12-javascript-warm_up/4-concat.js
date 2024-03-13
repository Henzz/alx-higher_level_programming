#!/usr/bin/node
const { argv } = require('node:process');

let arg1;
let arg2;
argv.forEach((val, index) => {
  if (index === 2) {
    arg1 = val;
  }
  if (index === 3) {
    arg2 = val;
  }
});
console.log(`${arg1} is ${arg2}`);
