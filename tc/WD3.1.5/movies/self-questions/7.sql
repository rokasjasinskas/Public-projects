SELECT movies.title, movies.year FROM movies
JOIN stars AS stars1 ON movies.id = stars1.movie_id
JOIN stars AS stars2  ON movies.id = stars2.movie_id
JOIN people AS people1 ON stars1.person_id = people1.id
JOIN people AS people2 ON stars2.person_id = people2.id
WHERE people1.name = 'Robert Downey Jr.'
AND people2.name = 'Tom Holland';

-- Spider-Man: Homecoming|2017
