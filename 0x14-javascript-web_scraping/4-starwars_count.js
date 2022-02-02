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
  for (let i = 0; i < bod.count; i++) {
    let j = 0;
    while (j < bod.results[i].characters.length) {
      if (bod.results[i].characters[j] === 'https://swapi-api.hbtn.io/api/people/56/') {
        cnt++;
      }
      j++;
    }
  }
  console.log(cnt);
});
