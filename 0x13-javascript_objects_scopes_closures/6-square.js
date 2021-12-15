#!/usr/bin/node
const Rectangle = require('./5-square');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
        let x;
        let y;
        for (x = 0; x < this.height; x++) {
          let rect = '';
          for (y = 0; y < this.width; y++) {
            rect += c;
          }
          console.log(rect);
        }
    } else {
      let x;
        let y;
        for (x = 0; x < this.height; x++) {
          let rect = '';
          for (y = 0; y < this.width; y++) {
            rect += 'X';
          }
          console.log(rect);
        }
    }
  }
};
