# Python 기초



## 파이썬(Python)이란?

- Easy to learn
  - 다른 프로그래밍 언어보다 문법이 간단하면서도 엄격하지 않음
    - 예시 : 변수에 별도의 타입 지정이 필요 없음
  - 문법 표현이 매우 간결하여 프로그래밍 경험이 없어도 짧은 시간 내에 마스터할 수 있음
    - 예시 : 문장을 구분할 때 중괄호({,}) 대신 들여쓰기를 사용
- Expressive Language
  - 같은 작업에 대해서도 C나 자바로 작성할 때 보다 더 간결하게 작성 가능
- 크로스 플랫폼 언어
  - 원도우즈(Windows), macOS, 리눅스(Linux), 유닉스(Unix) 등 다양한 운영체제에서 실행가능

## 파이썬의 특징

- 인터프리터 언어(Interpreter)
  - 소스코드를 기계어로 변환하는 컴파일 과정 없이 바로 실행 가능
  - 코드를 대화하듯 한 줄 입력하고 실행한 후, 바로 확인할 수 있음
- 객체 지향 프로그래밍(Object Oriented Programming)
  - 파이썬은 객체지향 언어이며, 모든 것이 객체로 구현되어 있음
  - 객체(Object) : 숫자, 문자, 클래스 등 값을 가지고 있는 모든 것

### 기초 문법

