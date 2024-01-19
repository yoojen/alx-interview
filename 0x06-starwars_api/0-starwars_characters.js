#!/usr/bin/node
const request = require('request');

const BaseUrl = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;
request(BaseUrl, function (error, response, body) {
  if (error) throw error;
  if (response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    loadCharacters(characters, 0);
  }
});
const loadCharacters = (charactersObj, index) => {
  if (index === charactersObj.length) return;
  request(charactersObj[index], (error, response, body) => {
    if (error) throw error;
    if (response.statusCode === 200) console.log(JSON.parse(body).name);
    loadCharacters(charactersObj, index + 1);
  });
};
