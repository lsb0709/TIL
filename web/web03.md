# CSS Position

- 문서 상에서 요소의 위치를 지정

- static : 모든 태그의 기본 값(기준 위치)

  - 일반적인 요소의 배치 순서에 따름(좌측 상단)

  - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치 됨

  ![web03-1](/web/images/web03-1.png)

- 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능

  1. relative : 상대 위치

     - 자기 자신의 static 위치를 기준으로 이동 (normal flow 유지)
     - 레이아웃에서 요소가 차지하는 공간은 static일 때와 같음 (normal position 대비 offset)

     ![web03-2](/web/images/web03-2.png)

  2. absolute : 절대 위치

     - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음 (normal flow에서 벗어남)
     - static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동 (없는 경우 브라우저 화면 기준으로 이동)

     ![web03-3](/web/images/web03-3.png)

  3. fixed : 고정 위치

     - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음 (normal flow에서 벗어남)
     - 부모 요소와 관계없이 viewport를 기준으로 이동
       - 스크롤 시에도 항상 같은 곳에 위치함

     ![web03-4](/web/images/web03-4.png)

  4. sticky : 스크롤에 따라 static -> fixed로 변경

     - 속성을 적용한 박스는 평소에 문서 안에서 position: static 상태와 같이 일반저인 흐름에 따르지만 스크롤 위치가 임계점에 이르면 

       Position: fixed와 같이 박스를 화면에 고정할 수 있는 속성

![web03-5](/web/images/web03-5.png)

- absolute : 특정 영역 위에 존재
- fixed : 브라우저 기준으로 위치



## position sticky

- sticky : 스크롤에 따라 static -> fixed로 변경

  - 속성을 적용한 박스는 평소에 문서 안에서 position: static 상태와 같이 일반적인 흐름에 따르지만, 스크롤 위치가 임계점에 이르면 

    position: fixed와 같이 박스를 화면에 고정할 수 있는 속성

  - 일반적으로 Navigation Bar에서 사용됨.



## CSS 원칙

- CSS 원칙 I, II : Normal flow
  - 모든 요소는 네모(박스모델), 좌측상단에 배치
  - display에 따라 크기와 배치가 달라짐
- CSS 원칙 III
  - position으로 위치의 기준을 변경
    - relative : 본인의 원래 위치
    - absolute : 특정 부모의 위치
    - fixed : 화면의 위치
    - sticky : 기본적으로 static이나 스크롤 이동에 따라 fixed로 변경



## Flexbox



![web03-6](/web/images/web03-6.png)

- Flex Container (부모 요소)
  - flexbox 레이아웃을 형성하는 가장 기본적인 모델
  - Flex Item들이 놓여있는 영역
  - display 속성을 flex 혹은 inline-flex로 지정
- Flex Item (자식 요소)
  - 컨테이너에 속해 있는 컨텐츠(박스)
- Flex는 왜 써야할까?
  - 수동 값 부여 없이 수직 정렬이 가능하다.
  - 아이템의 너비와 높이 혹은 간격을 동일하게 배치 시켜 준다.



#### Flex 속성

- 배치 설정
  - flex-direction
  - Flex-wrap
- 공간 나누기
  - Justify-content (main axis)
  - align-content (cross axis)
- 정렬
  - align-items (모든 아이템을 cross axis 기준으로)
  - align-self (개별 아이템)



![web03-7](/web/images/web03-7.png)





![web03-8](/web/images/web03-8.png)

- wrap : 넘치면 그 다음 줄로 배치
- no wrap (기본 값) : 한 줄에 배치



#### flex-flow

- flex-direction 과 flex-wrap 의 shorthand

- flex-direction과 flex-wrap에 대한 설정 값을 차례로 작성

  예시) flex-flow: row nowrap;



![web03-9](/web/images/web03-9.png)



![web03-10](/web/images/web03-10.png)



### Flex 속성 : justify-content & align-content

- 공간 배분
  - flex-start (기본 값) : 아이템들을 axis 시작점으로
  - flex-end : 아이템들을 axis 끝 쪽으로
  - center : 아이템들을 axis 중앙으로
  - space-between : 아이템 사이의 간격을 균일하게 분배
  - space-around : 아이템을 둘러싼 영역을 균일하게 분배 (가질 수 있는 영역을 반으로 나눠서 양쪽에)
  - space-evenly : 전체 영역에서 아이템 간 간격을 균일하게 분배



![web03-11](/web/images/web03-11.png)



![web03-12](/web/images/web03-12.png)

### Flex 속성 : align-items & align-self

- Cross axis를 중심으로
  - stretch (기본 값) : 컨테이너를 가득 채움
  - flex-start : 위
  - flex-end : 아래
  - center : 가운데
  - baseline : 텍스트 baseline에 기준선을 맞춤

![web03-13](/web/images/web03-13.png)



![web03-14](/web/images/web03-14.png)



![web03-15](/web/images/web03-15.png)

