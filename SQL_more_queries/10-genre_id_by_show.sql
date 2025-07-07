-- Task 10: List all shows that have at least one genre
-- This query joins tv_shows with tv_show_genres and sorts accordingly

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_show_genres
WHERE tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
