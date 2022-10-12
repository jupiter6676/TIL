# 1. Auth QnA

1. 왜 Django 내부의 auth.User를 사용하지 않고 accounts.User를 만들고 시작하나요?
   - 우리가 했던 것
     - settings.py: AUTH_USER_MODEL 변경
     - accounts 앱에 AbstractUser를 상속받아 빈 껍데기(pass) 생성
   - Model은 DB를 조작하는 것과 밀접한 관계를 가지고 있다.
   - 모델의 필드가 수정되거나 하는 것들은 마이그레이션 파일 등을 통해서 자동으로 관리할 수 있는데, 모델 자체가 변화하고 나면 별도의 수작업이 필요하다.
   - 따라서 프로젝트 중반에 모델을 변경하게 된다면, 문제가 발생할 수 있기 때문에 시작 시 미리 커스텀 해둘 필요가 있다.



2. 그러면 왜 AbstractUser를 상속받나요? User를 상속받으면 안 되나요?
   - User를 똑같이 쓰고 싶은데 User를 User로 상속받는 게 아니라, 그냥 User가 상속받고 있는 걸 받으면 된다.



3. UserCreationForm을 해서 어떻게 이용할 수 있나요?
   - UserCreationForm → ModelForm을 상속받아서 만들고 있다. ✨✨
   - 우리가 ModelForm을 정의할 때 가장 중요했던 설정은 무엇이었을까?
     - Meta의 model과 fields
   - UserCreationForm의 model은 django.contrib.auth.models의 User를 import한 것인데, 이걸 가져와서 accounts User로 커스텀해야 한다. (AUTH_USER_MODEL에 accounts User 쓴다고 했는데 그냥 UserCreationForm를 쓰면 오류가 뜬다.)
   - model에 클래스 정의하면, 클래스 변수에 해당하는 것은 필드였다. ModelForm에 클래스를 정의하면, 클래스 변수에 해당하는 것은 HTML 필드이다.
   - UserCreationForm, ModelForm은 **상속 관계**에 있다. 부모 클래스에 정의된 속성과 메소드(기능)를 상속받아서, ModelForm의 기본 기능을 구현할 수 있다.
   - 가령, ModelForm는 reqeuest.POST의 값을 가져와서 Meta의 model과 field에 값을 저장하고, is_valid() 체크도 하는 방식으로 동작한다.
   - 따라서 ModelForm을 상속받은 UserCreationForm 등은 model과 filed를 직접 지정해서 사용할 수 있는 것



4. User를 변경 vs 게시글 변경
   - User는 보통 기본 정보 변경과 별도로 암호 변경 기능을 제공한다.
   - UserChangeForm과 SetPasswordForm이 따로 존재한다.
   - 전자는 ModelForm, 후자는 Form을 상속받는다.
   - ModelForm은 CRUD를 생각하면 되고, 비밀번호는 그 외의 기능이 필요할 테니 Form을 사용하는 거라고 생각하자.



5. get_user_model의 사용 이유는 무엇인가요?
   - User 모델은 결국 변경이 가능한 것이면서, Django와 사용자가 사용하는 것.
   - 변경 가능한 것은 변수화 등을 통해 호출하는 것이 가장 좋다.
   - 이는 모든 개발 영역에서의 핵심을 관통하는 내용
   - URL도 마찬가지로, url에 name을 붙여두는 변수화를 통해 함수에서 사용했다.
   - 그래서 User 모델 클래스는 어딘가에 있겠지만, 이걸 get_user_model()을 호출해서 쓰면 알아서 AUTH_USER_MODEL에 정의된 클래스를 준다.



# 2. 로그인에 대한 이해

## (1) HTTP

- Hyper Text Transfer Protocol
- HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 프로토콜(규칙, 규약)
- 웹(WWW)에서 이루어지는 모든 데이터 교환의 기초
- 클라이언트 - 서버 프로토콜이라고도 부름
- 요청과 응답
  - 요청(request): 클라이언트(브라우저)에 의해 전송되는 메시지
  - 응답(response): 서버에서 응답으로 전송되는 메시지




## (2) HTTP의 특징

