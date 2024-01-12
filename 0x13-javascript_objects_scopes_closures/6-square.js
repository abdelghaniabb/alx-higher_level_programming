#!/usr/bin/node

const s5 = require('./5-square');

module.exports = class Square extends s5 {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      let row = '';
      for (let j = 0; j < this.size; j++) {
        row += c;
      }
      console.log(row);
    }
  }

  double () {
    this.size = this.size * 2;
  }
};
