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
};