- **비 연결 지향**(Connectionless)
  - 서버는 요청에 대한 응답을 보낸 후 연결을 끊는다.
  - 예를 들어, 우리가 네이버 메인 페이지를 보고 있을 때 우리는 네이버 서버와 연결되어 있는 것이 아니다.
  - 네이버 서버는 우리에게 메인 페이지를 보여주고 연결을 끊는다.
- **무상태**(Stateless)
  - 연결을 끊는 순간, 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않는다.
  - 클라이언트와 서버가 주고받는 메시지들은 서로 완전히 독립적이다.

- 그러면 어떻게 로그인 상태를 유지할까?
  - 그런데 우리가 로그인을 이용하고 웹 사이트를 사용할 때, 페이지를 이동해도 로그인 '상태'가 유지된다.
  - 서버와 클라이언트 간 지속적인 상태 유지를 위해, '**쿠키와 세션**'이 존재한다.



# 3. 쿠키(Cookie)🍪

## (1) 개념

- 서버가 사용자의 웹 브라우저(클라이언트)에 전송하는 작은 데이터 조각
- 사용자가 웹사이트를 방문할 경우, 해당 웹 사이트의 서버를 통해 사용자의 컴퓨터에 설치되는 작은 기록 정보 파일
  - 브라우저(클라이언트)는 로컬에 쿠키를 KEY-VALUE 데이터 형식으로 저장
  - 동일한 서버에 재요청 시 저장된 쿠키를 함께 전송
- 쿠키는 서로 다른 요청이 동일한 브라우저로부터 발생한 것인지 판단할 때 주로 사용된다.
  - 상태가 없는(stateless) HTTP에서 상태 정보를 관리하고, 사용자는 로그인 상태를 유지할 수 있다.
  - ex) 한 브라우저에서 네이버에 접속해 로그인을 한 뒤 '배너 하루 보지 않기'를 눌렀을 때, 다른 브라우저에서 네이버에 접속해 로그인하면 그 배너가 보인다.




## (2) 사용 목적

- 세션 관리 (Session management)
  - 로그인, 아이디 자동완성, 공지 하루 안 보기, 팝업 체크, 장바구니 등의 정보 관리
- 개인화 (Personalization)
  - 사용자 선호, 테마 등의 설정
- 트래킹 (Tracking)
  - 사용자 행동을 기록 및 분석



## (3) 세션(Session)

- 사이트와 특정 브라우저 사이의 상태(state)를 유지시키는 것
- 클라이언트가 서버에 접속하면 서버가 특정 session id를 발급하고, 클라이언트는 session id를 쿠키에 저장
  - 클라이언트가 다시 동일한 서버에 접속하면, 요청과 함께 쿠키(session id O)를 서버에 전달
  - 쿠키는 요청 때마다 서버에 함께 전송되므로, 서버에서 session id를 확인해 알맞은 로직을 처리
- session id는 세션을 구별하기 위해 필요하며, 쿠키에는 session id만 저장



## (4) 쿠키의 Lifetime(수명)

- Session cookie
  - 현재 세션(current session)이 종료되면 삭제된다.
  - 브라우저 종료와 함께 세션이 삭제된다.
- Persistent cookies
  - Expires 속성에 지정된 날짜, 혹은 Max-Age 속성에 지정된 기간이 지나면 삭제된다.



## (5) Session in Django

