# 서버 기초



### Q. IP와 도메인은 무엇일까요?

- IP 주소 (Internet Protocol Address)
  - 인터넷에서 다른 컴퓨터와 서로 인식하고 통신하기 위해 사용되는 특수한 번호
- 도메인(Domain)
  - 숫자로 표현된 IP 주소를 알기 쉽게 영문으로 표기한 것으로, 일반적으로 `컴퓨터이름.기관이름.기관종류.국가이름` 으로 구성
    현재 도메인 네임은 ICANN에서 관리
- DNS(Domain Name System)
  - IP주소를 Domain명으로 바꿔주는 것



### Q. 클라이언트와 서버는 무엇일까요?

- 웹에 연결된 컴퓨터는 **클라이언트** 와 **서버**
- 클라이언트는 일반적인 웹 사용자의 인터넷이 연결된 장치들 (예를 들어, 여러분의 컴퓨터는 WI-FI에 연결되어 있고, 또는 여러분의 폰은 모바일 네트워크에 연결되어 있습니다) 과 이런 장치들에서 이용가능한 웹에 접근하는 소프트웨어 (일반적으로 파이어폭스 또는 크롬 과 같은 웹 브라우저) 입니다.
- 클라이언트는 주로 서버에 요청을 보내고 응답을 받는 역을 합니다.
- 서버는 웹페이지, 사이트, 또는 앱을 저장하는 컴퓨터입니다. 클라이언트의 장비가 웹페이지에 접근하길 원할 때, 서버로부터 클라이언트의 장치로 사용자의 웹 브라우저에서 보여지기 위한 웹페이지의 사본이 다운로드 됩니다.

<img src="/Users/isangbaeg/Desktop/TIL/Django/images/django1_01.png" alt="django1_01" style="zoom:50%;" />

- **인터넷 연결**: 여러분이 웹에서 데이터를 보내고 받을 수 있게 해줍니다. 기본적으로 여러분의 집과 상점 사이의 거리와 같습니다.

- **TCP/IP**: Transmission Control Protocol (전송 제어 규약) 과 Internet Protocol (인터넷 규약) 은 데이터가 어떻게 웹을 건너 여행해야 하는지 정의하는 통신 규약입니다. 이것은 주문을 하고, 상점에 가고, 또 여러분의 상품을 살 수 있게 해주는 운송 장치와 같습니다. 우리 예시에서, 이것은 차 또는 자전거 (또는 여러분의 두 다리) 와 같습니다.

- **DNS**: Domain Name System Servers (도메인 이름 시스템 서버) 는 웹사이트를 위한 주소록과 같습니다. 여러분이 브라우저에 웹 주소를 입력할 때, 브라우저는 그 웹사이트를 검색하기 전에 DNS 를 살펴봅니다. 브라우저는 HTTP 메시지를 올바른 장소로 전송하기 위해 그 웹사이트가 있는 서버가 어떤것인지 찾아야 합니다 (아래를 보세요). 이것은 여러분이 접근하기 위해 상점의 주소를 찾아보는 것과 같습니다.

- **HTTP**: Hypertext Transfer Protocol (하이퍼텍스트 전송 규약) 은 클라이언트와 서버가 서로 통신할 수 있게 하기 위한 언어를 정의하는 어플리케이션 규약 입니다. 이것은 여러분의 상품을 주문하기 위해 여러분이 사용하는 언어와 같습니다.

- 컴포넌트 파일

  : 한 웹사이트는 여러분이 상점에서 사는 다양한 종류의 상품들과 같이 많은 다른 파일들로 만들어집니다. 이 파일들은 두개의 주요한 타입이 있습니다:

  - **코드 파일**: 다른 기술들도 잠시 뒤 보게 되실것이지만, 웹사이트는 근본적으로 HTML, CSS, 그리고 JavaScript 로 생성됩니다.
  - **자원**: 이것은 이미지, 음악, 비디오, 단어 문서, 그리고 PDF 같은, 웹사이트를 만드는 모든 다른 것들을 위한 공동적인 이름입니다.



### Q. 웹 서버란 무엇인가요?

