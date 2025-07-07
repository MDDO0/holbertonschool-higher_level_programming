-- Task 5: Create table unique_id with id default 1 and unique constraint
-- This script creates the table if it doesn't exist

CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
