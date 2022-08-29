# HTML



- HTML(Hypertext Markup Language, 하이퍼텍스트 마크업 언어)는 프로그래밍 언어는 아니고, 우리가 보는 웹페이지가 어떻게 구조화되어 있는지 브라우저로 하여금 알 수 있도록 하는 마크업 언어



## 웹 사이트의 구성 요소

- HTML - 구조(정보 또는 설계도)
- CSS - 표현 (디자인 또는 스타일링)
- Javascript - 동작 (기능과 효과)



## 웹 표준

- 웹에서 표준적으로 사용되는 기술이나 규치
- 어떤 브라우저든 웹 페이지가 동일하게 보이도록함(크로스 브라우징)



## 크롬 개발자 도구

- 웹 브라우저 크롬에서 제공하는 개발과 관련된 다양한 기능을 제공
- 주요 기능
  - Elements - DOM 탐색 및 CSS  확인 및 변경
  - Styles - 요소에 적용된 CSS 확인
  - Computed - 스타일이 계산된 최종 결과
  - Event Listeners - 해당 요소에 적용된 이벤트 (JS)
- Sources, Network, Preformance, Application, Security, Audits 등



## HTML 기초

- HTML 태그 구성 요소

  ```html
  <열린태그 속성 = '속성값'> 컨텐츠</닫힌태그>
  ```

  - 요소(element)

  - HTML 요소는 열린 태그와 닫힌 태그 그리고 태그 사이에 위치한 내용으로 구성

    - 요소는 태그로 컨텐츠(내용)를 감싸는 것으로 그 정보의 성격과 의미를 정의
    - 내용이 없는 태그들도 존재(닫는 태그가 없음)
    - br, hr, img, input, link, meta

    

  - 태그명

    - HTML이 갖고 있는 고유의 기능
    - <열린태그></닫힌태그> 형태로 입력

  - 컨텐츠

    - 열린 태그와 닫힌 태그 사이에 있는 내용물

  - 속성

    - HTML 태그가 갖고 있는 추가 정보

  - 속성값

    - 어떤 역할을 수행할지 구체적인 명령을 진행하는 값

```html
<!DOCTYPE html>
<html lang='en'>
<head>
  <meta charset ="UTF-8">
  <title>Document</title>
</head>
<body>
  
</body>
</html>
```

- ```html
  <!DOCTYPE html>
  ```

  HTML5라는 신조어로 문서를 선언하는 태그

- html : HTML 문서의 시작과 끝을 의미

  모든 HTML 태그들은 <html> 태그 안쪽에 입력

- head : 문서 메타데이터 요소

  문서 제목, 인코딩, 스타일, 외부 파일 로딩 등 

  일반적으로 브라우저에 나타나지 않는 내용

- body : 문서 본문 요소

  실제 화면 구성과 관련된 내용



- HTML 기본 구조

  ```html
  <head>
    <title>HTML 수업</title>
    <meta charset='UTF-8'>
    <link href='style.css' rel='stylesheet'>
    <script src='javascript.js'></script>
    <style>
    	p{
    		color: black;
      }
    </style>
  </head>
  ```

  - head  예시

    ```html
    <title> : 브라우저 상단 타이틀
    <meta> : 문서 레벨 메타데이터 요소
    <link> : 외부 리소스 연결 요소 (CSS 파일, favicon 등)
    <script> : 스크립트 요소 (JavaScript 파일/코드)
    <style> : CSS 직접 작성
    ```

- HTML Global Attribute

  - 모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성 (몇몇 요소에는 아무 효과가 없을 수 있음)
  - id : 문서 전체에서 유일한 고유 식별자 지정
  - class : 공백으로 구분된 해당 요소의 클래스의 목록 (CSS, JS에서 요소를 선택하거나 접근)
  - data-* : 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용
  - style : inline 스타일
  - title : 요소에 대한 추가 정보 지정
  - tabindex : 요소의 탭 순서



## 텍스트 요소

- ```html
  <a href = 'https://www.naver.com'>네이버</a>
  ```

  - href 속성을 활용하여 다른 URL로 연결하는 하이퍼링크 생성

- ```html
  <b>네이버</b>
  <strong>네이버</strong>
  ```

  - 굵은 글씨 요소
  - 중요한 강조하고자 하는 요소(보통 굵은 글씨로 표현)

- ```html
  <i>네이버</i>
  <em>네이버</em>
  ```

  - 기울임 글씨 요소
  - 중요한 강조하고자 하는 요소(보통 기울림 글씨로 표현)

- ```html
  <br>
  ```

  - 텍스트 내에 줄 바꿈 생성

- ```html
  <img src='logo.png' alt='회사로고'>
  ```

  - src 속성을 활용하여 이미지 표현
  - alt 속성을 활용하여 대체 텍스트

- ```html
  <span>네이버</span>
  ```

  - 의미 없는 인라인 컨테이너

- ```html
  <h1>네이버</h1>
  <h2>네이버</h2>
  ```

  - Heading의 약자로 제목이나 부제목 표현

- ```html
  <p>네이버 지식인</p>
  ```

  - 하나의 문단(Paragraph)

