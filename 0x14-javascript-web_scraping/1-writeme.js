#!/usr/bin/node
const { argv } = require('process');
const fs = require('fs');

fs.writeFile(argv[2], argv[3], 'utf8', function (err) {
  if (err) {
    return console.log(err);
  }
});
