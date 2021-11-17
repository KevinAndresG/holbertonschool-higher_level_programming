-- list scores and names
-- in MySQL server
INSERT INTO second_table (`id`,`name`,`score`) VALUES (5, "Aria", 18);
INSERT INTO second_table (`id`,`name`,`score`) VALUES (5, "Aria", 12);
DELETE FROM second_table WHERE score < 10;
SELECT score, name
FROM second_table
ORDER BY score DESC;
