-- Q. gender가 1인 경우는 남자를 gender가 2인 경우에는 여자를 출력하시오.

SELECT id,
    CASE
        WHEN gender = 1 THEN '남자'
        WHEN gender = 2 THEN '여자'
    END AS 성별
FROM healthcare
LIMiT 5;

-- id  성별
-- --  --
-- 1   남자
-- 2   여자
-- 3   여자
-- 4   남자
-- 5   여자
-- Q. 나이에 따라 청소년(~18), 청년(~30), 중장년(~64)로 출력하시오.

SELECT 
    last_name,
    age,
    CASE
        WHEN age <= 18 THEN '청소년'
        WHEN age <= 30 THEN '청년'
        WHEN age <= 64 THEN '중장년'
    END
FROM users
LIMIT 7;

-- "유",40,"중장년"
-- "이",36,"중장년"
-- "구",37,"중장년"
-- "장",40,"중장년"
-- "차",30,"청년"
-- "이",26,"청년"
-- "민",18,"청소년"