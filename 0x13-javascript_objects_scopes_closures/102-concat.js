#!/usr/bin/node
const { argv } = require('node:process');
const fs = require('fs');

function concatFiles (file1, file2, destFile) {
  const cont1 = fs.readFileSync(file1, 'utf8');
  const cont2 = fs.readFileSync(file2, 'utf8');
  fs.writeFileSync(destFile, cont1 + cont2);
}

const file1 = argv[2];
const file2 = argv[3];
const file3 = argv[4];

if (file1 && file2 && file3) {
  concatFiles(file1, file2, file3);
}
