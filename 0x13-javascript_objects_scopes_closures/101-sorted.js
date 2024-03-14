#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = {};
for (const key of Object.keys(dict)) {
  const val = dict[key];

  if (newDict[val]) {
    newDict[val].push(key);
  } else {
    newDict[val] = [key];
  }
}
console.log(newDict);
