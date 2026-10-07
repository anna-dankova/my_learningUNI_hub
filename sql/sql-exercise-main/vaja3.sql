select * from movies;

select movieid, genre_id, title
from movies
where title = 'Braveheart';

select *
from genres
where genre_id = 7;

select * from movies, genres
where movies.genre_id = genres.genre_id;

select * from movies inner join genres on movies.genre_id = genres.genre_id;
    
SELECT m.title, g.name, mr.rating_value
FROM movies m
INNER JOIN genres g
ON m.genre_id = g.genre_id
INNER JOIN mpaa_ratings mr
ON m.mpaa_rating_id = mr.mpaa_rating_id;

-- Izpišite imena karakterjev, ki jih je igral Arnold Schwarzenegger.
select c.character_name, c.actorid
from characters c
inner join actors a on c.actorid = a.actorid
where  a.`name` = 'Arnold Schwarzenegger';

-- Poiščite povprečno oceno vsakega žanra.
select g.name, AVG(m.rating) as avg_raiting
from movies m 
inner join genres g on m.genre_id= g.genre_id
group by g.name;

-- Poiščite povprečen čas trajanja filma vsakega žanra.
select g.name , avg(m.runtime) as avg_runtime
from movies m
inner join genres g on m.genre_id = g.genre_id
group by g.name;

-- Koliko filmov je v vsakem mpaa ratingu?
select mr.rating_value, count(*) as film_count
from movies m
inner join mpaa_ratings mr on m.mpaa_rating_id = mr.mpaa_rating_id
group by mr.rating_value;

-- Izpišite naslove filmov z ratingom 'R' in oceno večjo od 7.
select m.title, m.rating, mr.rating_value
from movies m 
inner join mpaa_ratings mr on m.mpaa_rating_id = mr.mpaa_rating_id
where m.rating>7 and mr.rating_value ="R";

-- Izpišite naslove filmov v katerih je igral Keanu Reeves.
select m.title
from movies m
INNER JOIN characters c ON m.movieid = c.movieid
INNER JOIN actors a ON c.actorid = a.actorid
WHERE a.name = 'Keanu Reeves';

-- Izpišite imena igralcev, ki so igrali v filmu Titanic.
SELECT a.name
FROM actors a
INNER JOIN characters c ON a.actorid = c.actorid  
INNER JOIN movies m ON m.movieid = c.movieid       
WHERE m.title = 'Titanic';

-- Izpišite imena igralcev, ki so kdaj igrali v grozljivki (Horror).
SELECT DISTINCT a.name
FROM actors a
INNER JOIN characters c ON a.actorid = c.actorid
INNER JOIN movies m ON m.movieid = c.movieid
INNER JOIN genres g ON g.genre_id = m.genre_id
WHERE g.name = 'Horror';

-- Kakšna je povprečna ocena filmov v katerih igra Robert De Niro?
select m.title, avg(m.rating) as avg_rating
from movies m
inner join characters c on c.movieid = m.movieid
inner join actors a on a.actorid = c.actorid
where a.name = "Robert De Niro";

-- Koliko so zaslužili filmi v katerih je igral Tom Cruise?
select m.gross, m.title
from movies m
inner join characters c on c.movieid = m.movieid
inner join actors a on c.actorid = a.actorid
where a.name = "Tom Cruise";


-- Prikaži vse žanre (genres), kjer je bilo ustvarjenih več kot 5 filmov.
select g.name ,count(m.movieid) as film_count
from genres g
inner join movies m on g.genre_id = m.genre_id
group by g.name
having count(m.movieid) >5;

-- Prikaži vse igralce, ki so igrali v več kot 10 filmih.
select a.name, count(movieid) as film_count
from actors a
inner join characters c on a.actorid = c.actorid
group by a.name
having count(movieid) >10;
-- Poišči naslove vseh filmov, ki so zaslužili več kot 1 milijardo USD (budget < gross).
select m.title, m.gross
from movies m
where m.gross > 1000000000;

-- Izpiši MPAA ocene (rating_value), ki jih ima več kot 150 filmov.
select mr.rating_value , count(movieid)
from mpaa_ratings mr
inner join movies m on mr.mpaa_rating_id = m.mpaa_rating_id
group by rating_value
having count(movieid)>150;

-- Izpiši vse igralce, ki so igrali v vsaj enem filmu z žanrom "Drama".
select a.name
from actors a
inner join characters c on c.actorid= a.actorid
inner join movies m on m.movieid = c.movieid
inner join genres g on  g.genre_id = m.genre_id
where g.name = "Drama";

-- Prikaži naslove filmov, ki imajo povprečno oceno (rating) več kot 8.0 in več kot 1000 ocen (rating_count).
select m.title
from movies m
where m.rating >=8.0 
and m.rating_count > 1000;

-- Poišči vse filme, katerih dolžina (runtime) je nad povprečno dolžino vseh filmov.
SELECT m.title, m.runtime
FROM movies m
WHERE m.runtime > (SELECT AVG(runtime) FROM movies);

-- Prikaži vse igralce, ki so višji od povprečne višine vseh igralcev (height_inches).
select a.height_inches
from actors a
where a.height_inches > (select avg(height_inches) from actors);

-- Prikaži naslove vseh filmov, ki so bili izdani po letu 2000 in imajo zaslužek (gross - budget) večji od povprečnega zaslužka
--  vseh filmov.
select m.title 
from movies m
where year(release_date) > 2000
and (m.gross - m.budget) > (select avg(gross - budget) from movies);

-- Poišči igralce, ki so igrali v vsaj 3 filmih iz žanra "Drama", kjer so filmi imeli povprečno oceno (rating) več kot 7.5 in skupen
-- zaslužek (gross - budget) več kot 10 milijonov. Prikaži ime igralca, število teh filmov, povprečno oceno teh filmov 
-- ter skupen zaslužek. Rezultate razvrsti po skupnem zaslužku.


