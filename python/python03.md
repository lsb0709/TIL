# 함수

## 함수 기초

### 함수의 정의

- 함수(Function)
  - 특정한 기능을 하는 코드의 조각(묶음)
  - 특정명령을수행하는코드를매번다시작성하지않고,필요시에만호출하여간편히사용

- 사용자 함수(Custom Function)
  - 구현되어있는함수가없는경우,사용자가직접함수를작성가능

``` python
 def function_name(parameter):
    # code block
    return returning_value
```

<img src="/Users/isangbaeg/Desktop/TIL/python/image/python03 -1.png" alt="python03 -1" style="zoom:50%;" />



- 내장함수(Built-in Function) 활용

```python
 import math
values = [100, 75, 85, 90, 65, 95]
mean = sum(values) / len(values)
sum_var = sum(pow(value - mean, 2) for value in values) / len(values) std_dev = math.sqrt(sum_var)
print(std_dev)
# 누적 합? sum!
```

- pstdev 함수 (파이썬 표준 라이브러리 - statistics)

```python
import statistics
values = [100, 75, 85, 90, 65, 95] 
statistics.pstdev(values)
# 코드 중복 방지 재사용 용이
```

<img src="/Users/isangbaeg/Desktop/TIL/python/image/python03-2.png" alt="python03-2" style="zoom:50%;" />

https://github.com/python/cpython/blob/main/Lib/statistics.py#L840

- 선언과 호출(define & call) 
- 입력(Input)
-  범위(Scope)
-  결과값(Output)

#### 선언과 호출

- 함수의 선언은 def 키워드를 활용함
- 들여쓰기를 통해 Function body(실행될 코드 블록)를 작성함 
  - Docstring은 함수 body 앞에 선택적으로 작성 가능
    - 작성시에는반드시첫번째문장에문자열''' '''
- 함수는 parameter를 넘겨줄 수 있음
- 함수는 동작 후에 return을 통해 결과값을 전달함



- 함수는 함수명()으로 호출
  - parameter가있는경우,함수명(값1,값2,...)로호출

예시

``` python
num1 = 0
num2 = 1

def func1(a, b):
    return a + b
  
def func2(a, b): 
  	return a - b
  
def func3(a, b):
    return func1(a, 5) + func2(5, b)
  
result = func3(num1, num2)
print(result)

# 답 : 9
```



### 함수의 결과값(Output)

#### return

- 함수는 반드시 값을 하나만 return한다.
  - 명시적인 return이 없는 경우에도 None을 반환한다.
- 함수는 return과 동시에 실행이 종료된다.

#### return vs print

- return은 함수 안에서 값을 반환하기 위해 사용되는 키워드
- print는 출력을 위해 사용되는 함수

### 함수의 입력(Input)

#### parameter vs argument

- Parameter : 함수를 실행할 때, 함수 내부에서 사용되는 식별자
- Argument:함수를호출할때,넣어주는값

````python
 def function(ham): # parameter : ham
    return ham
function('spam')   # argument: 'spam'
````

#### argument

- Argument란?
  - 함수호출시함수의parameter를통해전달되는값
  - Argument는 소괄호 안에 할당 func_name(argument)
    - 필수 Argument : 반드시 전달되어야 하는 argument
    - 선택Argument:값을전달하지않아도되는경우는기본값이전달

#### positional arguments

- 기본적으로 함수 호출 시 Argument는 위치에 따라 함수 내에 전달됨

````python
def add(x, y):   add(2, 3)
  return x + y
````

#### keyword arguments

- 직접 변수의 이름으로 특정 Argument를 전달할 수 있음
- Keyword Argument 다음에 Positional Argument를 활용할 수 없음

````python
def add(x, y): add(x=2, y=5) 
  return x + y add(2, y=5)
````

#### Default Arguments Values

- 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함
  - 정의된것보다더적은개수의argument들로호출될수있음

````python
def add(x, y=0): add(2)
  return x + y
````

<img src="/Users/isangbaeg/Desktop/TIL/python/image/python03-3.png" alt="python03-3" style="zoom:50%;" />

#### 정해지지 않은 개수의 arguments

- 여러 개의 Positional Argument를 하나의 필수 parameter로 받아서 사용
  - 몇 개의 Positional Argument를 받을지 모르는 함수를 정의할 때 유용 

- Argument들은 튜플로 묶여 처리되며, parameter에 *를 붙여 표현

```python
def add(*args): add(2)
	for arg in args: add(2, 3, 4, 5) 
  print(arg)
```

#### 정해지지 않은 개수의 keyword arguments

- 함수가 임의의 개수 Argument를 Keyword Argument로 호출될 수 있도록 지정
- Argument들은 딕셔너리로 묶여 처리되며, parameter에 **를 붙여 표현

```python
def family(**kwargs):
	for key, value in kwargs:
		print(key, ":", value) 
family(father='John', mother='Jane', me='John Jr.')
```

## 함수의 범위(Scope)

### 함수의 scope

- 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분

- scope
  - global scope : 코드 어디에서든 참조할 수 있는 공간
  - local scope : 함수가 만든 scope. 함수 내부에서만 참조 가능 

- variable
  - global variable : global scope에 정의된 변수
  - local variable : local scope에 정의된 변수

#### 객체 수명주기

- 객체는 각자의 수명주기(lifecycle)가 존재
  - built-inscope
    - 파이썬이 실행된 이후부터 영원히 유지
  - globalscope
    - 모듈이호출된시점이후혹은인터프리터가끝날때까지유지
  - local scope
    - 함수가호출될때생성되고,함수가종료될때까지유지

#### 이름 검색 규칙(Name Resolution)

- 파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어 있음
- 아래와 같은 순서로 이름을 찾아나가며, LEGB Rule이라고 부름
  - Local scope : 함수
  - Enclosed scope : 특정 함수의 상위 함수                                              
  - Global scope : 함수 밖의 변수, Import 모듈
  - Built-inscope:파이썬안에내장되어있는함수또는속성

<img src="/Users/isangbaeg/Desktop/TIL/python/image/python03-4.png" alt="python03-4" style="zoom: 33%;" />



- 즉,함수내에서는바깥Scope의변수에접근가능하나수정은할수없음

### 함수 응용

#### 내장 함수 응용

- 파이썬 인터프리터에는 사용할 수 있는 많은 함수와 형(type)이 내장되어 있음

<img src="/Users/isangbaeg/Desktop/TIL/python/image/python03-5.png" alt="python03-5" style="zoom:50%;" />

#### map

- map(function, iterable)
  - 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function)적용하고, 그 결과를 map object로 반환
  - 알고리즘 문제 풀이시 input 값들을 숫자로 바로 활용하고 싶을 때

```python
n, m = map(int, input().split())
# 3, 5
print(n, m)
# 3, 5
```

