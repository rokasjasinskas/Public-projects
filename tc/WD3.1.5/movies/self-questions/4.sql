SELECT COUNT (movie_id) FROM stars 
WHERE movie_id IN (
    SELECT id FROM movies
    WHERE year <1989
)

-- 294139