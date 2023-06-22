# 1. Asynchronous JavaScript

비동기: 요청을 보낸 후 응답이 오기 전에 다른 일을 한다.

## (1) 비동기식

- 병렬적 Task 수행
- 요청을 보낸 후, 응답을 기다리지 않고 다음 동작이 이루어진다. (Non-blocking)



```js
const request = new XMLHttpRequest();
const URL = 'https://jsonlaceholder.typicode.com/todos/1/';

request.open('GET', URL);
request.send();	// XMLHttpRequest 요청

const todo = request.response	// 빈 응답 값을 todo에 할당
console.log('data: ${todo}')	// console.log 실행
```

- XMLHttpRequest 요청을 보낸 후, 응답을 기다리지 않고 다음 코드가 실행된다. (언제 응답을 받는지 알 수 X)

- 결과적으로 변수 todo에는 응답 데이터가 할당되지 않고 빈 문자열이 출력된다.

- 그렇다면 JS는 왜 기다려주지 않는 방식으로 동작할까?

  → JavaScript는 single threaded



## (2) JS의 동작 원리

> JS는 단일 스레드 기반 → 동시에 하나의 작업만을 처리한다. 하지만 어떻게 동시성을 지원할까?

- JS의 엔진 구조
  - `Memory Heap`: 메모리 할당이 일어나는 곳
  - `Call Stack`: 코드 실행에 따라 스택 프레임이 쌓이는 곳 (이것이 1개 → 단일 스레드)
- JS의 런타임(동작 환경)
  - JS의 엔진을 구동하는 환경(웹 브라우저, node.js)에서는 여러 개의 스레드가 사용된다.
  - 이러한 구동환경에서 자바스크립트 엔진과 상호 연동하기 위해 사용하는 장치가 `Event loop`이다.
  - `Web APIs`: DOM, AJAX, Timer 등 브라우저에서 제공하는 API
  - `Callback Queue`: 콜백 함수들이 대기하는 곳
  - `Event Loop`: callback queue에 대기 중인 콜백 함수가 있다면, call stack이 비워질 때마다 callback 함수를 call stack에 보내준다.

- [예시]

  ```js
  // 1
  console.log("1");
  
  // 2
  setTimeout(function timeout() {
      console.log("2");
  }, 2000);
  
  // 3
  console.log("3");
  ```

  1. Call Stack에 1이 쌓이고, 빠지면서 1이 출력된다.
  2. Call Stack에 2가 쌓이고, 빠지면서 Web Apis에 들어간다.
  3. Call Stack에 3이 쌓이고, 빠지면서 3이 출력된다.
     - 파이썬에서는 2가 끝난 후 3이 출력된다.
  4. Web Apis에서 시간이 다 되면, timeout()이 Callback Queue에 들어간다.
  5. Call Stack이 비어있으면, Callback Queue의 timeout()을 Call Stack에 넣고, 2를 출력한다.



## (3) Event Loop 기반 동시성 모델

- Call Stack
  - 요청이 들어올 때마다, 해당 요청을 순차적으로 처리하는 Stack(LIFO) 형태의 자료구조
- Web API (Browser API)
  - JavaScript 엔진이 아닌, 브라우저 영역에서 제공하는 API
  - ex) setTimeout(), DOM events, AJAX
- Task Queue (Event Queue, Message Queue)
  - 비동기 처리된 Callback 함수가 대기하는 Queue(FIFO) 형태의 자료구조
  - Main thread가 끝난 후 실행되어, 후속 JavaScript 코드가 차단되는 것을 방지
- Event Loop
  - Call Stack이 비어있는지 확인
  - 비어있는 경우, Task Queue에서 실행 대기 중인 Callback 함수가 있는지 확인
  - Task Queue에 대기 중인 Callback 함수가 있다면, 가장 앞에 있는 Callback 함수를 Call Stack으로 push



# 2. Axios

## (1) AJAX

