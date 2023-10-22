SELF-PREPARED QUESTIONS

1st level
1. Count average movies ratings for movies which have more or equal to 20000 votes. 
2. List top 10 oldest movies and calculate these movies age in 2050 years. Print two columns name and age. List should be ordered by age. Age has to be not null.
3. List movies and their release year which has "learners" inside its title and was release 2019 or later. 

2nd level
4. Count how many actors participated in movies which were released before 1989. 
5. List actors which have starred in movies with over 20,000 votes, and what is the highest rating of any movie they've appeared in. It should return two columns. Bring top 100 results.  
6. Who are the actors that have starred in the movie 'Oppenheimer', ordered by their birth dates from the most recent to the earliest?

3rd level
7. Which movies, along with their release years, featured both 'Robert Downey Jr.' and 'Tom Holland' as part of the cast?
8. Which movies released from 2005 onwards were directed by individuals born after 2005, and what are their ratings? List the results in descending order of movie titles and provide the names of the directors for each movie. Is should be three columns of title, rating, and director name. 
9. Using Node.js, write a script that reads a local .env file to obtain values for the ACTOR and YEAR variables. The script should then access a SQLite movie database and retrieve a list of movies in which the specified actor has starred in, and which were released after the provided year. Your script should connect to the database using the better-sqlite3 library. Additionally, create a .env file in your project directory and set values for both the ACTOR and YEAR variables.

4th level
10. Simpson's Star Role. In 2023, a famous movie titled "Oppenheimer" was released, and a rising star named Bob Simpson played a key role in it. You've been given the task to add Bob Simpson to the database if he doesn't exist and then link him to the movie "Oppenheimer". Write the SQL statements required to add 'Bob Simpson' with his birth year as 1970 to the 'people' table, then associate him with the movie "Oppenheimer" in the 'stars' table. Finally, write a query to retrieve all the movies in which 'Bob Simpson' has acted.
11. Dive into our movie database to discern patterns related to titles ending in vowels. Determine the total ratings of movies based on the vowel they end with. Ensure the results are ordered by total ratings in descending order. How do movies ending with certain vowels fare compared to others?
12. In this exercise, you are tasked with creating a Node.js program that interface with a SQLite database of movies. Your challenge is to write a script that reads movie details from a CSV file named movies.csv. This file contains columns for title and year. For every movie listed in the CSV, your script should:
        a. Check if the movie title already exists in the database.
        b. If the movie title doesn't exist, add it to the movies table.
        c. Provide the newly added movie with an initial rating of 0 in the ratings table.
        d. It should be able to implement several rows of information at once.
