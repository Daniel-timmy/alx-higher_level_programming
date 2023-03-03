#!/usr/bin/node

const request = require('request');
const movie_id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movie_id;
request(url, (err, response, body) => {
    if (err) {
        console.log(err);
    } else {
        const json = JSON.parse(body);
        console.log(json.title);
    }
});
