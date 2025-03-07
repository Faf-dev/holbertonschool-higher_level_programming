-- List all shows contained in the database without a genre linked
--
-- tv_shows : contain the name of a show with their ID
-- tv_shows_genres : contain show ID with genre ID
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
