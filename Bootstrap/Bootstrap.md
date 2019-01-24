# Bootstrap

- Bootstrap은 css javascript html를 조작할 수 있는 프레임워크다.
- CDN사용(css는 타이틀 바로 아래, js는 바디태그 바로 위에 위치)으로 간편하게 적용할 수 있다.
- minify : 코드가 엄청 길면 한줄로 축약해버려서 로딩길이를 차이나게하는거, 공백도 다 바이트라서 로딩시간 먹음.
- 부트스트랩은 css를 리셋시킨다(브라우저마다 기본 css가 있기때문에 각각의 css 를 다 리셋시킨후에 (reset css) 다시 css 먹이기 위해): reboot.css

1. Utilities : 클래스명을 바꿔서 편하게 조작할 수 있다.

   1. spacing										rem값![1548284965188](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1548284965188.png)
   2. color : primary, warning ... 등 예쁜색깔로 세팅되어있는 색깔들을 활용할 수 있다.
   3. background color : bg-primary
   4. text color : text-primary
   5. boder : border, border-primary
   6. radius : rounded
2. Grid system
   1. 기본적으로 수평 grid는 총 12칸으로 구성되어 있다.
   2. view point처럼 브라우져가 나타내고있는 화면의 크기에 대비해서 크기 사이즈를 나타낼 수 있다.
      ![1548286130294](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1548286130294.png)
   3. offset : 공백을 뜻함, 마찬가지로 클래스명에 적용 가능.
3. Components : https://getbootstrap.com/docs/4.2/components
   소스따와서 간편하게 조작가능.
4. 
