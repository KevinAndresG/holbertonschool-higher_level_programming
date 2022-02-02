#!/usr/bin/node

const { argv } = require('process');
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + argv[2];

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const bod = JSON.parse(body);
  console.log(bod.title);
});
