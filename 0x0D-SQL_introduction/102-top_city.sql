-- Displays the top 3 cities temperature during July and
-- August ordered by temperature (desc)

-- Display avg temperature records by city
SELECT TOP 3 city, AVG(value) 'avg_temp'
FROM temperatures
WHERE month = 7 AND month = 8
GROUP BY city
ORDER BY avg_temp DESC;
