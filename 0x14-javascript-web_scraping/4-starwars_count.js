#!/usr/bin/node
const request = require('request');
const argv = require('process').argv;

let url = '';
const id = 18;

argv.forEach(function (val, index) {
  if (index === 2) {
    url = val;
  }
});

request.get(url, function (err, res, body) {
  if (err) {
    console.log(err);
    return;
  }

  if (res.statusCode === 200) {
    const data = JSON.parse(body).results;
    let count = 0;
    data.forEach((val) => {
      if (val.characters.length) {
        const counts = val.characters.filter((v) => v.includes(id));
        count += counts.length;
      }
    });
    console.log(count);
  }
});
