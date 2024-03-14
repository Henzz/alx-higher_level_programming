#!/usr/bin/node
const Square5 = require('./5-square');

class Square extends Square5 {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    const row = c.repeat(this.size);
    for (let i = 0; i < this.size; i++) {
      console.log(row);
    }
  }

  double () {
    this.size *= 2;
  }
}

module.exports = Square;
