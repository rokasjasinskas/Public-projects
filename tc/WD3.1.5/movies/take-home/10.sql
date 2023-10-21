SELECT * FROM movies 
JOIN directors ON movies.id = directors.movie_id
JOIN people ON directors.person_id = people.id
WHERE people.name IN ('Christopher Nolan', 'Greta Gerwig' )
AND movies.year = 2023