- ```html
  <hr>
  ```

  - 문단 레벨 요소에서의 주제의 분리를 의미하며 수평선으로 표현됨

- ```html
  <ol>
    	<li>메뉴1</li>
    	<li>메뉴2</li>
    	<li>메뉴3</li>
  </ol>
  <--!>
    1. 메뉴1
    2. 메뉴2
    3. 메뉴3 
  </--!>
  
  <ul>
    	<li>메뉴1</li>
    	<li>메뉴2</li>
    	<li>메뉴3</li>
  </ul>
  <--!>
  	- 메뉴1
    - 메뉴2
    - 메뉴3
  </--!>
  ```

  - ol(Ordered list) 순서가 있는 리스트 
  - ul(Unordered list) 순서가 없는 리스트 

- ```html
  <pre>그대로 표현</pre>
  ```

  - HTML에 작성한 내용을 그대로 표현.

    보통 고정폭 글꼴이 사용되고 공백문자를 유지

- ```html
  <blockquote>
    내용
  </blockquote>
  ```

  - 안쪽의 텍스트가 긴 인용문임을 나타냄. 

    주로 들여쓰기를 한 것으로 그려짐.

- ```html
  <div>
    임의의 공간을 생성
  </div>
  ```

  - 임의의 공간을 만들 때 사용



## HTML 태그 두 가지 성격

- Block 요소와 Inline 요소

  ```html
  <!-- Block 요소 -->
  <p>멀티 캠퍼스</p>
  <p>멀티 캠퍼스</p>
  <p>멀티 캠퍼스</p>
  
  출력 값
  멀티캠퍼스
  멀티캠퍼스
  멀티캠퍼스
  
  <!-- Inline 요소 -->
  <a>멀티 캠퍼스</a>
  <a>멀티 캠퍼스</a>
  <a>멀티 캠퍼스</a>
  
  출력 값
  멀티캠퍼스 멀티캠퍼스 멀티캠퍼스
  ```

  - Block 요소는 y축 정렬 형태로 출력

    공간을 만들 수 있고, 상하 배치 작업 가능

  - Inline 요소는 x축 정렬 형태로 출력

    공간을 만들 수 없고, 상하 배치 작업 불가능



## CSS

- CSS(Cascading Style Sheet)
- HTML로 작성된 정보를 꾸며주는 언어
- 문서의 레이아웃과 스타일 정의

```html
선택자 {속성 : 속성 값;}
```

- 선택자 : 디자인을 적용할 HTML 영역
- 속성 : 어떤 디자인을 적용할지 정의
- 속성 값 : 어떤 역할을 수행할지 구체적으로 명령, 세미콜론(;) 필수 입력



#### CSS 정의 방법

- 인라인(inline)

  - ```html
    <h1 style='color: blue; font-size: 100px;'>
      Hello
    </h1>
    ```

    해당 태그에 직접 style 속성을 활용

- 내부 참조(embedding) - style

  - ```html
    <style>
      h1 {
        color: blue;
        font-size: 100px;
      }
    </style>
    ```

    head 태그 내에 style에 지정

- 외부참조(link file) - 분리된 CSS 파일

  - ```html
    <head>
      	<link rel='stylesheet' href='sryle.css'
    </head>
    ```

    외부 CSS 파일을 head 내 link 를 통해 불러오기



#### CSS 기초 선택자

- 요소 선택자
  - HTML 태그를 직접 선택
- 클래스(class) 선택자
  - 마침표(.)문자로 시작하며, 해당 클래스가 적용된 항목을 선택
- 아이디(id) 선택자
  - #문자로 시작하며, 해당 아이디가 적용된 항목을 선택
  - 일반적으로 하나의 문서에 1번만 사용
  - 여러 번 사용해도 동작하지만, 단일 id를 사용하는 것을 권장

- Type Selector

  ```html
  <style>
  	h3 {color: blue;}
  </style>
  ```

  특정 태그에 스타일을 적용

- Class Selector

  ```html
  <style>
    .class {color: skyblue;}
  </style>
  ```

  클래스 이름으로 특정 위치에 스타일을 적용

- ID Selector

  ```html
  <style>
    #id {color: green;}
  </style>
  ```

  ID를 이용하여 스타일을 적용



## 캐스케이딩



#### CSS의 우선순위를 결정하는 세 가지 요소

1. 순서
2. 디테일
3. 선택자

- 순서에 의한 캐스케이딩

  ```html
  <p>Hello World</p>
  
  <style>
    p {color: red;}
    p {color: blue;}
  </style>
  ```

  나중에 적용한 속성값의 우선순위가 높음

  

- 디테일에 의한 캐스케이딩

  ```html
  <header>
  		<p>Hello World</p>
  </header>
  
  <style>
    header p{color: red;}
    p {color: blue;}
  </style>
  ```

  더 구체적으로 작성된 선택자의 우선순위가 높음



- 선택자에 의한 캐스케이딩

  ```html
  <h3 style='color: pink' id='color' class='color'>
    color
  </h3>
  
  #color {color: blue;}
  .color {color: red;}
  h3 {color: green;}
  ```

  style > id > class > type 순으로 우선순위가 높음

