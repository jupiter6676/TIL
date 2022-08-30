# 1. CSS

## (1) CSS은 무엇인가?

- Cascading Style Sheets
  
  - HTML이나 XML로 작성된 문서의 표시 방법을 기술하는 스타일 스트 언어
  - 요소가 화면, 종이, 음성이나 다른 매체 상에 어떻게 렌더링되어야 하는지 지정한다.
  
- 하나의 CSS 규칙은 선택자에 연결된 속성의 세트로 구성된다.

  ```css
  /* HTML의 모든 문단을 노란색 글자와 검은색 배경으로 만들기 */
  p {
      color: yellow;
      background-color: black;
  }
  ```

  ```html
  <p>
      문단1
  </p>
  
  <p>
      문단2
  </p>
  ```



## (2) HTML 요소 스타일링

1. CSS 외부 참조

   - `styles.css`

     ```css
     /* h1과 p는 선택자 */
     /* 선택자는 쉼표로 구분 */
     h1, p {
         color: red;
     }
     ```

   - `styles.css` 파일을 `index.html` 에 링크

     ```html
     <!-- index.html -->
     <head>
         …
         <link rel="stylesheet" href="styles.css">
     </head>
     ```



2. 요소의 기본 동작 변경

   ```css
   li {
       list-style-type: none;
   }
   ```

   - 요소에는 기본 스타일이 존재하는데, 이를 원하는 모양으로 변경할 수 있다.
   - 예를 들어, 위의 코드는 목록의 글머리 기호를 제거하며, 글머리 기호를 변경할 수도 있다.



3. class 추가

   ```html
   <ul>
     <li>항목 하나</li>
     <li class="special">항목 둘</li>
     <li>항목 <em>셋</em></li>
   </ul>
   ```

   ```css
   .special {
     color: orange;
     font-weight: bold;
   }
   ```

   - 다른 요소를 변경하지 않고 요소의 하위 부분을 선택할 수 있는 방법

   - css에서 클래스의 선택자는 `.`로 시작한다.

   - 문서의 위치에 따라 스타일을 지정

     ```css
     /* <li>의 하위 요소인 <em> 요소를 선택한다. */
     li em {
         color: rebeccapurple;
     }
     
     /* 제목 바로 다음에 오는 단락을 선택한다.  */
     h1 + p {
     	font-size: 200%;
     }
     ```



4. 상태에 따른 스타일링

   - 링크 스타일링

   - 링크의 스타일을 지정할 때에는, `<a>` 요소를 대상으로 해야 한다.

   - 방문되지 않음, 방문 중, 마우스 오버, 키보드를 통한 포커스, 클릭(활성화) 여부에 따른 상태가 다르다.

   - 아래 CSS는 방문하지 않은 링크는 분홍색, 방문한 링크는 녹색으로 스타일링한다.

     ```css
     a:link {
         color: pink;
     }
     
     a:visited {
         color: green;
     }
     ```

   - 아래 CSS는 사용자가 링크 위로 마우스를 올렸을 때, 링크의 밑줄을 제거한다.

     ```css
     a:hover {
       text-decoration: none;
     }
     ```

     

## (3) 선택자 우선 순위 (Specificity)

- 아래와 같이, 두 선택자가 동일한 HTML 요소를 선택할 수 있는 경우가 종종 있다.

  ```css
  .special {
  	color: red;
  }
  
  p {
  	color: blue;
  }
  ```

  ```html
  <p class="special">나는 무슨 색입니까?</p>
  ```

- CSS 언어에는 충돌시 어떤 규칙이 이기는지 제어하는 규칙이 있는데, 이 규칙을 **계단식(cascade)** 및 **우선 순위(specificity)** 라고 한다.

- class 선택자는 요소 선택자보다 우선 순위가 높기 때문에, 위의 경우 단락이 빨간색으로 표시된다.

- 추가 정보는 여기로 → [계단식 및 상속](https://developer.mozilla.org/ko/docs/Learn/CSS/Building_blocks/Cascade_and_inheritance)



## (4) 속성 및 값

- 속성 (Properties)
  - 변경할 스타일 기능을 나타내는 식별자
  - font-size, width, background-color 등

- 값 (Values)
  - 각 속성에는 값이 지정되어 있다.
  - 이 값은 해당 스타일 기능을 변경하는 방법을 나타낸다.




# 2. 출처

- [CSS: Cascading Style Sheets (Mozilla)](https://developer.mozilla.org/ko/docs/Web/CSS)

- [CSS를 이용한 HTML 스타일링 익히기 (Mozilla)](https://developer.mozilla.org/ko/docs/Learn/CSS)
