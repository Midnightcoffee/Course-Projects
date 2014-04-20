/* You've started a new movie-rating website, and you've been collecting data on */
/* reviewers' ratings of various movies. There's not much data yet, but you can */
/* still try out some interesting queries. Here's the schema: */

/* Movie ( mID, title, year, director ) English: There is a movie with ID number */
/* mID, a title, a release year, and a director. */

/* Reviewer ( rID, name ) English: The reviewer with ID number rID has a certain */
/* name. */

/* Rating ( rID, mID, stars, ratingDate ) English: The reviewer rID gave the movie */
/* mID a number of stars rating (1-5) on a certain ratingDate. */


/* -------------- queries ----------------------------- */
/* Find the titles of all movies directed by Steven Spielberg. */

SELECT title
FROM movie
WHERE director="Steven Spielberg";


/* Find all years that have a movie that received a rating of 4 or 5, and sort */
/* them in increasing order. */

SELECT DISTINCT year
FROM movie JOIN rating USING(mID)
WHERE stars = 4 or stars = 5
ORDER BY year ASc;

/* Find the titles of all movies that have no ratings. */ 

SELECT title
FROM movie
WHERE mid NOT in (SELECT mid FROM rating);

/* Some reviewers didn't provide a date with their rating. Find the names of
all reviewers who have ratings with a NULL value for the date. */ 

SELECT dIStinct name
FROM Rating natural JOIN Reviewer
WHERE ratingDate IS Null;

/* Write a query to return the ratings data in a more readable format: reviewer
name, movie title, stars, and ratingDate. Also, sort the data, first by
reviewer name, then by movie title, and lastly by number of stars. */ 

SELECT dIStinct name, title, stars, ratingDate
FROM Reviewer natural JOIN Rating natural JOIN Movie
ORDER BY name, title, stars;

/* For all cases where the same reviewer rated the same movie twice and gave it
a higher rating the second time, return the reviewer's name and the title of
the movie. */ 

SELECT movie.title, max(rating.stars)
FROM movie natural JOIN rating
GROUP BY movie.title
ORDER BY movie.title;

/* For each movie, return the title and the 'rating spread', that is, the
difference between highest and lowest ratings given to that movie. Sort by
rating spread from highest to lowest, then by movie title. */ 

SELECT movie.title, max(r1.stars) - min(r2.stars)
FROM rating AS r1 inner JOIN rating AS r2
ON r1.mID == r2.mID
CROSS JOIN movie ON movie.mID == r2.mID
GROUP BY r1.mID
ORDER BY max(r1.stars) - min(r2.stars) desc, movie.title ASc;


