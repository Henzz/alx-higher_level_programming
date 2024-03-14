#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    if (Object.keys(this).length === 0) {
      console.log('Empty object');
      return;
    }

    const row = 'X'.repeat(this.width);
    let i;
    for (i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
}

module.exports = Rectangle;
