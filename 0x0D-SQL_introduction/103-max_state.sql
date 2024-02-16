-- Displays the max temperature for each state
-- ordered by State name

-- Display top 3 with avg temperature records by city
SELECT state, MAX(value) `max_temp`
FROM temperatures
GROUP BY city
ORDER BY state
LIMIT 3;
