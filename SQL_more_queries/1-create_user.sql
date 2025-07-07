-- Task 1: Create MySQL user user_0d_1 with all privileges
-- This script creates the user and grants all privileges if not exists

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
