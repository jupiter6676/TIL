# 1. JavaScript가 뭔가요?

> https://developer.mozilla.org/ko/docs/Learn/JavaScript/First_steps/What_is_JavaScript

## (1) 웹 페이지에 JavaScript 넣기

1. 내부 JavaScript

   - `<script>...</script>` 코드를 닫는 `</head>` 태그 바로 앞에 넣기

     ```html
     <head>
         ...
         ...
         <script>
         	// JavaScript goes here
         </script>
     </head>
     ```

2. 외부 JavaScript

   - 확장자가 `.js`인 파일을 만들고, 그 안에 스크립트를 짠다.

   - 위의 `<script>` 요소를 다음과 같이 대체한다.

     ```html
     <head>
         ...
         ...
         <script src="~~~.js" defer></script>
     </head>
     ```

3. 인라인 JavaScript 처리기

   - `<button>`의 `onclick`과 같은 것. 하지만 권장되지 X.
   - 대신 `addEventListener`를 사용한다.



## (2) 스크립트 로딩 전략

- JavaScript를 사용해서 페이지 내의 요소(DOM)를 조작하려 할 때, HTML 코드보다 JavaScript를 먼저 불러와 버리면 코드가 올바르게 동작하지 못한다.
- 앞선 내부와 외부 JS 예제에서는 HTML 본문을 읽기 전, 문서의 헤드에서 JS를 불러와 실행한다. 여기서 문제가 생길 수 있다.



- 내부 JS에서 예방할 수 있는 방법

  ```js
  document.addEventListener('DOMContentLoaded', () => {
      ...
  });
  ```

  - 이것은 HTML 본문 전체를 불러와 읽었다는 것을 나타내는, 브라우저 `DOMContentLoaded` 이벤트를 수신하는 수신기이다.
  - 이 블록 내부의 JS는 이 이벤트가 발생하기 전에는 실행되지 않으므로, 로딩 시점으로 인한 오류를 예방할 수 있다.

- 외부 JS에서 예방할 수 있는 방법

  ```html
  <script src="script" defer></script>
  ```

  - `defer` 특성은 브라우저가 `<script>` 태그를 마주쳐도, 그 이후의 HTML 콘텐츠를 계속 불러오도록 지정한다.
  - 이렇게 하면 스크립트와 HTML을 동시에 불러오므로, 오류가 발생하지 않는다.

- 고전적 방법

  - 스크립트 요소를 본문의 맨 마지막(`</body>` 태그 바로 앞)에 배치하는 것
  - 성능 저하의 문제가 발생할 수 있다.

- `defer` vs. `async`
  - `async`
    - 스크립트를 가져오는 동안에도 페이지 로딩을 중단하지 않는다.
    - 스크립트가 다운되면 바로 실행되는데, 이때는 페이지 렌더링이 중단된다.
    - 스크립트의 실행 순서를 보장할 방법이 없다. 따라서 다른 스크립트에 의존하지 않는 독립 스크립트에 사용해야 한다.
    - 다수의 백그라운드 스크립트를 최대한 빠르게 불러와야 할 때 사용한다.
  - `defer`
    - 스크립트를 가져오는 동안에도 페이지 로딩을 중단하지 않는다.
    - 스크립트를 배치한 순서대로 불러온다.
    - 페이지 콘텐츠를 모두 불러오기 전까지는 실행하지 않으므로, DOM 작업을 하는 스크립트에 유용하다.



# 2. 문법과 자료형

## (1) 변수 선언

- 변수
  - 변수명은 식별자(Identifiers)라 불리며, 특정 규칙을 따른다.
  - JS 식별자는 문자, 밑줄(`_`), 달러 기호(`$`)로 시작해야 한다. 이후에는 숫자가 와도 O.
  - JS는 대소문자를 구분한다.

- 선언
  1. `var`: 변수를 선언하는 동시에 값을 초기화
  2. `let`: 블록 스코프 내 지역 변수를 선언하는 동시에 값을 초기화
  3. `const`: 블록 스코프 내 읽기 전용 상수를 선언
- 변수 선언
  - `var x = 42` → `var` 키워드로 실행 맥락에 따라 **지역 및 전역 변수**를 선언
  - `let x = 42` → `const` 혹은 `let` 키워드로 실행 맥락에 따라 **지역 변수**를 선언
  - 구조 분해 할당 구문



## (2) 변수 할당

- 초기 값 없이 `var` 혹은 `let` 문으로 선언된 변수는 `undefined` 값을 갖는다.
- `undefined`
  - Boolean 맥락에서 `false`로 동작
  - 수치 맥락에서 `NaN`으로 변환
- `null`
  - Boolean 맥락에서 `false`로 동작
  - 수치 맥락에서 `0`으로 변환



## (3) 변수 호이스팅(Hoisting)

- JS 변수는 나중에 선언된 변수를 참조할 수 있다.

- 하지만 끌어올려진 변수는 `undefined` 값을 반환한다.

  ```js
  console.log(x === undefined);	// true
  var x = 3
  ```

- 변수를 사용하거나, 참조한  후에 선언 및 초기화하더라도, 여전히 `undefined`를 반환한다.

  ```js
  var myvar = "my value";
  
  (function() {
      console.log(myvar);	// undefined
      var myvar = "local value";
  })();
  ```