- Asynchronous JavaScript And XML (비동기식 JS와 XML)
- 비동기 통신을 이용하면 화면 전체를 새로고침 하지 않아도, 서버로 요청을 보내고 데이터를 받아서 화면의 일부분만 업데이트할 수 있다.
- 이러한 '비동기통신 웹 개발 기술'을 AJAX라 한다.
- 비동기 웹 통신을 위한 라이브러리 중 하나가 Axios
- 특징
  - 페이지 전체를 reload(새로고침) 하지 않고서도 수행되는 **비동기성**
  - 서버의 응답에 따라, 전체 페이지가 아닌 일부분만을 업데이트할 수 있다.
    - 페이지 새로고침 없이 서버에 요청
    - 서버로부터 응답을 받아 작업을 수행



## (2) Axios

```js
axios.get('https://google.com')	// Promise return
	.then(...)
    .catch(...)
```

- "Promise based HTTP client for the browser and Node.js"
- 브라우저를 위한 Promise 기반의 클라이언트
  - Promise: 요청을 받아서, 도착하면 실행시켜 주겠다는 약속
- 원래는 "XHR" 이라는 브라우저 내장 객체를 활용해 AJAX 요청을 처리하는데, 이보다 편리한 AJAX 요청이 가능하도록 도움을 준다.
  - 확장 가능한 인터페이스와 함께, 패키지로 사용이 간편한 라이브러리를 제공한다.



## (3) Promise

- 비동기 작업을 관리하는 객체
  - 미래의 완료 또는 실패와 그 결과 값을 나타낸다.
  - 미래의 어떤 상황에 대한 약속
- 성공(이행)에 대한 약속 → `.then(callback)`
  - 이전 작업(promise)이 성공했을 때(이행했을 때) 수행할 작업을 나타내는 callback 함수
  - 그리고 각 callback 함수는 이전 작업의 성공 결과를 인자로 전달 받는다.
  - 따라서 성공했을 때의 코드를 callback 함수 안에 작성한다.
- 실패(거절)에 대한 약속 → `.catch(callback)`
  - `.then()`이 하나라도 실패하면(거부 되면) 동작한다. (동기식의 'try - except' 구문과 유사)
  - 이전 작업의 실패로 인해 생성된 error 객체는 catch 블록 안에서 사용할 수 있다.

- `.finally(callback)`
  - Promise 객체를 반환한다.
  - 결과와 상관없이 무조건 지정된 callback 함수가 실행된다.
  - 어떠한 인자도 전달받지 않는다.
    - Promise가 성공되었는지 거절되었는지 판단할 수 없기 때문
  - 무조건 실행되어야 하는 절에서 활용한다.
    - `.then()`과 `.catch()` 블록에서의 코드 중복을 방지



- 각각의 `.then()` 블록은 서로 다른 promise를 반환한다.
  - `.then()`을 여러 개 사용(chaining)하여 연쇄적인 작업을 수행할 수 있다.
  - 결국 여러 비동기 작업을 차례대로 수행할 수 있다는 뜻
- `.then()`과 `.catch()` 메서드는 모두 promise를 반환하기 때문에 chaining 가능
- 주의
  - 반환 값이 반드시 있어야 한다.
  - 없다면 callback 함수가 이전의 promise 결과를 받을 수 없다.



- `.then()`을 여러 번 사용하여 여러 개의 callback 함수를 추가할 수 있다. (Chaining)
- callback 함수는 JavaScript의 Event Loop가 현재 실행 중인 Call Stack을 완료하기 이전에는 절대 호출되지 않는다.
  - Promise callback 함수는 Event Queue에 배치되는 엄격한 순서로 호출된다.
  - 비동기 작업이 성공하거나 실패한 뒤에 `.then()` 메소드를 이용한 경우도 마찬가지



# 3. 비동기(Async) 적용하기

## (1) 팔로우 (follow) ①

1. axios CDN 작성

   ```html
   <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
   ```



2. form 요소 선택을 위해, id 속성 지정 및 선택

   ```html
   <form id="follow-form">
       ...
   </form>
   ```

   ```html
   <script>
   	const form = document.querySelector('#follow-form');
   </script>
   ```

   - 불필요해진 action과 method 속성은 삭제
   - 요청이 axios로 대체되기 때문



