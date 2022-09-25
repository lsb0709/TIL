# Git Branch



## 브랜치 생성 및 체크아웃

- 새로운 브랜치 생성 및 체크 아웃

  ```bash
  git checkout -b <branch-name>
  git checkout -b main
  ```

- 브랜치 삭제

  ```bash
  git branch -d, --delete <branch-name>
  
  명령 간소화
  git branch -d <branch-name>           
  git branch -d main
  ```

- 브랜치 이름 변경

  ```bash
  git branch -m, --move <old-branch><new-branch>
  
  명령 간소화
  git branch -m main movie 
  ```

- 원격 브랜치 가져오기

  ```bash
  git checkout -b master2 origin/master
  ```

- Diff(비교)

  변경 내용을 병합하기 전에 비교

  ```bash
  git diff <원본브랜치><대상브랜치>
  git diff master movie
  
  원격 저장소의 마스터브랜치와 로컬 마스터 브랜치를 비교할 때
  git diff master origin/master
  ```

- Merge(병합)

  마스터(master)에 브랜치(movie)를 병합

  ```bash
  git checkout master
  git merge movie
  ```

  로컬에 원격 브랜치 병합

  ```bash
  git diff master origin/master
  git merge origin/master
  ```

- Conflict(충돌)

  병합 취소

  ```bash
  git merge --abort
  ```

  충돌 해결

  ```bash
  충돌하는 파일을 수정 후 add, commit
  git add <conflict-filename>
  git commit -m "[merge]message"
  ```



# Git - Reset

#### Reset

돌아가려는 커밋으로 리파지토리는 재설정되고, 해당 커밋 이후의 이력은 사라짐

```bash
gitreset <option><commmit-id>
```

- hard

  되돌린 이력 이후의 내용은 지워짐

  INDEX 취소, ADD하기 전 상태(UNNSTAGED 상태)

  작업영역의 파일 삭제(모두 취소)

  ```bash
  git reset --hard <commit-id> (git log --oneline을 하면 commit-id를 확인 할 수 있음)
  ```

  커밋을 취소하고 Unstaged 상태로 되돌림(커밋되기 이전상태로 되돌림)

  ```bash
  git reset --hard HEAD^(현재시점보다 한 단계 이전시점으로 돌아가기)
  ```

  

- soft

  되돌린 이력 이후의 내용은 보존

  해당 내용의 인덱스 (스테이지)도 그대로 존재

  바로 다시 커밋할 수 있는 상태로 남아 있음

  index 보존, add한 상태(staged 상태)

  작업영역의 파일 보존(모두 보존)

  ```bash
  git reset --soft <commit-id>
  ```

  커밋이 된 경우 커밋 이전으로 되돌리기

  1. 커밋하기 이전의 staged(Added) 상태로 돌아 감

     ```bash
     git reset -soft HEAD^ 
     ```

  2. add하기 이전의 상태로 되돌리기(staged -> Unsraged)

     ```bash
     git reset filename
     git reset HEAD filename
     ```

     

- mixed

  옵션을 적지 않으면 mixed 옵션 적용(디폴트 값)

  commit만 취소하고 add 상태는 유지해 줌

  ```bash
  git reset --mixed HEAD^ (마지막 하나의 커밋 취소)
  ```

  add 취소(commit은 아직하지 않고 add한 상태만 취소하고 싶은 경우)

  ```bash
  git reset HEAD
  ```

  

## Git - Revert

#### Revert

돌아가려는 커밋으로 리파지토리는 재설정되고, 해당 커밋 이후의 이력은 유지되며 새로운 커밋이 만들어짐



한단계 이전으로 롤백

```bash
git revert HEAD
```



수정하기 이전 초기 버전으로 되돌리기

```bash
git checkout filename
```



#### 파일 삭제

```bash
git rm filename
```

파일 삭제 취소(되돌리기)

```bash
git reset HEAD filename
```

파일을 삭제하여 Unstaged(관리되지 않고 작업영역에만 남겨 놓음) 상태로 만듦

```bash
git rm --cached filename
```

파일 이름 변경

```bash
git mv filename filename2
```



#### 파일 복구

로컬 저장소의 삭제된 파일 복구

