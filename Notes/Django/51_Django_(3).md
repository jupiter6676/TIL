# 1. Variable routing

## (1) 필요성

> 템플릿의 많은 부분이 중복되고 일부분만 변경되는 상황에서, 비슷한 URL과 템플릿을 계속 만들어야 할까?

- Variable routing은 URL 주소를 변수로 사용하는 것
- URL의 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있다.
- 즉, 변수 값에 따라 하나의 path()에 여러 페이지를 연결할 수 있다.



## (2) Variable router 작성

```py
# urls.py
urlpatterns = [
    ...,
    # path('hello/<str:name>/', views.hello)
    path('hello/<name>/', views.hello)
]
```

- 변수는 `<>`에 정의하며, view 함수의 인자로 할당된다.
- 기본 타입은 string이며, 5가지 타입으로 명시할 수 있다.
  - str: `/`를 제외하고 비어있지 않은 모든 문자열
  - int: 0 또는 양의 정수와 매치
  - slug
  - uuid
  - path



## (3) View 함수 작성

```py
# articles/views.py

def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'hello.html', context)
```

- variable routing으로 할당된 변수를 인자로 받고, 템플릿 변수로 사용할 수 있다.



# 2. Sending and Retrieving Form Data

- 데이터를 보내고 가져오기
- HTML form element를 통해, 사용자와 애플리케이션 간의 상호작용 이해하기



## (1) Client-Server Architecture

- 웹은 기본적으로 클라이언트-서버 아키텍처를 사용
  - 클라이언트(일반적으로 웹 브라우저)가 서버에 요청을 보내고, 서버는 클라이언트의 요청에 응답
- 클라이언트 입장에서, HTML form은 HTTP 요청을 서버에 보내는 가장 편리한 방법
- 이를 통해 사용자는 HTTP 요청에서 전달할 정보를 제공할 수 있다.



## (2) Sending form data (Client)

1. HTML `<form>` element

   - 데이터가 전송되는 방법을 정의

   - 웹에서 사용자 정보를 입력하는 여러 방식(text, button, submit 등)을 제공하고, **사용자로부터 할당된 데이터를 서버로 전송**하는 역할을 담당

   - 데이터를 어디(action)로 어떤 방식(method)으로 보낼지

   - 핵심 속성: `action`, `method`

   

   - `action`
     - 입력 데이터가 전송될 URL을 지정
     - 데이터를 어디로 보낼 것인지 지정하는 것이며, 이 값은 반드시 유효한 URL이어야 한다.
     - 만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내진다.

   - `method`
     - 데이터를 어떻게 보낼 것인지 정의
     - 입력 데이터의 HTTP request methods를 지정
     - HTML form 데이터는 2가지 방법으로만 전송할 수 있다.
       - GET, POST 방식



2. HTML `<input>` element

   - 사용자로부터 데이터를 입력받기 위해 사용
   - `type` 속성에 따라 동작 방식이 달라진다.
     - input 요소의 동작 방식은 type 특성에 따라 현격히 달라지므로, 각각의 type은 별도로 MDN 문서에서 참고하여 사용하도록 한다.
     - type을 지정하지 않은 경우, 기본값은 text
   - 핵심 속성: `name`

   

   - `name`
     - form을 통해 데이터를 제출(submit)했을 때 name 속성에 설정된 값을 서버로 전송하고, 서버는 name 속성 에 설정된 값을 통해 사용자가 입력한 데이터 값에 접근할 수 있다.
     - 주요 용도는 GET/POST 방식으로 서버에 전달하는 파라미터(name은 key, value는 value)로 매핑하는 것
       - GET 방식에서는 URL형식으로 데이터를 전달
       - '?key=value&key=value/'



3. HTTP request methods

   - HTTP: HTML 문서와 같은 리소스(데이터, 자원)들을 가져올 수 있도록 해주는 프로토콜(규칙, 규약)
   - 웹에서 이루어지는 모든 데이터 교환의 기초
   - HTTP는 주어진 리소스가 수행 할 원하는 작업을 나타내는 request methods를 정의
   - 자원에 대한 행위(수행하고자 하는 동작)을 정의
   - 주어진 리소스(자원)에 수행하길 원하는 행동을 나타낸다.
   - **GET**, POST, PUT, DELETE

   

   - `GET`
     - 서버로부터 정보를 조회(리소스를 요청)하는 데 사용
     - 데이터를 가져올 때만 사용해야 한다.
     - 데이터를 서버로 전송할 때, Query String Parameters를 통해 전송
     - 데이터는 URL에 포함되어 서버로 보내진다.
     - Query String Parameters
       - 사용자가 입력 데이터를 전달하는 방법 중 하나로, url 주소에 데이터를 파라미터를 통해 넘기는 것
       - 이러한 문자열은 앰퍼샌드(&)로 연결된 key=value 쌍으로 구성되며 기본 URL과 물음표(?) 로 구분된다.
       - http://host:port/path?key=value&key=value
       - Query String이라고도 한다.
       - 정해진 주소 이후에 물음표를 쓰는 것으로 Query String이 시작함을 알린다.
       - “key=value”로 필요한 파라미터의 값을 적는다.
       - 파라미터가 여러 개일 경우 “&”를 붙여 여러 개의 파라미터를 넘길 수 있다.



## (3) Retrieving the data (Server)

- 데이터 가져오기(검색하기)
- 서버는 클라이언트로 받은 key-value 쌍의 목록과 같은 데이터를 받게 된다.
- 이러한 목록에 접근하는 방법은 사용하는 특정 프레임워크에 따라 다르다.
- 우리는 Django 프레임워크에서 어떻게 데이터를 가져올 수 있을지 알아볼 것 
- throw가 보낸 데이터를 catch에서 가져오기
  - GET method로 보내고 있기 때문에, 데이터는 URL에 포함되어 서버에 보내진다.
  - 그러면 우리가 작성해야 하는 view 함수에서는 해당 데이터에 어떻게 접근해야 할까?
  - → 모든 요청 데이터는 view 함수의 첫 번째 인자 **`request`**에 들어있다.

