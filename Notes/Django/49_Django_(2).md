# 1. Django 구조 이해하기 (MTV Design Pattern)

## (1) 소프트웨어 디자인 패턴

- 다양한 응용 소프트웨어를 개발할 때 공통적인 설계 문제가 존재하며, 이를 처리하는 해결책 사이에도 공통점이 있다.
- 이러한 유사점을 패턴이라고 한다.
- 앞서 배웠던 클라이언트-서버 구조도 소프트웨어 디자인 패턴 중 하나
- 자주 사용되는 소프트웨어의 구조를 소수의 뛰어난 엔지니어가 마치 건축의 공법처럼 일반적인 구조화를 해둔 것



## (2) 목적

- 특정 문맥에서 공통적으로 발생하는 문제에 대해 재사용 가능한 해결책을 제시
- 프로그래머가 애플리케이션이나 시스템을 디자인할 때 발생하는 공통된 문제들을 해결하는데 형식화 된 가장 좋은 관행
- 다수의 엔지니어들이 일반화된 패턴으로 소프트웨어 개발을 할 수 있도록 한 규칙, 커뮤니케이션의 효율성을 높이는 기법



## (3) Django의 디자인 패턴

- **MTV 패턴**
- MVC 디자인 패턴을 기반으로 조금 변형된 패턴이다.
  - Model(데이터 관련 로직) - View(레이아웃과 화면) - Controller(명령을 model과 view 부분으로 연결)
  - 하나의 큰 프로그램을 세 가지 역할로 구분한 개발 방법론
  - 업무의 분리, 향상된 관리
- Django는 MVC 패턴을 기반으로 한 MTV 패턴을 사용
  - 두 패턴은 서로 크게 다른 점은 없고, 일부 역할에 대해 부르는 이름이 다르다.
  - Model - Template - View



## (4) MTV 디자인 패턴

1. Model
   - MVC 패턴에서 Model의 역할
   - 데이터와 관련된 로직을 관리
   - 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리
2. Template
   - MVC 패턴에서 View의 역할
   - 레이아웃과 화면을 처리
   - 화면 상의 사용자 인터페이스 구조와 레이아웃을 정의
3. View
   - MVC 패턴에서 Controller의 역할
   - Model & Template과 관련한 로직을 처리해서 응답을 반환
   - 클라이언트의 요청에 대해 처리를 분기하는 역할
   - 동작 예시
     - 데이터가 필요하다면 model에 접근해서 데이터를 가져오고, 
     - 가져온 데이터를 template로 보내 화면을 구성하고, 
     - 구성된 화면을 응답으로 만들어 클라이언트에게 반환



# 2. Django Quick Start

## (1) Django 설치

- **설치 전 가상 환경** 설정 및 활성화를 마치고 진행

- Django 4.0 릴리즈로 인해 3.2(LTS) 버전을 명시해서 설치

  ```bash
  $ pip install django==3.2.13
  ```

- 패키지 목록 생성

  ```bash
  $ pip freeze > requirements.txt
  ```

- LTS

  - Long Term Support (장기 지원 버전)

  - 일반적인 경우보다, 장기간에 걸쳐 안정적으로 지원하도록 고안된 소프트웨어의 버전

  - 컴퓨터 소프트웨어의 제품 수명주기 관리 정책



## (2) Django Project

- 프로젝트 생성

  ```bash
  $ django-admin startproject [프로젝트이름] .
  ```

  - Project 이름에는 Python이나 Django에서 사용 중인 키워드 및 `-`(하이픈) 사용 불가
  -  `.` (dot)을 붙이지 않을 경우 현재 디렉토리에 프로젝트 디렉토리를 새로 생성

- 서버 실행

  ```bash
  $ python manage.py runserver
  ```



## (3) 프로젝트 구조

- `__init__.py`

  - Python에게 이 디렉토리를 하나의 Python 패키지로 다루도록 지시
  - 별도로 추가 코드를 작성하지 않는다.

- `asgi.py`

  - Asynchronous Server Gateway Interface
  - Django 애플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 돕는다.
  - 추후 배포 시에 사용하며 지금은 수정하지 않는다.

