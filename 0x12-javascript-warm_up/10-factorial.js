#!/usr/bin/node
const { argv } = require('node:process');

function factorial (a) {
  if (isNaN(a)) {
    return 1;
  } else if (a < 0) {
    return -1;
  } else if (a === 0) {
    return (1);
  } else {
    return (a * factorial(a - 1));
  }
}

let arg1;
argv.forEach((val, index) => {
  if (index === 2) {
    arg1 = parseInt(val);
  }
});

console.log(factorial(arg1));
