# 1. One-to-many Relationship

## (1) RDB(관계형 데이터베이스) 복습

- 데이터를 테이블, 행, 열 등으로 나누어 구조화하는 방식
- RDB의 모든 테이블에는 행에서 고유하게 식별 가능한 기본 키라는 속성이 있다.
- 외래 키를 사용하여 각 행에서 서로 다른 테이블 간의 관계를 만드는 데 사용할 수 있다.



## (2) 테이블 간 관계 예시

- 주문 서비스 DB: 고객 테이블, 주문 테이블

  - 고객 테이블 : 고객 정보(이름, 주소 정보)

    | 고객 id (primary key) |
    | :-------------------: |
    |         이름          |
    |        주소지         |
    |        배송지         |

  - 주문 테이블 : 주문 정보(제품, 주문/배송 정보)

    |  주문 id  |
    | :-------: |
    |  제품명   |
    |  주문일   |
    |  배송일   |
    | 주문 상태 |



- 고객이 제품을 주문하는 경우, 주문 테이블에 레코드가 생성된다.

- 주문 정보가 아래의 테이블처럼 기록이 되어 있을 때 고객 정보는 어떻게 표현할까?

  | 주문 id | 제품명 |   주문일   |   배송일   |  주문 상태  |
  | :-----: | :----: | :--------: | :--------: | :---------: |
  |    1    |  생수  | 2000-01-01 | 2000-01-03 |   배송중    |
  |    2    | 영양제 | 2000-01-02 | 2000-01-07 | 배송 준비중 |
  |    3    | 음료수 | 2000-01-03 | 2000-01-05 |   배송중    |



- 고객 정보(이름) 기록

  | 주문 id | 제품명 |   주문일   |   배송일   |  주문 상태  | 고객 정보 |
  | :-----: | :----: | :--------: | :--------: | :---------: | :-------: |
  |    1    |  생수  | 2000-01-01 | 2000-01-03 |   배송중    |  김진수   |
  |    2    | 영양제 | 2000-01-02 | 2000-01-07 | 배송 준비중 |  박영희   |
  |    3    | 음료수 | 2000-01-03 | 2000-01-05 |   배송중    |  김진수   |

  - 하지만 이렇게 이름으로 기록할 경우, 이름이 같은 다른 사용자를 구분할 수 없다.
  - 그렇다면 고객 정보의 어떤 데이터를 사용하는 것이 적합할까?



- 고객 정보(id) 기록

  | 주문 id | 제품명 |   주문일   |   배송일   |  주문 상태  | 고객 id |
  | :-----: | :----: | :--------: | :--------: | :---------: | :-----: |
  |    1    |  생수  | 2000-01-01 | 2000-01-03 |   배송중    |    2    |
  |    2    | 영양제 | 2000-01-02 | 2000-01-07 | 배송 준비중 |    1    |
  |    3    | 음료수 | 2000-01-03 | 2000-01-05 |   배송중    |    2    |

  - 외래 키(Foreign Key, FK) : 관계형 데이터베이스에서 다른 테이블의 행을 식별할 수 있는 필드(키)



## (3) RDB에서의 관계

- 1:1
  - One-to-one relationships
  - 한 테이블의 레코드 하나가, 다른 테이블의 레코드 단 한 개와 관련된 경우
  - ex) User - Profile
- 1:N
  - One-to-many relationships
  - 한 테이블의 0개 이상의 레코드가, 다른 테이블의 레코드 단 한 개와 관련된 경우
  - ex) 댓글 - 사용자의 글, 사용자 - 사용자의 댓글
- M:N
  - Many-to-many relationships
  - 한 테이블의 0개 이상의 레코드가, 다른 테이블의 0개 이상의 레코드와 관련된 경우
  - 양쪽 모두에서 1:N 관계를 가진다.



# 2. Foreign Key

## (1) 개념

- 외래 키 (외부 키)
- 관계형 데이터베이스에서 다른 테이블의 행을 식별할 수 있는 키
- **참조되는 테이블의 기본 키**(Primary Key)를 가리킨다.
- 참조하는 테이블의 행 1개의 값은, 참조되는 측 테이블의 행 값에 대응된다.
  - 이 때문에 참조하는 테이블의 행에는, 참조되는 테이블에 나타나지 않는 값을 포함할 수 없다.
- 참조하는 테이블 행 여러 개가, 참조되는 테이블의 동일한 행을 참조할 수 있다.



## (2) 특징

- 키를 사용하여 부모 테이블의 유일한 값을 참조 (참조 무결성)
  - 참조 무결성: 데이터베이스 관계 모델에서, 관련된 2개의 테이블 간의 일관성
  - 외래 키가 선언된 테이블의 외래 키 속성(열)의 값은 해당 테이블의 기본 키 값으로 존재
- 외래 키의 값이 반드시 부모 테이블의 기본 키 일 필요는 없지만 유일한 값이어야 한다.



# 3. 1:N (Article - Comment)

## (1) 모델 관계 설정

