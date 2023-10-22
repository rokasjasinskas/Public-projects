SELECT movies.title FROM movies
JOIN stars ON movies.id = stars.movie_id
JOIN people ON stars.person_id = people.id 
Where people.name LIKE 'Chris Evans'
AND movies.year > 2020