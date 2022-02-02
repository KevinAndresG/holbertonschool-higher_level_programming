#!/usr/bin/node

const { argv } = require('process');
const request = require('request');
const two = argv[2];
request(two, function (err, res, body) {
  console.log("code: " + res.statusCode);
});
