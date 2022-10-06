# 1. QnA

## (1) Django에 대한 근본적인 의문

1. 서비스가 커지면 장고로 서비스하기 힘들다는 이야기가 있는데, 장고의 한계는 어디까지 인가요?
   - 나중에 개발자마다 기술 스택 등이 다 다를 것이지만, 처음 시작을 Django로 해서 로직을 이해하고 나아가는 것
   - 국내 기술 생태계 대다수는 Java
   - 회사마다 기술 스택이 다 다르다. 심지어 스타트업에서는 CTO가 바뀌면서 기술 스택도 바뀔 수 있다.



## (2) 개념 및 활용

1. ModelForm을 사용하지 않고 만들 수 있는데, ModelForm을 사용하면 더 복잡해지는 느낌입니다. ModelForm을 사용하는 이점이 무엇인가요?

   - ModelForm은 DB 중심의 앱을 만들 때 도움을 주는 클래스를 제공한다.
   - ModelForm을 쓰면, Model의 Field가 변경되었을 때 html에서 직접 수정하는 것이 않아도, 별도로 관리할 수 있는 추상화된 클래스를 가질 수 있게 해준다.
   - ModelForm의 다양한 기능을 편하게 사용할 수 있다.
   - ModelForm을 쓰지 않으면 html을 직접 만들어야 하고, 유효성 검사를 별도로 진행해야 한다.
   - 즉, ModelForm은 기능을 하도록 추상화 된 것(Class)
     - ① HTML Form ↔ Model, ② Validation
   - Custom이 필요한 시점이 있다. 그때는 한 번 해 보면 되고, 지금은 우선 써먹자!

   

2. Django 부트스트랩 패키지를 활용하는 것보다, base.html에 부트스트랩 CDN 넣는 게 더 편한 것 같은데, Django 부트스트랩 패키지를 더 잘 활용할 수 있는 방법이 있을까요?

   - 역질문. Django Bootstrap을 왜 썼을까?

     - ModelForm을 Bootstrap Form 스타일로, 자동으로 꾸며준다.
     - {% bootstrap_form form %}을 했더니, 기본 HTML Form 스타일이 적용된다.

   - 커스텀 방법 ① → form 배치하기

     ```html
     <form action="" method="POST">
         {% csrf_token %}
         
         {% for field in article_form %}
             <p>{{ field.label_tag }}</p>
             {{ field }}
         {% endfor %}
     </form>
     ```

   - 커스텀 방법 ② → `widgets`를 통해 요소를 직접 바꾸기 (ex. field에 autofocus를 적용하고 싶을 때)

     

3. ModelForm, admin, model 등 왜 이렇게 클래스를 정의하는 경우가 많을까요?

   - 기본 기능을 상속받아서, 그걸 그대로 사용하고, 커스텀 설정도 하고, Django도 사용할 수 있다.
   - 현재까지는 View를 Function으로 정의했지만, Class로 정의할 수도 있다.



## (3) 기능

1. 글 작성 form과 수정 form이 비슷한 것 같은데, 둘을 합쳐 하나의 html로 구현할 수 있을까요?

   - 우선 문제 상황을 인식 → Template 파일 자체를 경우에 따라 다르게 볼 수 있을까?

   - 화면을 만드는 역할은 Template이 한다. 어떻게든 조건에 따른 화면을 보여줘야 한다.

   - 그러면 내가 템플릿에서 쓸 수 있는 변수/값들은 무엇일까? → context

   - views에서 context로 어떤 값을 넘겨서 처리한다. 그런데 다른 방법은 없을까?

   - {% if request.path == '/articles/create' %} → 근데 경로를 직접 작성한 적이 X

   - {% if request.resolver_match.url_name == 'create' %}

     

2. 날짜 형식을 직접적으로 바꿀 수는 없을까요?

   - MTV 중 누가 해줄까? → T

   - django에서 몇 분전 이런 것도 지원해준다.

   - 표시 형식을 바꾸는 작업 → Django Template Filter `{ | }`

   - 추가적인 문법 등을 도와주는 것 → Django Template Tag `{% %}`

     

3. 생성 날짜와 수정 날짜가 같을 때, 수정 날짜를 표시 안되게 하고 싶은데 방법이 있을까요?

   - T에서 조건문을 잘 작성한다.

   - 내가 템플릿에서 쓸 수 있는 변수/값들을 인지하고, 그것을 쓴다.

   - context + request + a ...

     

4. {% load ~ %}와 {% extends ~ %} 중에 더 상단에 작성해야 하는 코드는 무엇인가요?

   - 오류 메시지를 확인해본다.

   - 모든 템플릿의 최상단에는 {% extends ~ %}가 있어야 한다.

     

5. path 지정할 때 `<int:pk>/delete`를  `delete/<int:pk>`이런 식으로 순서를 바꿔도 상관 없을까요?

   - 순서를 바꿔도 상관은 없지만, URL 네임을 정하는 방식이라고 보면 된다.

   - ex) `teams/6/members/` : 축구팀 6번 팀의 멤버들

     

6. base.html에 {% load static %}을 썼는데 index.html에서 먹히지 않았는데, index.html에 {% load static %}을 써주니 작동하였습니다. load를 따로 써줘야 하는 이유를 알고 싶습니다.

   - Django Template에서 load는 파이썬의 import처럼 생각하자.
   - 내가 load를 쓰고 싶은 템플릿이 있으면, 해당 파일에서 load를 해주어야 한다.



# 2. 기타

- [Django Built-in Template Tags and Filters](https://docs.djangoproject.com/en/4.1/ref/templates/builtins/)
- 커뮤니티 사이트들 디자인 살펴보기
  - [eoPLANET](https://eopla.net/)
  - [Surfit](https://www.surfit.io/)
  - [Disquiet](https://disquiet.io/)
  - [인살롱](https://hr.wanted.co.kr/)
  - [Blind](https://www.teamblind.com/kr/)