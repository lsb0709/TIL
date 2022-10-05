# Django 반복실습(mac)

#### 1. 가상환경

- 설치

  ```python
  python3 -m venv 가상환경폴더명
  python3 -m venv venv
  ```

- 가상환경 실행

  ```python
  source venv/bin/activate
  ```

- 패키지 설치

  ```python
  pip install django==3.2.13
  ```

- 패키지 공유를 위한 requirements.txt 설치

  ```python
  pip freeze > requirements.txt
  ```

- requirements.txt 파일에 담긴 패키지들을 설치

  ```python
  pip instsall -r requirements.txt
  ```

#### 2. 프로젝트

- 프로젝트 생성

  ```python
  django-admin startproject 프로젝트명 .
  (.은 현재폴더에 생성해달라는 의미)
  django-admin startproject PJT .
  ```

- 잘 설치 됐는 지 확인(서버실행)

  ```python
  python3 manage.py runserver
  ```

- 인터넷 창을 키고 http://localhost:8000/ 치면 장고 화면 등장

#### 3. 앱 생성

- 앱 생성

  ```python
  python3 manage.py startapp 앱이름
  python3 manage.py startapp articles
  ```

- 앱 등록

  ```python
  PJT > settings.py > INSTALLED_APPS = ["articles",] 추가
  ```

#### 4. PJT > urls.py

- include == url 설정을 app단위로 하기 위해서

  ```python
  from django.urls import path, include
  
  urlpatterns = [
      path("admin/", admin.site.urls),
      path("articles/", include("articles.urls")),
  ]

### 기본 흐름

#### Url 등록(Urls.py) -> 함수생성(Views.py) -> Template 생성(Template 만들기)



#### 5. articles > urls.py 생성

```python
urls.py
from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),   
]
```



### 6. articles > views.py

- 함수 정의

```python
from django.shortcuts import render

def index(request):
    return render(request, "articles/index")
