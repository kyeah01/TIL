# error: cannot stat '': Permission denied

## 메시지

`error: cannot stat '': Permission denied`



## 상황

다른 branch로 커밋한 이후에 master에서 merge 하는 중 발생했다.



## 해결방법

파일이 실행 중일때 에러가 뜰 수 있다고해서 켜져있는 파일을 끄기 위해 vs code를 끄고 merge했더니 잘된다!