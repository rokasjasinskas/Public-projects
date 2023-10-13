-- Keep a log of any SQL queries you execute as you solve the mystery.

-- .schema
-- .mode
-- SELECT * from crime_scene_reports 
-- WHERE year = "2021"
-- AND month = "7"
-- AND day = "28"
-- AND street = "Humphrey Street";

-- CREATE TABLE crime_scene_reports (
--     id INTEGER,
--     year INTEGER,
--     month INTEGER,
--     day INTEGER,
--     street TEXT,
--     description TEXT,
--     PRIMARY KEY(id)
-- );

-- 295|2021|7|28|Humphrey Street|Theft of 
-- the CS50 duck took place at 10:15am at 
-- the Humphrey Street bakery. Interviews were 
-- conducted today with three witnesses who were 
-- present at the time – each of their interview 
-- transcripts mentions the bakery. 

-- CREATE TABLE interviews (
--     id INTEGER,
--     name TEXT,
--     year INTEGER,
--     month INTEGER,
--     day INTEGER,
--     transcript TEXT,
--     PRIMARY KEY(id)
-- );

-- SELECT * 
-- FROM interviews 
-- WHERE year = "2021"
-- AND month = "7"
-- AND day = "28";
-- needs to add word bakery 

-- 161|Ruth|2021|7|28|Sometime within ten minutes of 
-- the theft, I saw the thief get into a car in the 
-- bakery parking lot and drive away. If you have 
-- security footage from the bakery parking lot, you 
-- might want to look for cars that left the parking 
-- lot in that time frame.

-- 162|Eugene|2021|7|28|I don't know the thief's 
-- name, but it was someone I recognized. Earlier 
-- this morning, before I arrived at Emma's bakery, 
-- I was walking by the ATM on Leggett Street and saw 
-- the thief there withdrawing some money.

-- 163|Raymond|2021|7|28|As the thief was leaving the 
-- bakery, they called someone who talked to them for 
-- less than a minute. In the call, I heard the thief 
-- say that they were planning to take the earliest 
-- flight out of Fiftyville tomorrow. The thief then 
-- asked the person on the other end of the phone to 
-- purchase the flight ticket.


-- CREATE TABLE bakery_security_logs (
--     id INTEGER,
--     year INTEGER,
--     month INTEGER,
--     day INTEGER,
--     hour INTEGER,
--     minute INTEGER,
--     activity TEXT,
--     license_plate TEXT,
--     PRIMARY KEY(id)
-- );

-- SELECT * 
-- FROM bakery_security_logs 
-- WHERE year = "2021"
-- AND month = "7"
-- AND day = "28"
-- AND hour = "10";

-- 258|2021|7|28|10|8|entrance|R3G7486
-- 259|2021|7|28|10|14|entrance|13FNH73
-- 260|2021|7|28|10|16|exit|5P2BI95
-- 261|2021|7|28|10|18|exit|94KL13X
-- 262|2021|7|28|10|18|exit|6P58WS2
-- 263|2021|7|28|10|19|exit|4328GD8
-- 264|2021|7|28|10|20|exit|G412CB7
-- 265|2021|7|28|10|21|exit|L93JTIZ
-- 266|2021|7|28|10|23|exit|322W7JE
-- 267|2021|7|28|10|23|exit|0NTHK55
-- 268|2021|7|28|10|35|exit|1106N58
-- 269|2021|7|28|10|42|entrance|NRYN856
-- 270|2021|7|28|10|44|entrance|WD5M8I6
-- 271|2021|7|28|10|55|entrance|V47T75I

-- CREATE TABLE atm_transactions (
--     id INTEGER,
--     account_number INTEGER,
--     year INTEGER,
--     month INTEGER,
--     day INTEGER,
--     atm_location TEXT,
--     transaction_type TEXT,
--     amount INTEGER,
--     PRIMARY KEY(id)
-- );

-- SELECT *
-- FROM atm_transactions
-- WHERE year = "2021"
-- AND month = "7"
-- AND day = "28"
-- AND atm_location like "Leggett Street";

-- 246|28500762|2021|7|28|Leggett Street|withdraw|48
-- 264|28296815|2021|7|28|Leggett Street|withdraw|20
-- 266|76054385|2021|7|28|Leggett Street|withdraw|60
-- 267|49610011|2021|7|28|Leggett Street|withdraw|50       
-- 269|16153065|2021|7|28|Leggett Street|withdraw|80       
-- 275|86363979|2021|7|28|Leggett Street|deposit|10        
-- 288|25506511|2021|7|28|Leggett Street|withdraw|20       
-- 313|81061156|2021|7|28|Leggett Street|withdraw|30       
-- 336|26013199|2021|7|28|Leggett Street|withdraw|35

-- CREATE TABLE bank_accounts (
--     account_number INTEGER,
--     person_id INTEGER,
--     creation_year INTEGER,
--     FOREIGN KEY(person_id) REFERENCES people(id)  
-- );

-- SELECT * 
-- FROM bank_accounts
-- WHERE account_number IN
-- (
--     SELECT account_number
--     FROM atm_transactions
--     WHERE year = "2021"
--     AND month = "7"
--     AND day = "28"
--     AND atm_location like "Leggett Street"
-- );

-- 49610011|686048|2010
-- 86363979|948985|2010
-- 26013199|514354|2012
-- 16153065|458378|2012
-- 28296815|395717|2014
-- 25506511|396669|2014
-- 28500762|467400|2014
-- 76054385|449774|2015
-- 81061156|438727|2018

-- CREATE TABLE people (
--     id INTEGER,
--     name TEXT,
--     phone_number TEXT,
--     passport_number INTEGER,
--     license_plate TEXT,
--     PRIMARY KEY(id)
-- );


-- SELECT * 
-- FROM people
-- WHERE id IN 
-- (
--     SELECT person_id
--     FROM bank_accounts
--     WHERE account_number IN
--     (
--         SELECT account_number
--         FROM atm_transactions
--         WHERE year = "2021"
--         AND month = "7"
--         AND day = "28"
--         AND atm_location like "Leggett Street"
--     )
-- )

-- 395717|Kenny|(826) 555-1652|9878712108|30G67EN
-- 396669|Iman|(829) 555-5269|7049073643|L93JTIZ
-- 438727|Benista|(338) 555-6650|9586786673|8X428L0        
-- 449774|Taylor|(286) 555-6063|1988161715|1106N58
-- 458378|Brooke|(122) 555-4581|4408372428|QX4YZN3
-- 467400|Luca|(389) 555-5198|8496433585|4328GD8
-- 514354|Diana|(770) 555-1861|3592750733|322W7JE
-- 686048|Bruce|(367) 555-5533|5773159633|94KL13X
-- 948985|Kaelyn|(098) 555-1164|8304650265|I449449