- `settings.py`

  - Django 프로젝트 설정을 관리

- `urls.py`

  - 사이트의 url과 적절한 views의 연결을 지정

- `wsgi.py`

  - Web Server Gateway Interface
  - Django 애플리케이션이 웹 서버와 연결 및 소통하는 것을 돕는다.
  - 추후 배포 시에 사용하며 지금은 수정하지 않는다.

- `manage.py`

  - Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티

    ```bash
    $ python manage.py <command> [options]
    ```



# 3. Django Application

## (1) 애플리케이션(앱) 생성

```bash
$ python manage.py startapp [앱이름]
```

- 일반적으로, 애플리케이션 이름은 복수형으로 작성



## (2) 애플리케이션 구조

- `admin.py`
  - 관리자용 페이지를 설정하는 곳
- `apps.py`
  - 앱의 정보가 작성된 곳
  - 별도로 추가 코드를 작성하지 않는다.
- **`models.py`**
  - 애플리케이션에서 사용하는 Model을 정의하는 곳
  - MTV 패턴의 M에 해당
- `tests.py`
  - 프로젝트의 테스트 코드를 작성하는 곳
- **`views.py`**
  - view 함수들이 정의되는 곳
  - MTV 패턴의 V에 해당



- 프로젝트에서 앱을 사용하기 위해서는, `settings.py`의 `INSTALLED_APPS` 리스트에 반드시 추가해야 한다.
  - 리스트 안에는 Local apps, Third Party apps, Django apps의 순서를 지키며 작성하는 것을 권장한다.



## (3) Project & Application

- Project
  - “collection of apps”
  - 프로젝트는 앱의 집합
  - 프로젝트에는 여러 앱이 포함될 수 있다.
  - 앱은 여러 프로젝트에 있을 수 있다.

- Application
  - 앱은 실제 요청을 처리하고 페이지를 보여주는 등의 역할을 담당
  - 일반적으로 앱은 하나의 역할 및 기능 단위로 작성하는 것을 권장



## (4) 총 과정

1. 가상 환경 생성, 실행
2. django lts 버전 설치
3. django 프로젝트 생성
4. 앱 생성: 주의 → 커맨드를 manage.py가 있는 경로에서 실행해야 한다.
5. 앱 등록
6. 서버 실행 테스트
7. 앱의 url, view, template 작성



# 4. 요청과 응답

- URL  → VIEW → TEMPLATE 순의 순서로 코드를 작성해보고, 데이터의 흐름을 이해하기

- ① 주문서 정의, ② 로직 구현, ③ HTML 페이지 구성

  → ① urls.py, ② views.py, ③ index.html (③ 이름은 자유)



## (1) URLs

- urls.py

  ```python
  from django.contrib import admin
  from django.urls import path
  from articles import views	# views.py 파일은 articles 폴더에 있음.
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('index/', views.index),
      # path('주문서', '어떤 view 파일(함수)에서 핸들링 할 것인지')
  ]
  ```



## (2) Views

- views.py

  ```python
  from django.shortcuts import render
  
  # django에게 뭘 해달라고 시키는 것..
  # 인자에는 사용자 요청 정보가 들어온다.
  def index(request):
      # 환영하는 메인 페이지를 보여준다.
      return render(requests, 'index.html')
  ```

- HTTP 요청을 수신하고, HTTP 응답을 반환하는 함수 작성

- Template에서 HTTP 응답 서식을 맡긴다.

- Render()

  - ```python
    render(requests, template_name, context)
    ```

  - 주어진 템플릿을 주어진 컨텍스트 데이터와 결합하고, 렌더링 된 텍스트와 함께 HttpResponse(응답) 객체를 반환하는 함수

    - request: 응답을 생성하는 데 사용되는 요청 객체
    - template_name: 템플릿의 전체 이름 또는 템플릿 이름의 경로
    - context: 템플릿에서 사용할 데이터 (딕셔너리 타입으로 작성)



## (3) Templates

- articles 폴더 내에 templates 폴더를 생성
- 그 안에 index.html 파일 생성 후 내용 작성