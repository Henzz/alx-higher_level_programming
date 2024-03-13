#!/usr/bin/node
const val = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let string = '';
let i = 0;
while (val[i]) {
  string += val[i];
  string += val[i + 1] ? '\n' : '';
  i++;
}
console.log(string);
