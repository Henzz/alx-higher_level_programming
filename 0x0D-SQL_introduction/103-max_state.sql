-- Displays the max temperature for each state
-- ordered by State name

-- Display max temperature records by state
SELECT state, MAX(value) `max_temp`
FROM temperatures
GROUP BY state
ORDER BY state;
