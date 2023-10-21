INSERT INTO ratings (movie_id, rating, votes)
SELECT movies.id, 10, 1 FROM movies
JOIN directors ON movies.id = directors.movie_id
JOIN people ON directors.person_id = people.id
WHERE people.name = 'Christopher Nolan'
AND movies.year = 2023;
