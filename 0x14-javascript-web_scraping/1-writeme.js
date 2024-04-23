#!/usr/bin/node
const fs = require('fs');
const { argv } = require('node:process');

let file = '';
let str = '';

argv.forEach(function (val, index) {
  if (index === 2) {
    file = val;
  }
  if (index === 3) {
    str = val;
  }
});

fs.writeFile(file, str, 'utf-8', function (err, data) {
  if (err) {
    console.error(err);
  }
});
