-- Displays the average temperature (Fahrenheit) by city ordered
-- by temperature (desc)

-- Select database
USE hbtn_0c_0;

-- Import table dump file
SOURCE temperatures.sql

-- Display avg temperature records by city
SELECT city, AVG(value) 'avg_temp'
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
