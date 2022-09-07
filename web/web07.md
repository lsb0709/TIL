# Bootstrap Grid System

### Grid system (web design)

- 요소들의 디자인과 배치에 도움을 주는 시스템
- 기본 요소
  - Column : 실제 컨텐츠를 포함하는 부분
  - Gutter : 칼럼과 칼럼 사이의 공간 (사이 간격)
  - Container : Column들을 담고 있는 공간



### Bootstrap grid System

- Bootstrap Grid system은 flexbox로 제작됨

- container, rows, column으로 컨텐츠를 배치하고 정렬

- 반드시 기억해야 할 2가지!

  1. 12개의 column
  2. 6개의 grid breakpoints

- Grid system

- 정리

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <!-- CSS only -->
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
      <title>Document</title>
  </head>
  <body>
      <style>
          .box{
              background-color: antiquewhite;
              border: 1px solid black;
              text-align: center;
          }
      </style>
      <h2>기본</h2>
      <!-- flex만 한 일반적인 box의 배치 -->
      <div class="d-flex">
        <div class="box">col</div>
        <div class="box">col</div>
        <div class="box">col</div>
      </div>
      <!--Bootstrap grid System, 자동으로 화면에서 12등분 된 화면을 균등하게 나눠가짐 -->
      <div class="row my-3">
          <div class="col">
              <div class="box">col1</div>
          </div>
          <div class="col">
              <div class="box">col2</div>
          </div>
          <div class="col">
              <div class="box">col3</div>
          </div>
      </div>
      <!-- 4개로 늘려도 화면에 맞게 나눠짐 -->   
      <div class="row my-3">
          <div class="col">
              <div class="box">col1</div>
          </div>
          <div class="col">
              <div class="box">col2</div>
          </div>
          <div class="col">
              <div class="box">col3</div>
          </div>
          <div class="col">
              <div class="box">col4</div>
          </div>
      </div>
      
      <div class="row my-3">
          <div class="col-2">
              <div class="box">col-2</div>
          </div>
          <div class="col-6">
              <div class="box">col-6</div>
          </div>
      </div>     
      <!-- 12를 넘으면 아래로 흘러내려감 -->   
      <div class="row my-3">
          <div class="col-5">
              <div class="box">col-5</div>
          </div>
          <div class="col-6">
              <div class="box">col-6</div>
          </div>
          <div class="col-4">
              <div class="box">col-4</div>
          </div>
      </div>   
      
      <!-- 총 6개 배치를 할건데, 한 줄에 가장 작은 화면 : 한개, 모바일 : 2개, 태블릿 : 3개, PC : 4개를 보여주게 하고싶다면? -->
      <h2>breakpoint</h2>
      <div class="row my-3"> 
        <div class="col-12 col-sm6 col-md-4 col-lg-3">
          <div class="box">col1</div>
        </div>
        <div class="col-12 col-sm6 col-md-4 col-lg-3">
          <div class="box">col2</div>
        </div>
        <div class="col-12 col-sm6 col-md-4 col-lg-3">
          <div class="box">col3</div>
        </div>
        <div class="col-12 col-sm6 col-md-4 col-lg-3">
          <div class="box">col4</div>
        </div>
        <div class="col-12 col-sm6 col-md-4 col-lg-3">
          <div class="box">col5</div>
        </div>
        <div class="col-12 col-sm6 col-md-4 col-lg-3">
          <div class="box">col6</div>
        </div>
      
      </div>
      <!-- offset -->
      <h2>offset</h2>
      <div class="row my-3">
          <div class="col-4">
              <div class="box">col-4</div>
          </div>
          <div class="col-4 offset-4">
              <div class="box">col-4</div>
          </div>
          <div class="col-3">
              <div class="box">col-3</div>
          </div>
          <div class="col-3 offset-3">
              <div class="box">col-3</div>
      </div>
      <!-- Gutter vs no_gutter -->
      <h2>Gutter vs no_gutter</h2>
      <div class="row my-3">
          <div class="col-6">
              <div class="box">col-6</div>
          </div>
          <div class="col-6">
              <div class="box">col-6</div>
          </div> 
      </div>
      
      <div class="row g-0 my-3">
          <div class="col-6">
              <div class="box">col-6</div>
          </div>
          <div class="col-6">
              <div class="box">col-6</div>
          </div> 
      </div>
      <!-- JavaScript Bundle with Popper -->
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
  </body>
  </html>
  
  ```

![web07-1](/web/images/web07-1.png)

