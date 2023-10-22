const Database = require('better-sqlite3');
const db = new Database('../movies.db');
const fs = require('fs');
const csv = require('csv-parser');

function check_title(title) {
  const results = db
    .prepare(
      `SELECT title FROM movies 
    WHERE title like @movie_title`
    )
    .all({ movie_title: title });

  return results.length === 0;
}

function add_new_row(title, year) {
  db.prepare('BEGIN').run();

  try {
    const insertMovieStmt = db.prepare(
      `INSERT INTO movies (title, year)
         SELECT @movietitle, @movieyear
         WHERE NOT EXISTS (
             SELECT title FROM movies 
             WHERE title LIKE @movietitle)`
    );

    const info = insertMovieStmt.run({
      movietitle: title,
      movieyear: year,
    });

    if (info.changes) {
      const movieId = info.lastInsertRowid;

      const insertRatingStmt = db.prepare(
        `INSERT INTO ratings (movie_id, rating, votes)
           VALUES (?, 0, 0)`
      );

      insertRatingStmt.run(movieId);

      console.log('New movie ID:', movieId);
    }

    db.prepare('COMMIT').run();
  } catch (err) {
    db.prepare('ROLLBACK').run();
    console.error('Transaction failed', err);
  }
}

// main
try {
  fs.createReadStream('movies.csv')
    .pipe(csv())
    .on('data', (row) => {
      const title = row.title;
      const year = row.year;

      if (check_title(title)) {
        add_new_row(title, year);
      } else {
        console.log(`Error. The title "${title}" already exists`);
      }
    });
} catch (error) {
  console.error(error);
}
