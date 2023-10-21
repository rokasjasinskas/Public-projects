require('dotenv').config();

const Database = require('better-sqlite3');
const db = new Database('../movies.db');

const favorite = process.env.FAVORITE;
const row = db
  .prepare(
    `SELECT movies.title 
    FROM movies 
    JOIN directors ON movies.id = directors.movie_id 
    JOIN ratings ON movies.id = ratings.movie_id 
    JOIN people ON directors.person_id = people.id 
    Where people.name LIKE @favoriteName
    ORDER BY ratings.rating DESC`
  )
  .all({ favoriteName: favorite });
console.log(row);
