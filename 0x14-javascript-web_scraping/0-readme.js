#!/usr/bin/node
const fs = require('fs');
const { argv } = require('node:process');

let file = '';

argv.forEach(function (val, index) {
  if (index === 2) {
    file = val;

    fs.readFile(file, 'utf-8', function (err, data) {
      if (err) {
        console.error(err);
        return;
      }
      console.log(data);
    });
  }
});
