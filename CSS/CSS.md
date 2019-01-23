# CSS

1. ## CSS

   html은 마크업, 뼈대를 구축하는 언어

   <-> css는 보여주기위한 디자인을 하는 언어

   html은 css를 포함할 수 있으나, css는 단독으로는 불가능하다.

   html과 css는 별개의 언어다.

   기본적으로 가장 마지막에 선언된것이 적용된다.

   

2. ## 선택자(selector)

   ![css_selector_discription](C:\Users\student\Desktop\git\TIL\CSS\css_selector_discription.png)
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
             % (상속된 경우 부모에 대한 상대크기),
             em(배수단위로 상대단위, 
             요소에 지정된 사이즈에 대한 상대적 사이즈)
             rem(최상위요소 html에 대한 상대적 사이즈)
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

   



​    달라지는 점이 무엇일까라고 했을때, tag를 통해서 여기는 강조, 혹은 볼드체라는 것을 명시! 

​    따라서 단순 볼드체를 하기 위해서 strong 태그를 남발하는 경우에는 브라우저가 모든 볼드체를 강조하게 된다.

모든 html은 박스모델이라고 생각하면 됨.

html은 기본값이 박스, 원도 박스를 깎은 것.

보더가 픽셀값을 먹음 그래서 원하는대로 안나올수도잇음

1. block

   항상 새로ㅜㄴ 라인에서 시작하고 화면크기전체의 가로폭을 차지한다. width 는 100%, 디브, 패딩, h태ㅡㄱ, form table...

2. inline

   새로운 라인에서 시작하지 ㅇ낳으며  너비를 지정할 수 없다.

   프로퍼티값을 지정할 수없다

   span, a, strong, img, br, input, select, button 등...

3. inline-block

   블럭처럼 크기지정가능. 두개의 특징을 모두 가지고있따. line 처럼 한줄에 표시되면서

4. None

   해당요소를 화면에 표시하지않는다. 공간조차 사라짐.

Visiblity Property 기본값임

1. visible
2. hidden 공간은 존재하지만 해당요소를 보이지않게함
3. 

스태틱 기본위치

부모의 위치를 기준으로 배치된다. 

릴레이티브, 상대위치

기본위치를 기준으로 위치이동(스태틱에서 움직인정도.

앱솔루트, 절대위치

부모를 기준으로 이동, 부모박스밖으로 이동 가능

픽스드, ㄱ정위치

브라우저 뷰포인트 대상 위치. 그냥 고정임

static - 기본값

relative - 현재 위치에서 상하좌우 상대적으로 움직일 수 있게 된다. position  적용 전 (static일때) 기준으로 움직임. 움직인 후 원래 있었던 공간이 유지됨

absolute - 기본 레이어 관계에서 벗어난다(집나간 자식, 붕 뜬다) 즉 다른 도형들도 새로운 자리로 움직이게 된다. 움직인 후 원래 있었던 공간이 사라진다. 부모 영역을 벗어나 자유롭게 어디든 위치할 수 있다.부모가 static 이외에 position 프로퍼티가 지정되어 있을 경우에만 부모를 기준으로 위치하게 된다. 만약 부모, 조상이 모두 static이면 document body를 기준으로 위치하게 된다.

fixed - absolute 와 동일하게 움직이지만 스크롤이 생길때 움직이지 않고 고정되어 있다.

TIP> 부모에게 relative를 줘서 자식이 absolute를 받을 때 기준점을 부모로 인식하도록 하는 것이 편하다.

`alt` `shift` `f`



nth-child(n)

모든 자식의 순서에서 찾음, 해당하는 태그의 순서

nth-of-type(n)

해당하는 자식 태그 요소에서 순서를 찾음

부모 속성에서 특정 태그를 가진 자식속성에서 몇번째에 해당하는지