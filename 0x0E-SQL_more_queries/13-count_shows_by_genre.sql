-- Lists all genres from 'hbtn_0d_tvshows' and displays the number of shows linked to each
SELECT tv_genres.name AS `genre`, COUNT(tv_genres.id) AS `number_of_shows`
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_show_genres.show_id is NOT NULL
GROUP BY genre
ORDER BY number_of_shows DESC;
