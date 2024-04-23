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

function getMovie (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (err) {
        reject(err);
        return;
      }

      if (res.statusCode === 200) {
        const movieData = JSON.parse(body);
        const characters = movieData.characters;
        resolve(characters);
      } else {
        reject(new Error('Something went wrong'));
      }
    });
  });
}

function getUser (url) {
  return new Promise((resolve, reject) => {
    request.get(url, function (err, res, body) {
      if (err) {
        reject(err);
        return;
      }
      resolve({ err, res, body });
    });
  });
}

getMovie(url)
  .then(async characters => {
    for (const valUrl of characters) {
      const res = await getUser(valUrl);

      if (!res.err && res.res.statusCode === 200) {
        const data = JSON.parse(res.body);
        console.log(data.name);
      } else {
        console.log(res);
      }
    }
  })
  .catch(err => {
    console.log(err.message);
  });
