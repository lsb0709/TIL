# Django CRUD



## 1. 가상환경 및 Django 설치(mac)

### 1. 가상환경 생성 및 실행

* 가상환경 폴더를  `.gitignore` 로 설정을 해둔다.

* 가상환경 생성 및 실행

  ``` python
  python3 -m venv venv
  source venv/bin/activate
  ```



## 2. Django 설치 및 기록

- pip install을 통해 장고 설치 및 기록

  ```python
  pip install django==3.2.13
  pip freeze > requirements.txt
  ```

- pip list을 통해 설치 확인



## 3. Django 프로젝트 생성

- 프로젝트 생성

  ```python
  django-admin startproject pjt .
  ```

- 생성이 잘 되었는지 확인

  ```python
  python3 manage.py runserver
  ```

  

## 4. Django 앱 생성 및 등록

- 앱 생성

  ```python
  python3 manage.py startapp 앱이름
  python3 manage.py startapp articles
  ```

- 앱 등록

  ```python
  pjt -> sttings.py 이동
  INSTALLED_APPS = [
    "articles",
  ]
  
  pjt -> urls.py 이동
  from django.urls import path, include 추가
  
  urlpatterns = [
      path("admin/", admin.site.urls),
      path("articles/", include("articles.urls")),
  ]
  ```

  

## 5. Django urls.py 설정 및 Index 생성

- url 설정 및 Index 생성

  1. url 등록

  ```python
  앱 폴더(articles) 안에 urls.py 생성
  urls.py 이동
  
  from django.urls import path
  from . import views
  
  app_name = 'articles'
  
  urlpatterns = [
      path('', views.index, name='index'),
  ]
  ```

  2. view 함수 생성

  ```python
  views.py 이동 후 함수 생성
  def index(request):
    return render(request, 'articles/index.html')
  ```

  3. template 생성

  ```python
  앱 폴더(articles) 안에 templates폴더 생성
  templates폴더 안에 articles폴더 생성
  articles폴더 안에 index.html 파일 생성
  ```

- template 생성 후 잘 실행 되는지 확인

  ```python
  python3 manage.py runserver
  ```



## 6. Model 정의 (DB 설계)

1. 클래스 정의

   ```python
   models.py 이동
   
   게시판 기능
   제목(20글자이내)
   내용(긴 글)
   글 작성시간, 수정시간(자동으로 기록, 날짜/시간)
   
   class Article(models.Model):
       title = models.CharField(max_length=20)
       content = models.TextField()
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)
   ```

   

2. 마이그레이션 파일 생성

   ```python
   python3 manage.py makemigrations
   ```

   

3. DB 반영(`migrate`)

   ```python
   python3 manage.py migrate
   ```

4. DB 생성완료 확인방법

   ```python
   db.sqlite3 우클릭 Open Database 클릭
   좌측하단 타임라인 아래 SQLITE EXPLORER로 확인 가능
   ```



## 7. CRUD 기능 구현

#### 1. 게시글 생성

- 사용자에게 HTML Form 제공, 입력받은 데이터를 처리

  ```html
  articles/templates/articles/index.html 이동
  글쓰기 버튼 생성
  <body>
    <h1>게시판</h1>
    <!-- <a href="{% url 'articles:new' %}">글 쓰기</a> -->
    <a href="{% url 'articles:create' %}">글 쓰기</a>
    {% for article in articles %}
    <h3><a href="{% url 'articles:detail' article.pk %}">{{ article.title }}</a></h3>
    <p>{{ article.created_at}} | {{ article.updated_at }}</p>
    <hr>
    {% endfor %}
  </body>
  ```

#### 2. HTML Form 제공

- 주소

  ```html
  articles/templates/articles/new.html 생성
  
  <!-- form 태그로 사용자에게 양식을 제공하고 값을 받아서(input : name, value) 
  서버에 전송(form : action) -->
  
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {{ article_form.as_p }}
  	<!-- <label for="title">제목 :</label>
    <input type="text" name="title" id="title">
    <label for="content">내용 : </label>
    <textarea name="content" id="content" cols="30" rows="10" required></textarea> -->
    <input type="submit" value="글쓰기">
  </form>
  ```