3. form 요소에 이벤트 핸들러 작성 및 submit 이벤트 취소

   ```html
   <script>
       const form = document.querySelector('#follow-form');
   
       form.addEventListener('submit', function (event) {
       	event.preventDefault();
       });
   </script>
   ```



4. axios 요청 준비

   ```html
   <script>
       const form = document.querySelector('#follow-form');
   
       form.addEventListener('submit', function (event) {
       	event.preventDefault();
           
           axios({
           	method: 'post',
           	url: '/accounts/${???}/follow/',
       	});
       }); 
   </script>
   ```

   - 현재 axios로 POST 요청을 보내기 위해 필요한 것
     - **url에 작성할 user pk는 어떻게 작성해야 할까?**
     - csrftoken은 어떻게 보내야 할까?



5. url에 작성할 user pk 가져오기 (HTML → JavaScript)

   ```html
   <form id="follow-form" data-user-id="{{ person.pk }}">
   	...
   </form>
   ```

   ```html
   <script>
   	const form = document.querySelector('#follow-form');
       
       form.addEventListener('submit', function (event) {
       	event.preventDefault();
       
       	const userId = event.target.dataset.userId;
       	...
       });
   </script>
   ```

   - **data-* attributes**

     - 사용자 지정 데이터 특성을 만들어, 임의의 데이터를 HTML과 DOM사이에서 교환 할 수 있는 방법

     - 사용 예시

       ```html
       <div data-my-id="my-data"></div>
       
       <script>
       	const myId = event.target.dataset.myId;
       </script>
       ```

     - 모든 사용자 지정 데이터는 dataset 속성을 통해 사용할 수 있다.

     - [https://developer.mozilla.org/ko/docs/Web/HTML/Global_attributes/data-*](https://developer.mozilla.org/ko/docs/Web/HTML/Global_attributes/data-*)

   - 예를 들어 `data-test-value` 라는 이름의 특성을 지정했다면, JavaScript에서는 `element.dataset.testValue`로 접근할 수 있다.

   - 속성명 작성 시 주의사항

     - 대소문자 여부에 상관없이 xml로 시작하면 X
     - 세미콜론을 포함해서는 X
     - 대문자를 포함해서는 X



6. url 작성 마치기

   ```html
   <script>
       const form = document.querySelector('#follow-form');
   
       form.addEventListener('submit', function (event) {
       	event.preventDefault();
           const userId = event.target.dataset.userId;
           
           axios({
           	method: 'post',
           	url: '/accounts/${userId}/follow/',
       	});
       }); 
   </script>
   ```

   

7. 우선 csrf 값을 가진 input 태그 선택하기

   ```html
   <script>
   	const form = document.querySelector('#follow-form');
   	const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
   </script>
   ```



8. AJAX로 csrftoken을 보내기

   ```html
   <script>
       const form = document.querySelector('#follow-form');
       const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
   
       form.addEventListener('submit', function (event) {
       	event.preventDefault();
           const userId = event.target.dataset.userId;
           
           axios({
           	method: 'post',
           	url: '/accounts/${userId}/follow/',
               headers: {'X-CSRFToken': csrftoken,}
       	});
       }); 
   </script>
   ```



## (2) 팔로우 (follow) ②

- 팔로우 버튼을 토글하기 위해서는, 현재 팔로우가 된 상태인지 확인이 필요
- axios 요청을 통해 받는 response 객체를 활용해, view 함수를 통해서 팔로우 여부를 파악할 수 있는 변수를 담아 JSON 타입으로 응답하기



1. 팔로우 여부를 확인하기 위한 is_followed 변수 작성 및 JSON 응답

   ```python
   # accounts/views.py
   
   @require_POST
   def follow(request, user_pk):
       # 1. 요청 보낸 유저가 로그인했는지
   	if request.user.is_authenticated:
   		User = get_user_model()
   		me = request.user
   		you = User.objects.get(pk=user_pk)
           
           # 2. 로그인 한 유저와 팔로우를 할 유저가 같지 않은지
   		if me != you:
               # 3. 이미 팔로우를 했는지
   			if you.followers.filter(pk=me.pk).exists():
   				you.followers.remove(me)
   				is_followed = False	# 추가
   			else:
   				you.followers.add(me)
   				is_followed = True	# 추가
                   
               context = {
               	'is_followed': is_followed,
               }
               
   			return JsonResponse(context)
           
   		return redirect('accounts:profile', you.username)	# 2
       
   	return redirect('accounts:login')	# 1
   ```

   ```html
   <script>
   	...
           
       axios({
           method: 'post',
           url: '/accounts/${userId}/follow/',
           headers: {'X-CSRFToken': csrftoken,}
       })
       .then(response => {
           const = isFollowed = reponse.data.is_followed;
           const followBtn = document.querySelector('#follow-form > input[type=submit]');
           
           if (isFollowed === true) {
   			followBtn.value = '언팔로우’;
   		} else {
   			followBtn.value = '팔로우’;
   		}
       });
   </script>
   ```



# 4. 기타

- CDN, JS는 항상 CDN을 활용하거나, 해당 파일을 불러와야 한다.
  - npm을 활용해서 node 환경에서 개발하는 것은, 지금 하는 것과 전혀 다르다.
  - 반드시 CDN으로 해야 한다.
  - JS 개발 환경이 아니라서, 나중에 react, vue를 배울 때도 axios를 쓰고, 그때 하는 것이 npm

- Python의 객체, 데이터와 JS의 객체, 데이터는 다 다르다.
  - 그런데 데이터를 주고받을 수 있는 이유? JSON 통용되는 표준 체계가 있기 때문.
  - JSON은 문자열. 이걸 본인들의 객체 세계에 맞춰서 해석하는 것. JSON을 Python은 리스트 속 딕셔너리. JS는 배열 속 오브젝트의 형태로 해석 및 변환한다. 그리고 이런 식으로 변환하는 것을 파싱이라고 한다.
  - 시간은 Epoch Time 사용



- 기존에는
  1. 링크, 버튼, url 등등을 조작하면
  2. 서버에서 요청을 받아서
  3. HTML 혹은 redirect로 응답

- 비동기는
  1. 링크, 버튼, url 등등을 조작하면, **이벤트가 발생하여 axios 요청**
  2. 서버에서 요청을 받아서
  3. **응답을 JSON**으로 하고, 그 다음 .then 메소드 안에서 **DOM으로 화면 일부를 변경**시키는 수작업을 한다.



- 좋아요 토글

  ```html
  event.target.classList.toggle('bi-heart')
  event.target.classList.toggle('bi-heart-fill')
  ```

  

- 댓글

  ```html
  <script>
  	const commentForm = document.querySelector('#comment-form');
      const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
      
      commentForm.addEventListener('submit', function(event) {
  		event.preventDefault();
          axios({
              method: 'post',
              url: '/articles/${event.target.dataset.articleId}/comments/',
              headers: {'X-CSRFToken': csrftoken},
              data: new FormData(commentForm)
          })
          .then(response => {
              // 댓글을 추가하는 로직
              const comments = document.querySelector('#comments');
              const p = document.createElement('p');
              p.innerText = '${response.data.userName} | ${response.data.content}';
              const hr = document.createElement('hr');
              comments.append(p, hr) ;
              commentForm.reset();
          });
      });
  </script>
  ```

  - 이거 1인 서비스 X. 그 사이에 댓글이 엄청 달리면?
  - Article.comment.all()을 JSON으로 바꿔서 보내고, 기존 걸 없애고 이걸 반복해서 댓글창에 붙이면 된다..



# 5. 자료

- JavaScript  비동기 처리
  - 비동기 처리 필요성
  - 비동기 처리 원리와 과정
  - [자바스크립트 비동기 처리와 콜백 함수](https://joshua1988.github.io/web-development/javascript/javascript-asynchronous-operation/)
  - [[자바스크립트] 비동기 처리 1부 - Callback](https://www.daleseo.com/js-async-callback/)