- Django는 database-backed sessions 저장 방식을 기본 값으로 사용한다.
  - session 정보는 Django DB의 `django_session` 테이블에 저장한다.
  - [설정을 통해 다른 저장 방식으로 변경 가능하다.](https://docs.djangoproject.com/en/3.2/topics/http/sessions/)
- Django는 특정 session id를 포함하는 쿠키를 사용해서, 각각의 브라우저와 사이트가 연결된 session을 확인한다.



# 4. Login

## (1) AuthenticationForm

- 로그인을 위한 built-in form
  - 로그인하고자 하는 사용자 정보(username, password)를 입력 받는다.
  
  - ModelForm이 아닌 일반 Form을 상속받고 있으며, `request`를 첫 번째 인자로 취한다.
  
  - https://docs.djangoproject.com/en/4.1/topics/auth/default/#django.contrib.auth.forms.AuthenticationForm
  
  - https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L174
  
  - views.py에 login 함수 작성
  
    ```python
    # accounts/views.py
    
    from django.contrib.auth.forms import AuthenticationForm
    
    def login(request):
        if request.method == 'POST':
            pass
        else:
            form = AuthenticationForm()
            
        context = {
            'form': form,
        }
        
        return render(request, 'accounts/login.html', context)
    ```



## (2) login()

- login(request, user, backend=None)
- 인증된 사용자를 로그인
  - 유저의 ID를 세션에 저장하여 세션을 기록
- HttpRequest 객체와 User 객체가 필요
  - 유저 정보는 반드시 인증된 유저 정보여야 한다.
  - authenticate() 함수를 활용한 인증
  - 혹은, AuthenticationForm을 활용한 is_valid



## (3) 로그인 로직 작성

- 일반적인 ModelForm 기반의 Create 로직과 동일하지만,

- ModelForm이 아닌 From으로, 필수 인자 구성이 다르다.

- DB에 저장하는 것 대신 세션에 유저를 기록하는 함수를 호출한다.
  - View 함수와 이름이 동일하기 때문에, 함수 이름을 변경하여 호출한다.
  - 로그인 URL이 '/accounts/login/'에서 변경되는 경우, settings.py의 LOGIN_URL을 변경하여야 한다.
  
- views.py에 login 함수 작성

  ```python
  # accounts/views.py
  
  from django.contrib.auth.forms import AuthenticationForm
  from django.contrib.auth import login as auth_login
  
  def login(request):
      if request.method == 'POST':
          form = AuthenticationForm(reqeust, data=request.POST)
          if form.is_valid():
              auth_login(request, form.get_user())	# save() X
              return redirect('articles:index')
      else:
          form = AuthenticationForm()
          
      context = {
          'form': form,
      }
      
      return render(request, 'accounts/login.html', context)
  ```

  

- `get_user()`
  - AuthenticationForm의 인스턴스 메소드
  - 유효성 검사를 통과했을 경우, 로그인 한 사용자 객체를 반환한다.
  - https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L244



# 5. Authentication with User

- 현재 로그인 되어있는 유저 정보 출력하기

  ```html
  <!-- base.html -->
  <body>
      <h1>Hello, {{ user }}</h1>
  </body>
  ```

- 어떻게 base 템플릿에서 context 데이터 없이 user 변수를 사용할 수 있는 걸까?

  - settings.py의 context processors 설정의 'django.contrib.auth.context_processors.auth'
  - context processors
    - 템플릿이 렌더링 될 때 호출 가능한 context 데이터 목록
    - 작성된 context 데이터는 기본적으로 템플릿에서 사용 가능한 변수로 포함된다.
    - 즉, Django에서 자주 사용하는 데이터 목록을 미리 템플릿에 로드해 둔 것
  - django.contrib.auth.context_processors.auth
    - 템플릿 변수 {{ user }}
    - 클라이언트가 로그인한 경우 User 클래스의 인스턴스
    - 클라이언트가 로그인하지 않은 경우 AnonymousUser 클래스의 인스턴스



# 5. Logout

## (1) logout()

- logout(request)

- 요청 유저에 대한 세션 정보를 삭제한다.

  - DB에서 session data 삭제
  - 클라이언트의 쿠키에서 session id 삭제

- HttpRequest 객체를 인자로 받고, 반환 값이 없다.

- 사용자가 로그인하지 않은 경우 오류를 발생시키지 않는다.

- views.py에 logout 함수 작성

  ```python
  # accounts/views.py
  
  from django.contrib.auth import logout as auth_logout
  
  def logout(request):
      auth_logout(request)
      return redirect('articles:index')
  ```



# 6. Limiting access to logged-in users

## (1) 개요

- 로그인 사용자의 접근 제한하기
- 2가지 방법
  - `is_authenticated` 속성을 활용한 조건문
  - `The login_required decorator`를 활용한 view 제한



## (2) is_authenticated

- User model의 속성(attributes) 중 하나

- 사용자가 인증되었는지 여부를 알 수 있는 방법

- 모든 User 인스턴스에 대해 항상 True인, 읽기 전용 속성

  - AnonymousUser에 대해서는 항상 False

- 일반적으로, `request.user`에서 이 속성을 사용한다.

  - request.user.is_authenticated

- 권한(permisson)과는 관련이 없으며, 사용자가 활성화 상태(active)이거나, 유효한 세션(valid session)을 가지고 있는지도 확인하지 않는다.

- https://github.com/django/django/blob/main/django/contrib/auth/base_user.py#L56



- is_authenticated 적용하기

  - 로그인과 비로그인 상태에서 출력되는 링크를 다르게 설정

    ```html
    <!-- base.html -->
    {% if request.user.is_authenticated %}
    	<!-- 로그아웃 form 태그 -->
        <form action="{% url 'accounts:logout' %}" method="POST">
            {% csrf_token %}
            <input type="submit" value="Logout">
        </form>
    	<!-- 회원 정보 수정 a 태그 -->
    	<!-- 회원 탈퇴 form 태그 -->
    {% else %}
    	<!-- 로그인 a 태그 -->
    	<!-- 회원 가입 a 태그 -->
    {% endif %}
    ```

  - 인증된 사용자라면 로그인 로직을 수행할 수 없도록 처리

    - 버튼을 없애도 URL을 직접 입력하면 게시글 작성 페이지로 갈 수 있기 때문에,

    - View에서의 처리도 반드시 필요하다.

      ```html
      <!-- articles/index.html -->
      {% extends 'base.html' %}
      
      {% block content %}
          {% if request.user.is_authenticated %}
              <!-- Create a 태그 -->
          {% else %}
              <!-- Login a 태그 -->
          {% endif %}
      {% endblock %}
      ```

      ```python
      # accounts/views.py
      def login(request):
          if request.user.is_authenticated:
              return redirect('articles:index')
          
          # ...
      ```



## (3) login_required

- login_required decorator
  - 사용자가 로그인 되어 있으면, 정상적으로 view 함수를 실행
  - 로그인 하지 않은 사용자의 경우, settings.py의 LOGIN_URL 문자열 주소로 redirect 
    - LOGIN_URL의 기본 값은 /accounts/login/



- 로그인 상태에서만 글을 작성/수정/삭제할 수 있도록 변경

  ```python
  from django.contrib.auth.decorators import login_required
  
  @login_required
  def create(request):
      pass
  ```



- login_required 적용 확인하기
  - /articles/create/로 브라우저에 직접 요청
  - 로그인 페이지로 리다이렉트 되는데, 이때의 URL을 확인해보면,
    - 인증 성공 시 사용자가 redirect 되어야하는 경로는 "next"라는 쿼리 문자열 매개 변수에 저장된다.
    - 예시) /accounts/login/?next=/articles/create/



