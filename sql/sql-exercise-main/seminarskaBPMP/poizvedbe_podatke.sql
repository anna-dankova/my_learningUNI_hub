-- ============================================================
--  VIDEO GAME CATALOG вЂ” FULL DATABASE SCRIPT
--  Updated: May 2026
-- ============================================================

-- ------------------------------------------------------------
-- 0. DROP (РµСЃР»Рё РЅСѓР¶РЅРѕ РЅР°С‡Р°С‚СЊ Р·Р°РЅРѕРІРѕ)
-- ------------------------------------------------------------
SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS purchase_item;
DROP TABLE IF EXISTS purchase;
DROP TABLE IF EXISTS review;
DROP TABLE IF EXISTS discount;
DROP TABLE IF EXISTS game_platform;
DROP TABLE IF EXISTS game;
DROP TABLE IF EXISTS genre;
DROP TABLE IF EXISTS studio;
DROP TABLE IF EXISTS platform;
DROP TABLE IF EXISTS customer;
SET FOREIGN_KEY_CHECKS = 1;


-- ------------------------------------------------------------
-- 1. genre
-- ------------------------------------------------------------
CREATE TABLE genre (
    id   INT          NOT NULL AUTO_INCREMENT,
    name VARCHAR(50)  NOT NULL,
    PRIMARY KEY (id)
);


-- ------------------------------------------------------------
-- 2. studio
-- ------------------------------------------------------------
CREATE TABLE studio (
    id             INT           NOT NULL AUTO_INCREMENT,
    name           VARCHAR(100)  NOT NULL,
    country        VARCHAR(50),
    founded_year   INT,
    num_employees  INT,
    website        VARCHAR(100),
    PRIMARY KEY (id)
);


-- ------------------------------------------------------------
-- 3. platform
-- ------------------------------------------------------------
CREATE TABLE platform (
    id            INT          NOT NULL AUTO_INCREMENT,
    name          VARCHAR(50)  NOT NULL,
    type          VARCHAR(30),
    release_year  INT,
    PRIMARY KEY (id)
);


-- ------------------------------------------------------------
-- 4. customer
-- ------------------------------------------------------------
CREATE TABLE customer (
    id                 INT           NOT NULL AUTO_INCREMENT,
    first_name         VARCHAR(50)   NOT NULL,
    last_name          VARCHAR(50)   NOT NULL,
    email              VARCHAR(100)  NOT NULL,
    registration_date  DATE,
    country            VARCHAR(50),
    birth_date         DATE,
    PRIMARY KEY (id),
    UNIQUE KEY uq_customer_email (email)
);


-- ------------------------------------------------------------
-- 5. game
-- ------------------------------------------------------------
CREATE TABLE game (
    id            INT            NOT NULL AUTO_INCREMENT,
    name          VARCHAR(100)   NOT NULL,
    release_year  INT,
    price         DECIMAL(8,2),
    age_rating    INT,
    description   TEXT,
    genre_id      INT,
    studio_id     INT,
    PRIMARY KEY (id),
    CONSTRAINT chk_age_rating CHECK (age_rating IN (3, 7, 12, 16, 18)),
    CONSTRAINT fk_game_genre   FOREIGN KEY (genre_id)  REFERENCES genre(id),
    CONSTRAINT fk_game_studio  FOREIGN KEY (studio_id) REFERENCES studio(id)
);


-- ------------------------------------------------------------
-- 6. game_platform  (M:N bridge)
-- ------------------------------------------------------------
CREATE TABLE game_platform (
    id           INT  NOT NULL AUTO_INCREMENT,
    game_id      INT  NOT NULL,
    platform_id  INT  NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY uq_game_platform (game_id, platform_id),
    CONSTRAINT fk_gp_game      FOREIGN KEY (game_id)     REFERENCES game(id),
    CONSTRAINT fk_gp_platform  FOREIGN KEY (platform_id) REFERENCES platform(id)
);


-- ------------------------------------------------------------
-- 7. discount
-- ------------------------------------------------------------
CREATE TABLE discount (
    id                INT           NOT NULL AUTO_INCREMENT,
    game_id           INT           NOT NULL,
    discount_percent  DECIMAL(5,2)  NOT NULL,
    start_date        DATE          NOT NULL,
    end_date          DATE          NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT chk_discount_dates  CHECK (end_date > start_date),
    CONSTRAINT chk_discount_pct    CHECK (discount_percent > 0 AND discount_percent <= 100),
    CONSTRAINT fk_discount_game    FOREIGN KEY (game_id) REFERENCES game(id)
);


