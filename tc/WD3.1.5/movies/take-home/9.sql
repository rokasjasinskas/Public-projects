SELECT movies.title FROM movies
JOIN directors ON movies.id = directors.movie_id
JOIN ratings ON movies.id = ratings.movie_id
JOIN people ON directors.person_id = people.id 
Where people.name LIKE 'Christopher Nolan'