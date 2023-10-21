SELECT SUBSTR(movies.title, 1) AS firsletter, AVG(ratings.rating)
FROM movies
JOIN ratings ON ratings.movie_id = movies.id
WHERE firsletter NOT NULL 
AND firsletter GLOB '[A-Z]' 
GROUP BY firsletter