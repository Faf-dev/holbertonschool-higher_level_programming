-- Display the score, name (best score first and if row have name value)
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC