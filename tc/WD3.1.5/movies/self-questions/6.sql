SELECT people.name, people.birth FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON stars.movie_id = movies.id 
WHERE movies.title LIKE 'Oppenheimer'
ORDER BY people.birth DESC

-- Florence Pugh|1996
-- Cillian Murphy|1976
-- Matt Damon|1970
-- Kenneth Branagh|1960