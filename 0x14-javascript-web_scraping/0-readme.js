#!/usr/bin/node


const fs = require('fs');
const i_file = process.argv[2];

fs.readFile(i_file, 'utf-8', (err, data) => {
    if (err) {
        console.log(err)
    } else {
        console.log(data)
    }
});