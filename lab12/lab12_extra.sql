.read lab12.sql

-- Q5
CREATE TABLE greatstudents AS
  SELECT a.date, a.color,a.pet,a.number,b.number from students as a, fa17students as b where a.date = b.date
  and a.color = b.color and a.pet = b.pet;

-- Q6
CREATE TABLE sevens AS
  SELECT a.seven from students as a, checkboxes as b where a.time = b.time and a.number = 7 and b.'7' = 'True';

-- Q7
CREATE TABLE fa17favnum AS
  SELECT number, count(*) from fa17students group by number order by count(*) Desc limit 1;


CREATE TABLE fa17favpets AS
  SELECT pet, count(*) as total from fa17students group by pet order by total Desc limit 10;


CREATE TABLE sp18favpets AS
 SELECT pet, count(*) as total from students group by pet order by total Desc limit 10;


CREATE TABLE sp18dog AS
  SELECT pet,count(*) as total from students group by pet having pet='dog';


CREATE TABLE sp18alldogs AS
  SELECT pet,count(*) as total from students where pet like "%dog%" group by pet like "%dog%";


CREATE TABLE obedienceimages AS
  SELECT seven,denero,count(*) from students where seven='7' group by denero;

-- Q8
CREATE TABLE smallest_int_count AS
  SELECT smallest, count(*) from students group by smallest order by smallest;
