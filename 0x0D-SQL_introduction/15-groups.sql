-- a script that lists the number of records with the same score in the table
SELECT score, COUNT(*) AS number
FROM select_table
GROUP BY score
ORDER BY number DESC;
