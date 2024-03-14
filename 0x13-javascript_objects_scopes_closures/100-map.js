#!/usr/bin/node
const list = require('./100-data').list;

const map = list.map((val, index) => (val * index));
console.log(list);
console.log(map);