-- ------------------------------------------------------------
-- 8. review
-- ------------------------------------------------------------
CREATE TABLE review (
    id           INT   NOT NULL AUTO_INCREMENT,
    game_id      INT   NOT NULL,
    customer_id  INT   NOT NULL,
    score        INT   NOT NULL,
    comment      TEXT,
    review_date  DATE,
    PRIMARY KEY (id),
    UNIQUE KEY uq_review_once (game_id, customer_id),
    CONSTRAINT chk_score        CHECK (score BETWEEN 1 AND 10),
    CONSTRAINT fk_review_game   FOREIGN KEY (game_id)     REFERENCES game(id),
    CONSTRAINT fk_review_cust   FOREIGN KEY (customer_id) REFERENCES customer(id)
);


-- ------------------------------------------------------------
-- 9. purchase
-- ------------------------------------------------------------
CREATE TABLE purchase (
    id             INT           NOT NULL AUTO_INCREMENT,
    customer_id    INT           NOT NULL,
    purchase_date  DATE          NOT NULL,
    total_price    DECIMAL(8,2),
    status         ENUM('paid','pending','refunded','cancelled') NOT NULL DEFAULT 'pending',
    payment_method VARCHAR(30),
    PRIMARY KEY (id),
    CONSTRAINT fk_purchase_cust FOREIGN KEY (customer_id) REFERENCES customer(id)
);


-- ------------------------------------------------------------
-- 10. purchase_item
-- ------------------------------------------------------------
CREATE TABLE purchase_item (
    id           INT           NOT NULL AUTO_INCREMENT,
    purchase_id  INT           NOT NULL,
    game_id      INT           NOT NULL,
    quantity     INT,
    unit_price   DECIMAL(8,2),
    PRIMARY KEY (id),
    CONSTRAINT fk_pi_purchase  FOREIGN KEY (purchase_id) REFERENCES purchase(id),
    CONSTRAINT fk_pi_game      FOREIGN KEY (game_id)     REFERENCES game(id)
);


-- ============================================================
-- INSERT DATA
-- ============================================================

-- genre
INSERT INTO genre (name) VALUES
('RPG'),
('FPS'),
('Strategy'),
('Adventure'),
('Sports'),
('Horror'),
('Racing'),
('Fighting'),
('Simulation'),
('Platformer');

-- studio
INSERT INTO studio (name, country, founded_year, num_employees, website) VALUES
('CD Projekt Red',        'Poland',      1994,   865,   'cdprojektred.com'),
('Valve',                 'USA',         1996,   360,   'valvesoftware.com'),
('Rockstar Games',        'USA',         1998,   3000,  'rockstargames.com'),
('Ubisoft',               'France',      1986,   19000, 'ubisoft.com'),
('Naughty Dog',           'USA',         1984,   600,   'naughtydog.com'),
('FromSoftware',          'Japan',       1986,   330,   'fromsoftware.jp'),
('Bethesda Game Studios', 'USA',         1986,   2300,  'bethesdagamestudios.com'),
('Nintendo',              'Japan',       1889,   6700,  'nintendo.com'),
('Bandai Namco',          'Japan',       2006,   10000, 'bandainamcoent.com'),
('Square Enix',           'Japan',       2003,   4500,  'square-enix.com'),
('Capcom',                'Japan',       1979,   3000,  'capcom.com'),
('Insomniac Games',       'USA',         1994,   800,   'insomniacgames.com'),
('Guerrilla Games',       'Netherlands', 2000,   400,   'guerrilla-games.com'),
('Blizzard Entertainment','USA',         1991,   4400,  'blizzard.com'),
('343 Industries',        'USA',         2009,   700,   '343industries.com');

-- platform
INSERT INTO platform (name, type, release_year) VALUES
('PC',              'Computer', 1981),
('PlayStation 5',   'Console',  2020),
('Xbox Series X',   'Console',  2020),
('Nintendo Switch', 'Console',  2017),
('PlayStation 4',   'Console',  2013),
('Xbox One',        'Console',  2013),
('PlayStation 3',   'Console',  2006),
('Steam Deck',      'Handheld', 2022);

