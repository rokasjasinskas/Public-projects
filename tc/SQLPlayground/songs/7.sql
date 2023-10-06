.mode box
SELECT AVG(energy) 
AS average_energy
FROM songs 
WHERE artist_id = 
(SELECT id from artists WHERE name = "Drake");