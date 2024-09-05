#!/usr/bin/node
const request = require('request');
const starWars_API = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  request(`${starWars_API}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.log(err);
    }
    const APIurlsChar = JSON.parse(body).characters;
    const CharNames = APIurlsChar.map(
      UrlChar => new Promise((resolve, reject) => {
        request(UrlChar, (charError, __, charBody) => {
	  if (charError) {
	    reject(charError);
	  }
	  resolve(JSON.parse(charBody).name);
	});
      }));
  
    Promise.all(CharNames)
      .then(names => console.log(names.join('\n')))
      .catch(allError => console.log(allError));
  });
}
