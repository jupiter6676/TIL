# 1. 자바스크립트

> 브라우저(BOM)와 그 내부의 문서(DOM)를 조작하기 위해, ECMAJavascript(JS)를 학습



## (1) 브라우저

- URL로 웹(WWW)을 탐색하며 서버와 통신하고, HTML 문서나 파일을 출력하는 GUI 기반의 소프트웨어
- 인터넷의 컨텐츠를 검색 및 열람하도록 한다.
- 웹 브라우저라고도 한다.
- 주요 브라우저
  - Google Chrome, Mozilla Firefox, Microsoft Edge, Opera, Safari



## (2) 자바스크립트의 필요성

- 브라우저 화면을 '동적'으로 만들기 위해서
- 브라우저를 조작할 수 있는 유일한 언어



# 2. DOM (Document Object Model)

## (1) 브라우저에서 할 수 있는 일

- DOM 조작
  - 문서(HTML) 조작
- BOM 조작
  - navigator, screen, location, frames, history, XHR
- JavaScript Core (ECMAScript)
  - 프로그래밍 문법
  - Data Structure(Object, Array), Conditional Expression, Iteration



## (2) DOM 이란?

- HTML, XML과 같은 문서를 다루기 위한 문서 프로그래밍 인터페이스
- 문서를 구조화하고, 구조화된 구성 요소를 하나의 객체로 취급하여 다루는 논리적 트리 모델
- 문서가 구조화되어 있으며, 각 요소는 객체로 취급
- 단순한 속성 접근, 메소드 활용뿐만 아니라, 프로그래밍 언어적 특성을 활용한 조작이 가능
- 주요 객체
  - window : DOM을 표현하는 창. 가장 최상위 객체 (작성 시 생략 가능)

  - document : 페이지 컨텐츠의 Entry Point 역할을 하며,  등과 같은 수많은 다른 요소들을 포함

  - navigator, location, history, screen




## (3) BOM 이란?

- Browser Object Model
- 자바스크립트가 브라우저와 소통하기 위한 모델
- 브라우저의 창이나 프레임을 추상화해서, 프로그래밍적으로 제어할 수 있도록 제공하는 수단
  - 버튼, URL 입력창, 타이틀 바 등, 브라우저 윈도우 및 웹 페이지 일부분을 제어 가능

- window 객체는 모든 브라우저로부터 지원받으며, 브라우저의 창(window)을 지칭



# 3. DOM 조작

> 선택과 변경

- `querySelector()`(하나를 선택), `querySelectorAll()`(모든 결과를 선택)

- `innerText`, ~~`innerHTML`(보안 문제로 사용하지 X)~~

- `appendChild()`

- `remove()`, `removeChild()`

- `setAttribute()`, `getAttribute()`

  ```javascript
  // a tag 조작
  const a = document.createElement('a');
  a.innerText = 'Google';
  const body = document.createElement('body');
  body.appendChild(a)
  
  a.setAttribute('href', 'https://google.com')
  console.log(a.getAttribute('href'))
  ```

- `classList`

  ```javascript
  // <h1 class="red text-center my-5">안녕하세요</h1>
  const h1 = document.querySelector('h1')
  console.log(h1.classList)
  
  // red → blue
  h1.classList.replace('red', 'blue')
  ```

- `addEventListener()`

  ```javascript
  // <h1>제목</h1>
  // <button id="btn1">클릭</button>
  const btn1 = document.querySelector('#btn1')
  btn1.addEventListener('click', function() {
      // 팝업 창 띄우기
      alert('버튼 클릭!')
      
      // h1 태그를 잡아서, 클래스 blue를 토글
      const h1 = document.querySelector('h1')
      h1.classList.toggle('blue')
  })
  ```

  ```javascript
  // <input type="text">
  const input = document.querySelector('input')
  input.addEventListener('input', function(e) {
      console.log(e.target.value)
  })
  ```




# 4. 기타

- https://developer.mozilla.org/ko/docs/Web/JavaScript
- https://developer.mozilla.org/ko/docs/Learn/JavaScript
  - https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide 



- 추천 (n++, == vs ===, switch)
  - 시작: https://developer.mozilla.org/ko/docs/Learn/JavaScript/First_steps/What_is_JavaScript
  - 문법과 자료형: https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Grammar_and_types
  - 제어문: https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Control_flow_and_error_handling
  - 반복: https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Loops_and_iteration
  - 함수: https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Functions
  - 표현식 연산자: https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Expressions_and_Operators



- 간단하게 보는 JS 동향
  - https://d2.naver.com/helloworld/7495331
  - https://d2.naver.com/helloworld/4268738