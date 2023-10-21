SELECT movies.title, ratings.rating, people.name 
FROM movies
JOIN stars ON movies.id = stars.movie_id 
JOIN people ON stars.person_id = people.id 
JOIN ratings ON movies.id = ratings.movie_id
WHERE ratings.rating >= 8.5
AND people.birth > 2005
ORDER BY ratings.rating DESC