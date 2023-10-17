const sqlite3 = require('sqlite3').verbose();
const fs = require('fs');

// Create a new database or connect to an existing one
const db = new sqlite3.Database('./tables.db');

// Read the SQL commands from create-tables.sql
fs.readFile('./create-tables.sql', 'utf8', (err, sqlCommands) => {
  if (err) {
    console.error('Failed to read the SQL file:', err);
    return;
  }

  // Execute SQL commands
  db.exec(sqlCommands, (err) => {
    if (err) {
      console.error('Failed to execute SQL commands:', err);
    } else {
      console.log('Tables created successfully!');
    }
    // Close the database inside the callback
    db.close((err) => {
      if (err) {
        console.error('Error closing the database:', err);
      } else {
        console.log('Database closed.');
      }
    });
  });
});

// Optionally, here you could also execute your migration-* SQL files
// if they contain changes to your database schema.
