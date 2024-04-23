#!/usr/bin/node
const request = require('request');
const argv = require('process').argv;

let url = 'https://swapi-api.alx-tools.com/api/films/:id';
let id = 0;

argv.forEach(function (val, index) {
  if (index === 2) {
    id = val;
  }
});

url = url.replace(':id', id);

request.get(url, function (err, res, body) {
  if (err) {
    console.log(err);
    return;
  }

  if (res.statusCode === 200) {
    const data = JSON.parse(body);
    data.characters.forEach((val) => {
      getUser(val);
    });
  }
});

function getUser (url) {
  request.get(url, function (err, res, body) {
    if (err) {
      console.log(err);
      return;
    }

    if (res.statusCode === 200) {
      const data = JSON.parse(body);
      console.log(data.name);
    }
  });
}
