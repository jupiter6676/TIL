# 1. Django Template

## (1) Django Template?

- 데이터 표현을 제어하는 도구이자, 표현에 관련된 로직을 담당
- Django Template을 이용해, HTML 정적 부분과 동적 콘텐츠 삽입



## (2) Django Template Language (DTL)

- Django template에서 사용하는 built-in template system
- 조건, 반복, 변수 치환, 필터 등의 기능을 제공
  - Python처럼 일부 프로그래밍 구조(if, for 등)를 사용할 수 있지만 이것은 Python 코드로 실행되는 것은 X
  - Django 템플릿 시스템은 단순히 Python이 HTML에 포함 된 것이 아니니 주의
- 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것임을 명심



## (3) DTL Syntax

1. Variable

   ```html
   {{ variable }}
   ```

   - dot(.)을 사용하여 변수 속성에 접근할 수 있다.
   - render()의 세 번째 인자로 {'key': value} 와 같이 딕셔너리 형태로 넘겨주며, 여기서 정의한 key가 template에서 사용 가능한 변수명이 된다.



2. Filters

   ```html
   {{ variable|filter }}
   ```

   - 표시할 변수를 수정할 때 사용
   - 60개의 built-in template filters를 제공
   - chained가 가능하며, 일부 필터는 인자를 받기도 한다.



3. Tags

   ```html
   {% tag %}
   ```

   - 출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행
   - 일부 태그는 시작과 종료 태그가 필요 (ex. if-endif)
   - 약 24개의 built-in template tags를 제공



4. Comments

   ```html
   {# #}
   ```

   - Django template에서 라인의 주석을 표현하기 위해 사용
   - 한 줄 주석에만 사용할 수 있다. (줄 바꿈이 허용되지 않는다.)
   - 여러 줄 주석은 {% comment %}와 {% endcomment %} 사이에 입력



## (4) Template inheritance

- 템플릿 상속은 기본적으로 코드의 재사용성에 초점을 맞춘 것이다.
- 템플릿 상속을 사용하면 사이트의 모든 공통 요소를 포함하고, 하위 템플릿이 재정의(override) 할 수 있는 블록을 정의하는 기본 'skeleton' 템플릿을 만들 수 있다.



- 템플릿 상속 관련 태그

  ```html
  {% extends '~.html' %}
  ```

  - 자식(하위)템플릿이 부모 템플릿을 확장한다는 것을 알린다.
  - 반드시 템플릿 최상단에 작성 되어야 한다. 즉, 2개 이상 사용할 수 없다.

  ```html
  {% block content %}
  {% endblock content %}
  ```

  - 하위 템플릿에서 재지정(overridden)할 수 있는 블록을 정의
  - 즉, 하위 템플릿이 채울 수 있는 공간
  - 가독성을 높이기 위해 선택적으로 endblock 태그에 이름을 지정할 수 있다.



- \+α. 템플릿 경로 추가하기

  - base.html의 위치한 앱 안의 template 디렉토리가 아닌, 프로젝트 최상단의 templates 디렉토리에 위치하게 하고 싶다면?

  - 기본 templates 경로가 아닌 다른 경로를 추가하기 위해, 다음과 같은 코드 작성

    ```python
    # settings.py
    TEMPLATES = [
        {
            ...,
            'DIRS': [BASE_DIR/'templates',],
            ...,
        }
    ]
    ```

  - app_name/templates/ 디렉토리 경로 외 추가 경로를 설정할 것

  - base.html의 위치를 다음과 같이 이동한 후, 상속에 문제가 없는지 확인

    ```
    articles/
    firstpjt/
    tmplates/
    	base.html
    ```



# 2. Django URLs

- Dispatcher(운행 관리원)로서의 URL 이해하기
- 웹 애플리케이션은 URL을 통한 클라이언트의 요청에서부터 시작한다.



## (1) Trailing Slash

- Django는 URL 끝에 '/'가(Trailing slash) 없다면 자동으로 붙여주는 것이 기본 설정
  - 그래서 모든 주소가 '/'로 끝나도록 구성되어 있다.
  - 그러나, 모든 프레임워크가 이렇게 동작하는 것은 아니다.
