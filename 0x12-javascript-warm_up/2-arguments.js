#!/usr/bin/node
const { argv } = require('node:process');

// Check length of arguments
if (argv.length < 3) {
	return console.log('No argument');
}
console.log('Arguments found');
