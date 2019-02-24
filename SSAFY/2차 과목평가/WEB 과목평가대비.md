# WEB 과목평가대비

## HTML

### TAG

- heading tag - h1, h2, h3, h4, h5, h6 ...
  자동개행을 가지며 각 행 전체를 블럭으로 먹는다.

- div - division, 묶어주는 태그, 
  heading 태그와 마찬가지로 자동개행을 가지며 각 행 전체를 블럭으로 먹는다.

- bold              | strong

  <b>굵은글씨</b>       | <strong>굵은 시맨틱글씨</strong>

- Italic              | em

  <i>이탤릭글씨</i>   |<em>이탤릭 시맨틱글씨</em>

- mark : <mark>highligted</mark>

- del(취소선) : <del>가운데 취소선이 그입니다</del>

- ins(밑줄) : <ins>밑줄긋기</ins>

- sub(아랫첨자) : <sub>아랫첨자</sub>

- sup(윗첨자) : <sup>윗첨자</sup>

- p태그 - pharagraph, 각 행 전체를 블럭으로 가지는 태그, 주로 글자쓸때.

- q태그  - quote, 따옴표 출력을 위한 태그, 
  <q>처럼 쓴다</q>

- pre태그 - 있는그대로~~ 출력해주는 태그, 파이썬의 """와 비교하면 된다.

- 숫자있는 리스트

  <ol>
      <li>a</li>
  </ol>

- 숫자없는 리스트

  <ul>
      <li>a</li>
  </ul>



### SEMANTIC TAG

- article, aside, body,  header, footer, 



## CSS

### SELECTOR

- `*` : 전체 셀렉터
- 그냥 tag에 대한 선택은 그냥 `h2`처럼 쓰면 됨.
- class선택은 `.`으로
- id선택은 `#`으로
- `id` > `class` > `tag` > `전체 셀렉터`순으로 우선순위.
- n-th child보다 n-th of type이 좀 더 명확함.



### DISPLAY

- block : 화면크기 전체의 가로폭을 차지함(width:100%), block레벨 요소 내에서 inline 레벨 요소를 포함할 수 있다.  div, h1~h6, p, ol, ul, hr, table, form

- inline : content의 넓이만큼 가로폭을 차지한다. width, height, margin프로퍼티를 지정할 수 없다. 상, 하 여백은 line-height로 지정한다.
  span, a, strong...

- inline-block : 블락내에서 width, height, margin속성을 모두 지정할 수 있다.

- none값도 줄수있지롱 : none은 아예 없어짐!! 공간도!!

  (visibility : hidden은 보이지 않게 하는것만 함.)



### POSITION

- static(기본위치) : 부모요소의 위치를 기준으로 배치
- relative(상대위치) : 기본위치를 중심으로 위치를 이동한다.



### 크기

- px - 절대단위에 가까움
- % - 상속된 경우 부모에 대한 상대크기
- viewport - font-size:5vh처럼 줄수있음, vh, vw, viewport에 대비해서 사이즈가 변환됨

- Em / Rem
  - html 요소의 크기는 16px이다.(기본값)
  - em은 내가 원래 가질 값에 대해서 배수값을 가지고
  - rem은 root값인 html요소에 대해서 em이 된다.



### COLOR

- hex, rgb, rgba



### BOX MODEL

- margin, border, padding, content
- Margin : 테두리 바깥의 외부여백, 배경색 지정가능.
- Border : 테두리 영역
- padding : 테두리 안쪽의  내부여백, 요소에 적용된 배경의 컬러, 이미지는 패딩까지 적용.
- content
- 원을 만들때도 boder-radius로 깎아서 만듦, px과 %, 둘 다를 가지고 만들 수 있다. 좌상, 우상, 우하, 좌하 순.



### POSITION

- static : 기본위치
- relative : 상대위치, 기본위치를 중심으로 좌표프로퍼티를 사용해서 이동한다. 움직인 후 원래 있었던 공간이 유지된다.
- absolute : 절대위치, 기본레이어관계에서 벗어나서 움직이게된다. 움직인 후 원래 있었던 공간이 사라진다. 부모영역을 벗어나 자유롭게 어디든지 위치할 수 있으며, 부모가 static이외의 포지션이 지정되어있을 경우에만 부모를 기준으로 위치하게 된다. 만약, 부모, 조상이 모두 static이면 body를 기준으로 위치하게 된다.
- fixed 뷰포트 기준으로 위치, 결론적으로 고정되어버림.
- z-index : 값이 클수록 앞으로 위치



## Bootstrap

### Utilities

- spacing : 5는 3rem, 48px을 뜻한다.
- color는 primary, warning......
- border : border border-primary
- rounded circle, rounded pill