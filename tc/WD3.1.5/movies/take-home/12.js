const Database = require('better-sqlite3');
const db = new Database('../movies.db');

const title = process.argv[2];
const year = process.argv[3];

function check_argument(title, year) {
  if (title != null && year != null && typeof process.argv[4] === 'undefined') {
    return true;
  } else {
    return false;
  }
}

function check_title() {
  const results = db
    .prepare(
      `SELECT title FROM movies 
    WHERE title like @movie_title`
    )
    .all({ movie_title: title });

  if (results.length === 0) {
    return false;
  } else {
    return true;
  }
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
  if (check_argument(title, year) === true) {
    if (check_title() === false) {
      add_new_row(title, year);
    } else {
      console.log('Error. This title already exists');
    }
  } else {
    console.log('Error with console arguments');
  }
} catch (error) {
  console.error(error);
}
