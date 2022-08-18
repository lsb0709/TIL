-- 2 일 차 실습 문제

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

SELECT id, waist FROM healthcare WHERE is_drinking = 1 AND waist <>'' ORDER BY waist DESC LIMIT 5;

-- id 		waist
-- 993531   146.0
-- 878897   142.0
-- 826643   141.4
-- 567314   140.0
-- 611146   140.0
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

SELECT COUNT(*) FROM healthcare WHERE 10000 * weight / (height * height) >= 30;

-- COUNT(*)
-- 53121

SELECT id, weight / ((height / 0.01) * (height / 0.01)) as BMI FROM healthcare WHERE smoking = 3 ORDER BY BMI DESC LIMIT 5;

-- id	    BMI
-- 231431	5.078125e-07
-- 934714	4.99479708636837e-07
-- 722707	4.8828125e-07
-- 947281	4.77502295684114e-07
-- 948801	4.77502295684114e-07

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