# Git

- 버전관리도구.



## Repository

- git repository(저장소)는, 프로젝트의 리비전과 히스토리를 유지하고 관리하는데 필요한 모든 정보를 담고있는 데이터베이스.
- 데이터구조
  - 객체
    - blob : 파일의 각 버전.
    - tree : 한 레벨의 디렉토리 정보. 파일트리를 뜻하는 듯.
    - commit : 저장소에 제출된 각 변경사항에 대한 메타데이터를 가진다. 작성자, 커밋실행자, 커밋날짜, 로그메시지 등이 포함된다. 각 커밋은 트리객체를 가르키고, 이 트리 객체에는 커밋이 실행된 당시의 저장소 상태를 완전한 스냅샷으로 캡쳐한 내용이 담겨있다. 루트 커밋이 아닌 경우, 상위 커밋을 가지며, 두개의 커밋을 상위커밋으로 가지는 경우도 있다.
    - tag : 특정 객체(주로 커밋)에 사람이 읽을 수 있는 임시 이름을 할당한다.
  - 인덱스 
    - 어떤 시점에서 캡처한 프로젝트의 전체 구조의 한 버전을 나타냄.



## git 기본 명령어

- `add`

  ```bash
  $ git add .
  ```

  - `add`뒤에 특정 파일명을 입력하거나, `.` 또는`--all`을 작성하여 바뀐 파일 모두를 add할 수 있다.

- `commit`

  ```bash
  $ git commit -m "commit message"
  ```
  
  혹은, 
  
  ```bash
  $ git commit -message "commit message"
  ```
  
  를 활용해서 사용할 수 있다.
  
  만약 새로 생긴 디렉토리나 파일은 제외하고, 수정된 파일만 커밋하고싶다면, `add`를 생략하고
  
  ```bash
  $ git commit --all -m "commit message"
  ```
  
  를 통해서 커밋할 수 있다.
  
- `rm`

  ```bash
  $ git rm --cached [ file_name ] 
  ```

  을 활용해서 `add`되어있는 git 인덱스를 삭제하거나

  ```bash
  $ git rm [ file_name ]
  ```

  을 활용해서 `add`되어있는 git 인덱스와 파일 모두를 지울 수 있다.

- `mv` 

  `a.txt`라는 이름의 파일이 `add`되어 onstage된 상태에서 이름을 변경하고, 다시 `add`하려고 한다.

  ```bash
  $ mv a.txt b.txt
  $ git rm a.txt
  $ git add b.txt
  ```

  ```bash
  $ git mv a.txt b.txt
  ```

  두경우 모두 같은 명령어이며, 같은 동작을 수행한다.



## Diff

- 리눅스에서 `diff`명령은 두 파일의 콘텐츠를 한줄씩 비교하여 서로 차이가 나는 부분을 요약해서 보여주는 것이다. 

- git에서도 `diff`명령이 존재한다

- git에서의 diff는 세가지 기본 형태의 트리객체나 그와 유사한 객체를 활용한다.

  - 전체 커밋 그래프 내에 있는 임의의 트리 객체
  - 사용자의 작업디렉토리
  - 인덱스

- git diff
  
  
  ```bash
$ git diff
  ```

  작업디렉토리와 인덱스 간의 차이점을 보여준다. 작업디렉토리에서 변경된사항으로, 다음커밋동안 준비된 상태(onstage)가 될 후보 항복들을 보여주는 것.
  
  ```bash
$ git diff HEAD
  ```

  작업 디렉토리와 HEAD를 비교해준다.
  
  ```bash
$ git diff --cached
  ```

  인덱스와 HEAD를 비교해준다.
  
  ```bash
$ git diff HEAD^ HEAD
  ```

  이전 헤드와 현재 헤드의 비교
  
  ```bash
  $ git diff --cached [ commit ]
  ```
  
  onstage상황과 지정된 커밋간의 차이점
  
  ```bash
  $ git diff [ commit 1 ] [ commit 2 ]
  ```
  
  두 커밋과의 차이점



## Bisect

- git을 활용하다가, 프로그램이 뭔가 결함이 있어 작동하지 않는다고 가정하자. 이전의 작동하는 `나쁜`버전이 아니라, `좋은` 버전을 찾아야 한다.

- `bisect`명령어를 통해 알아낼 수 있다.

