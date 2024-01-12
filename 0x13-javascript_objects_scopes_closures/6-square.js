#!/usr/bin/node

const s5 = require('./5-square');

module.exports = class Square extends s5 {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (str) {
    if (!str) {
      str = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      let row = '';
      for (let j = 0; j < this.size; j++) {
        row += str;
      }
      console.log(row);
    }
  }
};
