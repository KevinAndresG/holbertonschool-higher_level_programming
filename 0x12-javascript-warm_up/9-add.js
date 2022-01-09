#!/usr/bin/node
const args = require('process');

function add (a, b) {
  console.log(a + b);
}
add(parseInt(args.argv[2]), parseInt(args.argv[3]));
