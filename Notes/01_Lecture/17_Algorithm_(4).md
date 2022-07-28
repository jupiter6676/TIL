# 1. 코드 리뷰 (220727)

## (1) 크로아티아 알파벳

- replace 메소드로 c=, c-, dz-, d-, lj, nj, s=, z=를 하나의 알파벳으로 취급
- 2개의 문자로 구성된 애들의 개수를 구해서, 총 문자열의 길이에서 빼 줌. 3개짜리는 2를 빼 줌.



## (2) 슈퍼마리오

- 버섯의 점수를 담는 배열과 누적 점수를 구하는 배열 생성

- 각각의 누적 점수가 100과 가까운지 어떻게 알 수 있을까?

  - 누적 점수와 100의 차이가 작을수록 100과 가깝다.

  - 그 차이(절댓값)을 저장하는 변수

  - 가장 작은 차이는, 순회하면서 min_ 변수에 갱신

    ```python
    for 점수 in 점수리스트:
        누적점수 += 점수
        
        차이 = abs(100 - 누적점수)
        
        if 차이 < 가장작은차이:
            가장작은차이 = 차이
            가장큰누적점수 = 누적점수
    ```

  - 만약 100에 가까운 수가 2개라면, 마리오는 큰 값을 선택

    ```python
    for 점수 in 점수리스트:
        누적점수 += 점수
        
        차이 = abs(100 - 누적점수)
        
        # 등호 하나를 붙여서, 차이가 같을 때도 값을 갱신
        # 차이는 같지만, 순회를 할수록 누적 점수가 커지기 때문에
        if 차이 <= 가장작은차이:
            가장작은차이 = 차이
            가장큰누적점수 = 누적점수
    ```

- 모든 코드

  ```python
  import sys
  sys.stdin = open("슈퍼마리오.txt")
  
  N = 10	# 10개의 정수
  scores = list()	# 점수 저장 리스트
  
  # 점수 입력
  for i in range(N):
      score = int(input())
      scores.append(score)
      
  prefix_sum = 0
  min_diff = 10e9	# 가장 작은 차이
  max_score = 0	# 가장 큰 누적 점수
  
  for i in range(N):
      prefix_sum += score[i]	# 누적합
      diff = abs(100 - prefix_sum)
      
      # 차이가 이전의 가장 작은 차이보다 작거나 같을 때
      if diff <= min_diff:
          # 가장 작은 차이와, 가장 큰 누적 점수를 갱신한다.
          min_diff = diff
          max_score = prefix_sum
  ```



## (3) 덩치

- 자신보다 덩치가 큰 사람의 수를 카운트하는 배열

- 자신보다 덩치가 큰 사람을 만나면, 그 배열의 값을 1씩 증가시킨다.

  ```python
  import sys
  sys.stdin = open('_덩치.txt')
  
  N = int(input())	# 사람의 수 N
  
  wh = list()	# (몸무게, 키)
  for i in range(N):
      w, h = map(int, input().split())
      wh.append((w, h))
      
  ranks = [0] * N
  
  # 모든 사람을 비교하기 위한 이중 반복문
  for a in range(N):
      A = wh[a]	# 기준이 되는 사람
      
      for b in range(N):
          B = wh[b]	# 비교가 되는 사람
          
          # A가 B보다 덩치가 크면
          # B가 A보다 덩치가 작다.
          # 즉, B보다 덩치가 큰 사람의 수 1 증가
          if A[0] > B[0] and A[1] > B[1]:
              ranks[b] += 1
         
  # 등수는 덩치 큰 사람의 수 +1
  for rank in ranks:
      print(rank + 1, end=' ')
  ```



# 2. 딕셔너리 (Dictionary)

> Non-sequence & Key-Value

- 순서가 있으면 무조건 iterable
  - 그러나 순서가 없다고 iterable이 아닌 건 X
  - ex) 딕셔너리
