-- List all shows that habe at least one genre linked 
--
-- tv_shows : contain the name of a show with their ID
-- tv_shows_genres : contain show ID with genre ID
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_show_genres
JOIN tv_shows ON tv_show_genres.show_id =
tv_shows.id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
