#!/usr/bin/node
const fs = require('fs');
const argv = require('process').argv;
const request = require('request');

let url = '';
let file = '';
let str = '';

argv.forEach(function (val, index) {
  if (index === 2) {
    url = val;
  }
  if (index === 3) {
    file = val;
  }
});

request.get(url, function (err, res, body) {
  if (err) {
    console.log(err);
    return;
  }

  str = body;
  fs.writeFile(file, str, 'utf-8', function (err, data) {
    if (err) {
      console.error(err);
    }
  });
});
