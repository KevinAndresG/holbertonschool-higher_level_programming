-- list all the cities and states
-- in MySQL server
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
