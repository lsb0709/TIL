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

-- 1일차 실습 문제

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

