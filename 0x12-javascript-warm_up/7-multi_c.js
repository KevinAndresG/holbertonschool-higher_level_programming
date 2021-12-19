#!/usr/bin/node

const args = require('process');
let x = 0;

if (!parseInt(args.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (x; x < parseInt(args.argv[2]); x++) {
    console.log('C is fun');
  }
}
