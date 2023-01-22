#!/usr/bin/node
// This script writes a string to a file

const file = process.argv[2];
const ecrit = process.argv[3];
const fs = require('fs');

fs.writeFile(file, ecrit, 'utf8', function (error) {
  if (error) {
    console.log(error);
  }
});
