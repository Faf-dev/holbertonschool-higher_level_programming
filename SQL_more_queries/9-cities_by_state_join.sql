-- List all cities countain in the database hbtn_0d_usa (table : cities, states)
SELECT cities.id, cities.name, states.name FROM cities 
JOIN states ON cities.state_id = states.id;
ORDER BY cities.id ASC;
