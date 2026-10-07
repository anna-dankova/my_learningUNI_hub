USE vaja3;
-- ############################################################
-- 		+ 1. +
-- Izdelava tabele oseba
CREATE TABLE oseba (
  idoseba INT AUTO_INCREMENT PRIMARY KEY,
  ime VARCHAR(45),
  priimek VARCHAR(45),
  kraj_rojstva varchar(100)
);

-- dodajanje podatkov v tabelo oseba
insert into 
oseba 
values 
(null, 'Janez', 'Novak', 'Ljubljana'), 
(null, 'Miha', 'Kovač', 'Novo mesto'), 
(null, 'Ana', 'Metelko', 'Kranj'), 
(null, 'Lucija', 'Božič', 'Ljublana'),
(null, 'Božidar', 'Jaklič', 'Ptuj');

select * from oseba;

-- iskanje vseh, ki so rojeni v ljubljani
select * from oseba where kraj_rojstva = 'ljubljana';

-- brisanje tabele oseba
drop table oseba;
-- 		- 1. -
-- ############################################################






-- ############################################################
-- 		+ 2. +
-- izdelava tabele oseba (brez kraja rojstva)
CREATE TABLE oseba (
  idoseba INT AUTO_INCREMENT PRIMARY KEY,
  ime VARCHAR(45),
  priimek VARCHAR(45)
);

-- izdelava tabele kraj
CREATE TABLE kraj (
  idkraj INT PRIMARY KEY,
  ime VARCHAR(100)
);

-- dodajanje oseb
insert into 
oseba 
values 
(null, 'Janez', 'Novak'), 
(null, 'Miha', 'Kovač'), 
(null, 'Ana', 'Metelko'), 
(null, 'Lucija', 'Božič'),
(null, 'Božidar', 'Jaklič');

-- dodajanje krajev
insert into
kraj
values
(1000, 'Ljubljana'),
(4000, 'Kranj'),
(2250, 'Ptuj'),
(8000, 'Novo mesto'),
(2000, 'Maribor'),
(6000, 'Koper');

-- izpis vseh oseb
select * from oseba;

-- izpis vseh krajev
select * from kraj;

-- kartezični produkt (vsaka oseba (5) z vsakim krajem(6) = 5 x 6 = 30 zapisov)
select * from oseba, kraj;

-- izbris tabele oseba
drop table oseba;

-- izbris tabele kraj
drop table kraj;
-- 		- 2. -
-- ############################################################







-- ############################################################
-- 		+ 3. +
-- povezovanje tabel
-- izdelava tabele kraj
CREATE TABLE kraj (
  idkraj INT PRIMARY KEY,
  ime VARCHAR(100)
);

-- izdelava tabele oseba
CREATE TABLE oseba (
  idoseba INT AUTO_INCREMENT PRIMARY KEY,
  ime VARCHAR(45),
  priimek VARCHAR(45),
  idkraj int,
  foreign key(idkraj) references kraj(idkraj)
);

-- dodajanje krajev
insert into
kraj
values
(1000, 'Ljubljana'),
(4000, 'Kranj'),
(2250, 'Ptuj'),
(8000, 'Novo mesto'),
(2000, 'Maribor'),
(6000, 'Koper');

-- dodajanje oseb
insert into 
oseba 
values 
(null, 'Janez', 'Novak', 1000), 
(null, 'Miha', 'Kovač', 8000), 
(null, 'Ana', 'Metelko', 2000), 
(null, 'Lucija', 'Božič', 2250),
(null, 'Božidar', 'Jaklič', 1000);

-- izpis vseh krajev
select * from kraj;

-- izpis vseh oseb
select * from oseba;

-- kartezični produkt
select * from oseba, kraj;
-- izpišimo vse osebe in njihove kraje rojstva
-- koliko oseb je rojenih v ljubljani?
-- 		- 3. -
-- ############################################################







-- ############################################################
-- 		+ 4. +
-- left join, right join
insert into oseba values (null, 'John', 'Snow', null);
-- 		- 4. -
-- ############################################################