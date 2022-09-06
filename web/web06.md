# Bootstrap 컴포넌트



### Components

- Bootstrap의 다양한 UI 요소를 활용할 수 있음
- 아래 Components 탭 및 검색으로 원하는 UI 요소를 찾을 수 있음
- 기본 제공된 Components를 변환해서 활용



### Buttons

- 클릭 했을 때 어떤 동작이 일어나도록 하는 요소

  ```html
  <button type="button" class="btn btn-primary">Primary</button>
  <button type="button" class="btn btn-Secondary">Secondary</button>
  <button type="button" class="btn btn-Success">Success</button>
  <button type="button" class="btn btn-Danger">Danger</button>
  <button type="button" class="btn btn-Warning">Warning</button>
  <button type="button" class="btn btn-Info">Info</button>
  <button type="button" class="btn btn-Light">Light</button>
  <button type="button" class="btn btn-Dark">Dark</button>
  <button type="button" class="btn btn-Link">Link</button>
  ```

  

![web06-1](/web/images/web06-1.png)

### Dropdowns

- dropdown, dropdown-menu, dropdown-item 클래스를 활용해 옵션 메뉴를 만듬

  ```html
  <div class="dropdown">
    <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
      Dropdown button
    </button>
    <ul class="dropdown-menu">
      <li><a class="dropdown-item" href="#">Action</a></li>
      <li><a class="dropdown-item" href="#">Another action</a></li>
      <li><a class="dropdown-item" href="#">Something else here</a></li>
    </ul>
  </div>
  ```

  

![web06-2](/web/images/web06-2.png)

### Forms > form controls

- form-control 클래스를 사용해 input 및 form 태그를 스타일링 가능

  ```html
  <div calss="mb-3">
    <label for="exmpleFormControlInput1" class="form-label">Email address</label>
    <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com">
  </div>
  <div class="mb-3">
    <label for="exmpleFormControlInput1" class="form-label">Email textarea</label>
    <textarea class="form-control" id="exampleFormControlTrxtarea1" rows="3"></textarea>
  </div>
  ```

  

![web06-3](/web/images/web06-3.png)

### Navbar

- navbar 클래스를 활용하면 네비게이션 바를 제작

  ```html
  <nav class="navbar navbar-expand-lg bg-light">
    <div class="container-fluid">
      <a class="navar-brand" href="#">Navbar</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbar SupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  ```

![web06-4](/web/images/web06-4.png)



### Carousel

- 콘텐츠(사진)을 순환시키기 위한 슬라이드쇼

  ```html
  <div id="carouselExampleSlidesOnly" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-inner">
      <div class="carousel-item active">
        <img src="..." class="d-block w-100" alt="...">
      </div>
      <div class="carousel-item">
        <img src="..." class="d-block w-100" alt="...">
      </div>
      <div class="carousel-item">
        <img src="..." class="d-block w-100" alt="...">
      </div>
    </div>
  </div>
  ```



### Modal

- 사용자와 상호작용 하기 위해서 사용하며, 긴급 상황을 알리는데 주로 사용
- 현재 열려 있는 페이지 위에 또 다른 레이어를 띄움
- 페이지를 이동하면 자연스럽게 사라짐(제거를 하ㅣ 않고도 배경 클릭시 사라짐 - 옵션에 따라 다름)
- Modal은 자바스크립트를 활용하며, 반드시 target과 id가 일치되어야 함