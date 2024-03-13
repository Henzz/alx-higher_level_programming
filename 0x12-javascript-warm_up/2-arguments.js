#!/usr/bin/node
const { argv } = require('node:process');

// Check length of arguments
if (argv.length < 3) {
  console.log('No argument');
} else if (argv.length < 4) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
