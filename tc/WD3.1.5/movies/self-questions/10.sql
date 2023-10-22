INSERT INTO people (name, birth)
VALUES ('Bob Simpson', 1970);

INSERT INTO stars (person_id, movie_id)
SELECT (SELECT id FROM people WHERE name = 'Bob Simpson'),
       (SELECT id FROM movies WHERE title LIKE 'Oppenheimer');

SELECT * FROM people 
JOIN stars ON people.id = stars.person_id
JOIN movies ON stars.movie_id = movies.id
WHERE name = 'Bob Simpson';

-- 14146337|Bob Simpson|1970|15398776|14146337|15398776|Oppenheimer|2023
