#!/usr/bin/node
const request = require('request');
const starWarsAPI = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  request(`${starWarsAPI}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.log(err);
    }
    const charUrlsAPI = JSON.parse(body).characters;
    const charNames = charUrlsAPI.map(
      charUrl => new Promise((resolve, reject) => {
        request(charUrl, (charError, __, charBody) => {
          if (charError) {
            reject(charError);
          }
          resolve(JSON.parse(charBody).name);
        });
      }));

    Promise.all(charNames)
      .then(names => console.log(names.join('\n')))
      .catch(allError => console.log(allError));
  });
}
