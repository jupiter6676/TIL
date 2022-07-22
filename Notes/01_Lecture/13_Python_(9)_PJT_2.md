# 1. 프로젝트 02

## (1) API

- Application Programming Interface
- 응용 프로그램 인터페이스
- 프로그램으로 제어를 한다.



- API를 사용하기 전에 확인해야 할 것
  - 정보를 원하는 사람이 **Url 주소로 요청**
  - 정보를 주는 사람이 **JSON 문서로 응답**



## (2) API 활용 시 확인 사항

- 요청 방식 이해
  - 인증 방식
  - URL 생성
    - 기본 주소
    - 원하는 기능에 대한 추가 경로
    - 요청 변수 (필수/선택)
- 응답 결과 이해
  - 응답 결과 타입 (JSON)
  - 응답 결과 구조



## (3) API 활용 예시

1. Bithumb

   ```json
   {
       "status": "0000",
       
       "data": {
           "BTC": {
               "opening_prise": "2497",
               "closing_prise": "2497",
           },
           "ETC": {
               "opening_prise": "2497",
               "closing_prise": "2497",
           },
           
           "date": "12345365"
       }
   }
   ```

   ```python
   import requests
   
   order_currency = 'ALL'
   payment_currency = 'KRW'
   URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'
   
   # URL로 요청을 해서, JSON으로 응답 받아옴.
   response = requests.get(URL).json
   coins = response.get('data')
   
   # coins: 딕셔너리
   # key: coin 이름
   # value: 딕셔너리(코인의 정보)
   for coin in coins:
       # 이물질
       if coin == 'date':
           continue
           
       # coins.get(coin): 코인의 정보인 딕셔너리
       # 그 딕셔너리의 closing price
       print(coin, coins.get(coin).get('closing_price'))
       
   ```

   

2. agify

   ```python
   import requests
   
   URL = 'https://api.agify.io'
   params = {
       'name': 'john'
   }
   
   response = requests.get(URL, params=params).json()
   print(response)	# {'name': 'john', 'age': xx, 'count': xx}
   ```



## (4) TMDB API 활용 예시

```python
import requests

BASE_URL = 'https://api.themoviedb.org/3'
path1 = '/movie/76341'	# /movie/{movie_id}
path2 = '/movie/popular'

# Query String
params = {
    'api_key': 'xxxxxxxxxxxxxxxxxxxxxx',
    'language': 'ko-KR'	# optional
}

response = requests.get(BASE_URL + path, params=params).json()
print(response)
```



## (5) 도전과제

```python
# 랜덤 번호 하나 고르고
# 내가 실제로 이 번호로 1024회 동안 샀으면
# 얼마나 당첨되었을까?
# 1 ~ 5등
URL = f'https://www.dhlottery.co.kr/common,do?method=getLottoNumber&drwNo={n}'
```



# 2. 참고

- [TMDB 사이트](https://www.themoviedb.org/?language=ko)
- [Requests: HTTP for Humans™](https://requests.readthedocs.io/en/latest/)