-- customer
INSERT INTO customer (first_name, last_name, email, registration_date, country, birth_date) VALUES
('Ana',     'Novak',    'ana.novak@email.com',      '2022-01-15', 'Slovenia', '1998-04-12'),
('Marko',   'Horvat',   'marko.horvat@email.com',   '2022-03-20', 'Slovenia', '1995-07-23'),
('Luka',    'Kovac',    'luka.kovac@email.com',      '2023-06-10', 'Croatia',  '2000-11-05'),
('Sara',    'Petrovic', 'sara.p@email.com',          '2023-09-05', 'Serbia',   '1997-03-18'),
('Jan',     'Kos',      'jan.kos@email.com',         '2024-01-22', 'Slovenia', '2001-09-30'),
('Maja',    'Zupan',    'maja.z@email.com',          '2024-03-14', 'Slovenia', '1999-06-14'),
('Tomas',   'Breznik',  'tomas.b@email.com',         '2024-04-01', 'Slovenia', '1993-02-28'),
('Nina',    'Zajc',     'nina.zajc@email.com',       '2024-05-10', 'Croatia',  '2002-12-01'),
('Aleksej', 'Popov',    'aleksej.p@email.com',       '2024-06-20', 'Russia',   '1996-08-17'),
('Elena',   'Kovac',    'elena.kovac@email.com',     '2024-07-15', 'Slovenia', '1994-05-22'),
('Jure',    'Mrak',     'jure.mrak@email.com',       '2024-08-03', 'Slovenia', '2003-01-09'),
('Petra',   'Oblak',    'petra.oblak@email.com',     '2024-09-11', 'Austria',  '1990-10-31');

-- game
INSERT INTO game (name, release_year, price, age_rating, description, genre_id, studio_id) VALUES
('The Witcher 3: Wild Hunt',   2015, 29.99, 18, 'Open-world RPG set in a dark fantasy universe.',      1,  1),
('Cyberpunk 2077',             2020, 49.99, 18, 'Futuristic open-world RPG in Night City.',            1,  1),
('Elden Ring',                 2022, 59.99, 16, 'Open-world action RPG by FromSoftware.',              1,  6),
('Dark Souls III',             2016, 39.99, 16, 'Challenging action RPG with deep lore.',              1,  6),
('Skyrim',                     2011, 19.99, 18, 'Epic open-world RPG in the land of Tamriel.',         1,  7),
('Fallout 4',                  2015, 29.99, 18, 'Post-apocalyptic RPG in a retro-futuristic world.',   1,  7),
('Final Fantasy XVI',          2023, 59.99, 18, 'Action RPG with breathtaking summon battles.',        1, 10),
('Dragon Age: Inquisition',    2014, 19.99, 18, 'Epic RPG with tactical combat and rich story.',       1,  4),
('Half-Life 2',                2004,  9.99, 16, 'Legendary sci-fi FPS that changed gaming.',           2,  2),
('Counter-Strike 2',           2023,  0.00, 16, 'Iconic competitive tactical shooter.',                2,  2),
('Portal 2',                   2011, 14.99, 12, 'Mind-bending puzzle FPS with dark humor.',            2,  2),
('Doom Eternal',               2020, 39.99, 18, 'Ultra-fast demon-slaying FPS experience.',            2,  7),
('Halo Infinite',              2021, 59.99, 12, 'Master Chief returns in open-world Halo.',            2, 15),
('Titanfall 2',                2016, 19.99, 16, 'Best single-player campaign in FPS history.',         2,  4),
('Civilization VI',            2016, 29.99,  7, 'Turn-based strategy вЂ” build an empire.',              3, 14),
('StarCraft II',               2010,  0.00, 12, 'Premier real-time strategy esports title.',           3, 14),
('Total War: Warhammer III',   2022, 59.99, 16, 'Grand strategy meets real-time battles.',             3,  4),
('Age of Empires IV',          2021, 39.99,  7, 'Classic RTS reborn with modern visuals.',             3,  9),
('GTA V',                      2013, 19.99, 18, 'Massive open-world crime action game.',               4,  3),
('Red Dead Redemption 2',      2018, 39.99, 18, 'Cinematic open-world western masterpiece.',           4,  3),
('Assassins Creed Mirage',     2023, 49.99, 18, 'Return to roots in ancient Baghdad.',                 4,  4),
('The Last of Us Part I',      2022, 59.99, 18, 'Rebuilt classic post-apocalyptic adventure.',         4,  5),
('The Last of Us Part II',     2020, 49.99, 18, 'Emotional and brutal sequel to TLOU.',                4,  5),
('Uncharted 4',                2016, 19.99, 16, 'Action-adventure treasure hunting epic.',             4,  5),
('Spider-Man 2',               2023, 69.99, 16, 'Play as both Peter Parker and Miles Morales.',        4, 12),
('Horizon Zero Dawn',          2017, 29.99, 12, 'Hunt robot dinosaurs in post-human world.',           4, 13),
('Horizon Forbidden West',     2022, 59.99, 12, 'Aloy journeys west into new forbidden lands.',        4, 13),
('God of War',                 2018, 39.99, 18, 'Kratos and Atreus explore Norse mythology.',          4, 12),
('God of War Ragnarok',        2022, 69.99, 18, 'Epic conclusion to the Norse saga.',                  4, 12),
('FIFA 23',                    2022, 39.99,  3, 'Global football simulation game.',                    5,  4),
('NBA 2K24',                   2023, 49.99,  3, 'Realistic basketball simulation with MyCareer mode.', 5,  9),
('Resident Evil Village',      2021, 39.99, 18, 'Survival horror in a mysterious Eastern village.',    6, 11),
('Resident Evil 4 Remake',     2023, 59.99, 18, 'Masterful remake of the survival horror classic.',   6, 11),
('Silent Hill 2 Remake',       2024, 59.99, 18, 'Psychological horror reimagined.',                    6,  9),
('Alien Isolation',            2014, 19.99, 18, 'Terrifying stealth survival horror on a space station.',6, 4),
('Forza Horizon 5',            2021, 49.99,  3, 'Open-world racing set in Mexico.',                    7, 15),
('Gran Turismo 7',             2022, 59.99,  3, 'Realistic driving simulation for PlayStation.',       7, 12),
('Tekken 8',                   2024, 59.99, 16, 'Next-gen 3D fighting game with cinematic story.',     8,  9),
('Mortal Kombat 1',            2023, 69.99, 18, 'Brutal rebooted timeline fighter.',                   8,  9),
('Super Mario Odyssey',        2017, 49.99,  3, 'Joyful 3D platformer across creative kingdoms.',     10,  8);

