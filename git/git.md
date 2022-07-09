# git

Git 이란?

 분산 버전 관리 시스템(DVCS)

리눅스 토르발스가 개발

컴퓨터 파일의 변경사항 추척, 여러 명의 사용자들 간에 해당 파일 작업 조율

## 명령어 정리

```bash
$ git init
```

새로운 git 저장소(repository)를 생성할 때 사용되는 명령어



```bash
$ git status
```

현재 위치한 저장소에 대한 정보를 알려주는 명령어



```bash
$ git add .
$ git add 파일이름
```

commit 하기 전의 1차 공간(Staging Area) 상태



```bash
$ git commit -m '커밋메세지'
```

로컬 저장소에 저장



기본적으로 로컬에서 git commit 까지 하면 github에 올릴 준비는 다 한 상태

```bash
$ git log
```

commit 한 버전들을 확인



### 로컬 저장소에서 원격저장소로 보낼 때

Github 사이트에 등록된 user name과 e-mail 주소등록

```bash
$ git config --global user.name "닉네임"
$ git config --global user.email "이메일주소입력"
```



```bash
$ git push
```

```bash
$ git remote add origin "github주소/닉네임/설정주소값"
```

```bash
$ git push origin master 혹은 (main)
```



#### git 저장소로 버전관리 시작하기

1. $ git init 을 통해 master로 접속

2. 작업에 필요한 파일 및 문서 생성 및 작성 완료

3. 작업이 끝나면 $ git add 파일명 or $ git add . 으로 1차적으로 저장

4. $ git commit -m '커밋메세지' 를 통해 2차로 저장

5. $ git log 로 commit 된 버전들을 확인

6. 최종적으로 수정, 삭제 등 작업이 완료가 되면 git hub에 원격저장소 생성

   $ git remote add origin "깃헙주소/닉네임/설정주소값"

   (한번만 설정해 주면 그 후로 push 시 항시 저장)

7. $ git push origin master

   마지막으로 푸쉬까지 해주면 자신의 깃헙사이트에 버전이 등록



#### git 사이트에서 로컬 컴퓨터로 폴더 가져오고 싶을 때

터미널에서 $ git clone 가져오고 싶은 github 주소

주의 : 클론 해준 원격 저장소 이름의 폴더 생성

#### git에서 clone과 zip으로 로컬로 가져 올 때 차이점

Zip : 최신 버전의 파일을 그대로 가져온다.

Clone : git 저장소를 그대로 가져온다. => 

​			저장소를 그대로 가져온다는 의미는 git 사이트에서 git 주소의 해당 관리자가 업데이트(git commit)을 새로이 한게 있다면

​			최신 버전이 갱신 됐으므로 git pull origin master 명령어만 입력해 준다면 바로 업데이트를 받아 볼 수 있다.

#### branch 

branch

- 사용목적
  - 독립적인 버전들을 만들어 나가기 위해 사용

- 브랜치 생성

  ``` bash
  (master) $ git branch <브랜치 이름>
  ```

- 브랜치 이동

  ``` bash
  (master) $ git checkout <브랜치 이름>
  ```

- 브랜치 생성 및 이동

  ```bash
  (master) $ git checkout -b <브랜치 이름>
  ```

- 브랜치 목록

  ``` bash
  (master) $ git branch
  ```

- 브랜치 삭제

  ``` bash
  (master) $ git branch -d <브랜치 이름>
  ```



### Github Flow Models

> 해당 프로젝트 저장소에 직접적인 push 권한이 있는지의 여부

#### Feature Branch Workflow (저장소의 소유권이 있는 경우)

1. 혼자작업, 조원 프리라이딩(Fast-forward)
2. 서로 다른 이력을 병합하는 과정에서 다른 파일이 수정되어 있는 상황
3. 각자 커밋이 있는데, 같은 파일이 수정



#### Forking Workflow (저장소의 소유권이 없는 경우)

1. 소유권이 없는 원격 저장소를 fork를 통해 복제
2. 추후 로컬 저장소를 원본 원격 저장소와 동기화하기 위해 URL을 연결
3. 기능 추가를 위해 branch 생성 및 기능 구현
4. 기능 구현 후 원격 저장소에 브랜치 반영
5. Pull requests 요청
6. 병합 완료/ 완료 된 브랜치 삭제
7. master 브랜치로 switch
8. 병합된 master의 내용을 pull
9. 원격 저장소에서 병합 완료 된 로컬 브랜치 삭제
10. 새로운 기능 추가를 위해 branch 생성 및 과정 반복

---



### branch 예시

0. branch 전 작업

> root commit을 발생시키는 작업(master)

```bash
$ git add 

$ git commit -m '<>'
```



1. branch 

> 브랜치에서 작업을 한 이후 이력을 합치기 위해서 일반적으로 merge 를 사용

```bash
$ git init #저장소 설정

$ touch README.md #첫번째 커밋

$ git add README.md

$ git commit -m 'Add README' #(root-commit)

$ git branch #브랜치 조회

git $ git branch example #example 이라는 이름의 브랜치 생성

$ git checkout example #브랜치 이동 (master -> example)
```

- 브랜치할때 가장 중요한것은 첫번재 커밋
- (master) 는 브랜치를 의미



2. 작업 후 (브랜치 : example)

```bash
$ git status

$ git add .

$ git commit -m '예시 만듬'

$ git log --oneline #작업한 로그 확인

$ git checkout master #master 브랜치로 돌아감

$ git log --oneline #example.txt 사라짐
```

- HEAD의 의미 : 전체 중에 내가이동한 정보의 위치를 가지고있다



3. 합치기

```bash
(master)$ git merge example #병합

$ git log --oneline

$ git branch

$ git branch -d example #example브랜치를 지운다

$ git log --oneline
```

- 브랜치/git/github -> 작업/협업을 위한 것

- 붙이는 메인이 되는 브랜치에 병합




​	