-- SQLite commands to create a database and table
.headers on -- Show headers in the SQLite shell
.open FILENAME -- Open a connection to a database file
.backup FILENAME -- Create a backup of the database
.restore FILENAME -- Restore a backup of the database
.schema -- Visualize the database schema
.tables -- Visualize the tables in the database
.quit -- Exit the SQLite shell
----------------------------------------------------------------------------------------------------------------------
-- Create a table
CREATE TABLE table_name (
    column1_name column1_type,
    column2_name column2_type,
...
);
-- Insert a row into a table
INSERT INTO table_name (column1_name, column2_name,...)
VALUES (value1, value2,...);
-- Select all rows from a table
SELECT *
FROM table_name;
-- Select specific columns from a table
SELECT column1_name,
    column2_name,
...
FROM table_name;
-- Select rows that meet a condition
SELECT *
FROM table_name
WHERE column_name = value;
-- Update rows in a table
UPDATE table_name
SET column_name = value
WHERE column_name = value;
-- Delete rows from a table
DELETE FROM table_name
WHERE column_name = value;
-- Drop a table
DROP TABLE table_name;
-- Drop a view
DROP VIEW view_name;
-- Ignore case when comparing strings
COLLATE NOCASE -- Order rows by a column
ORDER BY column_name ASC | DESC;
----------------------------------------------------------------------------------------------------------------------
-- Select all rows from the albums table and order them by the artist and name columns in ascending order, ignoring case.
SELECT *
FROM albums
ORDER BY albums.artist,
    albums.name COLLATE NOCASE;
-- Select the track, title, and album name columns from the songs table, joining the albums table on the album column.
SELECT songs.track,
    songs.title,
    albums.name
FROM songs
    JOIN albums ON songs.album = albums._id;
-- Select the artist name, album name, track, and title columns from the songs table,
-- joining the albums and artists tables on the album and artist columns, respectively.
-- Filter the results to only include rows where the artist name contains the string 'doctor'.
-- Order the results by artist name, album name, and track.
SELECT songs.track,
    songs.title,
    albums.name
FROM songs
    INNER JOIN albums ON songs.album = albums._id
SELECT artists.name,
    albums.name,
    songs.track,
    songs.title
FROM songs
    INNER JOIN albums ON songs.album = albums._id
    INNER JOIN artists ON albums.artist = artists._id -- WHERE artists.name = "Doolittle"
WHERE songs.title LIKE '%doctor%'
ORDER BY artists.name,
    albums.name,
    songs.track;
-- Create a view that combines the artist, album, track, and title columns from the songs, albums, and artists tables.
CREATE VIEW artist_list AS
SELECT artists.name AS Artist,
    albums.name as Album,
    songs.track AS Track,
    songs.title AS Title
FROM songs
    INNER JOIN albums ON songs.album = albums._id
    INNER JOIN artists ON albums.artist = artists._id
ORDER BY artists.name,
    albums.name,
    songs.track;
-- Count the number of rows in the artists table.
SELECT count(*)
FROM artists;