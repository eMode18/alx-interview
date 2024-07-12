#!/usr/bin/node

const request = require('request');
const SWAPI_URL = 'https://swapi-api.hbtn.io/api'; // Renamed API_URL to SWAPI_URL

if (process.argv.length > 2) {
  request(`${SWAPI_URL}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.log(err);
    }
    const charactersURL = JSON.parse(body).characters;
    const characterNames = charactersURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseErr, __, charactersReqBody) => {
          if (promiseErr) {
            reject(promiseErr);
          }
          resolve(JSON.parse(charactersReqBody).name);
        });
      }));

    Promise.all(characterNames)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}
