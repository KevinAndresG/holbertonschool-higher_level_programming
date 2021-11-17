-- update the score just with name
-- in MySQL server
UPDATE second_table
set
`score` = 10
WHERE `second_table`.`name` = "Bob";
