#!/usr/bin/node

const args = require('process');
if (!parseInt(args.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(args.argv[2]));
}