-- game_platform (selected key combinations)
INSERT INTO game_platform (game_id, platform_id) VALUES
(1,1),(1,2),(1,5),(1,8),
(2,1),(2,2),(2,5),
(3,1),(3,2),(3,3),
(4,1),(4,2),(4,5),
(5,1),(5,2),(5,5),
(6,1),(6,2),(6,5),
(7,2),
(8,1),(8,5),
(9,1),(9,8),
(10,1),
(11,1),(11,8),
(12,1),(12,2),(12,3),
(13,1),(13,3),
(14,1),(14,5),(14,6),
(15,1),
(16,1),
(17,1),
(18,1),(18,3),
(19,1),(19,2),(19,3),(19,5),
(20,1),(20,2),(20,3),(20,5),
(21,1),(21,2),(21,3),
(22,2),(22,1),
(23,2),(23,5),
(24,2),(24,5),
(25,2),
(26,1),(26,2),(26,5),
(27,2),
(28,2),(28,5),
(29,2),
(30,1),(30,2),(30,3),
(31,1),(31,2),(31,3),
(32,1),(32,2),(32,3),(32,5),
(33,1),(33,2),(33,3),
(34,1),(34,2),(34,3),
(35,1),(35,5),
(36,1),(36,3),(36,8),
(37,2),
(38,1),(38,2),(38,3),
(39,1),(39,2),(39,3),
(40,4);

