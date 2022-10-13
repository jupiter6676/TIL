# 1. QnA

1. 쿠키와 세션의 차이는 무엇인가요?
   - HTTP는 Connectionless. 서버는 응답을 하면 끝. 연결을 끊는다.
   - 그리고 Stateless. 서버는 요청을 보낸 사람이 누군지 모른다.
   - 로그인을 한 이후의 요청들에는 인증 정보를 가지고 있다고 생각하면 된다.
   - 만약에 지금 Connectionless, Stateless 상태라면 쿠팡의 상태를 볼 때마다 password를 입력해야 한다.
   - 이를 해결하기 위해 '쿠키'라는 개념이 있는 것
   - 지난 번 요청을 한 사람에게 서버가 응답할 때 쿠키를 던져준다.
   - 그럼 다음에 요청을 할 때 서버가 그 쿠키 정보를 보면, 장바구니에 뭘 담았던 사람이구나 하고 알 수 있다.
   - 그러면 세션은 뭘까? 세션은 범컴퓨터적 용어로 사용된다. 세션은 연결되어 있다는 상태를 나타낸다고 보면 된다.
   - 쿠팡에 로그인한 상태로 무언가를 하게 된다면, 쿠팡에 인증을 받은 이후로 특정 상태를 유지하고 있을 수 있다.
   - 그러면 세션을 어떻게 관리할 것인가? django_session 테이블에서.
   - 즉, 쿠키는 HTTP 상에서 상태를 관리할 수 있는 하나의 도구, 세션은 이 둘의 연결된 상태를 의미한다.
   - 이 세션을 유지하려면 서버도 알아야 하고, 사용자 정보도 알아야 하는데, 이때 쿠키를 사용해서 사용자에게 전달해놓고, DB에 세션 id를 저장해서 이 둘을 확인하면서 세션을 유지하는 것이다.
   - 정의를 잘 알아보자!



2. 어제 실습에서 {{ user.username }}부분을 클릭하면 해당 회원의 detail 페이지로 넘어가야 하는데, 다른 회원의 detail 페이지로 넘어갔습니다. {{ request.user.username }}로 고치니까 해결됐는데, 이 미묘한 차이는 왜 발생하는 걸까요?
   - context에서 전달되고 있는 user라는 것이 있었기 때문일 것이다.
   - 그러다 보니, 요청한 유저인 경우에는 그냥 편하게 request.user를 쓰면 좋을 것 같다.



3. 게시글을 작성한 계정만 글을 수정하고 삭제할 수 있도록 할 수 있을까요?

   - 게시글을 작성한 계정인지 어떻게 알 수 있을까?

   - 게시글에 User PK를 저장해야 한다.

     ```html
     {% if request.user == article.user %}
     	<!-- 삭제, 수정 버튼 보여주기 -->
     {% endif %}
     ```

   - 다음 주 수업 내용!