- "Web server"는 하드웨어, 소프트웨어 혹은 두 개가 같이 동작하는 것을 의미
  1. 하드웨어 측면에서, web server는 web server의 소프트웨어와 website의 컴포넌트 파일들을 저장하는 컴퓨터입니다. (컴포넌트 파일에는 HTML 문서, images, CSS stylesheets, 그리고 JavaScript files가 있습니다.) Web server는 인터넷에 연결되어 웹에 연결된 다른 기기들이 웹 서버의 데이터(컴포넌트 파일들)를 주고받을 수 있도록 합니다.
  2. 소프트웨어 측면에서, web server는 기본적으로 웹 사용자가 어떻게 호스트 파일들에 접근하는지를 관리합니다. 이 문서에서 web server는 HTTP서버로 국한합니다. HTTP 서버는 URL(Web addresses)과 HTTP(당신의 브라우저가 웹 페이지를 보여주기 위해 사용하는 프로토콜)의 소프트웨어 일부입니다.



### Q. 정적 웹 사이트와 동적 웹 사이트의 차이점은 무엇일까요?

##### 정적 웹 페이지(Static Web Page)

- 서버(Web Server)에 **미리 저장된 파일**(HTML, 이미지, JavaScript 파일 등)이 그대로 전달되는 웹 페이지
- 서버는 사용자가 요청(Request)에 해당하는 저장된 웹 페이지를 보냄
- 사용자는 서버에 저장된 데이터가 변경되지 않는 한 고정된 웹 페이지를 보게 됨

<img src="/Users/isangbaeg/Desktop/TIL/Django/images/django1_02.png" alt="django1_02" style="zoom:50%;" />

#### 동적 웹 페이지(Dynamic Web Page)

- 서버(Web Server)에 있는 데이터들을 스크립트에 의해 **가공처리한 후 생성**되어 전달되는 웹 페이지
- 서버는 사용자의 요청(Request)을 해석하여 데이터를 가공한 후 생성되는 웹 페이지를 보냄
- 사용자는 상황, 시간, 요청 등에 따라 달라지는 웹 페이지를 보게 됨

<img src="/Users/isangbaeg/Desktop/TIL/Django/images/django1_03.png" alt="django1_03" style="zoom:50%;" />



#### 정적 웹 페이지 VS 동적 웹 페이지

<img src="/Users/isangbaeg/Desktop/TIL/Django/images/django1_04.png" alt="django1_04" style="zoom:50%;" />

- 정적 웹 페이지 장점
  - 빠르다 : 요청에 대한 파일만 전송하면 되기 때문에 추가적인 작업이 없음
  - 비용이 적다 : 웹 서버만 구축하면 됨
- 정적 웹 페이지 단점
  - 서비스가 한정적이다 : 저장된 정보만 보여줄 수 있음
  - 관리가 힘들다 : 추가/수정/삭제의 작업 모두 수동
- 동적 웹 페이지 장점
  - 서비스가 다양하다 : 다양한 정보를 조합하여 동적으로 생성하여 제공 가능
  - 관리가 쉽다 : 웹 사이트 구조에 따라서 추가/수정/삭제 등의 작업이 용이
- 동적 웹 페이지 단점
  - 상대적으로 느리다 : 사용자에게 웹 페이지를 전달하기 전에 처리하는 작업이 필요
  - 추가 비용이 든다 : 웹 서버외에 추가적으로 처리를 위한 어플리케이션 서버가 필요



### Django는 무엇을 위한 도구인가요?

- 소프트웨어 개발에 도움을 주는 웹 프레임워크

- 보안이 우수하고 유지보수가 편리한 웹사이트를 신속하게 개발하는 하도록 도움을 주는 파이썬 웹 프레임워크

- **URLs:** 단일 함수를 통해 모든 URL 요청을 처리하는 것이 가능하지만, 분리된 뷰 함수를 작성하는 것이 각각의 리소스를 유지보수하기 훨씬 쉽습니다. URL mapper는 요청 URL을 기준으로 HTTP 요청을 적절한 뷰(view)로 보내주기 위해 사용됩니다. 또한 URL mapper는 URL에 나타나는 특정한 문자열이나 숫자의 패턴을 일치시켜 데이터로서 뷰 함수에 전달할 수 있습니다.
- **View:** 뷰는 HTTP 요청을 수신하고 HTTP 응답을 반환하는 요청 처리 함수입니다. 뷰는 Model을 통해 요청을 충족시키는데 필요한 데이터에 접근합니다. 그리고 탬플릿에게 응답의 서식 설정을 맡깁니다.
- **Models:** 모델은 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리(추가, 수정, 삭제)하고 쿼리하는 방법을 제공하는 파이썬 객체입니다.
- **Templates:** 탬플릿은 파일의 구조나 레이아웃을 정의하고(예: HTML 페이지), 실제 내용을 보여주는 데 사용되는 플레이스홀더를 가진 텍스트 파일입니다. 뷰는 HTML 탬플릿을 이용하여 동적으로 HTML 페이지를 만들고 모델에서 가져온 데이터로 채웁니다. 탬플릿으로 모든 파일의 구조를 정의할 수 있습니다.탬플릿이 꼭 HTML 타입일 필요는 없습니다!

