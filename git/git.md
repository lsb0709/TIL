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





​	