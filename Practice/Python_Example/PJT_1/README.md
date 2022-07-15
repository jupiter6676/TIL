# 프로젝트 01 - 파이썬 기반 데이터 활용

## 후기

- 파일 입출력은 언어마다 꼭 한 번씩은 하게 되는 것 같은데, 파이썬이 젤 간결한 것 같다.. 자바가 제일 어렵다. 함수 기억이 하나도 나지 않는다.

- 0번
  
  - 파일을 쓸 때는 `f.write()`
  
  - 줄바꿈 하려면 맨 뒤에 '\n'

- 1번
  
  - txt 파일에서 한 줄씩 읽으려면 `for line in f` (여기서 f는 파일)
  
  - line.strip()으로 뒤의 개행 문자를 지워야 함.

- 2번
  
  - if 'berry' in fruit 했다가, 마지막이 berry로 끝나는 걸로 해야해서
  
  - fruit.strip()으로 개행 지워주고
  
  - fruit[:-5]까지 문자들 붙인 문자열 만들고 berry랑 비교

- 4번
  
  - 수업시간에 강사님께서 짜주신 코드 그대로 했다..

- 5, 6번
  
  - 6번 → [[Python] list에서 dictionary 정렬](https://inma.tistory.com/138)을 참고하였다.
  
  - 결과는 제대로 출력되는데, for문을 너무 많이 중첩시킨 것 같아서 마음에 들지 않는다.
  
  - 딕셔너리의 특성과 관련 메소드를 잘 활용하면 피할 수 있을 것 같은데 잘 모르겠다..
  
  - 어떻게 개선해야 할까?

## 코드

- **05.py**의 `movie_info()` 함수
  
  ```python
  # movie: dict, genres: list
  def movie_info(movie, genres):
      genre_ids = movie.get('genre_ids')  # [18, 80]
      genre_names = list()
  
      # id의 개수만큼 for문 → 해당 id가 genres에 있는지 검색
      for id in genre_ids:
          for g in genres:    # g: dict, genres: list
              if id == g.get('id'):
                  genre_names.append(g.get('name'))
  
      info = {
          'genre_names': genre_names,
  
          'id': movie.get('id'),
          'overview': movie.get('overview'),
          'title': movie.get('title'),
          'vote_average': movie.get('vote_average')
      }
  
      return info
  ```

- **06.py**의 `movie_info()` 함수
  
  ```python
  # movies, genres: list
  def movie_info(movies, genres):
      # 별점이 높은 순서대로, 리스트 속 딕셔너리 정렬
      movies_sorted_by_vote = sorted(movies, key=itemgetter('vote_average'), reverse=True)
  
      info = dict()
      movies_info_list = list()
  
      # 정렬된 리스트 속 딕셔너리 탐색
      for m in movies_sorted_by_vote:
          genre_ids = m.get('genre_ids')  # [18, 80]
          genre_names = list()
  
          # id에 따른 장르 이름 리스트 반환
          for id in genre_ids:
              for g in genres:
                  if id == g.get('id'):
                      genre_names.append(g.get('name'))
  
          # 영화마다 필요한 정보 담기
          info = {
              'genre_names': genre_names,
              'id': m.get('id'),
              'overview': m.get('overview'),
              'title': m.get('title'),
              'vote_average': m.get('vote_average')
          }
  
          # 영화 정보들이 담긴 딕셔너리를 리스트에 추가
          movies_info_list.append(info)
  
      return movies_info_list
  ```