-- Q. users에서 가장 나이가 작은 사람의 수는?

-- 가장 나이가 작은 사람의 수

SELECT age, COUNT(*)
FROM users
GROUP BY age
ORDER BY age
LIMIT 1;

-- age  COUNT(*)
-- ---  --------
-- 15   39

-- 확인해보기

SELECT MIN(age) 
FROM users;

-- MIN(age)
-- --------
-- 15

SELECT COUNT(*)
FROM users 
WHERE age = 15;

-- COUNT(*)
-- --------
-- 39

SELECT COUNT(*)
FROM users 
WHERE age = (SELECT MIN(age) FROM users);

-- COUNT(*)
-- --------
-- 39

-- Q. users에서 평균 계좌 잔고가 높은 사람의 수는?

-- 평균 계좌금액

SELECT AVG(balance)
FROM users;

-- AVG(balance)
-- ------------
-- 151456.89   

SELECT COUNT(*)
FROM users
WHERE balance > (SELECT AVG(balance) FROM users);

-- COUNT(*)
-- --------
-- 222     

-- Q. users에서 유은정과 같은 지역에 사는 사람의 수는?

SELECT COUNT(*)
FROM users
WHERE country = (
    SELECT country
    FROM users
    WHERE first_name = '은정' AND last_name = '유'
);

-- COUNT(*)
-- --------
-- 101     

-- Q. 전체 인원과 평균 연봉, 평균 나이를 출력하세요.

SELECT
    (SELECT COUNT(*) FROM users) AS 총인원,
    (SELECT AVG(balance) FROM users) AS 평균연봉,
    (SELECT AVG(age) FROM users) AS 평균나이;

-- 총인원   평균연봉    평균나이  
-- ----  ---------  ------
-- 1000  151456.89  27.346

-- UPDATE 활용
UPDATE users
SET balance = (SELECT AVG(balance) FROM users);

-- Q. users에서 이은정과 같은 지역에 사는 사람의 수는?

SELECT COUNT(*)
FROM users
WHERE country IN (
    SELECT country
    FROM users
    WHERE first_name = '은정' AND last_name = '이'
); 

-- COUNT(*)
-- --------
-- 218     

-- Q. 특정 성씨에서 가장 어린 사람들의 이름과 나이

SELECT
    last_name,
    first_name,
    age
FROM users
WHERE (last_name, age) IN (
    SELECT last_name, MIN(age)
    FROM users
    GROUP BY last_name)
ORDER BY last_name;

-- last_name  first_name  age
-- ---------  ----------  ---
-- 강          정수          15 
-- 고          우진          15 
-- 고          시우          15 
-- 곽          현숙          15 
-- 구          성현          17 
-- 권          수빈          16 
-- 권          지훈          16 
-- 권          성호          16 
-- 김          서영          15 
-- 김          지훈          15 
-- 김          주원          15 
-- 김          예준          15 
-- 김          예준          15 
-- 김          서영          15 
-- 김          진우          15 
-- 김          재호          15 
-- 김          민지          15 
-- 김          정숙          15 
-- 김          정식          15 
-- 나          은정          17 
-- 남          예은          17 
-- 남          명자          17 
-- 노          정숙          16 
-- 류          승민          15 
-- 문          유진          16 
-- 문          동현          16 
-- 문          현정          16 
-- 민          주원          18 
-- 박          정남          15 
-- 박          서윤          15 
-- 박          승민          15 
-- 박          유진          15 
-- 배          재호          19 
-- 백          진호          17 
-- 백          정호          17 
-- 서          은경          19 
-- 성          영수          15 
-- 손          정호          16 
-- 손          순자          16 
-- 송          순옥          16 
-- 송          지영          16 
-- 신          성현          26 
-- 심          준서          22 
-- 안          준혁          16 
-- 양          성훈          16 
-- 엄          지후          15 
-- 오          상현          15 
-- 우          민석          17 
-- 유          성호          15 
-- 윤          건우          16 
-- 윤          서윤          16 
-- 이          은영          15 
-- 이          은정          15 
-- 이          정순          15 
-- 이          하윤          15 
-- 이          종수          15 
-- 이          상호          15 
-- 임          지원          24 
-- 장          승현          15 
-- 전          영일          19 
-- 정          지민          15 
-- 조          영환          22 
-- 주          영진          16 
-- 지          영환          15 
-- 진          재현          16 
-- 차          지후          15 
-- 최          지은          15 
-- 하          영호          16 
-- 한          우진          15 
-- 한          주원          15 
-- 허          순자          16 
-- 홍          재현          15 
-- 홍          미숙          15 
-- 황          은정          16 
-- 황          준영          16 

