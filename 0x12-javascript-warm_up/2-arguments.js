#!/usr/bin/node
const { argv } = require('node:process');

// Check length of arguments
if (argv.length < 2) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