- `bisect`는 한쪽 끝에서는 좋은 동작을 기준으로, 한쪽 끝에서는 나쁜 동작을 기준으로 범위를 좁혀가면서 새 커밋을 선택하게 되는 과정이고, 결과적으로 잘못된 동작이 도입된 커밋에 도달할 수 있게 된다. 한마디로, 이분검색을 통해 디버깅해가는 과정이다.

  ```bash
  $ git bisect start
  ```

  이분 검색을 위한 새로운 브랜치가 생성되는 순간이다.

  ```bash
  $ git bisect bad
  ```

  현재 헤드(HEAD)에 문제가 있음을 알린다. 혹은, `bad`명령어 뒤에 커밋id를 남겨서 bad 커밋이 무엇인지 알릴 수 있다.

  ```bash
  $ git bisect good [ commit_ID ]
  ```

  오류가 없는 커밋을 알려준다.

  그러면 git은 자동으로 사용자의 디렉토리를 good커밋과 bad 커밋사이의 특정 리비전으로 바꿔준다. 우리가 할 일은 해당 버전이 좋은 버전인지 나쁜 버전인지 테스트 한 다음, git에게 결과를 알려주는 일이다.

  ```bash
  $ git bisect [good/bad]
  ```

  이분검색을 최대로 실행할 경우 단 하나의 커밋에 도달할때까지 검색이 반복되며, 하나의 good을 찾는 경우 이분검색이 끝났음을 알리는 커밋메시지가 뜬다.

  ```bash
  $ git bisect reset
  ```

  명령어를 활용해서 체크인 되어있는 브랜치에서 체크아웃하고, 원래 브랜치로 돌아오게 된다.

  만약, good, bad 선택시 뭔가가 잘못되었거나 다시 시작하고 싶다면

  ```bash
  $ git bisect replay
  ```

  를 통해서 한단계 이전으로 돌아갈 수 있다.



## Reset

- git res et명령은 `soft`, `mixed`, `hard`의 세가지 옵션을 가진다.

- soft

  ```bash
  $ git reset --soft [ commit ]
  ```

  soft 옵션은 지정된 커밋을 가리키도록 HEAD 참조를 변경한다. 인덱스와 작업 디렉터리의 콘텐츠는 변경되지 않고 그대로 유지된다.

- mixed

  ```bash
  $ git reset --mixed [ commit ]
  ```

  mixed 옵션은 지정된 커밋을 가르키도록 HEAD를 변경한다. 커밋에 지정된 트리구조에 맞게 인덱스의 콘텐츠도 수정된다.

- hard

  ```bash
  $ git reset --hard [ commit ]
  ```

  hard 옵션은 지정된 커밋을 가르키도록 HEAD를 변경한다. 커밋에 지정된 트리구조에 맞게 인덱스의 콘텐츠도 수정되며, 작업 디렉토리의 콘텐츠도 지정된 커밋이 나타내는 트리의 상태를 반영하도록 변경된다.

| 옵션   | HEAD | 인덱스 | 작업디렉토리 |
| ------ | ---- | ------ | ------------ |
| --soft | O | X | X |
|--mixed|O|O|X|
|--hard|O|O|O|



## Stash

- 이전 커밋 이후 작업한 내용을 킵해놓고 싶을 때 쓰는 명령어.

- `stash` 시키면 커밋 이후의 내용은 전부 로컬에서 사라지게 되고, stash list에 stash된 해당 버전이 저장된다.

- `stash`시키기.

  ```bash
  $ git stash
  ```

- 해당 `stash`된 버전들을 확인하고싶다면

  ```bash
  $ git stash list
  ```

- 해당 버전을 다시 로컬로 적용시키고싶다면 (버전 쓰지않으면 제일 마지막꺼를 적용시킴)

  ```bash
  $ git stash apply 해당버전
  ```

- 해당 `stash` 버전을 드랍하고싶다면 `git stash list`에서 해당 버전을 확인한 후  (버전 쓰지않으면 제일 마지막꺼를 적용시킴)

  ```bash
  $ git stash drop 해당버전
  ```

- 다른 브랜치에서 해당 `stash` 버전을 적용시키고싶다면 브랜치 이동한 후  (버전 쓰지않으면 제일 마지막꺼를 적용시킴)

  ```bash
  $ git stash pop 해당버전
  ```