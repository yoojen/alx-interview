#!/usr/bin/node
const request = require('request');

const BaseUrl = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(BaseUrl, function (error, response, body) {
  if (error) throw error;
  if (response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    loadCharacters(characters);
  }
});
const loadCharacters = (charactersObj) => {
  if (charactersObj) {
    for (const character of charactersObj) {
      if (character) {
        request(character, (error, response, body) => {
          if (error) throw error;
          if (response.statusCode === 200) {
            console.log(JSON.parse(body).name);
          }
        });
      } else {
        throw new Error('Found nothing');
      }
    }
  }
};
