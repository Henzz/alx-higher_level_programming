-- Lists all the cities of California that can be found in the db 'hbtn_0d_usa'

-- Select cities
SELECT cities.id, cities.name FROM cities, states
WHERE cities.state_id = states.id
	AND state.name = 'California'
ORDER BY cities.id ASC;
