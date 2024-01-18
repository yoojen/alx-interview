#!/usr/bin/node

const request = require("request");

request(
  "https://swapi-api.hbtn.io/api/films/" + process.argv[2],
  function (error, res, body) {
    if (error) throw error;
    const characters = JSON.parse(body).characters;
    loadCharacters(characters, 0);
  }
);
const loadCharacters = (characters, index) => {
  if (index === characters.length) return;
  request(characters[index], function (error, res, body) {
    if (error) throw error;
    console.log(JSON.parse(body).name);
    loadCharacters(characters, index + 1);
  });
};
