-- GROUP BY

-- 성별 갯수
SELECT last_name, COUNT(*)
FROM users
GROUP BY last_name;
/* last_name  COUNT(*)
    ---------  --------
    강          23      
    고          10      
    곽          4       
    구          2       
    권          17      
    김          268     
    나          3       
    남          7       
    노          6       
    류          14      
    문          12      
    민          4       
    박          98      
    배          9       
    백          12      
    서          9       
    성          4       
    손          13      
    송          15      
    신          3       
    심          7       
    안          14      
    양          7       
    엄          3       
    오          20      
    우          7       
    유          6       
    윤          22      
    이          179     
    임          3       
    장          32      
    전          5       
    정          2       
    조          9       
    주          5       
    지          4       
    진          5       
    차          5       
    최          55      
    하          6       
    한          19      
    허          6       
    홍          25      
    황          21    */

-- GROUP BY에서 활용하는 컬럼을 제외하고는
-- 집계함수를 쓰세요.
SELECT last_name, AVG(age), COUNT(*)
FROM users
GROUP BY last_name;

-- last_name  AVG(age)          COUNT(*)
-- ---------  ----------------  --------
-- 강          28.6086956521739  23      
-- 고          27.2              10      
-- 곽          24.5              4       
-- 구          27.0              2       
-- 권          25.4117647058824  17      
-- 김          27.6679104477612  268     
-- 나          28.6666666666667  3       
-- 남          28.0              7       
-- 노          21.0              6       
-- 류          28.0              14      
-- 문          26.4166666666667  12      
-- 민          32.5              4       
-- 박          27.4489795918367  98      
-- 배          33.0              9       
-- 백          25.1666666666667  12      
-- 서          31.2222222222222  9       
-- 성          22.75             4       
-- 손          25.7692307692308  13      
-- 송          25.7333333333333  15      
-- 신          30.6666666666667  3       
-- 심          27.8571428571429  7       
-- 안          27.9285714285714  14      
-- 양          32.5714285714286  7       
-- 엄          24.3333333333333  3       
-- 오          28.0              20      
-- 우          22.7142857142857  7       
-- 유          25.3333333333333  6       
-- 윤          25.8181818181818  22      
-- 이          26.9664804469274  179     
-- 임          28.6666666666667  3       
-- 장          26.84375          32      
-- 전          31.8              5       
-- 정          26.5              2       
-- 조          29.0              9       
-- 주          26.2              5       
-- 지          22.5              4       
-- 진          23.8              5       
-- 차          29.0              5       
-- 최          28.4363636363636  55      
-- 하          23.5              6       
-- 한          28.3684210526316  19      
-- 허          23.3333333333333  6       
-- 홍          28.24             25      
-- 황          26.1904761904762  21     

SELECT last_name, age
FROM users
WHERE last_name = '곽';
-- last_name  age
-- ---------  ---
-- 곽          25
-- 곽          30
-- 곽          28
-- 곽          15

-- GROUP BY는 결과가 정렬되지 않아요. 기존 순서와 바뀜
-- 원칙적으로 내가 정렬해서 보고 싶으면 ORDER BY!

SELECT *
FROM users
LIMIT 5;
-- first_name  last_name  age  country  phone          balance       
-- ----------  ---------  ---  -------  -------------  -------       
-- 정호          유          40   전라북도     016-7280-2855  370    
-- 경희          이          36   경상남도     011-9854-5133  5900   
-- 정자          구          37   전라남도     011-4177-8170  3100   
-- 미경          장          40   충청남도     011-9079-4419  250000 
-- 영환          차          30   충청북도     011-2921-4284  220  

SELECT last_name, COUNT(*)
FROM users
GROUP BY last_name
LIMIT 5;

-- last_name  COUNT(*)
-- ---------  --------
-- 강          23
-- 고          10
-- 곽          4
-- 구          2
-- 권          17

-- GROUP BY WHERE를 쓰고 싶다.
-- 100번 이상 등장한 성만 출력하고 싶음. 
SELECT last_name, COUNT(last_name)
FROM users
WHERE COUNT(last_name) > 100
GROUP BY last_name;
-- 오류 발생!
-- Parse error: misuse of aggregate: COUNT()
--   LECT last_name, COUNT(last_name) FROM users WHERE COUNT(last_name) > 100 GROUP

-- 조건에 따른 GROUP 하려면
-- HAVING을 쓴다!
SELECT last_name, COUNT(last_name)
FROM users
GROUP BY last_name
HAVING COUNT(last_name) > 100;

-- last_name  COUNT(last_name)
-- ---------  ----------------
-- 김          268             
-- 이          179          