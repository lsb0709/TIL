# 사전 설정

## 실행

```bash
$ sqlite3 healthcare.sqlite3 
```

## Column 출력 설정

```sql
sqlite3> .headers on 
sqlite3> .mode column
```

## table 및 스키마 조회

```sql
sqlite3> .tables
healthcare

sqlite3> .schema healthcare
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

blood_pressure INTEGER 
NOT NULL,
smoking INTEGER NOT NULL,
is_drinking BOOLEAN NOT NULL
);
```

# 문제

### 1. 추가되어 있는 모든 데이터의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare;
```

```
COUNT(*)
--------
1000000
```

### 2. 나이 그룹이 10(age)미만인 사람의 수를 출력하시오.

```sql
SELECT COUNT(age) FROM healthcare WHERE age < 10;
```

```
COUNT(age)
--------
156277
```

### 3. 성별이 1인 사람의 수를 출력하시오.

```sql
SELECT COUNT(sido) FROM healthcare WHERE gender = 1;
```

```
COUNT(sido)
--------
510689
```

### 4. 흡연 수치(smoking)가 3이면서 음주(is_drinking)가 1인 사람의 수를 출력하시오.

```sql
SELECT COUNT(sido) FROM healthcare WHERE smoking = 3 and is_drinking = 1;
```

```
COUNT(sido)
--------
510689
```

### 5. 양쪽 시력이(va_left, va_right) 모두 2.0이상인 사람의 수를 출력하시오.

```sql
SELECT COUNT(sido) FROM healthcare WHERE va_left = 2.0 and va_right = 2.0;
```

```
COUNT(sido)
--------
1692
```

### 6. 시도(sido)를 모두 중복 없이 출력하시오.

```sql
SELECT DISTINCT sido FROM healthcare;
```

```
sido
36
27
11
31
41
44
48
30
42
43
46
28
26
47
45
29
49
```

### 자유롭게 조합해서 원하는 데이터를 출력해보세요.

> 예) 허리 둘레가 x이상이면서 몸무게가 y이하인 사람
>
> ```sql
> SELECT height, weight FROM healthcare WHERE height > 190 and weight > 120;
> ```
>
> ```
> height	weight
> 195	    125
> ```
>
> 
# 2일차 실습

## 사전 확인

### 실행

```bash
$ sqlite3 healthcare.sqlite3 
```

### Column 출력 설정

```sql
sqlite3> .headers on 
sqlite3> .mode column
```

### table 및 스키마 조회

```sql
sqlite3> .tables
healthcare

sqlite3> .schema healthcare
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

    blood_pressure INTEGER 
    NOT NULL,
    smoking INTEGER NOT NULL,
    is_drinking BOOLEAN NOT NULL
);
```

## 문제

### 1. 추가되어 있는 모든 데이터의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare;
```

```
-- COUNT(*)
-- 1000000
```

### 2. 연령 코드(age)의 최대, 최소 값을 모두 출력하시오. 

```sql
SELECT MAX(age), MIN(age) FROM healthcare;
```

```
-- MAX(age)	  MIN(age)
--   18	        9
```

### 3. 신장(height)과 체중(weight)의 최대, 최소 값을 모두 출력하시오.

```sql
SELECT MAX(height), MAX(weight), MIN(height), MIN(weight) FROM healthcare;
```

```
-- MAX(height)	MAX(weight)	MIN(height)	MIN(weight)
-- 195	        135	        130	        30
```

### 4. 신장(height)이 160이상 170이하인 사람은 몇 명인지 출력하시오.

```sql
SELECT COUNT(sido) FROM healthcare WHERE 160 <= height and height <= 170;
```

```
-- COUNT(sido)
-- 516930
```

### 5. 음주(is_drinking)를 하는 사람(1)의 허리 둘레(waist)를 높은 순으로 5명 출력하시오. 

```sql
SELECT id, waist FROM healthcare WHERE is_drinking = 1 AND waist <>'' ORDER BY waist DESC LIMIT 5;
```

```
id 		waist
993531  146.0
878897  142.0
826643  141.4
567314  140.0
611146  140.0
```

### 6. 시력 양쪽(va_left, va_right)이 1.5이상이면서 음주(is_drinking)를 하는 사람의 수를 출력하시오.

```sql
SELECT COUNT(sido) FROM healthcare WHERE (va_left >= 1.5 and va_right >= 1.5) and is_drinking = 1;
```

```
COUNT(sido)
36697
```

### 7. 혈압(blood_pressure)이 정상 범위(120미만)인 사람의 수를 출력하시오.

```sql
SELECT COUNT(sido) FROM healthcare WHERE blood_pressure < 120;
```

```
OUNT(sido)
360808
```

### 8. 혈압(blood_pressure)이 140이상인 사람들의 평균 허리둘레(waist)를 출력하시오.

```sql
SELECT AVG(waist) FROM healthcare WHERE blood_pressure >= 140;
```

```
AVG(waist)
85.8665098512525
```

### 9. 성별(gender)이 1인 사람의 평균 키(height)와 평균 몸무게(weight)를 출력하시오.

```sql
SELECT AVG(waist) FROM healthcare WHERE blood_pressure >= 140;
```

```
AVG(height)				AVG(weight)
167.452735422145	    69.7131620222875
```

### 10. 키가 가장 큰 사람 중에 두번째로 무거운 사람의 id와 키(height), 몸무게(weight)를 출력하시오.

```sql
SELECT id, height, weight FROM healthcare ORDER BY height DESC, weight DESC LIMIT 1 OFFSET 1;
```

```
id			height	weight
836005	    195		110
```

### 11. BMI가 30이상인 사람의 수를 출력하시오. 

> BMI는 체중/(키*키)의 계산 결과이다. 
> 키는 미터 단위로 계산한다.

```sql
SELECT COUNT(*) FROM healthcare WHERE weight / ((height / 0.01) * (height / 0.01)) >= 30;
```

```
COUNT(*)
53121
```

### 12. 흡연(smoking)이 3인 사람의 BMI지수가 제일 높은 사람 순서대로 5명의 id와 BMI를 출력하시오.

> BMI는 체중/(키*키)의 계산 결과이다. 
> 키는 미터 단위로 계산한다.

```sql
SELECT id, weight / ((height / 0.01) * (height / 0.01)) as BMI FROM healthcare WHERE smoking = 3 ORDER BY BMI DESC LIMIT 5;
```

```
id			BMI
99120		135
100174	    135
142639	    135
172459	    135
239321	    135
```

### 13. 자유롭게 쿼리를 작성해주시고, 결과와 함께 공유해주세요.

```sql
SELECT id, height FROM healthcare ORDER BY height ASC, weight ASC LIMIT 5 OFFSET 2;
```

```
-- id	    height
-- 78640	130
-- 155732	130
-- 156645	130
-- 158262	130
-- 190817	130
```

### 14. 자유롭게 쿼리를 작성해주시고, 결과와 함께 공유해주세요.

```sql
SELECT gender, age FROM healthcare WHERE gender = 1 and age > 17 LIMIT 1;
```

```
gender	age
1		18
```

### 15. 자유롭게 쿼리를 작성해주시고, 결과와 함께 공유해주세요.

```sql
SELECT * FROM healthcare WHERE age > 15 and height > 180 and weight > 80;
```

```
id			sido	gender	age	height	weight		waist		va_left	    va_right	blood_pressure	smoking		is_drinking
565978	    47		1		16	185		100			113.0		0.7		    0.3			110		        2			1
574661	    11		1		16	185		85			96.0		0.5			0.5			122				1	        0
```

