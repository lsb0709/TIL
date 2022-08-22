-- Q. 사용자(users)와 각각의 역할을 출력하시오

SELECT *
FROM users JOIN role
    ON users.role_id = role.id;

-- id  name  role_id  id  title
-- --  ----  -------  --  -----
-- 1   관리자   1        1   admin
-- 2   김철수   2        2   staff
-- 3   이영희   2        2   staff

-- Q. staff(2) 사용자(users)를 역활과 함께 출력하시오.

SELECT *
FROM users JOIN role
    ON users.role_id = role.id
WHERE role.id = 2;

-- id  name  role_id  id  title
-- --  ----  -------  --  -----
-- 2   김철수   2        2   staff
-- 3   이영희   2        2   staff

-- Q. 사용자(users)와 각각의 역할을 이름의 내림차순으로 출력하시오.

SELECT *
FROM users JOIN role
    ON users.role_id = role.id
ORDER BY users.name DESC;

-- id  name  role_id  id  title
-- --  ----  -------  --  -----
-- 3   이영희   2        2   staff
-- 2   김철수   2        2   staff
-- 1   관리자   1        1   admin

-- Q. 모든 게시글을 사용자 정보와 함께 출력하시오.

SELECT *
FROM articles LEFT OUTER JOIN users
    ON users.role_id = articles.user_id;

-- id  title  content  user_id  id  name  role_id
-- --  -----  -------  -------  --  ----  -------
-- 1   1번글    111      1        1   관리자   1      
-- 2   2번글    222      2        2   김철수   2      
-- 2   2번글    222      2        3   이영희   2      
-- 3   3번글    333      1        1   관리자   1     

-- Q. 작성자가 있는 모든 게시글을 사용자 정보와 함께 출력하시오.

SELECT *
FROM articles LEFT OUTER JOIN users
    ON users.id = articles.user_id
WHERE articles.user_id IS NOT NULL;

-- id  title  content  user_id  id  name  role_id
-- --  -----  -------  -------  --  ----  -------
-- 1   1번글    111      1        1   관리자   1      
-- 2   2번글    222      2        2   김철수   2      
-- 3   3번글    333      1        1   관리자   1   

-- Q. 모든 게시글과 모든 사용자 정보를 출력하시오.

SELECT *
FROM articles FULL OUTER JOIN users
    ON users.id = articles.user_id;

-- Q. user와 role의 CROSS JOIN 결과를 출력하시오.

SELECT *
FROM users CROSS JOIN role;

-- id  name  role_id  id  title  
-- --  ----  -------  --  -------
-- 1   관리자   1        1   admin  
-- 1   관리자   1        2   staff  
-- 1   관리자   1        3   student
-- 2   김철수   2        1   admin  
-- 2   김철수   2        2   staff  
-- 2   김철수   2        3   student
-- 3   이영희   2        1   admin  
-- 3   이영희   2        2   staff  
-- 3   이영희   2        3   student

-- 3개의 테이블 조인
SELECT * 
FROM articles
    JOIN users
        ON articles.user_id = users.id
    JOIN role
        ON users.role_id = role.id;
-- id  title  content  user_id  id  name  role_id  id  title
-- --  -----  -------  -------  --  ----  -------  --  -----
-- 1   1번글    111      1        1   관리자   1        1   admin
-- 2   2번글    222      2        2   김철수   2        2   staff
-- 3   3번글    333      1        1   관리자   1        1   admin