# 기본 함수와 연산



- 문자열 함수

  - SUBSTR(문자열 ,start, length) : 문자열 자르기
    - 시작 인덱스는 1, 마지막 인덱스는 -1
  - TRIM(문자열), LTRIM(문자열), RTRIM(문자열) : 문자열 공백 제거

  

  - LENGTH(문자열) : 문자열 길이

    ```sqlite
    SELECT 
        LENGTH(first_name),
        first_name
    FROM users
    LIMIT 5;
    ```

    ```sqlite
    LENGTH(first_name)  first_name
    ------------------  ----------
    2                   정호
    2                   경희
    2                   정자
    2                   미경
    2                   영환
    ```

    

  - REPLACE(문자열, 패턴, 변경값) : 패턴에 일치하는 부분을 변경

    ```sqlite
    SELECT
        first_name,
        phone,
        REPLACE(phone, '-', '')
    FROM users
    LIMIT 5;
    ```

    ```sqlite
    first_name  phone          REPLACE(phone, '-', '')
    ----------  -------------  -----------------------
    정호          016-7280-2855  01672802855            
    경희          011-9854-5133  01198545133            
    정자          011-4177-8170  01141778170            
    미경          011-9079-4419  01190794419            
    영환          011-2921-4284  01129214284 
    ```

    

  - UPPER(문자열 ), LOWER(문자열) : 대소문자 변경

  

  

  - || : 문자열 합치기(concatenation)

    ```sqlite
    SELECT 
        last_name || first_name 이름,
        age,
        country,
        phone,
        balance
    FROM users
    LIMIT 5;
    ```

    ```sqlite
    이름   age  country  phone          balance
    ---  ---  -------  -------------  -------
    유정호  40   전라북도     016-7280-2855  370
    이경희  36   경상남도     011-9854-5133  5900
    구정자  37   전라남도     011-4177-8170  3100
    장미경  40   충청남도     011-9079-4419  250000
    차영환  30   충청북도     011-2921-4284  220
    ```



- 숫자 함수

  - ABS(숫자) : 절대 값

    ```sqlite
    SELECT ABS(-10)
    FROM users;
    ```

  - SIGN(숫자) : 부호 (양수 1, 음수 -1, 0 0)

    ```sqlite
    select sign(-10000), sign(999), sign(0)
    from users;
    ```

  - MOD(숫자1, 숫자2) : 숫자1을 숫자2로 나눈 나머지

    ```sqlite
    SELECT MOD(5, 2)
    FROM users;
    ```

  - CEIL(숫자), FLOOR(숫자), ROUND(숫자, 자리) : 올림 , 내림, 반올림

    ```sqlite
    SELECT CEIL(3.14), FLOOR(3.14), ROUND(3.14)
    FROM users;
    ```

  - POWER(숫자1, 숫자2) : 숫자1의 숫자2 제곱

    ```sqlite
    SELECT POWER(9, 2)
    FROM users;
    ```

  - SQRT(숫자) : 제곱근

    ```sqlite
    SELECT SQRT(9)
    FROM suers;
    ```



- 산술 연산자

  - +, -, *, / 와 같은 산술 연산자와 우선 순위를 지정하는 () 기호를 연산에 활용할 수 있음

    ```sqlite
    SELECT age + 1 FROM users;
    ```



## GROUP BY



- ALIAS

  - 칼럼명이나 테이블명이 너무 길거나 다른 명칭으로 확인하고 싶을 때는 ALIAS를 활용

  - AS를 생략하여 공백으로 표현할 수 있음

  - 별칭에 공백, 특수문자 등이 있는 경우 따옴표로 묶어서 표기

    ```sqlite
    SELECT last_name 성 FROM users;
    SELECT last_name AS 성 FROM users;
    SELECT last_name AS 성 FROM users WHERE 성 = '김';
    ```



- GROUP BY

  - SELECT 문의 optional 절

  - 행 집합에서 요약 행 집합을 만듦

  - 선택된 행 그룹을 하나 이상의 열 값으로 요약 행으로 만듦

  - 문장에 WHERE 절이 포함된 경우 반드시 WHERE 절 뒤에 작성해야 함

    ```sqlite
    SELECT * FROM 테이블이름 GROUP BY 컬럼1, 컬럼2;
    ```

  - 지정된 컬럼의 값이 같은 행들로 묶음

  - 집계함수와 활용하였을 때 의미가 있음

  - 그룹화된 각각의 그룹이 하나의 집합으로 집계함수의 인수로 넘겨짐

    ```sqlite
    SELECT * FROM users GROUP BY last_name; 
    ```

  - GROUP BY절에 명시하지 않은 컬럼은 별도로 지정할 수 없음
    - 그룹마다 하나의 행을 출력하게 되므로 집계 함수 등을 활용해야 함
  - GROUP BY의 결과는 정렬되지 않음
    - 기존의 순서와 바뀌는 모습도 있음
    - 원칙적으로 관계형 데이터베이스에서는 ORDER BY를 통해 정렬



- HAVING

  - 집계함수는 WHERE 절의 조건식에서는 사용할 수 없음(실행 순서에 의해)

    - WHERE로 처리하는 것이 GROUP BY 그룹화보다 순서상 앞서 있기 때문

  - 집계 결과에서 조건에 맞는 값을 따로 활용하기 위해서 HVAING을 활용

    ```sqlite
    SELECT * FROM 테이블이름 GROUP BY 컬럼1, 컬럼2 HAVING 그룹조건;
    ```



- SELECT 문장 실행 순서

  - FROM => WHERE => GROUP BY => HAVING => SELECT => ORDER BY

    - FROM 테이블을 대상으로 

    - WHERE 제약조건에 맞춰서 뽑아서 

    - GROUP BY 그룹화 한다.

    - HAVING 그룹 중에 조건과 맞는 것 만을

    - SELECT 조회하여

    - ORDER BY 정렬하고

    - LIMIT / OFFSET 특정 위치의 값을 가져온다.

      ```sqlite
      SELECT 칼럼명
      FROM 테이블명
      WHERE 조건식
      GROUP BY 칼럼 혹은 표현식
      HAVING 그룹조건식
      ORDER BY 칼럼 혹은 표현식
      LIMIT 숫자 OFFSET 숫자;
      ```



## ALTER TABLE



- ALTER TABLE

  - 테이블 이름 변경

    ```sqlite
    ALTER TABLE 기존테이블이름 RENAME TO 새로운테이블이름;
    
    ALTER TABLE talbe_name
    RENAME TO new_name;
    ```

  - 새로운 column 추가

    ```sqlite
    ALTER TABLE 테이블이름 ADD COLUMN 컬럼이름 데이터타입설정;
    
    ALTER TABLE talbe_name
    ADD COLUMN column_definiton;
    ```

  - Column 이름 수정 (new in sqlite 3.25.0)

    ```sqlite
    ALTER TABLE talbe_name
    RENAME COLUMN current_name TO new_name;
    ```

  - Column 삭제 (new in sqlite 3.35.0)

    ```sqlite
    ALTER TABLE talbe_name
    DROP COLUMN column_name;
    ```

    