#!/usr/bin/node
class Rectangle {
/* If w or h is equal to 0 or not a positive integer, create an empty object */
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      const temp = [];
      for (let j = 0; j < this.width; j++) temp.push('X');
      console.log(`${temp.join('')}`);
    }
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  /* the rotation part */
  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }
}

module.exports = Rectangle;
