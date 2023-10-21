SELECT DISTINCT movies.title 
FROM movies
WHERE movies.id IN (
    SELECT s1.movie_id
    FROM stars AS s1
    JOIN stars AS s2 ON s1.movie_id = s2.movie_id
    JOIN people AS p1 ON s1.person_id = p1.id
    JOIN people AS p2 ON s2.person_id = p2.id
    WHERE p1.name = 'Bradley Cooper' AND p2.name = 'Jennifer Lawrence'
);
