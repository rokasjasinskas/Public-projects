const Database = require('better-sqlite3');
const db = new Database('movies.db');

const rows = db.prepare('SELECT * FROM people ').get();
console.log(rows);
