#!/usr/bin/node
const request = require('request');
const { argv } = require('node:process');

let url = '';

argv.forEach(function (val, index) {
  if (index === 2) {
    url = val;
  }
});

request
  .get(url)
  .on('response', function (res) {
    console.log('code:', res.statusCode);
  });
