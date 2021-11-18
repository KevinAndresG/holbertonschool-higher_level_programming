-- create database with id set in 1
-- in MySQL server
CREATE TABLE IF NOT EXISTS id_not_null
(
	id INT DEFAULT (1),
	name VARCHAR(256)
);
