require('dotenv').config();

const Database = require('better-sqlite3');
const db = new Database('../movies.db');

const actor = process.env.ACTOR;
const year = process.env.YEAR;
const row = db
  .prepare(
    `SELECT movies.title FROM movies
    JOIN stars ON movies.id = stars.movie_id
    JOIN people ON stars.person_id = people.id 
    Where people.name LIKE @actor
    AND movies.year > @year`
  )
  .all({ actor: actor, year: year });
console.log(row);

// [
//     { title: 'Lightyear' },
//     { title: 'Red One' },
//     { title: 'The Gray Man' }
//   ]
