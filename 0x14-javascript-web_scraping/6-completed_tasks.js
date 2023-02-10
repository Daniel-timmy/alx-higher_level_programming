#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
var dict = {};
console.log(url);
request(url, (err, response, body) => {
    if (err) {
        console.log(err);
    } else {
        const json = JSON.parse(body);
        for (const item in json) {
            if (item.completed === true) {
                dict[item.userId] += 1;
            }
            
        }
        console.log(dict);
    }
});