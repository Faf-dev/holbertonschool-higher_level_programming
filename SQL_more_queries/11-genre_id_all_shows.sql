-- List all shows contained in the database
--
-- tv_shows : contain the name of a show with their ID
-- tv_shows_genres : contain show ID with genre ID
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
