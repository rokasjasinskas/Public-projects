SELECT movies.title, ratings.rating, people.name 
FROM movies
JOIN directors ON movies.id = directors.movie_id 
JOIN people ON directors.person_id = people.id 
JOIN ratings ON movies.id = ratings.movie_id
WHERE movies.year >= 2005
AND people.birth > 2005
ORDER BY movies.title DESC

-- Raavan|8.0|Sumit Kirtania
-- Krrish 3|5.3|Sumit Kirtania
-- Kacher Manush|8.3|Sumit Kirtania
-- Golondaaj|7.3|Sumit Kirtania