- Key는 Immutable, Unique



## (1) 해시 테이블

> 파이썬에서는 딕셔너리라고 부르지만, 보통 다른 언어에서는 '**해시 테이블**'이라는 학술적 이름으로 불림.

- [아무거나 입력하면 해시 값으로 랜덤한 16진수로 반환해주는 사이트](https://emn178.github.io/online-tools/sha256.html)
  - 16진수 값이 엄청 크기 때문에, 해시 값이 웬만하면 겹치지 X

- **해시 함수**: 임의 길이의 데이터를 고정 길이의 데이터로 매핑하는 함수
- 해시: 해시 함수를 통해 얻어진 값



- 파이썬의 딕셔너리
  - 해시 함수와 해시 테이블을 이용한다.
  - 따라서, **삽입, 삭제, 수정, 조회 연산(CRUD)의 속도가 리스트보다 빠르다.**



- 딕셔너리 vs 리스트

  |  연산 종류  | Dictionary |     List     |
  | :---------: | :--------: | :----------: |
  |  Get Item   |    O(1)    |     O(1)     |
  | Insert Item |    O(1)    | O(1) or O(N) |
  | Update Item |    O(1)    |     O(1)     |
  | Delete Item |    O(1)    | O(1) or O(N) |
  | Search Item |    O(1)    |     O(N)     |

  - Insert: 리스트는 끝에서 넣을 때 O(1), 중간에 넣을 때 O(N)
  - 딕셔너리는 **key로 바로 조회**할 수 있기 때문에, 인덱스 접근과 같이, 모든 연산의 시간 복잡도가 O(1)이다.



## (2) 딕셔너리 기본 문법

1. 기본적 사용

   - 선언

     ```python
     a = {
         'name': 'Kyle',
         'gender': 'male',
         'address': 'Seoul',
     }
     ```

   - 삽입 / 수정

     ```python
     a['job'] = 'coach'	# 해당 key가 없으면 삽입
     a['address'] = 'Busan'	# 해당 key가 있으면 수정
     ```

   - 삭제

     ```python
     gender = a.pop('gender')	# value 삭제 및 반환
     phone = a.pop('phone')	# 해당 key가 없으면 KeyError
     ```

   - 조회

     ```python
     print(a['name'])
     print(a.get('name'))
     
     print(a['phone'])	# 해당 key가 없으면 KeyError
     print(a.get('phone'))	# 해당 key가 없으면 None 반환
     ```



## (3) 딕셔너리 메소드

> 기본적으로, 딕셔너리를 순회할 때 key를 순회한다.
>
> 하지만 메소드를 통해 iterable하게 만들어줄 수 O

```python
john = {'name': 'john', 'role': 'ceo'}

for element in john:
    # print(element, end=' ')	# name role
    print(john[element], end=' ')	# john ceo
```



1. `.keys()`
   - 딕셔너리의 key 목록이 담긴 dict_keys 객체 반환

2. `.values()`
   - 딕셔너리의 value 목록이 담긴 dict_values 객체 반환

3. `.items()`
   - 딕셔너리의 (key, value) 쌍의 목록이 담긴 dict_items 객체 반환



## (4) 카운트 문제

- 딕셔너리는 카운트 문제에 자주 쓰인다.

  ```python
  scores = ['A', 'A', 'B', 'C', 'D', 'A', 'B']
  dict_ = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
  
  for score in scores:
      dict_[score] += 1
  ```

  

- 흑마법으로 Counter를 사용할 수도 있다.

  ```python
  from collections import Counter	# 흑마법...
  
  scores = ['A', 'A', 'B', 'C', 'D', 'A', 'B']
  
  easy_counter = Counter(scores)
  print(easy_counter)	# Counter({'A': 3, 'B': 2, 'C': 1, 'D': 1})
  ```

  ```python
  # 초 흑마법
  print(Counter(scores).most_common())
  ```

  
