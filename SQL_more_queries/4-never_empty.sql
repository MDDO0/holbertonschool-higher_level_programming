-- Task 4: Create table id_not_null with id default 1
-- This script creates the table if it doesn't exist

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256)
);
