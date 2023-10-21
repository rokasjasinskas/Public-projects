const Database = require('better-sqlite3');
const db = new Database('../movies.db');

const title = 'from command line';
const year = 'from command line';

const row = db.prepare('SELECT * FROM people LIMIT 10').all();
console.log(row);

function check_title () {

}

if check_title = TRUE { 
const add_new_rows = db.prepare('

')
}
else{
    console.log('Error. This title already exists')
}