- 게시판의 게시글과 1:N 관계를 나타낼 수 있는 댓글 구현
- 1:N 관계에서, 댓글을 담당할 Article 모델은 1, Comment 모델은 N이 될 것
  - 게시글은 댓글을 0개 이상 가진다.
    - 게시글(1)은 여러 개의 댓글(N)을 가진다.
    - 게시글(1)은 댓글을 가지지 않을 수도 있다.
  - 댓글은 반드시 하나의 게시글에 속한다.



## (2) Django Relationship Fields 종류

- OneToOneField() → 1:1
- ForiegnKey() → 1:N
- ManyToManyField() → M:N



## (3) Foreign Key(to, on_delete, **options)

- 1:N 관계를 담당하는 Django의 모델 필드 클래스
- Django 모델에서 관계형 DB의 외래 키 속성을 담당
- 2개의 필수 위치 인자가 필요
  - 참조하는 model class
  - on_delete 옵션
- https://docs.djangoproject.com/en/3.2/ref/models/fields/#foreignkey



- on_delete
  - 외래 키가 참조하는 객체가 사라졌을 때, 외래 키를 가진 객체를 어떻게 처리할지를 정의
  - 데이터 무결성을 위해서 매우 중요한 설정
  - on_delete 옵션 값
    - CASCADE: 부모 객체(참조된 객체)가 삭제됐을 때, 이를 참조하는 객체도 삭제
    - PROTECT, SET_NULL, SET_DEFAULT 등 여러 옵션 값들이 존재



## (4) Comment 모델 정의

- 외래 키 필드는 ForeignKey 클래스를 작성하는 위치와 관계 없이, 필드의 마지막에 작성된다.

- ForeignKey() 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형(소문자)으로 작성하는 것을 권장

  ```python
  class Comment(models.Model):
      article = models.ForeignKey(Article, on_delete=models.CASCADE)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
  ```

   - 만약 ForeignKey 인스턴스를 article이 아닌 abcd로 생성 했다면 abcd_id로 만들어진다.
     - 명시적인 모델 관계 파악을 위해 참조하는 클래스 이름의 소문자(단수형)로 작성하는 것이 권장되었던 이유



# 4. 관계 모델 참조

## (1) Related manager

- Related manager는 1:N 혹은 M:N 관계에서 사용 가능한 문맥(context)
- Django는 모델 간 1:N 혹은 M:N 관계가 설정되면 **역참조** 할 때에 사용할 수 있는 manager를 생성
  - 우리가 이전에 모델 생성 시 objects라는 매니저를 통해 queryset api를 사용했던 것처럼,
  - related manager를 통해 queryset api를 사용할 수 있게 된다.
- https://docs.djangoproject.com/en/3.2/ref/models/relations/



## (2) 역참조

- 나를 참조하는(나를 외래 키로 지정한) 테이블을 참조하는 것
- 즉, 본인을 외래 키로 참조 중인 다른 테이블에 접근하는 것
-  1:N 관계에서는 1이 N을 참조하는 상황
  - 외래 키를 가지지 않은 1이 외래 키를 가진 N을 참조



- ```python
  article.comment_set.method()
  ```

  - Article 모델이 Comment 모델을 참조(역참조)할 때 사용하는 매니저
  - article.comment 형식으로는 댓글 객체를 참조 할 수 없다.
  - 대신 Django가 역참조 할 수 있는 comment_set manager를 자동으로 생성해 article.comment_set 형태로 댓글 객체를 참조할 수 있다.
    -  1:N 관계에서 생성되는 Related manger의 이름은 참조하는 `모델명_set` 이름 규칙으로 만들어진다.



- related_name

  ```python
  class Comment(models.Model):
      article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
  ```

  - ForeignKey 클래스의 선택 옵션
  - 역참조 시 사용하는 매니저 이름(model_set manager)을 변경할 수 있다.
  - 작성 후 마이그레이션 과정이 필요하다.
  - 선택 옵션이지만 상황에 따라 반드시 작성해야 하는 경우가 생기기도 하는데, 추후 알아볼 예정
  - 위와 같이 변경 하면 기존 article.comment_set은 더 이상 사용할 수 없고, article.comments로 대체된다.



# 5. 정리

1. 모델 정의 → Foreign Key
   - 대상 모델 (누구를 참조?)
   - 삭제 시 (대상이 사라지면?)

2. comment는 article을 참조, article은 comment를 역참조

   - comment.article → article 객체

   - article.comment_set.all() → comment 쿼리셋 (comment는 N이니까)

3. ModelForm 활용한 정의

   1. 요청 데이터(request.POST)를 모델 폼에 넣고
   2. 유효성 검사(is_valid)
   3. DB에 저장
      - 이때 값을 추가로 저장해야 한다.
      - `.save(commit=False)`는 인스턴스만 만들고, DB에 저장하지 않는다.
      - 인스턴스를 직접 조작해서, article_id를 함께 넣어준다. (comment.article = article)
      - 인스턴스.save()로 DB에 저장한다. → 위의 save()와 다르다. 이건 모델 인스턴스의 save, 위는 모델폼 인스턴스의 save