# 1. QuerySet API

## (1) 종류

- gt (초과), gte (이상)

  ```python
  Entry.objects.filter(id__gt=4)	# greater than
  Entry.objects.filter(id__gte=4)	# greater than equal
  ```

  ```sql
  SELECT ... WHERE id > 4;
  SELECT ... WHERE id >= 4;
  ```

- lt (미만), lte (이하)

  ```python
  Entry.objects.filter(id__lt=4)
  Entry.objects.filter(id__lte=4)
  ```

  ```sql
  SELECT ... WHERE id < 4;
  SELECT ... WHERE id <= 4;
  ```



- in

  ```python
  Entry.objects.filter(id__in=[1, 3, 4])
  Entry.objects.filter(headline__in='abc')
  ```

  ```sql
  SELECT ... WHERE id IN (1, 3, 4);
  SELECT ... WHERE headline IN ('a', 'b', 'c')
  ```



- startswith

  ```python
  Entry.objects.filter(headline__startswith='Lennon')
  ```

  ```sql
  SELECT ... WHERE headline LIKE 'Lennon%';
  ```

- istartswith (대소문자 구분 X)

  ```python
  Entry.objects.filter(headline__istartswith='Lennon')
  ```

  ```sql
  SELECT ... WHERE headline ILIKE 'Lennon%';
  ```

- contains

  ```python
  Entry.objects.filter(headline__contains='Lennon')
  Entry.objects.filter(headline__icontains='Lennon')
  ```

  ```sql
  SELECT ... WHERE headline LIKE '%Lennon%';
  SELECT ... WHERE headline ILIKE '%Lennon%';
  ```



- range

  ```python
  import datetime
  start_date = datetime.date(2005, 1, 1)
  end_date = datetime.date(2005, 3, 31)
  Entry.objects.filter(pub_date__range=(start_date, end_date))
  ```

  ```sql
  SELECT ... WHERE pub_date
  BETWEEN '2005-01-01' AND '2005-03-31'
  ```



- all

  ```python
  Entry.objects.all()[0]
  Entry.objects.all()[m : n]
  ```

  ```sql
  SELECT ... LIMIT 1;
  SELECT ... LIMIT (n - m) OFFSET m;
  ```



- order_by

  ```python
  Entry.objects.order_by('id')
  Entry.objects.order_by('-id')
  ```

  ```sql
  SELECT ... ORDER BY id;
  SELECT ... ORDER BY id DESC;
  ```



## (2) 활용

- 복합 활용

  ```python
  inner_qs = Blog.objects.filter(name__contains='Cheddar')
  entries = Entry.objects.filter(blog__in=inner_qs)
  ```

  ```sql
  SELECT ... 
  WHERE blog.id IN
  	(SELECT id FROM ... WHERE name LIKE '%Cheddar%')
  ```



- .query

  ```python
  In [1]: print(Genre.objects.all().query)
  SELECT "db_genre"."id", "db_genre"."name" FROM "db_genre"
  
  In [2]: print(Genre.objects.order_by('-id'.query)
  SELECT "db_genre"."id", "db_genre"."name" FROM "db_genre" ORDER BY "db_genre"."id" DESC
               
  In [3]: print(Genre.objects.get(id=1).query)
  # AttributeError → get은 개별 인스턴스를 반환하기 때문에
  ```



# 2. ORM 확장 (1: N)

## (1) ERD

- 장르 ↔ 앨범 ↔ 아티스트

- 모델링

  ```python
  class Genre(models.Model):
      name = models.CharField(max_length=30)
      
  class Artist(models.Model):
      name = models.CharField(max_length=30)
      debut = models.DateField()
      
  class Album(models.Model):
      name = models.CharField(max_length=30)
      
      # ForeignKey는 테이블의 필드 이름에 자동으로 '_id'가 붙어서 생성된다.
      genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
      artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
  ```



## (2) **models.ForeignKey** 필드

- 2개의 필수 위치 인자
  - Model class: 참조하는 모델
  - **on_delete**: 외래 키가 참조하는 객체가 삭제되었을 때 처리 방식
    - CASCADE: 부모 객체(참조 된 객체)가 삭제됐을 때, 이를 참조하는 객체도 삭제 (글이 지워지면 댓글을 지워야 한다.)
    - PROTECT:  삭제되지 않는다. (댓글이 있으면 글을 지우지 못한다.)
    - SET_NULL: NULL 설정
    - SET_DEFAULT: 기본 값 설정
    - …

- Foreign Key (외래 키)
  - 키를 사용하여 부모 테이블의 유일한 값을 참조 (참조 무결성)
    - DB 관계 모델에서, 관련된 2개의 테이블 간의 일관성
  - 외래 키의 값이 반드시 부모 테이블의 기본 키일 필요는 없지만, 유일한 값이어야 한다.



## (3) 예제

- album에 genre는 어떻게 추가해야 할까?

  ```python
  # 1. Genre 인스턴스를 만든 후, album의 genre에 넣어준다.
  album = Album()
  
  genre = Genre.objects.get(id=1)
  album.genre = genre
  
  album.artist = Artist.objects.get(id=1)
  album.save()
  
  # 2. 혹은 값을 통해 넣어준다.
  album = Album()
  
  album.genre_id = 2
  album.artist_id = 2
  album.name = '미아'
  album.save()
  ```

  - 위와 같이 하면, album 테이블의 genre(genre_id)와 artist(artist_id)에는 객체가 아닌, id가 저장된다.



- **N → 1 (참조)** ❤️

  ```python
  # 앨범의 id가 1인 것의 장르의 이름은?
  album = Album.objects.get(id=1)	# 앨범 객체
  
  album.genre	# 장르 객체
  album.genre.name	# 장르의 이름
  ```

  	- 앨범 입장에서, 장르와 아티스트를 직접 참조할 수 있다.
  	- 그래서 `album.genre`, `album.artist`를 통해 인스턴스 객체를 참조할 수 있다.



- **1 → N (역참조)** 💙

  ```python
  # id가 1인 장르의 모든 앨범은?
  g1 = Genre.objects.get(id=1)
  g1.album_set.all()	# album의 인스턴스 객체
  ```

  - 장르에서 앨범을 역으로 참조하고 있다.
  - 별도의 설정이 없다면, 역참조 시에는 항상 `_set`을 붙인다.
  - 그래서 `genre.album_set.all()`을 통해, album의 인스턴스가 담긴 **Query Set** (1: N이기 때문에)을 받아올 수 있다.