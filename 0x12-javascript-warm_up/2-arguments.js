#!/usr/bin/node
const args = require('process');
if (args.argv.length <= 2) {
  console.log('No argument');
} else if (args.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
