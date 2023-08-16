#!/usr/bin/node
const SprSquare = require('./5-square');
class Square extends SprSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let prC = '';
      for (let j = 0; j < this.width; j++) {
        prC += c;
      }
      console.log(s);
    }
  }
}
module.exports = Square;
