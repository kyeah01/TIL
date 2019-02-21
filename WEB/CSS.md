# CSS

1. ## CSS

   html은 마크업, 뼈대를 구축하는 언어

   <-> css는 보여주기위한 디자인을 하는 언어

   html은 css를 포함할 수 있으나, css는 단독으로는 불가능하다.

   html과 css는 별개의 언어다.

   기본적으로 가장 마지막에 선언된것이 적용된다.

2. ## 선택자(selector)

   ![css_selector_discription](css_selector_discription.png)
   특정요소들을 선택하여 스타일을 적용할 수 있게 해주는 것.

   이러한 선택자들을 활용하여 스타일적용하기 위해 html에서 의미없지만 구분하는 코드들을 짜게 된다. 예를 들어 div와 span같은 경우.

   1) 활용법

   1. Inline : 라인안에 쓰기
   2. Embedding: 내부참조
   3. Link File : 외부참조

   컴포넌트화를 위해 외부참조를 가장 많이 쓰게 됨
   코드의 재사용성을 높이기 위해!

   2) 선언에 포함되는 속성값에 들어갈 수 있는 것.

   1. 키워드
   2. 크기단위 - px (절대단위에 가까움), 
         ​    % (상속된 경우 부모에 대한 상대크기),
         ​    em(배수단위로 상대단위, 
         ​    요소에 지정된 사이즈에 대한 상대적 사이즈)
         ​    rem(최상위요소 html에 대한 상대적 사이즈)
            Viewport 단위(화면크기에 비례한 사이즈)
   3. 색상 - HEX, RGB, RGBA(A는 투명도)

   3) 속성값의 단위

   1. 키워드
   2. 크기단위
      1. px
      2. %
      3. em : 요소에 지정된 사이즈(상속된 사이즈나 디폴트 사이즈)에 대한 상대적인 사이즈 크기단위이다.
      4. rem : 최상위요소(html 자체)에 대한 크기단위
      5. viewpoint 단위: vw,vh,vmin,vmax 등 뷰포인트 대비
   3. 색상표현단위 : HEX, RGB, RGBA(A는 투명도!)

3. ## Box model

   html의 모든 모양은 박스모델이다. 
   따라서 html을 꾸며주는 기본적으로 css도 박스모양을 가진다.

   ![css ë°ì¤ëª¨ë¸ì ëí ì´ë¯¸ì§ ê²ìê²°ê³¼](https://s3.amazonaws.com/viking_education/web_development/web_app_eng/css_box_model_chrome.png)

   1) Margin : 테두리 바깥의 외부 여백, 배경색을 지정할 수 없다.

   2) Border : 테두리영역(보더에 픽셀값을 주지 않아도 알아서 보더는 할당되는 순간 자체적으로 픽셀값을 가진다. 그래서 해당 div나 p가 할당해 준 픽셀값보다 더 차지하는 경우가 생긴다.)

   3) padding : 테두리 안쪽의 내부 여백, 요소에 적용된 배경의 컬러, 이미지는 패딩까지 적용.

   4) contents : 실제 내용이 위치

4. ## Display

   1) block : 항상 새로운 라인에서 시작한다. 화면 크기 전체의 가로폭을 차지한다(width : 100%). block레벨 요소 내에 inline 레벨 요소를 포함할 수 있다. (div, h1~h6, p, ol, ul, li, hr, table, form ...)

   2) inline : 새로운 라인에서 시작하지 않으며 문장의 중간에 들어갈 수 있다. cotent의 너비만큼 가로폭을 차지한다.  width, heght, margin(top, bottom) 프로퍼티를 지정할 수 없다. 상, 하 여백은 line-height로 지정한다. (span, a, strong, )

   3) inline-block : block에서의 width, heght, margin(top, bottom) 속성을 모두 지정할 수 있다.

   4) none

5. ## Visibility Property

   1) visible : 해당요소를 보이게 한다.(기본값)

   2) hidden : 해당요소를 보이지 않게 한다.(공간은 존재함)

6. ## Position

   1) static(기본위치) : 기본적인 요소의 배치 순서에 따라 위에서 아래로, 왼쪽에서 오른쪽으로 순서에 따라 배치되며, 부모 요소 내에 자식 요소로써 존재할 때는 부모 요소의 위치를 기준으로 배치된다.

   2) relative(상대위치) : 기본위치(static)을 기준으로 좌표 프로퍼티를 사용하여 위치를 이동.(좌표 프로퍼티-top, bottom, left, right) 움직인 후 원래 있었던 공간이 유지된다.

   3) absolute(절대위치) : 선언하면 기본 레이어 관계에서 벗어나게 된다. 즉 다른 도형들도 새로운 자리로 움직이게 된다. 움직인 후 원래 있었던 공간이 사라진다. 부모영역을 벗어나 자유롭게 어디든 위치할 수 있으며, 부모가 static 이외에 position 프로퍼티가 지정되어 있을 경우에만 부모를 기준으로 위치하게 된다. 만약 부모, 조상이 모두 static이면 document body를 기준으로 위치하게 된다.

   4) fixed(고정위치) : 부모 요소와 관계없이 브라우저의 뷰포인트를 기준으로 좌표 프로퍼티를 사용하여 위치를 이동한다. absolute와 동일하게 움직이지만 스크롤이 생길때 움직이지 않고 고정되어 있다.

   5) z-index : 값이 클수록 앞으로 배치

   6) overflow

   TIP > 부모에게 relative 를 줘서 자식이 absolute를 받을 때 기준점을 부모로 인식하도록 하는 것이 편하다.

   > n-th child(n) : 모든 자식의 순서에서 n번째, 해당하는 태그의 순서.
   > 			다른 종류를 선언해도 무조건 n번째를 찾음.
   >
   > nth-of-type(n) : 해당하는 자식 태그 요소에서 순서를 찾음.
   > 			    특정 태그를 가진 자식속성에서 몇번째에
   > 			   해당하는지 찾음

7. ## Emmet
