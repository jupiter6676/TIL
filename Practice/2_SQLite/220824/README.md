# 데이터베이스 07 - ORM

<aside>
💡 코드를 작성한 실습 파일을 압축해서 실라버스에 제출해주세요.


</aside>

### 1. `db/models.py` 파일에 아래의 모델 2개 `Director` `Genre` 를 작성하세요.

> 기본 코드

```python
class Director(models.Model):
    name = models.TextField()
    debut = models.DateTimeField()
    country = models.TextField()

class Genre(models.Model):
    title = models.TextField()
```



### 2. 모델을 마이그레이트(migrate) 하세요.

```bash
# 가상환경 실행 확인 후 아래 명령어를 터미널에 입력합니다.
python manage.py makemigrations

python manage.py migrate
```



### 3. Queryset 메소드 `create` 를 활용해서  `Director` 테이블에 아래 데이터를 추가하는 코드를 작성하세요.

| name            | debut      | country |
| --------------- | ---------- | ------- |
| 봉준호          | 1993-01-01 | KOR     |
| 김한민          | 1999-01-01 | KOR     |
| 최동훈          | 2004-01-01 | KOR     |
| 이정재          | 2022-01-01 | KOR     |
| 이경규          | 1992-01-01 | KOR     |
| 한재림          | 2005-01-01 | KOR     |
| Joseph Kosinski | 1999-01-01 | KOR     |
| 김철수          | 2022-01-01 | KOR     |

> 코드 작성

```python
Director.objects.create(name='봉준호', debut='1993-01-01', country='KOR')

Director.objects.create(name='김한민', debut='1999-01-01', country='KOR')

Director.objects.create(name='최동훈', debut='2004-01-01', country='KOR')

Director.objects.create(name='이정재', debut='2022-01-01', country='KOR')

Director.objects.create(name='이경규', debut='1992-01-01', country='KOR')

Director.objects.create(name='한재림', debut='2005-01-01', country='KOR')

Director.objects.create(name='Joseph Kosinski', debut='1999-01-01', country='KOR')

Director.objects.create(name='김철수', debut='2022-01-01', country='KOR')
```



### 4. `인스턴스 조작` 을 활용하여`Genre` 테이블에 아래 데이터를 추가하는 코드를 작성하세요.

| title  |
| ------ |
| 액션   |
| 드라마 |
| 사극   |
| 범죄   |
| 스릴러 |
| SF     |
| 무협   |
| 첩보   |
| 재난   |

> 코드 작성

```python
genre = Genre()
genre.title = '액션'
genre.save()

genre = Genre()
genre.title = '드라마'
genre.save()

genre = Genre()
genre.title = '사극'
genre.save()

genre = Genre()
genre.title = '범죄'
genre.save()

genre = Genre()
genre.title = '스릴러'
genre.save()

genre = Genre()
genre.title = 'SF'
genre.save()

genre = Genre()
genre.title = '무협'
genre.save()

genre = Genre()
genre.title = '첩보'
genre.save()

genre = Genre()
genre.title = '재난'
genre.save()
```

```python
# 반복문
genres = ['액션', '드라마', '사극']

for genre_name in genres:
    genre = Genre()
    genre.title = genre_name
    genre.save()
```



### 5. Queryset 메소드 `all` 을 활용해서 `Director` 테이블의 모든 데이터를 출력하는 코드를 작성하세요.

> 출력 예시

```
봉준호 1993-01-01 00:00:00 KOR
김한민 1999-01-01 00:00:00 KOR
최동훈 2004-01-01 00:00:00 KOR
이정재 2022-01-01 00:00:00 KOR
이경규 1992-01-01 00:00:00 KOR
한재림 2005-01-01 00:00:00 KOR
Joseph Kosinski 1999-01-01 00:00:00 KOR
김철수 2022-01-01 00:00:00 KOR
```

> 코드 작성

```python
directors = Director.objects.all()

for director in directors:
    print(director.name, director.debut, direcor.country)
```



### 6. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `id` 가 1인 데이터를 출력하는 코드를 작성하세요.

> 출력 예시

```
봉준호 1993-01-01 00:00:00 KOR
```

> 코드 작성

```python
director = Director.objects.get(id=1)

print(director.name, director.debut, director.country)
```



### 7. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `country` 가 USA인 데이터를 출력하는 코드를 작성하세요.

> 코드 작성

```python
director = Director.objects.get(country='USA')
```



### 8. 위 문제에서 오류가 발생합니다. 출력된 오류 메세지와 본인이 생각하는 혹은 찾은 오류가 발생한 이유를 작성하세요.

> 오류 메세지

```bash
DoesNotExist: Director matching query does not exist.
```

> 이유 작성

```
country가 USA인 행이 존재하지 않는다.
```



### 9. Queryset 메소드 `get` 과 `save` 를 활용해서 `Director` 테이블에서  `name` 이 Joseph Kosinski인 데이터를 조회해서 `country` 를 USA 로 수정하고, 출력하는 코드를 작성하세요.

> 출력 예시

```
Joseph Kosinski 1999-01-01 00:00:00 USA
```

> 코드 작성

```python
director = Director.objects.get(name='Joseph Kosinski')

director.country = 'USA'
director.save()
```



### 10. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `country` 가 KOR인 데이터를 출력하는 코드를 작성하세요.

> 코드 작성

```python
director = Director.objects.get(country='KOR')
```



### 11. 위 문제에서 오류가 발생합니다. 출력된 오류 메세지와 본인이 생각하는 혹은 찾은 오류가 발생한 이유를 작성하세요.

> 오류 메세지

```bash
MultipleObjectsReturned: get() returned more than one Director -- it returned 7!
```

> 이유 작성

```
get()은 하나의 값만 반환해야 하는데, country가 KOR인 행이 하나보다 많다.
```



### 12. Queryset 메소드 `filter` 를 활용해서 `Director` 테이블에서 `country` 가 KOR인 데이터를 출력하는 코드를 작성하세요.

> 출력 예시

```
봉준호 1993-01-01 00:00:00 KOR
김한민 1999-01-01 00:00:00 KOR
최동훈 2004-01-01 00:00:00 KOR
이정재 2022-01-01 00:00:00 KOR
이경규 1992-01-01 00:00:00 KOR
한재림 2005-01-01 00:00:00 KOR
김철수 2022-01-01 00:00:00 KOR
```

> 코드 작성

```python
directors = Director.objects.filter(country='KOR')

for director in directors:
    print(director.name, director.debut, director.country)
```



### 13. 본인이 생각하는 혹은 찾은 `get` 과 `filter` 의 차이를 작성하세요.

```
get()은 하나의 값만 반환하고, filter()는 여러 개의 값을 반환할 수 있다.
```



### 14. Queryset 메소드 `get` 과 `delete`를 활용해서  `Director` 테이블에서 `name` 이 김철수인 데이터를 삭제하는 코드를 작성하세요.

> 코드 작성

```python
director = Director.objects.get(name='김철수')

director.delete()
```