- 삭제된 파일 리스트

  ```bash
  git ls-files -d
  ```

- 삭제된 파일 복구

  ```bash
  git checkout [files]
  ```

- 삭제된 모든 파일 복구

  ```bash
  git ls-files -d|xargs git checkout --
  ```



#### Unstaged 파일 삭제

추적 중이지 않은 파일만 삭제(git에서 관리되고 있지 않은 파일들)

```bash
git clean
```

파일만 삭제

```bash
git clean -f
```

파일과 

폴더 삭제

```bash
git clean -f -d
```

파일과 폴더 및 무시된 파일까지 삭제

```bash
git clean -f -d -x
```

가상으로 실행해 보고 어떤 파일이 지워지는지 알려줌

```bash
git clean -n -f
```



## git-Remote

```bash
git remote add <name><url>
git remote add origin https://github.com/username/repo.git
```



원격 저장소

```bash
원격 저장소 목록 보기
git remote -v
git remote --verbose
```

원경 저장소 갱신

```bash
git remote update
git remote prune origin
git fetch --prune
```

원격에서 삭제된 브랜치 업데이트

```bash
git remote prune origin
git remote update --prune
```

원격 저장소 브랜치 확인

```bash
git branch -r
git branch --remotes
```

원격과 로컬의 브랜치 확인

```bash
git branch -a
git branch --all
```



원격 저장소의 브랜치 가져오기

(가져온 후에 동일 한 이름으로 브랜치를 생성하고 체크아웃)

```bash
git checkout -t origin/master
```

원격 저장소의 브랜치 가져오기

(가져온 후에 이름을 변경하여 브랜치를 생성하고 체크아웃)

```bash
git checkout -b master2 origin/master
```

원격 저장소의 브랜치 확인하기

(로컬에 받아서 확인해 보고 테스트해 볼 수 있지만 커밋, 푸시할 수 없으며 체크아웃하면 사라짐)

```bash
git checkout origin/master
```



## Git-Pull

Pull

원격 저장소의 내용을 로컬 저장소에 갱신

원격 저장소의 변경 내용을 로컬 작업 영역으로 내려(fetch) 받은 후 병합(merge)

```bash
git pull
git pull origin master
git pull --rebase origin master
충돌이 발생하면 수정 후 (git add or git rm)
git rebase --continue
or
git rebase --abort
```



원격 브랜치 가져 오기

원격 브랜치를 가져와 새로운 이름으로 체크아웃

```bash
git checkout -b master2 origin/master
```



## Git-Push

Push

로컬 저장소의 변경 내용을 원격 저장소로 보냄

원격 저장소의 업스트림 브랜치 지정하기(한 번 설정하면 그 다음부터는 할 필요가 없음)

```bash
git push --set-upstream origin master
```

원격 브랜치로 전송

```bash
git push origin master
```

새로운 브랜치를 원격에 전송(원격저장소에 새로운 브랜치가 만들어 지고 반영 됨)

```bash
git checkout -b master2
git push origin master2
```

강제푸쉬(Force Push)

```bash
git push --force origin HEAD: master
git push origin +HAED: master
```

원격 브랜치 삭제

```bash
git push -delete origin feature
git push [remotename][:brench]
git push origin: master2
git push [remotename][localbranch][:remotebranch]
```

새로운 브랜치 만들고 원격에 전송

```bash
git checkout -b master2
git push origin master2
```



## Git-Fetch

fetch

원격 저장소의 내용을 로컬 저장소에 내려받음

```bash
git fetch origin
```

원격 저장소의 데이터를 가져온 후 병합

```bash
git fetch origin master
git merge origin/master
```

원격 저장소의 데이터를 가져온 후 로컬의 브랜치가 원격의 이력을 가지도록 변경

로컬에 있는 모든 변경 내용과 확정본을 포기

```bash
git fetch origin master
git reset --hard orgin/master
```



## Git-원격 저장소 관리

원격 저장소 살펴보기

```bash
git remote show[remotename]
git remote show origin
```

원격 저장소 이름 변경

```bash
git remote rename[대상이름][새로운이름]
git remote rename origin origin2
```

원격 저장소 삭제

```bash
git remote rm[remotename]
git remote rm origin
```

