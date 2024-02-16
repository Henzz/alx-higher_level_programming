-- Create the database 'hbtn_0d_usa' and the table 'states' in the created DB
-- on your MySQL server

-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the created database
USE hbtn_0d_usa;

-- Create table
CREATE TABLE IF NOT EXISTS states(
	id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
