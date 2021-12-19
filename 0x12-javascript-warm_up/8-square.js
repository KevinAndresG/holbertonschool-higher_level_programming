#!/usr/bin/node

const args = require('process');
let x = 0;
let y = 0;
if (!parseInt(args.argv[2])) {
  console.log('Missing size');
} else {
  for (x = 0; x < parseInt(args.argv[2]); x++) {
    let square = '';
    for (y = 0; y < parseInt(args.argv[2]); y++) {
      square += 'X';
    }
    console.log(square + ' ');
  }
}