- 'next' query string parameter 대응

  ```python
  # accounts/views.py
  
  def login(request):
      if request.user.is_authenticated:
          return redirect('articles:index')
      
      if request.method == 'POST':
          form = AuthenticationForm(request, request.POST)
          
          if form.is_valid():
              auth_login(request, form.get_user())
              
              # 1. 만약 로그인 안 한 채로 글 작성 페이지에 들어가면,
              # 로그인 페이지로 이동한 후
              # 로그인이 완료되면 다시 글 작성 페이지에 이동할 수 있도록 해준다.
              # 2. 1이 아니라면 메인 페이지로 이동한다.
              return redirect(request.GET.get('next') or 'articles:index')
  ```

- 'next' query string parameter 주의사항

  - 만약 login 템플릿에서 form action이 작성되어 있다면 동작하지 않는다.

  - 해당 action 주소가 next 파라미터가 작성 되어있는 현재 url이 아닌, /accounts/login/ 으로 요청을 보내기 때문

  - 다음과 같이 작성해준다.

    ```html
    <!-- accounts/login.html -->
    
    {% block content %}
        <h1>로그인</h1>
        <form action="" method="POST">
            {% csrf_token %}
            {{ form.as_p }}
            <input type="submit">
        </form>
    {% endblock content %}
    ```



# 7. 기타

- git-flow
  - https://ujuc.github.io/2015/12/16/git-flow-github-flow-gitlab-flow/
- kdt-live/01-django-modelform
  - https://github.com/kdt-live/01-django-modelform