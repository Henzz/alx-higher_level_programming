-- Displays the average temperature (Fahrenheit) by city ordered
-- by temperature (desc)

-- Import database file
SOURCE temperatures.sql

-- Display avg temperature records
SELECT city, AVG(value) 'avg_temp' FROM temperatures ORDER BY city DESC;