4. DB를 두 개로 관리할 수 있는 방법이 있을까요?
   - DB가 하나인 것은 아니다. 여러 DB를 사용할 수도 있고, 각자 별도로 관리 시스템을 만들어서 할 수도 있고, 멀티 앱(django app X)으로 서비스를 제공할 수도 있다.
   - 예를 들어, 쿠팡에 보이는 페이지는 여러 개의 서버가 보여준다.
   - 다양한 서버에 각각 요청을 보내서 응답을 가져오는 것이다.
   - 특히, 상품을 추천하는 건 별도의 서버에서 가져오는 경우가 많다.
   - [[우아콘2020] 배달의민족 마이크로서비스 여행기](https://velog.io/@unow30/%EC%9A%B0%EC%95%84%EC%BD%982020-%EB%B0%B0%EB%8B%AC%EC%9D%98%EB%AF%BC%EC%A1%B1-%EB%A7%88%EC%9D%B4%ED%81%AC%EB%A1%9C%EC%84%9C%EB%B9%84%EC%8A%A4-%EC%97%AC%ED%96%89%EA%B8%B0-%EC%A0%95%EB%A6%AC)



5. 기타 → settings.py

- django.contrib.auth → login, logout

- django.contrib.auth.models → AbstractUser

- django.contrib.auth.forms → login_required

- django.contrib.auth.decorator → UserCreationForm

  

- articles.forms → ArticleForm

- articles.views → ...

- articles.models → Article



# 2. 회원 정보 수정

- 우선 브랜치를 만들고 그 안에서 작업을 한다.

  ```bash
  $ git checkout -b [branch]
  ```

  - pull은 덮어쓰기 느낌인데 merge는 변경 사항만 합쳐주는 느낌..?



- URL: /accounts/update/\<int:pk>
  - 여기서 질문. 과연 \<int:pk>가 필요할까?
  - 그냥 로그인한 유저의 정보를 수정하면 되는 것 아닐까?
  - URL은 /accounts/update/, 단 로그인 한 사용자만
- update
  - GET 요청: Form
  - POST 요청: 실제 수정
- 기능
  - Form
    - User ModelForm을 사용한다. → UserChangeForm
    - Article C/U에는 ArticleForm을 같이 썼는데, User C/U에는 왜 Form을 다른 걸 쓸까?
  - 사용자는 뭐가 다르다? 비밀번호.
    - User Create: 비밀번호 두 개를 받아서 일치하는지 검사하는 로직이 담긴 감사한 친구 → UserCreationForm
    - User Update: 비밀번호 두 개를 받을 필요가 있을까? 그리고 비밀번호는 그대로 입력해서 주면 될까? 구성이 다르지 않을까?
    - 수정은 우리 마음대로 로직을 만들면 된다. 그렇지만 일반적으로는 모든 회원가입 정보가 바뀌는 경우는 X
- 언제 login_required를 사용해야 할까?
  - 당연히 로그인이 필요한 상황에서...
  - 단, request.user로 유저 객체를 쓰는 함수에서는 무조건 쓰는 것이 좋다.

- \+ 번외

  ```python
  class User(AbstractUser):
      @property
      def full_name(self):
          return f'{self.last_name}{self.first_name}'
  ```



## (1) UserChangeForm

- 사용자의 정보 및 권한을 변경하기 위해 admin 인터페이스에서 사용되는 ModelForm

- UserChangeForm 또한 **ModelForm**이기 때문에, instance 인자로 기존 user 데이터 정보를 받는 구조 또한 동일하다.

- **CustomUserChangeForm**으로 확장해서 사용한다.

  ```python
  # accounts/forms.py
  
  from django.contrib.auth import get_user_model
  from django.contrib.auth.forms import UserChangeForm
  
  class CustomUserChangeForm(UserChangeForm):
      class Meta(UserChangeForm.Meta):
      	model = get_user_model()
  ```

  ```python
  # accounts/views.py
  
  def update(request):
      if request.method == 'POST':
          pass
      else:
          form = CustomUserChangeForm(instance=request.user)
      
      context = {
              'form': form,
      }
      
      return render(request, 'accounts/update.html', context)
  ```



## (2) CustomUserChangeForm fields 재정의

- UserChangeForm은 실제 관리자 화면에서 활용 중인 form으로 세부 필드들이 모두 노출되는 것을 확인할 수 있다.

- 직접 fields를 정의하여 원하는 형식으로 활용 가능하다.

- User 모델의 fields명은 어떻게 알 수 있을까?

- User 모델 상속 구조 살펴보기

  - **UserChangeForm** 클래스 구조 확인
    - Meta 클래스를 보면 **User**라는 model을 참조하는 ModelForm이라는 것을 확인할 수 있다.
    - https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L147
  - **User** 클래스 구조 확인
    - 실제로 User 클래스는 Meta 클래스를 제외한 코드가 없고, **AbstractUser** 클래스를 상속 받고있다.
    - https://github.com/django/django/blob/main/django/contrib/auth/models.py#L405
  - **AbstractUser** 클래스 구조 확인
    - 클래스 변수명들을 확인해보면, 회원수정 페이지에서 봤던 필드들과 일치한다는 것을 확인할 수 있다.
    - https://github.com/django/django/blob/main/django/contrib/auth/models.py#L334
  - 마지막으로 공식문서의 User 모델 Fields 확인
    - https://docs.djangoproject.com/en/3.2/ref/contrib/auth/#user-model

- 수정하고자 하는 필드 작성 후, 출력 변화 확인

  ```python
  # accounts/forms.py
  class CustomUserChangeForm(UserChangeForm):
      class Meta(UserChangeForm.Meta):
      	model = get_user_model()
          fields = ('email', 'first_name', 'last_name',)
  ```



## (3) 회원정보 수정 로직 작성

```python
# accounts/views.py

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    
    context = {
            'form': form,
    }
    
    return render(request, 'accounts/update.html', context)
```



# 3. 비밀번호 변경

