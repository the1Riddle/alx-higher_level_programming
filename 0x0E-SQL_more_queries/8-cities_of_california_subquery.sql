-- a script that lists all cities in a Db
SELECT cities.id, cities.name FROM cities
WHERE state_id = (SELECT states.id FROM states WHERE states.name = 'California'
);
