-- Task 3: Create table force_name with NOT NULL constraint on name
-- This script creates the table if it doesn't exist

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
