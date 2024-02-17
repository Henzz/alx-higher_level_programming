-- Lists all cities contained in the db 'hbtn_0d_usa'
SELECT cities.id, cities.name, states.name FROM cities, states
WHERE citites.state_id = states.id
ORDER BY cities.id ASC;
