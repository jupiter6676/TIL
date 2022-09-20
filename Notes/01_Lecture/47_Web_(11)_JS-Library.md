# 1. 실습 해설

- HTML

  ```html
  <form id="form" action="">
      <input type="password" name="password" id="password">
      <input type="password" name="password_confirmation" id="password_confirmation">
      <button type="submit">제출</button>
  </form>
  ```

- JS

  ```js
  const form = document.querySelector('#form');
  form.addEventListener('submit', function(e) {
      e.preventDefault();	// 이걸 해야 아래가 실행됨.
      
      // FormData 객체는 요소를 form으로
      const formData = new FormData(form);
      console.log(formData);	// 배열이 아닌 별도의 객체이기 때문에. 반복을 통해 요소를 조회해야 한다.
      // 아래는 id가 아닌, name을 통해 값을 가져온다.
    	console.log(formData.get('password'));
      console.log(formData.get('password_confirmation'));
  });
  ```



# 2. JS Library 활용

- SWIPER
- lodash

- [실습] 로또

  - 대략적 코드 (구체적인 건 9/20일자 실습 코드에 작성)

  - CSS

    ```css
    .ball-container {
        display: flex;
    }
    
    .ball {
        width: 10rem;
        height: 10rem;
        margin: 1rem;
        border-radius: 50%;
        background-color: yellow;
        /* 콘텐츠 중앙, 수직 정렬 */
        text-align: center;
        line-height: 10rem;
        /* 폰트 */
        font-size: xx-large;
        font-weight: bold;
    }
    ```

  - HTML

    ```html
    <h1>로또 추천 번호</h1>
    <button id="btn-lotto">번호 받기</button>
    
    <div id="result"></div>
    
    <div class="ball-container">
        <div class="ball">5</div>
    	<div class="ball">12</div>
        <div class="ball">12</div>
        <div class="ball">12</div>
        <div class="ball">12</div>
        <div class="ball">12</div>
    </div>
    
    <!-- lodash -->
    <script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
    ```

  - JS

    ```js
    const button = document.querySelector('#btn-lotto');
    button.addEventListener('click', function() {
        // 컨테이너를 만들고
    	const ballContainer = document.createElement('div');
        ballContainer.classList.add('ball-container');
        // 공을 만들어서 (6개)
        const numbers = _.sampleSize(_.range(1, 46), 6);	// 랜덤 숫자 6개(lodash)
        const ball = document.createElement('div');
        ball.classList.add('ball');
        ball.innerText = numbers[0];
        // 컨테이너에 붙인다.
        ballContainer.appendChild(ball);
        // 컨테이너를 결과 영역에 붙인다.
        const result = document.querySelector('#result');
        result.appendChild(ballContainer);
    });
    ```

    