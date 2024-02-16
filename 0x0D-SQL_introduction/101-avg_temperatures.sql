-- Displays the average temperature (Fahrenheit) by city ordered
-- by temperature (desc)

-- Display avg temperature records by city
SELECT city, AVG(value) 'avg_temp'
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
