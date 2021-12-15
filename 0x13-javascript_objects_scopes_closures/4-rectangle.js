#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w && h <= 0) {
      return 0;
    } else if (!(w && h)) {
      return 0;
    }
    this.width = w;
    this.height = h;
  }

  print () {
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

  rotate () {
   let temp = this.width;
   this.width = this.height;
   this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
