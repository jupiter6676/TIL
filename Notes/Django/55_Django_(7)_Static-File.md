# 1. ModelForm 정리

|      |                    기능                    |                    URL                     |      views.py      |                응답                |
| :--: | :----------------------------------------: | :----------------------------------------: | :----------------: | :--------------------------------: |
| 생성 |   HTML Form (GET)<br>DB 저장 과정 (POST)   |          /articles/<br>/articles/          | ~~new~~<br>create  | create.html<br>**redirect** detail |
| 조회 |         글을 누르면 **DB 값** 조회         |               /articles/...                |       detail       |            detail.html             |
| 삭제 |        버튼을 누르면 **DB 값** 삭제        |            /articles/delete/...            |       delete       |        redirect index.html         |
| 수정 | HTML Form + **기존 값**<br>기존 DB 값 수정 | /articles/edit/...<br>/articles/update/... | ~~edit~~<br>update | update.html<br>**redirect** detail |



## (1) 지난 주 복습

- Django : 웹 프레임워크로 서버의 역할
- 서버 : URL + method로 HTTP 요청 받아서 처리하여 HTTP 응답하는 역할
- 프레임워크의 구조 : MTV 
- Form : 사용자로부터 값을 받아서(input : name, value) 서버로 전송(form : action, method)



## (2) 저번 시간 복습

- 웹 서비스는 UI ↔ DB가 매우 밀접한 관계를 가진다.
- 모델의 필드는 사용자가 입력하는 input 필드와 관계가 있다. 이 과정에서 Django ModelForm이 아래의 주된 역할을 진행한다.
  1.  Model 필드를 기반으로 HTML Form input 구성
  2. 데이터 유효성 검사 이후 DB 저장 or 에러 메시지 전달
- 서버에 자료를 데이터를 전송하는 Form은 일반적으로 POST 요청으로 처리한다.
- Django에서는 CSRF를 방지하기 위한 Token 설정을 강제하고 있다. (보안상 이점)



- ModelForm
  1. DB 필드가 사실상 HTML Form
  2. Input 값을 DB에 저장하기 전에 유효성 검사

- Create / Update
  - 글 쓸 때 요청(GET) → 비어있는 Form
  - Form 입력 후 요청(POST) → 유효성 검사 → (통과) DB 저장 / (실패) 에러 + 입력 값



# 2.  Static Files

## (1) 웹 서버와 정적 파일

- 웹 서버

  - 웹 서버는 특정 위치(URL)에 있는 자원을 요청 받아서 제공하는 응답을 처리한다.

  - 즉, 웹 서버는 요청 받은 URL로, 서버에 존재하는 정적 자원(static resource)를 제공한다.

- 정적 파일
  - 응답할 때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일 (사용자의 요청에 따라 내용이 바뀌는 것이 X)
  - 예를 들어, 웹 서버는 일반적으로 이미지, 자바 스크립트 또는 CSS와 같은 미리 준비된 추가 파일을 제공한다.
  - 파일 자체가 고정되어 있고, 서비스 중에도 추가되거나 변경되지 않고 고정되어 있다.



## (2) 정적 파일 활용

- `INSTALLED_APPS`에 'django.contrib.staticfiles'가 포함되어 있는지 확인

- 템플릿에서 static 태그를 사용하여, 지정된 상대 경로에 대한 URL을 빌드

  ```html
  {% load static %}
  <img src="{% static 'images/example.png' %}">
  ```

  - load
    - 사용자 정의 템플릿 태그 세트를 로드한다.
    - 로드하는 라이브러리, 패키지에 등록된 모든 태그와 필터를 불러온다.
  - static
    - STATIC_ROOT에 저장된 정적 파일에 연결한다.

- 앱의 `static` 디렉토리에 정적 파일을 저장

  - 위의 경우는 `my_app/static/images/example.png`



# 3. 기타

- [django-bootstrap5 문서](https://django-bootstrap-v5.readthedocs.io/en/latest/)
- [django form에 bootstrap 적용](https://hyun-am-coding.tistory.com/entry/Django-Form%EC%97%90-bootstrap%EC%A0%81%EC%9A%A9%ED%95%98%EA%B8%B0)