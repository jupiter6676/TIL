# 1. 모듈

## (1) 파이썬 표준 라이브러리

- 파이썬에 기본적으로 설치된 모듈과 내장 함수
1. datetime
   
   ```python
   import datetime
   
   now = datetime.datetime.now()
   print(now)    # 2022-07-15 10:17:46.104175
   print(type(now))    # <class 'datetime.datetime'
   ```

2. random
   
   ```python
   import random
   
   # 1 ~ 45까지의 숫자
   # 그 중 6개
   nums = random.sample(range(1, 46), 6)
   print(nums, type(nums))    # [2, 20, 13, 5, 33, 29] <class 'list'>
   ```

# 2. 파일 입출력

1. with 키워드
   
   - 도중에 예외가 발생하더라도, 스위트가 종료될 때 파일이 올바르게 닫힌다.
   
   - 즉, 코드 블럭이 종료되면, close() 하지 않아도 된다.
     
     ```python
     # 파일을 쓰기 모드로 열기 (없으면 생성)
     with open('test.txt', 'w', encoding='utf-8') as f:
         f.write('Happy Hacking!\n')
         f.write('1번 줄\n')
         f.write('2번 줄\n')
     ```
     
     ```python
     # 파일명, 모드, 인코딩
     with open('students.txt', 'r', encoding='utf-8') as f:
         text = f.read()    # txt 통으로 가져옴.
         print(text, type(text))    # 타입은 str
     
         # 김씨인 사람만 찾기
         names = text.split()
         cnt = 0
         for name in names:
             if name[0] == '김':    # name.startswith('김')
                 cnt += 1
     
         print(cnt)
     ```
     
     ```python
     # 파일명, 모드, 인코딩
     with open('students.txt', 'r', encoding='utf-8') as f:
         line = f.readline()    # 한 줄씩 가져옴.
         print(text)
     
         # 파일에서 모든 줄들을 읽기
         for line in f:
             print(line, end='')
     
         print(cnt)
     ```
     
     ```python
     with open('students.txt', 'r', encoding='utf-8') as f:
         lines = f.readlines()
         print(lines)    # ['김OO\n', '최OO\n'] 이렇게 개행이 들어간다.
         print(type(lines))    # <class 'list'>
     ```

2. `json`
   
   ```python
   import json
   from pprint import pprint
   
   # 파일을 열고
   with open('stocks.json', 'r', encoding='utf-8') as f:
       # .json을 파이썬 객체 형식으로 만듦
       kospi_dict = json.load(f)
       samsung = kospi_dict['stocks'][0]
   
       print(samsung, type(samsung))    # 삼성전자의 모든 key-value, 타입은 dict
   
       # 삼성 딕셔너리 중, stockName, closePrice 정보만 가진 딕셔너리 만들기
       res = {
           'stockName': samsung.get('stockName'),
           'closePrice': samsung.get('closePrice'),
       }
   ```
