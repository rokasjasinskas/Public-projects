SELECT SUBSTR(movies.title, -1) AS lastletter, SUM(ratings.rating) AS total_rating
FROM movies
JOIN ratings ON ratings.movie_id = movies.id
WHERE lastletter IN ('A', 'E', 'I', 'O', 'U')
GROUP BY lastletter
ORDER BY total_rating DESC;

-- I|4420.5
-- A|1050.7
-- O|321.5
-- E|292.3
-- U|233.2
