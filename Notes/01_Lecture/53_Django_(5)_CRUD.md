# 1. Namespace

> 두 개의 앱에 index.html이 각각 있을 때의 결과를 살펴보자.



## (1) URL namespace

- 서로 다른 앱에서 동일한 URL 이름을 사용하는 경우에도, 이름이 지정된 URL을 고유하게 사용할 수 있다.

- `app_name` attribute를 작성해 URL namespace를 설정

  ```py
  # articles/urls.py
  app_name = 'articles'
  urlpatterns = [
      ...,
  ]
  ```

  ```python
  # pages/urls.py
  app_name = 'pages'
  urlpatterns = [
      ...,
  ]
  ```

- URL tag의 변화

  ```html
  {% url 'index' %} → {% url 'pages:index' %}
  ```

- URL 참조

  - '`:`' 연산자를 사용하여 지정
  - app_name을 지정한 이후에는 url 태그에서 반드시 `app_name:url_name` 형태로만 사용해야 한다.
  - 예를 들어, app_name이 articles이고 URL name이 index인 주소 참조는 articles:index가 된다.



## (2) Template namespace

- pages app의 index url(pages/index/)로 직접 이동해도 articles app의 index 페이지가 출력되는 문제

- Django는 기본적으로 `app_name/templates/` 경로에 있는 templates 파일들만 찾을 수 있으며, settings.py의 `INSTALLED_APPS`에 작성한 app 순서로 template을 검색 후 렌더링한다.

- 디렉토리 생성을 통해 물리적인 이름공간 구분

  - Django templates의 기본 경로에 app과 같은 이름의 폴더를 생성해 폴더 구조를 `app_name/templates/app_name/` 형태로 변경

  - Django templates의 기본 경로 자체를 변경할 수는 없기 때문에 물리적으로 이름 공간을 만드는 것

    ```
    articles/
        templates/
            articles/
                index.html
                ...
    pages/
    	templates/
    		pages/
                index.html
                ...
    ```

- 폴더 구조 변경 후, 변경된 경로에 해당하는 모든 부분을 수정

  ```python
  # articles/views.py
  
  return render(request, 'articles/index.html')
  ```

  ```python
  # pages/views.py
  
  return render(request, 'pages/index.html')
  ```



# 2. Naming URL patterns

```py
# pages/urls.py
urlpatterns = [
    path('index/', views.index, name='index'),
]
```

```html
{% url 'index' %}
```

- 링크에 URL을 직접 작성하는 것이 아니라 'path()' 함수의 name 인자를 정의해서 사용
- DTL의 Tag 중 하나인 URL 태그를 사용해서 'path()' 함수에 작성한 name을 사용
-  URL 설정에 정의된 특정한 경로들의 의존성을 제거



## (1) DRY 원칙

- Don't Repeat Yourself
- 소스 코드에서 동일한 코드를 반복하지 말자.
- 더 품질 좋은 코드를 작성하기 위해서 따르면 좋은 소프트웨어 원칙 중 하나.
- 동일한 코드의 반복은 잠재적 버그의 위협을 증가시키고, 반복되는 코드를 변경해야 할 경우에는 반복되는 모든 코드를 찾아 수정해야 한다.
- 이는 프로젝트 규모가 커질수록 애플리케이션의 유지 보수 비용이 커진다.



## (2) Django의 설계 철학 (Templates System)

1. 표현과 로직(view)을 분리
   - 템플릿 시스템은 표현을 제어하는 도구이자, 표현에 관련된 로직일 뿐
   - 즉, 템플릿 시스템은 이러한 기본 목표를 넘어서는 기능을 지원하지 말아야 한다.
2. 중복을 배제
   - 대다수의 동적 웹사이트는 공통 header, footer, navbar 같은 사이트 공통 디자인을 갖는다.
   - Django 템플릿 시스템은 이러한 요소를 한 곳에 저장하기 쉽게 하여 중복 코드를 없애야 한다.
   - 템플릿 상속의 기초가 되는 철학



## (3) Framework의 성격

1. 독선적(Opinionated)
   - Convention over Configuration (설정보다는 관례)
   - 특정 작업을 다루는 '올바른 방법'에 대한 분명한 규약을 가지고 있다.
   - 대체로 특정 문제 내에서 빠른 개발 방법을 제시한다.
   - 올바른 방법이란, 보통 잘 알려져 있고 문서화가 잘 되어있는 것이다.
   - 하지만 주요 상황을 벗어난 문제에 유연하지 못한 해결책을 제시할 수 있다.

2. 관용적(Unopinionated)
   - 관용적인 프레임워크들은 '올바른 방법'에 대한 제약이 거의 없다.
   - 이는 개발자들이 특정 작업을 완수할 때, 가장 적절한 도구를 선택적으로 이용할 수 있어 자유도가 높다.
   - 하지만 개발자 스스로가 그 도구들을 찾아야 한다는 수고가 필요하다.



## (4) Django의 성격

- 다소 독선적
  - 양쪽 모두에게 최선의 결과를 준다고 강조
- 결국, 현대 개발에 있어서 가장 중요한 것들 중 하나는 '생산성'
- 프레임워크는 우리가 하는 개발을 집중할 수 있도록 돕기 위해 만들어 진 것이지, 방해하기 위한 것이 아니다.
- "수레바퀴를 다시 만들지 말라."



# 4. Database

- 체계화된 데이터의 모임
- 검색 및 구조화 같은 작업을 보다 쉽게 하기 위해, 조직화된 데이터를 수집하는 저장 시스템



## (1) 기본 구조

1. 스키마(Schema)

   - 뼈대(Structure)

   - 데이터베이스에서 자료의 구조, 표현 방법, 관계 등을 정의한 구조

     | column | datatype |
     | :----: | :------: |
     |   id   |   INT    |
     |  name  |   TEXT   |
     |  age   |   INT    |

2. 테이블(Table)

   - 필드와 레코드를 사용해 조직된 데이터 요소들의 집합
   - 관계(Relation)
   - 필드(field) = 속성, 컬럼(Column)
   - 레코드(record) = 튜플, 행(Row)
   - PK (Primary Key)
     - 기본 키
     - 각 레코드의 고유한 값 (식별자로 사용)
     - 데이터베이스 관리 및 테이블 간 관계 설정 시 중요한 역할



## (2) Query

- 데이터를 조회하기 위한 명령어
- 조건에 맞는 데이터를 추출하거나 조작하는 명령어 (주로 테이블 형 자료구조)
- "Query를 날린다." = "데이터베이스를 조작한다."



# 5. Model

- Django는 Model을 통해 데이터에 접근하고 조작
- 사용하는 데이터들의 필수적인 필드와 동작을 포함
- 저장된 데이터베이스의 구조 (Layout)
- 일반적으로, 각각의 모델은 하나의 데이터베이스 테이블에 매핑
  - 모델 클래스 1개 = 데이터베이스 테이블 1개



# 6. 기타

- 삼성전자, 삼성SDS
  1. 알고리즘 역량: A → B (pro)
  2. 코드 리뷰 역량: 클린 코드 & 디자인 패턴 & TDD
  3. 아키텍트 역량: 설계 디자인 패턴 & 설계 원칙
- render에는 `app_name/template.html`이고 redirect는 `app_name:template_name` 이런 식으로 해야 하나?
