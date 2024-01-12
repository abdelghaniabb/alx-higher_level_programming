#!/usr/bin/node

const len = process.argv.length;

if (len <= 3) {
  console.log(0);
} else {
  let firstBiggest = parseInt(process.argv[2]);
  let secondBiggest = parseInt(process.argv[2]);
  for (let i = 3; i < len; i++) {
    if (firstBiggest < parseInt(process.argv[i])) {
      secondBiggest = firstBiggest;
      firstBiggest = parseInt(process.argv[i]);
    } else if (secondBiggest < parseInt(process.argv[i])) {
      secondBiggest = parseInt(process.argv[i]);
    }
  }
  console.log(secondBiggest);
}
