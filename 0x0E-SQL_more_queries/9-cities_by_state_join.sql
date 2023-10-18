-- a script that lists some contents of a Db
SELECT cities.id, cities.name, states.name
FROM cities JOIN states ON cities.state_id = states.id;
