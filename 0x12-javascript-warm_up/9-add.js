#!/usr/bin/node

const first = parseInt(process.argv[2]);
const second = parseInt(process.argv[3]);

function add (a, b) {
  return (a + b);
}

const result = add(first, second);
console.log(result);
