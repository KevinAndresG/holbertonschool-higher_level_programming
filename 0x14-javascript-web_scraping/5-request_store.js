#!/usr/bin/node

const fs = require('fs');
const { argv } = require('process');
const request = require('request');
const url = argv[2];

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  fs.writeFile(argv[3], body, 'utf8', function (err) {
    if (err) {
      return console.log(err);
    }
  });
});
