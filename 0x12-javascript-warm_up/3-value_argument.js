#!/usr/bin/node
const { argv } = require('node:process');

let i = 0;
argv.forEach((val, index) => { i++; });
if (i < 3) {
  console.log('No argument');
} else {
  argv.forEach((val, index) => {
    if (index > 1) {
      console.log(val);
    }
  });
}
