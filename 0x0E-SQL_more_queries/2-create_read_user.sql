-- Creates the database 'hbtn_0d_2' and the user 'user_0d_2'

-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant permission
GRANT SELECT TO 'user_0d_2'@'localhost';