-- discount (Р°РєС‚РёРІРЅС‹Рµ РІ 2026)
INSERT INTO discount (game_id, discount_percent, start_date, end_date) VALUES
(1,  50.00, '2026-05-01', '2026-05-31'),
(2,  20.00, '2026-05-07', '2026-05-14'),
(3,  15.00, '2026-06-01', '2026-06-15'),
(5,  75.00, '2026-04-20', '2026-04-30'),
(9,  80.00, '2026-05-01', '2026-05-31'),
(12, 25.00, '2026-06-10', '2026-06-20'),
(19, 30.00, '2026-05-15', '2026-05-25'),
(20, 25.00, '2026-07-01', '2026-07-15'),
(22, 40.00, '2026-05-01', '2026-05-31'),
(28, 20.00, '2026-08-01', '2026-08-10'),
(32, 35.00, '2026-05-10', '2026-05-20'),
(36, 10.00, '2026-05-01', '2026-05-31'),
(40, 15.00, '2026-09-01', '2026-09-10');

-- review
INSERT INTO review (game_id, customer_id, score, comment, review_date) VALUES
(1,  1,  10, 'Best game ever!',                       '2023-01-10'),
(1,  2,   9, 'Great story and graphics.',              '2023-02-14'),
(2,  3,   8, 'Buggy at launch, great now.',            '2023-03-05'),
(2,  4,   7, 'Good but expected more.',                '2023-04-20'),
(3,  5,  10, 'A masterpiece of game design.',         '2023-05-01'),
(3,  6,   9, 'Incredibly deep and rewarding.',         '2023-05-15'),
(4,  1,   8, 'Tough but fair. Amazing atmosphere.',   '2023-06-01'),
(5,  7,   8, 'Still holds up after all these years.', '2023-06-10'),
(9,  2,  10, 'A classic that never ages.',             '2023-06-15'),
(10, 8,   9, 'Best competitive shooter out there.',   '2023-07-01'),
(11, 9,  10, 'Brilliant puzzle design.',               '2023-07-10'),
(12, 10,  8, 'Non-stop action from start to finish.', '2023-07-22'),
(15, 11,  9, 'One more turn... every time.',           '2023-08-01'),
(19, 5,   8, 'Amazing open world, endless fun.',       '2023-08-10'),
(20, 1,   9, 'Beautiful story, like a film.',          '2023-08-30'),
(21, 3,   6, 'Too many microtransactions.',            '2023-09-10'),
(22, 6,  10, 'Emotionally perfect.',                   '2023-10-05'),
(23, 4,   9, 'Even better than the first.',           '2023-10-20'),
(25, 7,  10, 'Spider-Man at its absolute best.',      '2023-11-01'),
(28, 8,   9, 'A soft reboot done perfectly.',          '2023-11-15'),
(29, 9,  10, 'Epic conclusion, worth every penny.',   '2023-12-01'),
(32, 10,  8, 'Tense and atmospheric.',                '2023-12-10'),
(33, 11,  9, 'Better than the original. Incredible.', '2024-01-05'),
(36, 12,  8, 'Best racing game on PC.',               '2024-01-20'),
(38, 2,   9, 'Phenomenal fighting mechanics.',        '2024-02-10'),
(40, 5,  10, 'Pure joy. Perfect for all ages.',       '2024-03-01'),
(4,  7,   9, 'Dark Souls III is the best Souls game.','2024-03-15'),
(6,  8,   7, 'Good but not as good as Skyrim.',       '2024-04-01'),
(8,  11,  8, 'Underrated gem.',                       '2024-04-20'),
(35, 12,  9, 'Genuinely terrifying. Loved it.',       '2024-05-01');

-- purchase
INSERT INTO purchase (customer_id, purchase_date, total_price, status, payment_method) VALUES
(1,  '2023-01-05',  79.98, 'paid',      'Credit Card'),
(2,  '2023-02-10',  29.99, 'paid',      'PayPal'),
(3,  '2023-04-15',  49.99, 'paid',      'Credit Card'),
(1,  '2023-07-20',  69.98, 'paid',      'PayPal'),
(4,  '2023-09-01',  19.99, 'pending',   'Credit Card'),
(5,  '2024-01-30',  39.99, 'paid',      'PayPal'),
(6,  '2024-02-14',  29.99, 'paid',      'Credit Card'),
(7,  '2024-03-05',  99.98, 'paid',      'Credit Card'),
(8,  '2024-04-10',  59.99, 'paid',      'PayPal'),
(9,  '2024-05-01',  49.99, 'paid',      'Credit Card'),
(10, '2024-06-15',  89.98, 'paid',      'Credit Card'),
(11, '2024-07-20',  59.99, 'refunded',  'PayPal'),
(12, '2024-08-05',  69.99, 'paid',      'Credit Card'),
(1,  '2024-09-10',  59.99, 'paid',      'PayPal'),
(2,  '2024-10-22', 109.98, 'paid',      'Credit Card'),
(3,  '2024-11-11',  49.99, 'paid',      'PayPal'),
(4,  '2024-12-01',  39.99, 'cancelled', 'Credit Card'),
(5,  '2025-01-15',  69.99, 'paid',      'Credit Card'),
(6,  '2025-02-28',  59.99, 'paid',      'PayPal'),
(7,  '2025-03-14',  49.99, 'paid',      'Credit Card');

