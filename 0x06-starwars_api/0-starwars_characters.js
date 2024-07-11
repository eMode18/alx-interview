#!/usr/bin/node
const request = require('request');
const SWAPI_URL = 'https://swapi-api.hbtn.io/api'; // API URL for Star Wars data

if (process.argv.length > 2) {
  // Fetch film data based on the provided film ID
  request(`${SWAPI_URL}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.error('Error fetching film data:', err);
      return;
    }

    const charactersURLs = JSON.parse(body).characters; // URLs of characters in the film
    const characterNamesPromises = charactersURLs.map(
      url => new Promise((resolve, reject) => {
        // Fetch character data for each URL
        request(url, (promiseErr, __, charactersReqBody) => {
          if (promiseErr) {
            reject(promiseErr);
          }
          resolve(JSON.parse(charactersReqBody).name); // Extract character names
        });
      })
    );

    // Resolve all promises and log character names
    Promise.all(characterNamesPromises)
      .then(names => console.log('Character names:\n', names.join('\n')))
      .catch(allErr => console.error('Error fetching character names:', allErr));
  });
}

