-- Task 11: List all records from second_table with score >= 10
-- This query selects score and name where score is at least 10, ordered from highest to lowest
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
