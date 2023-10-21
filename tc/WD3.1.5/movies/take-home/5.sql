SELECT people.name, COUNT(stars.movie_id)
FROM people
JOIN stars ON people.id = stars.person_id
GROUP BY people.name
HAVING COUNT(stars.movie_id) > 300;