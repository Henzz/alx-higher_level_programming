-- Lists all shows contained in 'hbtn_0d_tvshows' that have at least one genre linked
SELECT tv_shows.title, tv_shows_genres.genre_id FROM tv_shows, tv_shows_genres, tv_genres
WHERE tv_shows_genres.genre_id = tv_genres.id AND tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title AND tv_show_genres.genre_id ASC;
