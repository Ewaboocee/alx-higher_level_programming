#!/usr/bin/node

class Rectangle {
  width;
  height;

  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      this.width;
      this.height;
    } else {
      this.width = w;
      this.height = h
    }
  }

  print () {
    for(let i = 0; i < this.height; i++){
      let line = '';
      for(let j = 0; j < this.width; j++){
	line += 'X';
      }
      console.log(line);
    }
  }
}


module.exports = Rectangle;
