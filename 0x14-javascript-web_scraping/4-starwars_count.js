#!/usr/bin/node
// This script prints number of movies where the character “Wedge Antilles” is present

const args = process.argv;
const request = require('request');
const url = args[2];
request(url, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    const corp = JSON.parse(body);
    const results = corp.results;
    let count = 0;
    for (let i = 0; i < results.length; i++) {
      const chars = (results[i].characters);
      for (let j = 0; j < chars.length; j++) {
        const check18 = chars[j].endsWith('18/');
        if (check18) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
