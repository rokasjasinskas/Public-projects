import sqlite from 'better-sqlite3';

const db = sqlite('roster.db');

const viewTables = db
  .prepare(`SELECT name, sql FROM sqlite_master WHERE type='table'`)
  .all();

const createStudents = db
  .prepare(
    `CREATE TABLE IF NOT EXISTS students (
    id INTEGER  NOT NULL,
    student_name TEXT NOT NULL,
    house TEXT NOT NULL,
    head TEXT NOT NULL,
    PRIMARY KEY (id)
  )`
  )
  .run();

const createHouses = db
  .prepare(
    `CREATE TABLE IF NOT EXISTS houses (
    id INTEGER  NOT NULL,
    house TEXT NOT NULL,
    head TEXT NOT NULL,
    PRIMARY KEY (id)
  )`
  )
  .run();

const createAssigments = db
  .prepare(
    `CREATE TABLE IF NOT EXISTS assigments (
    id INTEGER  NOT NULL,
    student_id INTEGER NOT NULL,
    house_id INTEGER NOT NULL,
    PRIMARY KEY (id)
  )`
  )
  .run();

const insertDataToHouses = db
  .prepare(
    `
INSERT INTO houses (house, head)
SELECT DISTINCT house, head FROM students
  `
  )
  .run();

const populateAssigments = db
  .prepare(
    `
    INSERT INTO assigments (student_id, house_id)
    SELECT students.id AS student_id, houses.id AS house_id
    FROM students
    JOIN houses ON students.house = houses.house
  `
  )
  .run();
