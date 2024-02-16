-- Displays the average temperature (Fahrenheit) by city ordered
-- by temperature (desc)

-- Import database file
SOURCE temperatures.sql

-- Display avg temperature records
SELECT hbtn_0c_0.temperatures.city, AVG(hbtn_0c_0.temperatures.value) 'avg_temp' FROM hbtn_0c_0.temperatures GROUP BY hbtn_0c_0.temperatures.city ORDER BY hbtn_0c_0.temperatures.value DESC;
