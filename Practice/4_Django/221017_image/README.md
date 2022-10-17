## 실습 주제

장고 13 - Django Media



## 실습 목표

Django Media를 활용한 이미지 업로드가 가능한 게시판 서비스를 개발합니다.



## 배운 점

- ImageField와 ProcessedImage는 각각 한 번씩 파일을 선택해야 한다.
- ImageField의 이미지를 원본으로 썸네일 이미지를 제작할 수도 있다. → ImageSpec



## 요구사항

### 모델 Model

---

- 모델 이름 : Article

  모델 필드
  
  | 필드 이름 |     역할      |      필드      | 속성 |
  | :-------: | :-----------: | :------------: | :--: |
  |   title   |    글 제목    |      Char      |      |
  |  content  |    글 내용    |      Text      |      |
  |   image   |   글 이미지   |     Image      |      |
  | thumbnail | 썸네일 이미지 | ProcessedImage |      |




### 기능 View

---

- 데이터 목록 조회
  - `GET` http://127.0.0.1:8000/articles/
- 데이터 정보 조회
  - `GET` http://127.0.0.1:8000/articles/[int:pk](int:pk)/
- 데이터 생성
  - `POST` http://127.0.0.1:8000/articles/create/
  - 사용자가 글 이미지 `image`와 썸네일 이미지 `thumbnail` 를 업로드할 수 있어야 합니다.
- 데이터 수정
  - `POST` http://127.0.0.1:8000/articles/[int:pk](int:pk)/update/
- 데이터 삭제
  - `POST` http://127.0.0.1:8000/articles/[int:pk](int:pk)/delete/



\+ 추가 기능

- 썸네일 이미지를 선택하지 않으면, 서버에서 기본 이미지를 제공 (Static Image)
- Grid로 index 페이지 정렬
- Card에 마우스 호버 시 애니메이션 추가
- nav bar에, 페이지의 url_name에 따라 active되는 게 다르도록 설정



### 화면 Template

---

- 목록 페이지
  - `GET` http://127.0.0.1:8000/articles/
  - 게시글 목록
  - 썸네일 이미지 `thumbnail`가 있으면 썸네일 이미지를 출력합니다.
- 정보 페이지
  - `GET` http://127.0.0.1:8000/articles/[int:pk](int:pk)/
  - 해당 게시글 정보 출력
    - 글 이미지 `image` 가 있으면 이미지를 출력합니다.
- 작성 페이지
  - `GET` http://127.0.0.1:8000/articles/create/
  - 게시글 작성 폼
    - 사용자가 이미지를 업로드할 수 있어야 합니다.
- 수정 페이지
  - `GET` http://127.0.0.1:8000/articles/[int:pk](int:pk)/update/
  - 게시글 수정 폼



## 사용 기술

- 언어: HTML, CSS, JavaScript, Python
- 라이브러리: 
- 프레임워크: Django
