-- List the number of records with the same score (print the score and the number of records with this score)
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC
