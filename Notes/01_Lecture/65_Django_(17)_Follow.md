# 1. M:N (User-User)

## (1) Profile

1. url 및 view 함수 작성

   ```python
   # accounts/urls.py
   
   urlpatterns = [
   	# ...
   	path('profile/<username>/', views.profile, name='profile'),
   ]
   ```

   ```python
   # accounts/views.py
   
   from django.contrib.auth import get_user_model
   
   def profile(request, username):
       user = get_user_model()
       person = user.objects.get(username=username)
       
       context = {
           'person': person,
       }
       
       return render(request, 'accounts/profile.html', context)
   ```



2. profile 템플릿 작성

   ```html
   <!-- 유저가 쓴 게시글 -->
   {% for article in person.article_set.all %}
   	<div>{{ article.title }}</div>
   {% endfor %}
   
   <!-- 유저가 쓴 댓글 -->
   {% for comment in person.comment_set.all %}
   	<div>{{ comment.content }}</div>
   {% endfor %}
   
   <!-- 유저가 좋아요 한 글 -->
   {% for article in person.like_articles.all %}
   	<div>{{ article.title }}</div>
   {% endfor %}
   ```



3. Profile 템플릿으로 이동할 수 있는 하이퍼 링크 작성



## (2) Follow

1. 모델 관계 설정 - ManyToManyField 작성 및 Mgration

   ```python
   # accounts/models.py
   
   class User(AbstractUser)
   	followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
   ```



2. url 및 view 함수 작성

   ```python
   # accounts/urls.py
   
   urlpatterns = [
   	# ...
   	path('<int:user_pk>/follow/', views.follow, name='follow'),
   ]
   ```

   ```python
   # accounts/views.py
   
   def follow(request, user_pk):
       User = get_user_model()
       person = User.objects.get(pk=user_pk)
       
       if person != request.user:
       	if person.followers.filter(pk=request.user.pk).exists():
       	# if request.user in person.followers.all():
       		person.followers.remove(request.user)
       else:
       	person.followers.add(request.user)
           
       return redirect('accounts:profile', person.username)
   ```



3.  프로필 유저의 팔로잉, 팔로워 수 & 팔로우, 언팔로우 버튼 작성

   ```html
   <!-- 팔로잉, 팔로워 수 -->
   <div>
       팔로잉: {{ person.followings.all|length }} / 
       팔로워: {{ person.followers.all|length }}
   </div>
   
   <!-- 팔로우, 언팔로우 버튼 -->
   <form action="{% url 'accounts:follow' person.pk %}" method="POST">
       {% csrf_token %}
       {% if request.user in person.followers.all %}
   		<input type="submit" value="Unfollow">
   	{% else %}
   		<input type="submit" value="Follow">
   	{% endif %}
   </form>
   ```



4. 데코레이터 및 is_authenticated 추가

   ```python
   @require_POST
   def follow(request, user_pk):
       if request.user.is_authenticated:
       	User = get_user_model()
       	person = User.objects.get(pk=user_pk)
       
       if person != request.user:
           # if request.user in person.followers.all():
       	if person.followers.filter(pk=request.user.pk).exists():
   			person.followers.remove(request.user)
       	else:
       		person.followers.add(request.user)
               
       	return redirect('accounts:profile', person.username)
       
       return redirect('accounts:login')
   ```

   



# 2. View decorators & functions

## (1) 데코레이터 (Decorator)

```python
def hello(func):
    def wrapper():
        print('HIHI')
        func()
        print('HIHI')
    return wrapper

@hello
def bye():
    print('byebye')
    
bye()
```

```python
# 출력
HIHI
byebye
HIHI
```

- 기존 함수를 수정하지 않고 기능을 추가해주는 wrapper 함수
- Django는 HTTP 처리를 위해 view 함수에 적용할 수 있는 데코레이터를 제공



## (2) 405 Method Not Allowed

- `django.views.decorators.http`의 데코레이터를 사용하여, 요청 메소드를 기반으로 접근을 제한할 수 있다.
- 일치하지 않는 메서드 요청이라면 405 Method Not Allowed를 반환
- 메소드 목록
  - `require_http_methods()`
  - `require_POST()`
  - `require_safe()`



- `require_http_methods()`

  - View 함수가 특정한 요청 method만 허용하도록 하는 데코레이터

    ```python
    from django.views.decorators.http import require_http_methods
    
    @require_http_methods(['GET', 'POST'])
    def create(request):
    	pass
    ```

- `require_POST()`

  - View 함수가 POST 요청 method만 허용하도록 하는 데코레이터

  - url로 delete 시도 후 서버 로그에서 405 http status code 확인 해보기

    ```python
    from django.views.decorators.http import require_http_methods, require_POST
    
    @require_POST
    def delete(request, pk):
    	pass
    ```

- `require_safe()`

  - require_GET이 있지만 Django에서는 require_safe를 사용하는 것을 권장

    ```python
    from django.views.decorators.http import require_http_methods, require_POST, require_safe
    
    @require_safe
    def index(request):
    	pass
    ```



- [참고] @login_require와 @require_POST

  - 상황
    - 비로그인 상태로 detail 페이지에서 게시글 삭제 시도
    - delete view 함수의 @login_required로 인해 로그인 페이지로 리다이렉트
      - http://127.0.0.1:8000/accounts/login/?next=/articles/1/delete/
    - redirect로 이동한 로그인 페이지에서 로그인 진행
      - **redirect는 반드시 GET요청으로만 가능**
    - delete view 함수의 @require_POST로 인해 405 상태 코드
      - 405(Method Not Allowed) status code 확인
  - @login_required는 GET 요청을 처리하는 View 함수에서만 사용해야 한다.

  - POST method만 허용하는 delete 같은 함수의 내부에서는, is_authenticated 속성 값을 사용해서 로그인 여부를 확인



## (3) 404 Not Found

- Django Shortcut functions
  - 해당하는 객체가 존재하지 없는 경우 404 상태 코드를 반환
  - `get_object_or_404(klass, *args, **kwargs)`
  - `get_list_or_404(klass, *args, **kwargs)`



- views.py는 템플릿만 반환하는 것이 아니라, HTTPResponse 객체를 반환한다.

- views.py는 HTTP Request를 받아서, Model과 Template의 도움을 받아 응답 객체를 반환한다.

- views.py

  - render → 2xx

  - redirect → 3xx

  - @login_required → 3xx

  - Page not found → 404

  - Internal server error → 500

  - get에서 오류가 날 때 → 500 에러. 사용자가 url을 잘못 입력했는데 왜 내 잘못?

    → 이런 억울한 상황 방지: **get_object_or_404**(Article, pk=pk) 또는 get_object_or_404(get_user_model(), pk=pk) 이런 식으로

    → 500 에러에서 404로 바뀐다.



# 3. 기타

- view shortcuts
  - https://docs.djangoproject.com/en/4.1/topics/http/shortcuts/#get-object-or-404
- view decorators (http)
  - https://docs.djangoproject.com/en/4.1/topics/http/decorators/

- 내일은 JS를 위한 비동기 처리(axios 활용)를 할 예정
  - 지난 JS 수업 시간의 코드를 눈에 익히고 오면 좋다.
  - https://github.com/kdt-hphk/01-resources/blob/master/05_js/04_event.html
  - https://github.com/kdt-hphk/01-resources/blob/master/05_js/0920/index.html