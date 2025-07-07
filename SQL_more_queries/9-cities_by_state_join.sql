-- Task 9: List all cities with their states
-- This query joins cities and states and sorts by city ID

SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