- [요청을 알맞은 뷰로 전달 (urls.py)](https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Introduction#요청을_알맞은_뷰로_전달_urls.py)

- [요청 처리하기 (views.py)](https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Introduction#요청_처리하기_views.py)

- [데이터 모델 정의하기 (models.py)](https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Introduction#데이터_모델_정의하기_models.py)

- [데이터 쿼리하기 (views.py)](https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Introduction#데이터_쿼리하기_views.py)

- [데이터 렌더링 (HTML 템플릿)](https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Introduction#데이터_렌더링_html_템플릿)



### Q. HTTP는 무엇이고 요청과 응답 메시지 구성은 어떻게 되나요?

- HyperText Transfer Protocol(문서를 전송하기 위한 약속) 
- **HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는** **프로토콜**입니다.
- 웹에서 이루어지는 모든 데이터 교환의 기초이며, 클라이언트-서버 프로토콜
- 클라이언트-서버 프로토콜이란 (보통 웹브라우저인) 수신자 측에 의해 요청이 초기화되는 프로토콜을 의미
- 하나의 완전한 문서는 텍스트, 레이아웃 설명, 이미지, 비디오, 스크립트 등 불러온(fetched) 하위 문서들로 재구성



#### 요청(Request)와 응답(Response)로 구성

<img src="/Users/isangbaeg/Desktop/TIL/Django/images/django1_05.png" alt="django1_05" style="zoom:50%;" />

```makefile
메세지 교환 형태의 프로토콜 
     - 클라이언트와 서버 간에 `HTTP 메세지`를 주고받으며 통신
        . SMTP 전자메일 프로토콜과 유사  ☞ 메일 메세지 포멧, MIME 참조
```



# HTTP 요청

요청은 **클라이언트가** 서버로 특정 데이터를 받아올 수 있게끔 **보내는 메세지**이다.

요청 메세지는 아래와 같이 구성되어 있다.
![img](https://velog.velcdn.com/images%2Fbining%2Fpost%2F9fecb873-dafa-4620-918c-9519d7dd83e6%2Fimage.png)

- 메서드 : 클라이언트가 서버에 요청할 동작
- 프로토콜 : 사용되는 프로토콜과 버전
- 헤더 : 클라이언트 자체에 대한 자세한 정보
- empty-line : 헤더와 본문을 구별함
- 본문 : 해당 요청 전송하는 메세지(데이터)
  보통 GET 메서드로 요청을 보내는 경우 body는 생략된다.



## HTTP 요청 메서드

### 1) GET

특정 리소스를 가져오도록 요청하는 메서드이다. GET 요청은 데이터를 가져올 때만 사용한다.
CRUD의 개념으로 생각하면 Read에 속한다.

URL 뒤에 데이터를 붙여 보낸다.

> www.example.com/upper

### 2) POST

서버로 리소스를 제출하는 메서드로 서버 상태의 변화를 일으킨다. 주로 새로운 리소스 생성(create) 할 때 사용된다.

URL에 붙여 쓰는 방식이 아닌 BODY에다 리소스를 넣어서 보낸다.

### 3) PUT

POST와 비슷하지만 연속적인 요청시에도 같은 효과를 가져온다. 기존 데이터를 교체하는 용도로 쓰인다.(update)

### 3) PATCH

리소스의 부분적인 수정(update)을 할 때에 사용된다.

### 4) DELETE

지정한 리소스를 삭제(delete) 요청할 때 사용한다.

### 5) OPTIONS

CORS에서 OPTIONS 메소드로 사전 요청을 보내 서버가 해당 parameters를 포함한 요청을 보내도 되는지에 대한 응답을 줄 수 있게 한다.

### 멱등성(idempotent)

mdn에 따르면 동일한 요청을 한 번 보내는 것과 여러 번 연속으로 보내는 것이 같은 효과를 지니고, 서버의 상태도 동일한 것을 멱등성을 가진다고 말한다.

예를 들어, DELETE로 서버의 유저1 정보를 지우는 요청을 보낸다고 하면, 처음 요청을 보냈을 때 유저1 정보가 삭제된다. 서버에서는 이미 유저1의 정보가 삭제되었기 때문에 유저1 삭제 요청을 또 보낸다고 아무런 영향을 끼치지 않는다.

**GET, HEAD, PUT, DELETE 메서드**는 멱등성을 가지는 메서드이다. POST는 멱등성의 특징을 가지지 않는다.



# HTTP 응답

요청에 대한 서버의 답변이다.

![img](https://velog.velcdn.com/images%2Fbining%2Fpost%2F7dd8e1f8-163a-4437-916b-9879c79a2687%2Fimage.png)

- 프로토콜 : 사용되는 프로토콜과 버전
- 상태코드 : 요청에 대한 응답 상태
- 상태메세지 : 상태코드와 함께 전달되는 메세지



## 상태코드(state code)

http 응답 상태코드는 요청에 대한 응답이 성공적으로 되었는지 알려준다.

자주 쓰이는 200, 400, 500번대는 자주 봐서 익혀두면 코드짤 때 편하다.
![img](https://velog.velcdn.com/images%2Fbining%2Fpost%2F99364a1c-17be-4689-bc0a-abcf62f14ed3%2Fimage.png)

## Content-Type

응답 헤더 안에 있는 Content-Type은 클라이언트한테 전달되는 데이터 유형을 알려준다.
Content-Type은 MIME 타입으로 표기된다.

##### MIME(Multipurpose Internet Mail Extension) 타입이란?

클라이언트에게 전송된 문서의 다양성을 알려주기 위한 메커니즘입니다. 웹에서 파일의 확장자는 별 의미가 없습니다. 그러므로, 각 문서와 함께 올바른 MIME 타입을 전송하도록, 서버가 정확히 설정하는 것이 중요합니다. 브라우저들은 리소스를 내려받았을 때 해야 할 기본 동작이 무엇인지를 결정하기 위해 대게 MIME 타입을 사용합니다.

Content-Type에 쓰이는 대표적인 MIME 타입들

- text/plain
- text/html
- text/css
- text/javascript
- application/json
- application/xml
- image/gif(이 외 이미지 파일 형식)
- video/webm
- audio/midi

### 프레임워크(Framework)란?

프레임워크(Framework) 라는 단어는 Frame(틀) + work(일)이라는 단어의 합성어입니다. 일 구조, 혹은 작업 구조라는 뜻과 같이 프레임워크는 **어떠한 일을 처리하기 위한 구조**를 제공합니다.
프레임워크 위에서 개발을 하면 우리는 일을 하기위한 전체 구조와 동작방식을 만들지 않습니다. 프레임워크로 개발을 할 경우 **전체 동작방식은 프레임워크가 제공하고 우리는 프레임워크의 일정 부분만 개발**합니다.

예를 들어 **웹 프레임워크**의 경우 HTTP 요청이 오면

1. Path, Params, Header, Body로 파싱 및 디코딩을 수행하고

2. 보안/인증 설정에 따라 보안/인증 처리를 수행하고

3. 요청을 수행 할 Handler/Router로 요청을 보냅니다.

4. 그리고 Handler에서 응답메세지를 만들면 사전에 정의된 타입에 따라 HTTP응답 합니다.

5. 만약 Handler나 Router가 없거나 처리시 에러가 발생하면 에러 HTTP Status와 HTTP 메세지를 응답합니다.



### Django

![img](https://velog.velcdn.com/images%2Fcouchcoding%2Fpost%2Faeb50970-ae88-4c99-ad70-71fb41a7b1c3%2Fimage.png)
Django는 Python에서 가장 많이 사용하는 웹 프레임워크로 Spring MVC가 MVC패턴을 구현하였다면 DJango는 MTV(Model - Template - View)를 구현한 프레임워크입니다.
**개인적으로 프레임워크가 무엇인지 공부하기에 가장 좋은 프레임워크라고 생각합니다.** (모든 개발을 프레임워크 설정하듯이 개발합니다)

Django의 View로 URL요청이 들어오면 Model을 변경하고 Template에 주입하여 반환하던가, 그냥 API응답을 진행합니다.
실제 개발은 Model과 View, Template을 정의하면 개발이 되는 것을 볼 수 있습니다. App을 정의하여 설정을 추가하고 Admin을 정의하여 관리자 페이지를 정의할 수 있습니다.(템플릿과 동작이 기본 제공됩니다)
![img](https://velog.velcdn.com/images%2Fcouchcoding%2Fpost%2F3979fb5f-2ac9-43e4-a7b6-2f3af250e135%2Fimage.png)

Django 폴더 구조