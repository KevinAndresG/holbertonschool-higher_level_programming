-- order the times that the same number is recordered
-- in MySQL server
SELECT score, COUNT(score)
AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;
