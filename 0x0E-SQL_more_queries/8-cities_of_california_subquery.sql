-- show the cities from California
-- in MySQL server
SELECT id, name
FROM cities
WHERE state_id =
(
	SELECT id
	FROM states
	WHERE name = 'California'
)
ORDER BY id ASC;
