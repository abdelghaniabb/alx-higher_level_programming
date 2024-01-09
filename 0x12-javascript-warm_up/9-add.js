#!/usr/bin/node

const first = parseInt(process.argv[2]);
const second = parseInt(process.argv[3]);
let result;

function add(a, b) {
  return (a + b);
}

result = add(first, second);
console.log(result);
