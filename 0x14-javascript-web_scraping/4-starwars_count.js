#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

request(argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const bod = JSON.parse(body);
  let cnt = 0;
  for (let i = 0; i < bod.count; i++) {
    let j = 0;
    const len = bod.results[i].characters.length;
    while (j < len) {
      if (bod.results[i].characters[j] === 'https://swapi-api.hbtn.io/api/people/18/') {
        cnt++;
      }
      j++;
    }
  }
  console.log(cnt);
});
