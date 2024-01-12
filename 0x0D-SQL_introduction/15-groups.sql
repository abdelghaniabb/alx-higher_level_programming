-- lists the number of records with the same score in
-- the table second_table of the database hbtn_0c_0 in
-- your MySQL server.
SELECT score, COUNT(*) AS number FROM second_table
WHERE name IS NOT NULL
GROUP BY score HAVING COUNT(*) > 1
ORDER BY score DESC;
