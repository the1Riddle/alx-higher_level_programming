#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;

const file1 = fs.readFileSync(argv[2], 'utf-8').toString();
const file2 = fs.readFileSync(argv[3], 'utf-8').toString();
fs.writeFileSync(argv[4], file1 + file2);
