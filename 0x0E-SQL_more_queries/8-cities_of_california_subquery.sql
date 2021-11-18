-- show the cities from California
-- in MySQL server
SELECT id, name
FROM cities
WHERE id =
(
	SELECT id
	FROM states
	WHERE name = 'California'
);
