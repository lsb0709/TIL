# QuerySet API



- gt

  ```python
  Entry.objects.filter(id__gt=4)
  ```

  sqlite에서의 표현

  ```sqlite
  SELCET * FROM Entry WHERE id > 4;
  ```

  - id 값 4 초과를 뜻함

- gte

  ```python
  Entry.objects.filter(id__gte=4)
  ```

  sqlite에서의 표현

  ```sqlite
  SELECT * FROM Entry WHERE id >= 4;
  ```

  - id 값 4 이상을 뜻함

- lt, lte

  ```python
  Entry.objects.filter(id__lt=4)
  Entry.objects.filter(id__lte=4)
  ```

  sqlite에서의 표현

  ```sqlite
  SELECT * FROM Entry WHERE id < 4;
  SELECT * FROM Entry WHERE id <= 4;
  ```

  - Id 값이 4 미만, 이하를 뜻함

- in

  ```python
  Entry.objects.filter(id__in=[1, 3, 4])
  Entry.objects.filter(headline__in='abc')
  ```

  sqlite에서의 표현

  ```sqlite
  SELECT * FROM Entry WHERE id IN (1, 3, 4);
  SELECT * FROM Entry WHERE headline IN ('a','b','c');
  ```

  - id(필드이름)에 포함
  - headline(필드이름)에 포함

- startswith

  ```python
  Entry.objects.filter(headline__startswith='Lennon')
  ```

  sqlite에서의 표현

  ```sqlite
  SELECT * FROM Entry WHERE headline LIKE 'Lennon%';
  ```

  - Lennon으로 시작하는 값

- istartswith

  ```python
  Entry.objects.filter(headline__istartswith='Lennon')
  ```

  sqlite에서의 표현

  ```sqlite
  SELECT * FROM Entry WHERE headline ILIKE 'Lennon%';
  ```

  - 대소문자구분없이 시작하는 값

- endswith

  ```python
  Entry.objects.filter(headline__endswith='Lennon')
  Entry.objects.filter(headline__iendswith='Lennon')
  ```

  sqlite에서의 표현

  ```sqlite
  SELECT * FROM Entry WHERE headline LIKE '%Lennon';
  SELECT * FROM Entry WHERE headline ILIKE '%Lennon';
  ```

  - Lennon으로 끝나는 값

- contains

  ```python
  Entry.objects.filter(headline__contains='Lennon')
  Entry.objects.filter(headline__icontains='Lennon')
  ```

  sqlite에서의 표현

  ```sqlite
  SELECT * FROM Entry WHERE headline LIKE '%Lennon%';
  SELECT * FROM Entry WHERE headline ILIKE '%Lennon%';
  ```

  - Lennon이 들어가는 값

- range

  ```python
  import datetime
  start_data = datetime.date(2005, 1, 1)
  end_date = datetime.date(2005, 3, 31)
  Entry.objects.filter(pub_date__reage=(start_date, end_date))
  ```

  sqlite에서의 표현

  ```sqlite
  SELECT * FROM Entry WHERE pub_date
  BETWEEN '2005-01-01' and '2005-03-31';
  ```

  - 날짜 데이터를 표현

- 복합 활용

  ```python
  inner_qs = Blog.objects.filter(name__contatins='Cheddar')
  entries = Entry.objects.filter(blog__in=inner_qs)
  ```

  sqlite에서의 표현

  ```sqlite
  SELECT * FROM Entry 
  WHERE blog.id IN (SELECT id FROM Blog WHERE NAME
  LIKE '%Cheddar%');
  ```

  - sqlite의 서브쿼리를 표현

- 활용 1

  ```python
  Entry.objects.all()[0]
  Entry.objects.all()[0:3]
  ```

  sqlite에서의 표현

  ```sqlite
  SELECT * FROM Entry LIMIT 1;
  SELECT * FROM Entry LIMIT 3 OFFSET 0;
  ```



- 활용 2

  ```python
  Entry.objects.order_by('id')
  Entry.objects.order_by('-id')
  ```

  sqlite에서의 표현

  ```sqlite
  SELECT * FROM Entry ORDER BY id;
  SELECT * FROM Entry ORDER BY id DESC;
  ```

  - Id 값으로 정렬



## ORM 확장 (1 : N)



![데이터베이스08-1](/db/images/%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A408-1.png)



- Foreign Key (외래키)
  - 키를 사용하여 부모 테이블의 유일한 값을 참조 (참조 무결성)
    - 데이터베이스 관계 모델에서 관련된 2개의 데이블 간의 일관성
  - 외래 키의 값이 반드시 부모 테이블의 기본 키일 필요는 없지만 유일한 값이어야 함



- Models.ForeignKey 필드

  - 2개의 필수 위치 인자
    - Model class : 참조하는 모델
    - on_delete : 외래 키가 참조하는 객체가 삭제되었을 때 처리 방식
      - CASCADE : 부모 객체(참조 된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제
      - PROTECT : 삭제되지 않음
      - SET_NULL : NULL 설정
      - SET_DEFAULT : 기본 값 설정

- Create

  ```python
  artist = Artist.objects.get(id=1)
  genre = Genre.objects.get(id=1)
  
  album = Album()
  album.name = '앨범1'
  album.artist = artist # 1. 객체의 저장
  album.genre = genre
  album.save()
  ```



![데이터베이스08-2](/db/images/%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A408-2.png)

