-- Task 16: List all records with non-empty name from second_table
-- This query selects score and name where name is not null or empty, ordered by score descending
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
