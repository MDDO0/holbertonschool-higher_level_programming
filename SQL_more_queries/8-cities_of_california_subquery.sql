-- Task 8: List all cities of California without using JOIN
-- This query uses a subquery to get the California state_id and match it in cities

SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY id ASC;
