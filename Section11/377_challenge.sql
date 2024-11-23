-- Query 1
SELECT songs.title
FROM songs
    INNER JOIN albums ON songs.album = albums._id
WHERE albums.name = 'Forbidden';
-----------------------------------------------------------------------------------------------------
-- Query 2
SELECT songs.track,
    songs.title
FROM songs
    INNER JOIN albums ON songs.album = albums._id
WHERE albums.name = 'Forbidden'
ORDER BY songs.track;
-----------------------------------------------------------------------------------------------------
-- Query 3
SELECT songs.track,
    songs.title,
    albums.name
FROM songs
    INNER JOIN albums ON songs.album = albums._id
    INNER JOIN artists ON albums.artist = artists._id
WHERE artists.name = 'Deep Purple'
ORDER BY songs.track,
    songs.title;
-----------------------------------------------------------------------------------------------------
-- Query 4
UPDATE artists
SET name = 'One Kitten'
WHERE artists.name = 'Mehitabel';
-----------------------------------------------------------------------------------------------------
-- Query 5
SELECT *
FROM artists
WHERE name = 'One Kitten';
-----------------------------------------------------------------------------------------------------
-- Query 6 and 8
SELECT DISTINCT songs.title
FROM songs
    INNER JOIN albums ON songs.album = albums._id
    INNER JOIN artists ON albums.artist = artists._id
WHERE artists.name = 'Aerosmith'
ORDER BY songs.title;
-----------------------------------------------------------------------------------------------------
-- Query 7 and 9
SELECT COUNT(DISTINCT songs.title)
FROM songs
    INNER JOIN albums ON songs.album = albums._id
    INNER JOIN artists ON albums.artist = artists._id
WHERE artists.name = 'Aerosmith';
-----------------------------------------------------------------------------------------------------
-- Query 10
SELECT COUNT(DISTINCT songs.title),
    COUNT(DISTINCT artists._id),
    COUNT(DISTINCT albums._id)
FROM songs
    INNER JOIN albums ON songs.album = albums._id
    INNER JOIN artists ON albums.artist = artists._id
WHERE artists.name = 'Aerosmith';