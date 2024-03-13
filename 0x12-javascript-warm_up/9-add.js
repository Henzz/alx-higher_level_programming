#!/usr/bin/node
const { argv } = require('node:process');

function add (a, b) {
  return a + b;
}

let arg1;
let arg2;
argv.forEach((val, index) => {
  if (index === 2) {
    arg1 = parseInt(val);
  }
  if (index === 3) {
    arg2 = parseInt(val);
  }
});

console.log(add(arg1, arg2));
