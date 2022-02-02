#!/usr/bin/node

const { argv } = require('process');
const { request } = require('http');

const response = request.get(argv[2], res => {
  console.log('Code: ' + res.statusCode);
});
response.end();
