-- Task 15: Count number of records per score in second_table
-- This query groups by score, counts how many records per score, and sorts by count descending
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
