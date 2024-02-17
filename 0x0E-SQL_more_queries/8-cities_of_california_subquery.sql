-- Lists all the cities of California that can be found in the db 'hbtn_0d_usa'

-- Select cities
SELECT id FROM states UNION SELECT state_id AS id, name FROM cities;
