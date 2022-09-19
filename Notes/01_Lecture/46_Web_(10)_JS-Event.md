# 1. Event

## (1) 개념

- 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체
- 이벤트 발생
  - 마우스를 클릭하거나 키보드를 누르는 등, 사용자 행동으로 발생할 수도 있다.
  - 특정 메소드를 호출(`Element.click()`)하여, 프로그래밍적으로도 만들어 낼 수 있다.



## (2) 역할

- ~하면, ~한다.
- 클릭하면, 경고창을 띄운다.
- 특정 이벤트가 발생하면, 할 일(함수)을 등록한다.



# 2. Event Handler

## (1) addEventListener

- 지정한 이벤트가 대상에 전달될 때마다 호출할 함수를 설정
- 이벤트를 지원하는 모든 객체(Element, Document, Window 등)를 대상으로 지정 가능
- 대상에 특정 이벤트가 발생하면, 할 일을 등록한다.

- `target.addEventListener(type, listener[, options])`
  - type: 반응할 이벤트 유형 (대소문자 구문 문자열)
  - listener
    - 지정된 타입의 이벤트가 발생했을 때 알림을 받는 객체
    - EventListener 인터페이스 혹은 JS function 객체(콜백 함수)여야 한다.
  - options
    - capture
      - {capture: true} → true로 축약 가능
      - `false`(default): 핸들러는 버블링 단계에서 동작
      - `true`: 핸들러는 캡처링 단계에서 동작 (흔치 않은 경우)
    - once, passive, signal 등



- 사용자 입력 받아오기

  ```js
  // <input type="text" id="text-input">
  
  // 1. input 선택
  const textInput = document.querySelector('#text-input');
  
  // 2. input 이벤트 등록
  textInput.addEventListener('input', function(event) {
      console.log(event);
      console.log(event.target.value);
  });
  ```



## (2) Event 취소

- `event.preventDefault()`
- 현재 이벤트의 기본 동작을 중단
- HTML 요소의 기본 동작을 작동하지 않게 막는다.
  - ex) a 태그의 기본 동작은 클릭 시 링크로 이동
  - ex) form 태그의 기본 동작은 form 데이터 전송
- 이벤트를 취소할 수 있는 경우, 이벤트의 전파를 막지 않고 그 이벤트를 취소
- 취소할 수 없는 이벤트도 존재
  - 이벤트의 취소 가능 여부는, `event.cancelable`을 사용해 확인



- 글자 복사 & 드래그 막기

  ```js
  const h1 = document.querySelector('#h1');
  h1.addEventListener('copy', function(event) {
     event.preventDefault();	// event의 기본 동작을 막음
     console.log('복사를 할 수 없습니다.')
  });
  
  h1.addEventListener('click', function(event) {
     event.preventDefault();
     console.log('드래그가 금지되어 있습니다.')
  });
  ```



## (3) Bubbling

```html
<!-- window → document → html → body → div → h1 → span -->
<body>
    <div>
        <h1>정말 <span>중요한</span> 내용</h1>
    </div>
</body>
```

- 여기서 '중요한'을 클릭하면 어떤 태그가 선택될까?
- 계층적 구조에 포함되어 있는 HTML 요소에 이벤트가 발생할 경우 연쇄적 반응(**이벤트의 전파**)이 일어난다.
  - 캡처링: 이벤트가 부모 요소부터 시작하여 이벤트를 발생시킨 자식 요소까지 도달
  - 버블링:  자식 요소에서 발생한 이벤트가 부모 요소로 전파



- 버블링으로 인해 원치 않은 이벤트가 발생한다면?
  - **`event.target`**
    - 이벤트가 발생한 가장 안쪽의 요소
    - 이벤트 발생 자체는 막을 수 없지만, `event.target`이나 `event.currentTarget`으로 조건을 걸어서 함수의 실행을 막을 수 있다.
  - `event.stopPropagation()`
    - 이 메소드를 호출하면, 버블링 단계에서 상위로 가는 이벤트 전파를 막을 수 있다.
    - 형제 이벤트 모두 실행, 부모 이벤트 전파 방지
  - `event.stopImmediatePropagation()`
    - 이 메소드를 호출하면, 같은 요소의 다른 이벤트도 막고, 상위로 가는 이벤트도 막는다.
    - 형제 이벤트 모두 방지, 부모 이벤트 전파 방지
  - `event.preventDefault()`
    - 이벤트 전파 뿐만 아니라, 동작 자체를 취소한다.



# 3. 기타

- Event 유형: https://developer.mozilla.org/en-US/docs/Web/Events
- 이벤트
  - https://developer.mozilla.org/ko/docs/Web/API/EventTarget/addEventListener
  - https://developer.mozilla.org/ko/docs/Web/Events
  - https://developer.mozilla.org/ko/docs/Learn/JavaScript/Building_blocks/Build_your_own_function
- (심화) 애니메이션 - CSS
  - https://developer.mozilla.org/ko/docs/Web/CSS/CSS_Animations/Using_CSS_animations
  - https://web.dev/learn/css/animations/
  - https://web.dev/learn/css/transitions/

- https://inpa.tistory.com/entry/JS-%F0%9F%93%9A-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%F0%9F%92%AF-%EC%B4%9D-%EC%A0%95%EB%A6%AC