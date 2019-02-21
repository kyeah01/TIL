# GET, POST

https://interconnection.tistory.com/72 참조.

## Get


![](C:/Users/student/Desktop/git/TIL/MD_Image/WEB/flask/GET.png)

- 가져온다는 개념에 가깝다. 서버의 어떤 값이나 내용, 상태를 바꾸지 않고 보여줄때 사용한다(검색이나 게시판 조회 같은 경우)
- 입력받은 query의 이름과 값이 결합되어 스트링 형태로 서버에 전달된다. (URL에 query의 값이 그대로 노출된다.)
- DB에 추가로 정보를 저장하거나 처리하지 않고 저장된 Data를 단순 요청하는 정도로 사용한다. 
- 데이터 양의 제한 존재한다.



## Post

![](C:/Users/student/Desktop/git/TIL/MD_Image/WEB/flask/POST.png)

- 수행한다는 개념에 가깝다. 서버의 값이나 상태를 변경하는 경우에 사용한다(게시판에 글을 쓰거나 수정하는 경우)
- 클라이언트와 서버간에 인코딩하여 서버로 전송됨.
- 헤더를 통해 요청이 전송된다.
- 데이터의 양은 제한이 없다.
- DB에 추자로 서버에서 갱신작업을 할 때 서버에서 정보가 가공되어 응답하는 경우에 주로 사용한다.

- GET과 POST 둘 다 보안에는 취약하고, 보안을 위해서는 2차 조치가 필요하다.

