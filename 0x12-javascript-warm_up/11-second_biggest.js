#!/usr/bin/node

const len = process.argv.length;

if (len <= 3) {
  console.log(0);
} else {
  let firstBiggest = process.argv[2];
  let secondBiggest = process.argv[2];
  for (let i = 3; i < len; i++) {
    if (firstBiggest < process.argv[i]) {
      secondBiggest = firstBiggest;
      firstBiggest = process.argv[i];
    } else if (secondBiggest < process.argv[i]) {
      secondBiggest = process.argv[i];
    }
  }
  console.log(secondBiggest);
}
