-- Displays the top 3 cities temperature during July and
-- August ordered by temperature (desc)

-- Display top 3 with avg temperature records by city
SELECT TOP 3 city, AVG(value) 'avg_temp'
FROM temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC;
