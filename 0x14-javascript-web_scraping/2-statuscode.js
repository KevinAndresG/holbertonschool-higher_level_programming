#!/usr/bin/node

const { argv } = require('process');
const https = require('https');

const option = {
  method : "GET"
}

const response = https.request(argv[2], option, res => {
  console.log('Code: ' + res.statusCode);
});
response.end();
