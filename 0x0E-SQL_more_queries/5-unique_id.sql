-- create a table the id must be default 1 and unique
-- in MySQL server
CREATE TABLE IF NOT EXISTS unique_id
(
	id INT DEFAULT (1) UNIQUE,
	name VARCHAR(256)
);
