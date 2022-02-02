#!/usr/bin/node

const { argv } = require('process');
const https = require('https');

const response = https.get(argv[2], res => {
  console.log("Code: " + res.statusCode);
});
response.end();
