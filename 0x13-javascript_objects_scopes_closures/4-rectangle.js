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
    let x;
    let y;
    for (y = 0; y < this.width; y++) {
      let rect = '';
      for (x = 0; x < this.height; x++) {
        rect += 'X';
      }
      console.log(rect);
    }
  }

  double () {
    let x;
    let y;
    for (x = 0; x < (this.height * 2); x++) {
      let rect = '';
      for (y = 0; y < (this.width * 2); y++) {
        rect += 'X';
      }
      console.log(rect);
    }
  }
};
