-- Task 2: Create database hbtn_0d_2 and user_0d_2 with SELECT privilege only
-- This script creates the database and user if they don't exist and grants only SELECT

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