- Django의 url 설계 철학: 기술적인 측면에서, foo.com/bar와 foo.com/bar/는 서로 다른 URL이다.
  - 검색 엔진 로봇이나 웹 트래픽 분석 도구에서는 그 둘을 서로 다른 페이지로 본다.
  - 그래서 Django는 URL을 정규화하여 검색 엔진 로봇이 혼동하지 않게 해야 한다.
- [참고] URL 정규화
  - 정규 URL(=오리지널로 평가되어야 할 URL)을 명시하는 것
  - 복수의 페이지에서 같은 콘텐츠가 존재하는 것을 방지하기 위함이다.
  - Django에서는 trailing slash가 없는 요청에 대해 자동으로 slash를 추가하여 통합된 하나의 콘텐츠로 볼 수 있도록 한다.



# 3. App URL Mapping

- 앱이 많아졌을 때 `urls.py`를 각 app에 매핑하는 방법
- 두 번째 app인 **pages**를 생성 및 등록 하고 진행
- 프로젝트의 urls.py에서 모두 관리하는 것은 프로젝트 유지보수에 좋지 않다.
  - app의 view 함수가 많아지면서 사용하는 path() 또한 많아지고, app 또한 더 많이 작성되기 때문이다.



## (1) App URL Mapping

- 하나의 프로젝트의 여러 앱이 존재한다면, 각각의 앱 안에 urls.py을 만들고 프로젝트 urls.py에서 각 앱의 urls.py 파일로 URL 매핑을 위탁할 수 있다.
- 자세한 건 9/27일자 실습 참고 (C:\Users\jupit\day3)



## (2) Including other URL Conferences

- urlpattern은 언제든지 다른 URLconf 모듈을 포함(include)할 수 있다.
- include되는 앱의 url.py에 urlpatterns가 작성되어 있지 않다면 에러가 발생
  - 예를 들어, pages 앱의 urlpatterns가 빈 리스트라도 작성되어 있어야 한다.
- 이제  메인 페이지의 주소는 이렇게 바뀌었다.
- http://127.0.0.1:8000/index/ → http://127.0.0.1:8000/articles/index/
- `include()` 함수
  - 다른 URLconfs를 참조할 수 있도록 돕는 함수
  - 함수 include()를 만나게 되면 URL의 그 시점까지 일치하는 부분을 잘라내고, 남은 문자열 부분은 후속 처리를 위해 include된 URLconf로 전달



# 4. Template namespace

## (1) 2가지 문제 발생

1. ~~articles app index 페이지에 작성한 두 번째 앱 index로 이동하는 하이퍼 링크를 클릭 시 현재 페이지로 다시 이동~~
   - ~~URL namespace~~ (해결)
2. pages app의 index url (http://127.0.0.1:8000/pages/index/)로 직접 이동해도 articles app의 index 페이지가 출력
   - Template namespace



## (2) 개요

- Django는 기본적으로 app_name/templates/ 경로에 있는 templates 파일들만 찾을 수 있다.
- Django는 settings.py의 INSTALLED_APPS에 작성한 app 순서로 template을 검색 후 렌더링한다.



## (3) 디렉토리 생성을 통해 물리적인 이름공간 구분

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

- Django templates의 기본 경로에 app과 같은 이름의 폴더를 생성해 폴더 구조를 app_name/templates/app_name/ 형태로 변경
- Django templates의 기본 경로 자체를 변경할 수는 없기 때문에, 물리적으로 이름 공간을 만드는 것



## (4) 템플릿 경로 변경

```python
# articles/views.py
return render(request, 'articles/index.html')
```

```python
# pages/views.py
return render(request, 'pages/index.html')
```

- 폴더 구조 변경 후, 해당하는 모든 부분을 변경된 경로로 수정



## (5) 반드시 Template namespace를 고려해야 할까?

- 만약 단일 앱으로만 이루어진 프로젝트라면 상관없다.
- 여러 앱이 되었을 때에도 템플릿 파일 이름이 겹치지 않게 하면 되지만, 앱이 많아지면 대부분은 같은 이름의 템플릿 파일이 존재하기 마련
- 따라서 고려하면 좋다.