```



### 7. Template 생성

- Template 생성경로

  ```python
  articles > Templates 폴더 생성 > articles 폴더 생성 > Index.html 파일 생성
  ```

- Template 생성까지 끝나면 서버를 실행시켜서 잘 나오는지 확인

  ```python
  python3 manage.py runserver
  ```



### 8. Model 정의(DB 스키마 설계)

- 클래스 정의(articles > models.py)

  ```python
  from django.db import models
  
  class Article(models.Model):
      title = models.CharField(max_length=20)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  ```

- 마이그레이션 파일 생성

  ```python
  python3 manage.py makemigrations
  ```

- DB 반영

  ```python
  python3 manage.py migrate
  ```

- DB 반영 확인

  ```python
  python3 manage.py showmigrations
  ```



### 9. CRUD 기능 구현

#### 1) 1-1. 게시글 생성

- urls

  ```python
  path("new/", views.new, name="new"),
  ```

- views

  ```python
  def new(request):
      return render(request, "articles/new.html")
  ```

- new.html 파일생성(templates > articles > 생성)

  ```html
  <form action="">
      <label for="title">제목 : </label>
      <input type="text" name="title">
      <label for="content">내용 : </label>
      <textarea name="content" id="content" cols="30" rows="10"></textarea>
      <input type="submit" value="글 쓰기">
  </form>
  ```

#### 1-2. 사용자로부터 입력받은 데이터 처리

- new.html

  ```html
  <form action="{% url 'articles:create' %}">
  ```

- urls

  ```python
  path('create/', views.create, name='create'),
  ```

- views

  ```python
  from django.shortcuts import render, redirect
  from .models import Article
  
  # DB저장
  def create(request):
      title = request.GET.get("title")
      content = request.GET.get("content")
      Article.objects.create(title=title, content=content)
      return redirect("articles:index")
  ```

  게시글 DB 생성, INDEX 페이지로 redirect

- index.html 작성버튼 생성(작성버튼을 누르면 new.html로 이동)

  ```html
  <a href="{% url 'articles:new' %}">글 쓰기</a>
  ```



#### 2) 2-1 게시글 목록

- views

  ```python
  def index(request):
      # 게시글을 작성이 나중에 된 순서대로 가져와서
      articles = Article.objects.order_by('-pk')
      # Template에 전달
      context = {
          "articles": articles,
      }
      return render(request, "articles/index.html", context)
  ```

- index.html

  ```python
  <h1>게시판</h1>
  <a href="{% url 'articles:new' %}">글쓰기</a>
  {% for article in articles %}
  <h3>{{ article.title }}</h3>
  <p>{{ article.created_at }} | {{ article.updated_at }}</p>
  <hr>
  {% endfor %}
  ```

  - for문을 이용해 코드를 반복

#### 2-2 POST 형식으로 전환

- new.html

  ```python
  <h1>글 쓰기</h1>
  <form action="{% url 'articles:create' %}" method="POST">
      {% csrf_token %}
      <label for="title">제목 : </label>
      <input type="text" name="title">
      <label for="content">내용 : </label>
      <textarea name="content" id="content" cols="30" rows="10"></textarea>
      <input type="submit" value="글 쓰기">
  </form>
  ```

  - method="POST" 추가
  - {% csrf_token %} 추가

- views(GET -> POST 변경)

  ```python
  # DB저장
  def create(request):
      title = request.POST.get("title")
      content = request.POST.get("content")
      Article.objects.create(title=title, content=content)
      return redirect("articles:index")
  ```

  - POST : 저장하고 기록하는 행위(로그인)
  - GET : 조회 하는 행위(검색하는 창)

- new.html input 태그에 required 추가

  ```html
  <h1>글 쓰기</h1>
  <form action="{% url 'articles:create' %}" method="POST">
      {% csrf_token %}
      <label for="title">제목 : </label>
      <input type="text" name="title" required>
      <label for="content">내용 : </label>
      <textarea name="content" id="content" cols="30" rows="10"></textarea>
      <input type="submit" value="글 쓰기" required>
  </form>
  ```

- HTTP POST
  - 게시글을 생성 할 때(CREATE 구현) GET을 쓰면 보안상의 문제와 유효성 검사의 문제가 생김
  - 지금 만들어진 form이 회원가입을 목적으로 클라이언트가 데이터를 submit 할 때 주소창(url)이나 log에 비밀번호 등 민감한 개인정보 노출
  - 따라서 form은 `POST`를 이용해서 작성해야 함

#### 2-3 django forms.py 이용하기

- DB 기반의 어플리케이션을 개발하다보면, HTML Form(UI)은 Django의 모델(DB)과 매우 밀접한 관계를 갖게됨
  - 사용자로부터 값을 받아 DB에 저장하여 활용하기 때문
  - 즉, 모델에 정의한 필드의 구성 및 종류에 따라 HTML Form이 결정

- Article 모델에 있는 fields를 사용하겠다는 의미
- 모델 form에 인스턴스를 넘겨준다.

- articles > forms.py 생성

  ```python
  from django import forms
  from .models import Article
  
  class ArticleForm(forms.ModelForm):
      class Meta:
          model = Article
          # all은 전부 ["title", "context"] 처럼 각 각을 불러 올 수도 있다.
          fields = "__all__"
          
  ```

- new.html, views.py 에 적용

  ```python
  <h1>글 쓰기</h1>
  <form action="{% url 'articles:create' %}" method="POST">
      {% csrf_token %}
      {{ article_form.as_p }}
      <label for="title">제목 : </label>
      <input type="text" name="title" required>
      <label for="content">내용 : </label>
      <textarea name="content" id="content" cols="30" rows="10"></textarea>
      <input type="submit" value="글 쓰기" required>
  </form>
  ```

  - {{ article_form.as_p }}
  - as.p -> p태그로 감싸라는 의미

  ```python
  from .froms import ArticleForm
  
  def new(request):
      article_form = ArticleForm()
      context = {
          "article_form": article_form,
      }
      return render(request, "articles/new.html", context)
  ```

  

#### 2-4 유효성 검사

- 유효성 검사가 없는 코드

  ```python
  def create(request):
      title = request.POST.get("title")
      content = request.POST.get("content")
      Article.objects.create(title=title, content=content)
      return redirect("articles:index")
  ```

- 유효성 검사가 포함된 코드

  ```python
  def create(request):
      # ArticleForm에 request.POST로 값을 그대로 넘겨받는다.
      article_form = ArticleForm(request.POST)
      # 만약 article_form가 valid한가?
      if article_form.is_valid():
          # valid하면 save
          article_form.save()
          return redirect("articles:index")
      # 그렇지 않다면 new.html로 넘겨라
      else:
          context = {
              "article_form": article_form,
          }
          return render(request, "articles/new.html", context=context)
  ```

#### 2-5 코드 병합

- view

  ```python
  # new 함수를 주석처리
  # def new(request):
  #     article_form = ArticleForm()
  #     context = {
  #         "article_form": article_form,
  #     }
  #     return render(request, "articles/new.html", context)
  
  # create함수와 병합
  def create(request):
      if request.method == 'POST':
          # DB에 저장하는 로직
          article_form = ArticleForm(request.POST)
          if article_form.is_valid():
              article_form.save()
              return redirect('articles:index')
      else: # request.method == 'GET':
          # 일반적인 사이트들은 유효하지 않을 때
          # 이슈가 발생한 페이지를 보여주고 정정하라고 하는데,
          # ModelForm 활용해서 new.html 로 넘겨주라고 else 문 작성하면
          # 우리가 원했던 기능이 구현됨
          article_form = ArticleForm()
      context = {
          'article_form': article_form
      }
      return render(request, 'articles/new.html', context=context)
  ```

- urls

  ```python
  # new url 주석처리
  # path("new/", views.new, name="new"),
  ```

#### 3) 3-1 상세보기

- 수정하기(UPDATE) 기능을 구현하기 위해, 상세보기 페이지를 먼저 작성(특정한 글을 본다 == id값이 필요하다)

- urls

  ```python
  path("<int:pk>/", views.detail, name="detail"),
  ```

- views

  ```python
  def detail(request, pk):
      # 특정 글을 가져온다.
      article = Article.objects.get(pk=pk)
      # template에 객체 전달
      context = {
          "article": article,
      }
      return render(request, "articels/detail.html", context)
  ```

- detail.html 생성

  ```python
  <h1>{{ article.pk }}번 게시글</h1>
  <h2>{{ article.created_at }} | {{ article.updated_at }}</h2>
  <p>{{ article.content }}</p>
  ```

- 상세페이지 이동 url생성(index.html)

  - 제목을 누르면 이동

  ```python
  <body>
      <h1>게시판</h1>
      <a href="{% url 'articles:create' %}">글 쓰기</a>
      {% for article in articles %}
      <h3><a href="{% url 'article:detail' article.pk %}"></a>{{ article.title }}</h3>
      <p>{{ article.created_at }} | {{ article.updated_at }}</p>
      <hr>
      {% endfor %}
  </body>
  ```



#### 4) 4-1 수정하기

- url

  ```python
  path("<int:pk>/", views.update, name="update"),
  ```

- detail.html(수정하기 버튼 생성)

  ```pyhon
  <a href="{% url 'articles:update' article.pk %}">수정하기</a>
  ```

- views

  ```python
  def update(request, pk):
      # GET 처리 : Form을 제공
      article_form = ArticleForm()
      context = {
          "article_form": article_form,
      }
      return render(request, "articles/update.html", context)
  ```

  

- update.html 생성

  ```python
  <h1>글 수정하기</h1>
  
  <form action="" method="POST">
      {{ article_form.as_p }}
      <input type="submit" value="수정">
  </form>
  ```

#### 글을 수정하기 위해 원래 있던 글이 남아있게 하려면?

- views

  ```python
  def update(request, pk):
      # GET 처리 : Form을 제공
      article = Article.objects.get(pk=pk)
      # 기존 instance 가진 상태의 ArticleForm()
      article_form = ArticleForm(instance=article)
      context = {
          "article_form": article_form,
      }
      return render(request, "articles/update.html", context)
  ```

- update.html

  ```python
  <h1>글 수정하기</h1>
  
  <form action="" method="POST">
      {% csrf_token %}
      {{ article_form.as_p }}
      <input type="submit" value="수정">
  </form>
  ```

- views 유효성 검사완료 코드

  ```python
  def update(request, pk):
      # GET 처리 : Form을 제공
      article = Article.objects.get(pk=pk)
      if request.method == "POST":
          # POST : input 가져와서 검증하고 DB에 저장
          article_form = ArticleForm(request.POST, instance=article)
          if article_form.is_valid():
              # 유효성 검사 통과하면 저장후 상세보기 페이지로
              article_form.save()
              return redirect("articles:detail", article.pk)
          # 유효성 검사 통과 못하면 => 오류페이지
      else:
          # GET 처리 : Form을 제공
          article_form = ArticleForm(instance=article)
      context = {
          "article_form": article_form,
      }
      return render(request, "articles/update.html", context)
  ```

  





