-- Create the database 'hbtn_0d_usa' and the table 'cities' in the created DB
-- on your MySQL server

-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the created database
USE hbtn_0d_usa;

-- Create table
CREATE TABLE IF NOT EXISTS cities(
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL
	PRIMARY KEY (id),
	FORIEGN KEY (state_id) REFERENCES states(id),
);