-- purchase_item
INSERT INTO purchase_item (purchase_id, game_id, quantity, unit_price) VALUES
(1,  1,  1, 29.99),
(1,  2,  1, 49.99),
(2,  1,  1, 29.99),
(3,  2,  1, 49.99),
(4,  19, 1, 19.99),
(4,  21, 1, 49.99),
(5,  19, 1, 19.99),
(6,  20, 1, 39.99),
(7,  22, 1, 29.99),
(8,  25, 1, 69.99),
(8,  29, 1, 29.99),
(9,  3,  1, 59.99),
(10, 2,  1, 49.99),
(11, 28, 1, 39.99),
(11, 29, 1, 49.99),
(12, 25, 1, 59.99),
(13, 38, 1, 69.99),
(14, 27, 1, 59.99),
(15, 29, 1, 69.99),
(15, 20, 1, 39.99),
(16, 7,  1, 49.99),
(17, 20, 1, 39.99),
(18, 29, 1, 69.99),
(19, 3,  1, 59.99),
(20, 2,  1, 49.99);



use game_catalog;
-- ------------------------------------------------------------
-- 1. Vse igre
-- ------------------------------------------------------------
select g.name as game, genre.name as genre, s.name as studio,  g.release_year, g.price as 'price $'
from game g
inner join genre on genre.id=g.genre_id
inner join studio s on s.id =g.studio_id
order by g.release_year desc;
-- ------------------------------------------------------------
-- 2.Igre po žanru
-- ------------------------------------------------------------
select game.name as game, s.name as studio, g.name as genre
from game 
inner join studio s on s.id = game.studio_id
inner join genre g on g.id = game.genre_id
order by game.name;
-- ------------------------------------------------------------
-- 3.Zgodovina nakupov
-- ------------------------------------------------------------
select  g.name as game, purchase_item.unit_price as price,  
concat(c.first_name, ' ',c.last_name)as customer, purchase.id as purchase_id
from customer c
inner join purchase on c.id = purchase.customer_id
inner join purchase_item on purchase.id = purchase_item.purchase_id
inner join game g on g.id = purchase_item.game_id 
order by purchase.id;
-- ------------------------------------------------------------
-- 4.top 10 iger
-- ------------------------------------------------------------
select g.name, g.price as 'price $', genre.name
from game g
inner join genre on g.genre_id = genre.id
order by g.price desc
limit 10;
-- ------------------------------------------------------------
-- 5.Ocene iger
-- ------------------------------------------------------------
select g.name as game , count(r.id) as reviews, min(r.score) as min,
round(avg(r.score)) as AVG, max(r.score) as max
from game g
left join review r on r.game_id= g.id
group by g.id, g.name 
order by avg(r.score) desc;
-- ------------------------------------------------------------
-- 6.Studii in igre
-- ------------------------------------------------------------
select s.name as 'name', s.country , count(g.id) as games, avg(g.price) as avg_price
from studio s
left join game g on g.studio_id=s.id
group by s.id, s.name, s.country
order by games desc;
-- ------------------------------------------------------------
-- 7.Aktualne popuste na igre
-- ------------------------------------------------------------
select g.name, g.price, round(d.discount_percent) as '%', 
round(g.price *(1-d.discount_percent/ 100.0 ),2) as final_price, d.end_date
from game g
inner join discount d on d.game_id = g.id
where curdate() between d.start_date and d.end_date
order by d.end_date;

-- ------------------------------------------------------------
-- 8.Igre po platformah
-- ------------------------------------------------------------
select p.name,p.type, count(g.id) as games
from platform p
inner join game_platform gp on gp.platform_id=p.id
inner join game g on g.id=gp.game_id
group by p.name, p.type
order by games desc;
