-- 테이블 만들기
CREATE TABLE healthcare (
id PRIMARY KEY,
sido INTEGER NOT NULL,
gender INTEGER NOT NULL,
age INTEGER NOT NULL,
height INTEGER NOT NULL,
weight INTEGER NOT NULL,
waist REAL NOT NULL,
va_left REAL NOT NULL,
va_right REAL NOT NULL,
blood_pressure INTEGER NOT NULL,
smoking INTEGER NOT NULL,
is_drinking BOOLEAN NOT NULL
);

-- csv import 하기
.mode csv 
.import health.csv healthcare

SELECT * FROM healthcare;

SELECT COUNT(*) FROM healthcare;

-- COUNT(*)
-- 1000000

SELECT COUNT(age) FROM healthcare WHERE age < 10;

-- COUNT(age)
-- 156277

SELECT COUNT(sido) FROM healthcare WHERE gender = 1;

-- COUNT(sido)
-- 510689

SELECT COUNT(sido) FROM healthcare WHERE smoking = 3 and is_drinking = 1;

-- COUNT(sido)
-- 150361

SELECT COUNT(sido) FROM healthcare WHERE va_left = 2.0 and va_right = 2.0;

-- COUNT(sido)
-- 1692

SELECT DISTINCT sido FROM healthcare;

-- sido
-- 36
-- 27
-- 11
-- 31
-- 41
-- 44
-- 48
-- 30
-- 42
-- 43
-- 46
-- 28
-- 26
-- 47
-- 45
-- 29
-- 49

SELECT height, weight FROM healthcare WHERE height > 190 and weight > 120;

-- height	weight
-- 195	    125

-- 2 일 차 문 제

SELECT COUNT(*) FROM healthcare;

-- COUNT(*)
-- 1000000

SELECT MAX(age), MIN(age) FROM healthcare;

-- MAX(age)	  MIN(age)
--   18	        9

SELECT MAX(height), MAX(weight), MIN(height), MIN(weight) FROM healthcare;

-- MAX(height)	MAX(weight)	MIN(height)	MIN(weight)
-- 195	        135	        130	        30

SELECT COUNT(sido) FROM healthcare WHERE 160 <= height and height <= 170;

-- COUNT(sido)
-- 516930

SELECT waist, is_drinking FROM healthcare WHERE is_drinking = 1 ORDER BY waist ASC LIMIT 5;

-- waist	is_drinking
-- 5.8	        1
-- 8.2	        1
-- 8.7	        1
-- 41.0	        1
-- 49.0	        1

SELECT COUNT(sido) FROM healthcare WHERE (va_left >= 1.5 and va_right >= 1.5) and is_drinking = 1;

--  COUNT(sido)
--  36697

SELECT COUNT(sido) FROM healthcare WHERE blood_pressure < 120;

-- COUNT(sido)
-- 360808

SELECT AVG(waist) FROM healthcare WHERE blood_pressure >= 140;

-- AVG(waist)
-- 85.8665098512525

SELECT AVG(height), AVG(weight) FROM healthcare WHERE gender = 1;

-- AVG(height)	    AVG(weight)
-- 167.452735422145	69.7131620222875

SELECT id, height, weight FROM healthcare ORDER BY height DESC, weight DESC LIMIT 1 OFFSET 1;

--  id	    height	weight
--  836005	195	    110

SELECT COUNT(sido) FROM healthcare WHERE weight / ((height / 100) * (height / 100)) >= 30;

-- COUNT(sido)
-- 1000000

SELECT id, weight / ((height / 100) * (height / 100)) as BMI FROM healthcare WHERE smoking = 3 ORDER BY BMI DESC LIMIT 5;

-- id	    BMI
-- 99120	135
-- 100174	135
-- 142639	135
-- 172459	135
-- 239321	135

SELECT id, height FROM healthcare ORDER BY height ASC, weight ASC LIMIT 5 OFFSET 2;

-- id	    height
-- 78640	130
-- 155732	130
-- 156645	130
-- 158262	130
-- 190817	130

SELECT gender, age FROM healthcare WHERE gender = 1 and age > 17 LIMIT 1;

-- gender	age
-- 1	    18

SELECT * FROM healthcare WHERE age > 15 and height > 180 and weight > 80;

-- id	    sido	gender	age	height	weight	waist	va_left	va_right	blood_pressure	smoking	is_drinking
-- 565978	47	    1	    16	185	    100	    113.0	0.7	    0.3	            110	            2	    1
-- 574661	11	    1	1   6	185	    85	    96.0	0.5	    0.5	            122	            1	    0