- 이 때문에, 함수 내의 모든 `var`문은 함수 상단 근처에 두는 것이 좋다.

- `let`과 `const`는 변수를 상단으로 끌어올리지만, 초기화하지 않는다. 따라서 변수가 선언되기 전에 블록 안에서 변수를 참조하면 `ReferenceError`를 발생시킨다.



## (4) 함수 호이스팅

- 함수 선언으로는 호이스팅되지만, 함수 표현식으로는 호이스팅되지 않는다.

- 함수 선언

  ```js
  foo();	// "bar"
  
  function foo() {
      console.log('bar');
  }
  ```

- 함수 표현식

  ```js
  baz();	// TypeError: baz is not a function
  
  var baz = function() {
      console.log('bar2');
  };
  ```



## (5) 상수

- `const` 키워드로 읽기 전용 상수를 만든다.

- 스크립트가 실행 중인 동안 대입을 통해 값을 바꾸거나, 재선언될 수 없다.

- 스코프 규칙은 `let` 블록 스코프 변수와 동일하다.

- 같은 스코프에 있는 함수나 변수와 같은 이름으로 선언할 수 없다.

- 그러나, 상수에 할당된 객체나 배열의 내용은 보호되지 않아서, 값을 변경할 수 있다.

  ```js
  const MY_ARRAY = ['HTML','CSS'];
  MY_ARRAY.push('JAVASCRIPT');
  console.log(MY_ARRAY); //logs ['HTML','CSS','JAVASCRIPT'];
  ```



## (6) 데이터 구조 및 데이터 형

- 데이터 형
  - Boolean
  - null: null 값을 나타내는 특별한 키워드
  - undefined: 값이 정의되어 있지 않은 최상위 속성
  - Number: 정수 또는 실수
  - BigInt
  - String
  - Symbol: 인스턴스가 고유하고 불변인 데이터 형
  - Object
- 변수를 선언할 때 데이터 형을 지정할 필요가 없고, 스크립트 실행 도중 필요에 의해 형 변환이 이루어질 수 있다.



- 숫자와 `+` 연산자

  - 숫자와 문자열 값 사이에 `+` 연산자를 포함한 식에서, JS는 숫자를 문자열로 변환한다.

    ```js
    x = 'The answer is ' + 42	// "The answer is 42"
    y = 42 + ' is the answer'	// "42 is the answer"
    ```

  - 다른 연산자를 포함한 식은 숫자를 문자열로 변환하지 않는다.

    ```js
    '37' - 7	// 30
    '37' + 7	// "377"
    ```

- 문자열을 숫자로 변환하기

  - `parseInt()`: 오직 정수만 반환한다. 진법(Radix) 매개변수를 포함해야 한다.

    ```js
    parseInt('101', 2)	// 5
    ```

  - `parseFloat()`



## (7) 리터럴

1. 배열 리터럴

   - `Array` 객체

   - 0개 이상의 식(expression) 목록

   - 각 식은 배열 요소를 나타내고, 대괄호로 묶인다.

   - 아래는 요소가 3개로, `length`가 3인 `coffees` 배열을 만든다

     ```js
     let coffees = ['French Roast', 'Colombian', 'Kona']
     ```

   - 추가 쉼표
     - 잇달아 두 개의 쉼표를 두면, 지정되지 않은 요소를 `undefined`로 채운다.
     - 만약 요소 맨 마지막을 후행 쉼표로 끝낸다면, 그 쉼표는 무시된다. (제거하는 것이 좋다.)
     - 코드를 작성할 땐 명시적으로 빠진 요소의 값을 `undefined`로 선언하는 것이 좋다.

2. 불리언 리터럴

3. 숫자 리터럴

   - 정수 리터럴 (10진수, 16진수, 8진수, 2진수)

   - 부동 소수점 리터럴 (10진수)

4. 객체 리터럴

   - 중괄호로 묶인다.

   - 문(statement)의 시작에 객체 리터럴을 사용하면 안 된다.

     ```js
     var sales = 'Toyota';
     
     function carTypes(name) {
       if (name === 'Honda') {
         return name;
       } else {
         return "Sorry, we don't sell " + name + ".";
       }
     }
     
     // 속성이 myCar, getCar, special인 객체
     var car = { myCar: 'Saturn', getCar: carTypes('Honda'), special: sales };
     
     console.log(car.myCar);   // Saturn
     console.log(car.getCar);  // Honda
     console.log(car.special); // Toyota
     ```

   - 속성명으로 숫자나 문자열 리터럴을 사용하거나, 객체 리터럴 속 객체를 중첩할 수 있다.

   - 속성명이 유효한 식별자나 숫자가 아닌 경우는 따옴표로 묶여야 한다.

     - 이 경우 접근을 `.`으로 할 수 없고, `[]`로 접근하여야 한다.

5. 정규식 리터럴

6. 문자열 리터럴: 큰 따옴표, 작은 따옴표로 묶인 0개 이상의 문자

   - `\0`: Null Byte
   - `\n`: New line
   - `\t`: tab 등
   - 문자 이스케이프: `\`를 통해서