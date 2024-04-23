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

getMovie(url)
  .then(characters => {
    characters.forEach(valUrl => {
      request.get(valUrl, function (err, res, body) {
        if (!err && res.statusCode === 200) {
          const data = JSON.parse(body);
          console.log(data.name);
        }
      });
    });
  })
  .catch(err => {
    console.log(err.message);
  });
