#!/usr/bin/node
const request = require('request');
const argv = require('process').argv;

let url = '';

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
    const data = JSON.parse(body);
    const users = {};
    data.forEach((val, index) => {
      if (val.completed === true && !users[val.userId]) {
        const counts = data.filter((v) => v.completed === true && v.userId === val.userId);
        users[val.userId] = counts.length;
      }
    });
    console.log(users);
  }
});
