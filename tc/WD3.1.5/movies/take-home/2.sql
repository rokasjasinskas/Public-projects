.mode box
SELECT name, 2023 - birth FROM people
WHERE birth IS NOT NULL
ORDER by birth 
LIMIT 10;