#### 3. 입력받은 데이터 처리

- 주소

- 게시글 DB에 생성하고 index 페이지로 redirect

  ```python
  articles/urls.py 이동
  
  # path('new/', views.new, name='new'),
  
  path('create/', views.create, name='create'),
  
  path('<int:pk>/', views.detail, name='detail'),
  ```

  ```python
  articles/views.py 이동
  
  from django.shortcuts import render, redirect
  from .models import Article
  from .forms import ArticleForm
  
  def index(request):
    # 게시글을 가져와서
    articles = Article.objects.order_by('-pk')
    # Template에 전달한다.
    context = {
      'articles': articles,
    }
    return render(request, 'articles/index.html', context)
  
  # def new(request):
    # article_form = ArticleForm()
    # context = {
      # 'article_form': article_form,
    # }
    # return render(request, 'articles/new.html', context=context)
  
  def create(request):
    # DB에 저장하는 로직
    #title = request.POST.get('title')
    #content = request.POST.get('content')
    #Article.objects.create(title=title, content=content)
    #return redirect('articles:index')
    
    if request.method == 'POST':
      #DB에 저장하는 로직
      article_form = ArticleForm(request.POST)
      if article_form.is_valid():
        article_form.save()
        return redirect('articles:index')
    else:
      	article_form = ArticleForm()
    context = {
      'article_form': article_form
    }
    return render(request, 'articles/new.html', context=context)
  
  def detail(request, pk):
    # 특정 글을 가져온다.
    article = Article.objects.get(pk=pk)
    # template에 객체 전달
    context = {
      'article': article,
    }
    return render(request, 'articles/detail.html', context)
  ```

- 모델 forms 불러오기

  ```python
  articles/forms.py 생성
  
  from django import forms
  from .models import Article
  
  class ArticleForm(forms.ModelForm):
    	
      class Meta:
        	model = Article
          fields = ['title', 'content']
  ```

- 상세보기

  ```html
  articles/templates/articles/detail.html 생성
  
  <h1>{{ article.pk }}번 게시글</h1>
  <p>{{ article.created_at }} | {{ article.updated_at }}</p>
  <p>{{ article.content }}</p>
  ```

#### 4. 수정하기

- 특정한 글을 수정한다. -> 사용자에게 수정할 수 있는 양식을 제공하고(GET) 특정한 글을 수정한다.(POST)

  ```html
  articles/templates/articles/detail.html 생성
  
  <h1>{{ article.pk }}번 게시글</h1>
  <p>{{ article.created_at }} | {{ article.updated_at }}</p>
  <p>{{ article.content }}</p>
  <a href="{% url 'articles:update' article.pk %}">수정하기</a>
  ```

  ```html
  articles/templates/articles/update.html 생성
  
  <h1>글 수정하기</h1>
  
  <form action="" method="POST">
    {% csrf_token %}
    {{ article_form.as_p }}
    <input type='submit' value='수정'>
  </form>
  ```

  ```python
  articles/urls.py 이동
  
  path('<int:pk>/update/', views.update, name='update'),
  ```

  - Update(GET)

  ```python
  articles/views.py
  
  def update(request, pk):
    # GET : Form을 제공
    article = Article.objects.get(pk=pk)
    article_form = ArticleForm(instance=article)
    context = {
      'article_form': article_form
    }
    return render(request, 'articles/update.html', context)
  ```

  - Update(POST)

  ```python
  def update(request, pk):
    # GET : Form을 제공
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
      # POST : input 값 가져와서, 검증하고, DB에 저장
      article_form = ArticleForm(request.POST, instance=article)
      if article_form.is_valid():
        # 유효성 검사 통과하면 저장하고, 상세보기 페이지로
        article_form.save()
        return redirect('articles:detail', article.pk)
      # 유효성 검사 통과하지 않으면 => context 부터해서 오류메세지 담긴 article_form을 랜더링
    else:
      	# GET : Form을 제공
        article_form = ArticleForm(instance=article)
    context = {
      'article_form': article_form
    }
    return render(request, "articles/update.html", context)
  ```

  

