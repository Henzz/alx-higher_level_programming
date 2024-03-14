#!/usr/bin/node
const Square = require('./6-square');

const s1 = new Square(4);
s1.charPrint();

s1.charPrint('C');

const s2 = new Square(3);
s2.charPrint('D');
s2.double();
s2.charPrint('O');
