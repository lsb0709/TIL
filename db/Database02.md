# WHERE



- Table users 생성

  ```sqlite
  CREATE TABLE users (
  	  first_name TEXT NOT NULL,
      last_name TEXT NOT NULL,
      age INTEGER NOT NULL,
      country TEXT NOT NULL,
      phone TEXT NOT NULL,
      balanec INTEGER NOT NULL
  );
  ```



- csv파일 정보를 테이블에 적용하기

  ```sqlite
  sqlite> .mode csv
  sqlite> import users.csv users
  
  -- 테이블 확인
  sqlite> .tables
  ```



- 특정 조건으로 테이터 조회하기

  ```sqlite
  SELECT * FROM 테이블이름 WHERE 조건;
  ```



- WHERE절에서 사용할 수 있는 연산자
  - 비교 연산자
    - =, >, >=, <, <= 는 숫자 혹은 문자 값의 대/소 동일 여부를 확인하는 연산자
  - 논리 연산자
    - AND
      - 앞에 있는 조건과 뒤에 오는 조건이 모두 참인 경우
    - OR
      - 앞의 조건이나 뒤의 조건이 참인 경우
    - NOT
      - 뒤에 오는 조건의 결과를 반대로
- SQL 사용할 수 있는 연산자
  - BETWEEN 값1 AND 값2
    - 값1과 값2 사이의 비교 (값1 <= 비교값 <= 값2)
  - IN (값1, 값2, ...)
    - 목록 중에 값이 하나라도 일치하면 성공
  - LIKE
    - 비교 문자열과 형태 일치
    - 와일드카드(% : 0개 이상 문자, _: 1개 단일 문자)
  - IS NULL / IS NOT NULL
    - NULL 여부를 확인할 때는 항상 = 대신에 IS를 활용
  - 부정 연산자
    - 같지 않다(!=, ^=, <>)
    - ~와 같지 않다. (NOT 칼럼명 =)
    - ~보다 크지 않다.(NOT 칼럼명 >)
- 연산자 우선순위
  - 1순위 : 괄호 ()
  - 2순위 : NOT
  - 3순위 : 비교 연산자, SQL
  - 4순위 : AND
  - 5순위 : OR



## SQLite Aggregate Functions



- Aggregate function (집계 함수)
  - 값 집합에 대한 계산을 수행하고 단일 값을 반환
    - 여러 행으로부터 하나의 결괏값을 반환하는 함수
  - SELECT 구문에서만 사용됨
  - 예시
    - 테이블 전체 행 수를 구하는 COUNT(*)
    - Age 컬럼 전체 평균 값을 구하는 AVG(age)
  - COUNT
    - 그룹의 항목 수를 가져옴
  - AVG
    - 모든 값의 평균을 계산
  - MAX
    - 그룹에 있는 모든 값의 최대값을 가져옴
  - MIN
    - 그룹에 있는 모든 값의 최소값을 가져옴
  - SUM
    - 모든 값의 합을 계산



## LIKE

- 패턴 일치를 기반으로 데이터를 조회하는 방법
- SQLite는 패턴 구성을 위한 2개의 wildcards를 제공
  - %(precent sign)
    - 0개 이상의 문자
    - 이 자리에 문자열이 있을수도, 없을 수도 있다.
  - _(underscore)
    - 임의의 단일 문자
    - 반드시 이 자리에 한 개의 문자가 존재해야 한다.



##### 와일드 카드 패턴

```sqlite
SELECT * FROM 테이블이름 WHERE 컬럼 LIKE '패턴';
```

| 와일드카드 패턴 | 의미                                          |
| --------------- | --------------------------------------------- |
| 2%              | 2로 시작하는 값                               |
| %2              | 2로 끝나는 값                                 |
| %2%             | 2가 들어가는 값                               |
| _2%             | 아무 값이 하나 있고 두 번째가 2로 시작하는 값 |
| 1___            | 1로 시작하고 총 4자리인 값                    |
| 2_ %_ % / 2__%  | 2로 시작하고 적어도 3자리인 값                |



## ORDER BY



- 조회 결과 집합을 정렬
- SELECT 문에 추가하여 사용
- 정렬 순서를 위한 2개의 keyword 제공
- 특정 컬럼을 기준으로 데이터를 정렬해서 조회하기
  - ASC - 오름차순 (default)
  - DESC - 내림차순

```sqlite
SELECT * FROM 테이블이름 ORDER BY 컬럼 ASC;
SELECT * FROM 테이블이름 ORDER BY 컬럼 DESC;
```