- 코드 스타일 가이드
  - 코드를 '어떻게 작성할지'에 대한 가이드 라인
  - 파이썬에서 제안하는 스타일 가이드
    - [PEP8](https://www.python.org/dev/peps/pep-0008/)
  - 기업, 오픈소스 등에서 사용되는 스타일 가이드
    - [Google Style guide](https://google.github.io/styleguide/pyguide.html) 등

#### 들여쓰기

- Space Sensitive
  - 문장을 구분할 때, 들여쓰기 (indentation)  사용
  - 들여쓰기를 할 때는 4칸(spaace키 4번) 혹은 1탭(Tab키 1번)을 입력
    - 주의! 한 코드 안에서는 반드시 한 종류의 들여쓰기를 사용 -> 혼용하면 안됨
      - Tab으로 들여쓰면 계속 Tab으로 들여써야 함
      - 원칙적으로는 공백(빈칸, space) 사용을 권장 *PEP8 권장사항

##  변수(Variable)

- 변수란 ?

  - 컴퓨터 메모리 어딘가에 저장되어 있는 객체를 참조하기 위해 사용되는 이름

    - 객체(object) : 숫자, 문자, 클래스 등 값을 가지고 있는 모든 것

      -> 파이썬은 객체지향 언어이며, 모든 것이 객체로 구현되어 있음

  - 동일 변수에 다른 객체를 언제든 할당할 수 있기 때문에,

    즉, 참조하는 객체가 바뀔 수 있기 때문에 '변수' 라고 불림

  - 변수는 할당 연산자(=)를 통해 값을 할당(assignment)

  - type()

    - 변수에 할당된 값의 타입

  - Id()

    - 변수에 할당된 값(객체)의 고유한 아이덴티티(identity) 값이며, 메모리주소

## 식별자(Identifiers)

- 파이썬 객체(변수, 함수, 모듈, 클래스 등)를 식별하는데 사용하는 이름
- 규칙
  - 식별자의 이름은 영문 알파벳, 언더스코어(_), 숫자로 구성
  - 첫 글자에 숫자가 올 수 없음
  - 길이제한이 없고, 대소문자를 구별
  - 다음의 키워드(keyword)는 예약어(reserved words)로 사용할 수 없음

- 내장함수나 모듈 등의 이름으로도 만들면 안됨

- 기존의이름에다른값을할당하게되므로더이상동작하지않음

## 사용자 입력

- input([prompt])

  - 사용자로부터값을즉시입력받을수있는내장함수

  - 대괄호부분에문자열을넣으면입력시,해당문자열을출력할수있음 

  - 반환값은항상문자열의형태로반환

    ``` python
    name = input('이름을 입력해주세요 :') print(name)
    # 이름을 입력해주세요 : 파이썬 type(name)
    # str
    ```

    

## 주석

- 코드에 대한 설명
  - 중요한점이나다시확인하여야하는부분을표시
  - 컴퓨터는 주석을 인식하지 않음 사용자만을 위한 것
- 가장 중요한 습관
  - 개발자에게 주석을 작성하는 습관은 매우 중요
  - 쉬운이해와코드의분석및수정이용이
    - 주석은코드실행에영향을미치지않을뿐만아니라
    -  프로그램의 속도를 느리게 하지 않으며, 용량을 늘리지 않음

- 한줄주석
  - 주석으로처리될내용앞에‘#’을입력
    - 한줄을온전히사용할수도있고,그줄코드뒷부분에작성할수있음

## 자료형 분류

- 불린형(Boolean Type)
- 수치형(Numeric Type)
  - int (정수, integer)
  - float (부동소수점, 실수, floating point number) 
  - complex(복소수,complexnumber)

- 문자열(String Type)

- None

  - 파이썬자료형중하나

  - 파이썬에서는 값이 없음을 표현하기 위해 None 타입이 존재함.
  - 일반적으로 반환 값이 없는 함수에서 사용하기도 함.



## 불린형(Boolean Type)

### 불린(Boolean)

- True / False 값을 가진 타입은 bool
- 비교/논리 연산을 수행함에 있어서 활용됨
- 다음은 모두 False로 변환
  - 0, 0.0, (), [], {}, '', None

- bool() 함수
  - 특정 데이터가 True인지 False인지 검증

## 연산자(Operator)

### 논리 연산자(Logical Operator)

- 논리식을 판단하여 참(True)와 거짓(False)를 반환함

  | 연산자  |              내용              |
  | :-----: | :----------------------------: |
  | A and B |    A와 B 모두 True시, True     |
  | A or B  |   A와 B 모두 False시, False    |
  |   Not   | True를 False로, False를 True로 |

- and:모두참인경우참,그렇지않으면거짓
- or:둘중하나만참이라도참,그렇지않으면거짓
- not : 참 거짓의 반대의 결과

## 수치형(Numeric Type)

### 정수(int)

- 모든 정수의 타입은 int
- 매우큰수를나타낼때오버플로우가발생하지않음
  - 오버플로우(overflow) : 데이터 타입별로 사용할 수 있는 메모리의 크기를 넘어서는 상황



### 실수(float)

- 정수가 아닌 모든 실수는 float 타입



### 복소수(Complex)

- 실수부와 허수부로 구성된 복소수는 모두 complex 타입
  - 허수부를j로표현

### 산술 연산자(Arithmetic Operator)

- 기본적인 사칙연산 및 수식 계산

| 연산자 |             내용              |
| :----: | :---------------------------: |
|   +    |             덧셈              |
|   -    |             뺄셈              |
|   *    |             곱셈              |
| **% ** | **나머지 (중요! ex : 홀,짝)** |
| **/**  |          **나눗셈**           |
| **//** |            **몫**             |
| ****** |         **거듭제곱**          |

### 복합 연산자(In-place Operator)

- 연산과 할당이 함께 이뤄짐

| 연산자  |    내용    |
| :-----: | :--------: |
| a += b  |   a=a+b    |
| a -= b  |   a=a-b    |
| a *= b  |  a =a * b  |
| a /= b  |  a =a / b  |
| a //= b | a = a // b |
| a %= b  |   a=a%b    |
| a **= b | a = a ** b |

### 비교 연산자(Comparison Operator)

- 값을 비교하며, True / False 값을 리턴함

| 연산자 |            내용             |
| :----: | :-------------------------: |
|   <    |            미만             |
|   <=   |            이하             |
|   >    |            초과             |
|   >=   |            이상             |
|   ==   |            같음             |
|   !=   |          같지 않음          |
|   is   |    객체 아이덴티티(OOP)     |
| is not | 객체 아이덴티티가 아닌 경우 |

## 문자열(String Type)

- 모든 문자는 str 타입
- 문자열은 작은 따옴표(')나 큰 따옴표(")를 활용하여 표기
  - 문자열을묶을때동일한문장부호를활용
  - PEP8에서는 소스코드 내에서 하나의 문장부호를 선택하여 유지하도록 함

### 중첩따옴표(Nested Quotes)

- 따옴표 안에 따옴표를 표현할 경우
  - 작은따옴표가들어있는경우는큰따옴표로문자열생성
  - 큰따옴표가들어있는경우는작은따옴표로문자열생성

### 삼중따옴표(Triple Quotes)

- 작은따옴표나큰따옴표를삼중으로사용
  - 따옴표 안에 따옴표를 넣을 때
  - 여러줄을나눠입력할때편리

### 인덱싱

- 인덱스를통해특정값에접근할수있음 

- s[1] => ‘b’

  [인덱싱 관련 자료](https://wikidocs.net/2838)

### 기타

- 결합(Concatenation)

  ``` python
  'hello, ' + 'python!' 
  # 'hello, python!'
  ```

- 반복(Repetition)

  ```python
  'hi!' * 3
  # 'hi!hi!hi!'
  ```

- 포함(Membership)

  ```python
  'a' in 'apple' # True
  'app' in 'apple' # True
  'b' in 'apple'
  # False
  ```

## 문자열(String Type) 활용

### Escape sequence

- 문자열 내에서 특정 문자나 조작을 위해서 역슬래시(\\)를 활용하여 구분

  [이스케이프 시퀀스 정리](https://docs.microsoft.com/ko-kr/cpp/c-language/escape-sequences?view=msvc-170)

  ```python
   print('철수 \'안녕\'')
  # 철수 '안녕'
  print('이 다음은 엔터.\n그리고 탭\t탭') # 이 다음은 엔터.
  #그리고탭 탭
  ```

### String Interpolation

- 문자열을 변수를 활용하여 만드는 법

  - %-formatting

  ```python
   name = 'Kim' score = 4.5
  print('Hello, %s' % name) print('내 성적은 %d' % score) print('내 성적은 %f' % score)
  # Hello, Kim
  # 내 성적은 4
  # 내 성적은 4.500000
  ```

## 형 변환(Typecasting)

### 자료형 변환 (Typecasting)

- 파이썬에서 데이터 형태는 서로 변환할 수 있음

  - 암시적형변환(Implicit)
    - 사용자가 의도하지 않고, 파이썬 내부적으로 자료형을 변환 하는 경우

  - 명시적형변환(Explicit)
    - 사용자가 특정 함수를 활용하여 의도적으로 자료형을 변환 하는 경우

### 암시적 형 변환(Implicit Typecasting)

- 사용자가 의도하지 않고, 파이썬 내부적으로 자료형을 변환 하는 경우
  - bool
  - Numeric type (int, float, complex)

```python
True + 3
3 + 5.0
3 + 4j + 5
True + 3 #4
3 + 5.0 # 8.0
3 + 4j + 5 # (8+4j)
```



### 명시적 형 변환(Explicit Typecasting)

- int
  - str*,float⇒int*
- *float*
  - str*,int⇒float
-  str
  - int, float, list, tuple, dict ⇒ str

```python
# 문자열은 암시적 타입 변환이 되지 않음 '3' + 4
# TypeError: can only concatenate str (not "int") to str
# 명시적 타입 변환이 필요함 int('3') + 4
#7
# 정수 형식이 아닌 경우 타입 변환할 수 없음 int('3.5') + 5
# ValueError: invalid literal for int() with base 10: '3.5'
float('3.5') + 5
# 8.5
```



## 컨테이너(Container)

### 컨테이너(Container) 정의

- 컨테이너란?
  - 여러개의값을담을수있는것(객체)으로,서로다른자료형을저장할수있음
  - 예시:List,tuple
- 컨테이너의 분류
  - 순서가 있는 데이터 (Ordered) vs. 순서가 없는 데이터 (Unordered)
  - 순서가있다 != 정렬되어있다.

- 시퀀스
  - 문자열(immutable):문자들의나열
  - 리스트 (mutable) : 변경 가능한 값들의 나열
  - 튜플(immutable):변경불가능한값들의나열 • 레인지(immutable):숫자의나열

- 컬렉션/비시퀀스
  - 세트(mutable):유일한값들의모음
  - 딕셔너리 (mutable) : 키-값들의 모음

## 시퀀스형 컨테이너 (Sequence Container)

### 시퀀스형 주요 공통 연산자

|       연산       |                            결과                            |
| :--------------: | :--------------------------------------------------------: |
|       s[i]       |             s 의 i 번째 항목, 0에서 시작합니다             |
|      s[i:j]      |               s 의 i 에서 j 까지의 슬라이스                |
|     s[i:j:k]     |           s 의 i 에서 j 까지 스텝 k 의 슬라이스            |
|       s+t        |                   s 와 t 의 이어 붙이기                    |
| s * n 또는 n * s |               s 를 그 자신에 n 번 더하는 것                |
|      x in s      | s 의 항목 중 하나가 x 와 같으면 True, 그 렇지 않으면 False |
|    x not in s    | s 의 항목 중 하나가 x 와 같으면 False, 그 렇지 않으면 True |
|      len(s)      |                         s 의 길이                          |
|      min(s)      |                    s 의 가장 작은 항목                     |
|      max(s)      |                     s 의 가장 큰 항목                      |



## 리스트(List)

### 리스트(List) 정의

- 변경 가능한 값들의 나열된 자료형
- 순서를가지며,서로다른타입의요소를가질수있음

- 변경 가능하며(mutable), 반복 가능함(iterable)
- 항상 대괄호 형태로 정의하며, 요소는 콤마로 구분

### 생성과 접근

- 리스트는 대괄호([]) 혹은 list() 를 통해 생성
- 순서가 있는 시퀀스로 인덱스를 통해 접근 가능
  - 값에 대한 접근은 list[i]

```python
 # 생성
my_list = [] another_list = list() type(my_list)
# <class 'list'> type(another_list)
# <class 'list'>
```

### 리스트 접근과 명령

``` python
# 값 접근
a = [1, 2, 3] print(a[0]) #1
# 값 변경
a[0] = '1' print(a)
# ['1', 2, 3]
```

### 리스트 값 추가/삭제

- 값 추가는 .append()를 활용하여 추가하고자 하는 값을 전달

``` python
 even_numbers = [2, 4, 6, 8] 
 even_numbers.append(10) 
 even_numbers
# => [2, 4, 6, 8, 10]
```

- 값 삭제는 .pop()을 활용하여 삭제하고자 하는 인덱스를 전달

```python
even_numbers = [2, 4, 6, 8]
even_numbers.pop(0)
even_numbers
# => [4, 6, 8]
```



## 튜플(Tuple)

### 튜플(Tuple) 정의

- 불변한 값들의 나열
- 순서를가지며,서로다른타입의요소를가질수있음
- 변경 불가능하며(immutable), 반복 가능함(iterable)
- 항상 소괄호 형태로 정의하며, 요소는 콤마로 구분

### 생성과 접근

- 소괄호(()) 혹은 tuple()을 통해 생성
- 값에 대한 접근은 리스트와 동일하게 인덱스로 접근
  - 값 변경은 불가능하여 추가/삭제도 불가능함

```python
 # 값 접근
a = (1, 2, 3, 1) a[1]
#값 변경=>불가능 a[1] = ‘3’
TypeError Traceback (most recent call last)
1 # 값 변경 => 불가능 ---->
2 a[1] = '3’
TypeError: 'tuple' object does not support item assignment
```

## 레인지(Range)

- 숫자의 시퀀스를 나타내기 위해 사용
  - 기본형:range(n)
    - 0부터 n-1까지의 숫자의 시퀀스

- 범위 지정 : range(n, m)
  - n부터 m-1까지의 숫자의 시퀀스

- 범위 및 스텝 지정 : range(n, m, s)
  - n부터 m-1까지 s만큼 증가시키며 숫자의 시퀀스

- 변경 불가능하며(immutable), 반복 가능함(iterable)
- range는 숫자의 시퀀스를 나타내기 위해 사용

## 비시퀀스형 컨테이너 (Associative Container)

### 세트 (Set)

#### 세트(Set) 생성

- 유일한 값들의 모음(collection)
- 순서가 없고 중복된 값이 없음.
  - 수학에서의 집합과 동일한 구조를 가지며, 집합 연산도 가능

- 변경 가능하며(mutable), 반복 가능함(iterable)
  - 단,셋은순서가없어반복의결과가정의한순서와다를수있음

- 중괄호({}) 혹은 set()을 통해 생성
  - 빈 Set를 만들기 위해서는 set()을 반드시 활용해야 함

- 순서가없어별도의값에접근할수없음

```python
{1, 2, 3, 1, 2} 
# {1, 2, 3} <--- 중복값 제거
type({1, 2, 3}) 
# <class 'set'> 
blank_set = set()
```

#### 세트(Set) 추가/삭제

- 값 추가는 .add()를 활용하여 추가하고자 하는 값을 전달
- 값 삭제는 .remove()를 활용하여 삭제하고자 하는 값을 전달

.add()

````python
numbers = {1, 2, 3}
numbers.add(5) numbers
# => {1, 2, 3, 5}
numbers.add(1) 
numbers
# => {1, 2, 3, 5}
````

.remove()

```python
numbers = {1, 2, 3} 
numbers.remove(1) 
numbers
# => {2, 3} 
numbers.remove(5)
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module> 
#KeyError: 5
```

#### 셋(Set) 활용

- 세트를활용하면다른컨테이너에서중복된값을쉽게제거할수있음
  - 단,이후순서가무시되므로순서가중요한경우사용할수없음 
- 아래의 리스트에서 고유한 지역의 개수는?

````python
my_list = ['서울', '서울', '대전', '광주', '서울', '대전', '부산', '부산’]
len(set(my_list))
#4
set(my_list)
# {'광주', '대전', '부산', '서울'}
````



## 딕셔너리 (Dictionary)

- 키-값(key-value) 쌍으로 이뤄진 모음(collection)
  - 키(key)
    - 불변 자료형만 가능 (리스트, 딕셔너리 등은 불가능함)
  - 값(values)
    - 어떠한형태든관계없음

- 키와값은:로구분됩니다.개별요소는,로구분됩니다.

- 변경 가능하며(mutable), 반복 가능함(iterable)
  - 딕셔너리는 반복하면 키가 반환됩니다.

``` python
students = {'홍길동': 30, '김철수': 25} 
students['홍길동']
# 30
```

### 딕셔너리(Dictionary) 생성

- key와 value가 쌍으로 이뤄진 자료구조
  - key는변경불가능한데이터(immutable)만활용가능
    - string, integer, float, boolean, tuple, range
  - value는모든값으로설정가능(List,Dictionary등)

``` bash
dict_c = {[1, 2, 3]: 'hi’} 
TypeError Traceback (most recent call last) 
----> 1 dict_c = {[1, 2, 3]: 'hi’} 
TypeError: unhashable type: 'list'
```

### 딕셔너리(Dictionary) 접근

``` python
 movie = {
		'title': '설국열차',
		'genres': ['SF', '액션', '드라마'],
		'open_date': '2013-08-01',
		'time': 126,
		'adult': False,
}
movie['genres']
# ['SF', '액션', '드라마']
movie['actors’]
Traceback (most recent call last): File "<stdin>", line 1, in <module> KeyError: 'actors'
```

### 딕셔너리(Dictionary) 키-값 추가 및 변경

- 딕셔너리에 키와 값의 쌍을 추가할 수 있으며,
- 이미 해당하는 키가 있다면 기존 값이 변경됩니다.

``` python
students = {'홍길동': 100, '김철수': 90} 
students['홍길동'] = 80
# {'홍길동': 80, '김철수': 90} 
students['박영희'] = 95
# {'홍길동': 80, '김철수': 90, '박영희': 95}
```

### 딕셔너리(Dictionary) 키-값 삭제

- 키를 삭제하고자하면 .pop()을 활용하여 삭제하고자 하는 키를 전달

``` python
students = {'홍길동': 30, '김철수': 25} 
students.pop('홍길동')
students
# {'김철수': 25}
```

- 키가 없는 경우는 KeyError 발생

``` python
students = {'홍길동': 30, '김철수': 25} 
students.pop('jane')
Traceback (most recent call last):
File "<stdin>", line 1, in <module> 
KeyError: 'jane'
```

