#!/usr/bin/node
const args = require('process');

function fact (x) {
  if (!x) {
    return 1;
  }
  if (x !== 0) {
    return x * fact(x - 1);
  } else {
    return 1;
  }
}

const result = fact(parseInt(args.argv[2]));
if (!args.argv[2]) {
  console.log(result);
}
if (parseInt(args.argv[2]) >= 0) {
  const result = fact(parseInt(args.argv[2]));
  console.log(result);
}
fact(parseInt(args.argv[2]));
