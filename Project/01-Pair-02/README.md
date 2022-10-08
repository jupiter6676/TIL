## 프로젝트 주제

주간 페어 프로그래밍 2 - 영화 리뷰 커뮤니티 CRUD 



## 프로젝트 기간

2022.10.07



## 프로젝트 목적

세 사람이 팀을 이뤄서 영화 리뷰 커뮤니티 서비스를 개발합니다. 아래 조건을 만족해야 합니다.

- ModelForm 활용 CRUD 구현
- Staticfiles 활용 서비스 로고 표시



## 프로젝트 설명

### 모델 Model

---

모델은 아래 조건을 만족해야 합니다.

적절한 필드와 속성을 부여하세요.

- 모델 이름 : Review

  모델 필드

  | 이름       | 역할          | 필드     | 속성              |
  | ---------- | ------------- | -------- | ----------------- |
  | title      | 리뷰 제목     |          |                   |
  | content    | 리뷰 내용     |          |                   |
  | movie_name | 영화 이름     |          |                   |
  | grade      | 영화 평점     |          |                   |
  | created_at | 리뷰 생성시간 | DateTime | auto_now_add=True |
  | updated_at | 리뷰 수정시간 | DateTime | auto_now = True   |

  

### 기능 View

---

아래 작성된 기능을 구현합니다.

생성 및 수정은 ModelForm을 사용하여 구현합니다.

- 데이터 목록 조회

  - `GET` http://127.0.0.1:8000/reviews/

- 데이터 정보 조회

  - `GET` http://127.0.0.1:8000/reviews/[int:pk](int:pk)/

- 데이터 생성

  - `POST` http://127.0.0.1:8000/reviews/create/

  사용자에게 아래 데이터를 입력 받습니다.

  - 리뷰 제목
  - 리뷰 내용
  - 영화 이름
  - 영화 평점

- 데이터 수정

  - `POST` http://127.0.0.1:8000/reviews/[int:pk](int:pk)/update/

- 데이터 삭제

  - `POST` http://127.0.0.1:8000/reviews/[int:pk](int:pk)/delete/



### 화면 Template

---

아래 작성된 페이지를 구현합니다.

- **네비게이션바, Bootstrap `<nav>`**

  - 서비스 로고
    - Django Staticfiles 활용
    - 클릭 시 메인 페이지로 이동
  - 리뷰 목록 버튼
    - 클릭 시 목록 페이지로 이동
  - 리뷰 작성 버튼
    - 클릭 시 작성 페이지로 이동

  **메인 페이지**

  - `GET` http://127.0.0.1:8000/reviews/
  - 자유 디자인

  목록 페이지

  - `GET` http://127.0.0.1:8000/reviews/index/
  - 리뷰 목록 출력
    - 리뷰 제목
    - 영화 이름
  - 제목을 클릭하면 해당 리뷰의 정보 페이지로 이동

  **리뷰 정보 페이지**

  - `GET` http://127.0.0.1:8000/reviews/[int:pk](int:pk)/
  - 해당 리뷰 정보 출력
  - 수정 / 삭제 버튼

  **리뷰 작성 페이지**

  - `GET` http://127.0.0.1:8000/reviews/create/
  - 리뷰 작성 폼

  **리뷰 수정 페이지**

  - `GET` http://127.0.0.1:8000/reviews/[int:pk](int:pk)/update/
  - 리뷰 수정 폼



## 사용 기술

- 언어: HTML, CSS, JavaScript, Python
- 라이브러리: urllib, re, request, bs4
- 프레임워크: Django



## 역할 (개발 내용)

- 이용환: DB 글 목록 배치, 글 작성 및 검색 기능 구현, 페이지 디자인 등
- 윤효근: 영화 정보 크롤링, form 별점 기능 등
- 최보영: 영화 세부 페이지, 댓글 작성 기능 구현, 페이지 디자인 등



## 스크린샷

![pair_2](Assets/README.assets/pair_2.gif)



## 배운 점

- 크롤링한 데이터를 DB에 저장하고 활용하는 방법
- Django Model에서 Foreign Key를 활용하는 방법
- git conflict 해결하는 방법
- 페이지 검색 기능을 구현하는 방법
- ModelForm에서 별점 기능을 구현하는 방법 등
