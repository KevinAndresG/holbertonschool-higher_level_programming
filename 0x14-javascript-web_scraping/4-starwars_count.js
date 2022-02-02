#!/usr/bin/node

const { argv } = require('process');
const request = require('request');
const url = argv[2];

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const bod = JSON.parse(body);
  let cnt = 0;
  for (const i in bod.results) {
    for (let j in bod.results[i].characters) {
      if (bod.results[i].characters[j] === 'https://swapi-api.hbtn.io/api/people/18/') {
        cnt++;
      }
      j++;
    }
  }
  console.log(cnt);
});
