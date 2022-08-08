# 1. 코드 리뷰

## (1) 파리 퇴치

- https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq

- N × N 행렬을 탐색하면서, M × M 영역의 합을 구해나간다.

  이때, 인덱스 범위를 벗어나지 않기 위해 (N - M + 1) × (N - M + 1)만큼 반복한다.

  ```python
  for i in range(N - M + 1):
      for j in range(N - M + 1):
          # M × M 영역의 합
  ```

- 기준점이 (1, 1)이고 M = 2일 때, M × M 영역의 합 구하기

  ```python
  영역합 = 0
  for 행 in range(1, 3):
      for 열 in range(1, 3):
          영역합 += 리스트[행][열]
  ```

- M × M 영역의 합 구하는 법 일반화

  ```python
  최대영역합 = 0
  영역합 = 0
  
  for 행 in range(기준행, 기준행 + M):
      for 열 in range(기준열, 기준열 + M):
          if 행
          영역합 += 리스트[행][열]
          
  if 영역합 > 최대영역합:
      최대영역합 = 영역합
  ```

- 【코드】

  ```python
  max_ = 0
  
  # 이중 리스트를 순회하는 이중 반복문
  for i in range(N - M + 1):
      for j in range(N - M + 1):
          # 각 기준 좌표에서의 영역합 계산
          area = 0
          for r in range(i, i + M):
              for c in range(j, j + M):
                  area += lst[r][c]
                  
          if area > max_:
              max_ = area
  ```



## (2) 어디에 단어가 들어갈 수 있을까

- https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PuPq6AaQDFAUq

- 조건 1. 들어갈 수 있는 자리가 K여야 들어갈 수 있는 자리가 증가한다.

- 조건 2. 중간에 벽이 있으면 빈 공간의 수를 초기화한다.

- 조건 3. 벽 이전의 빈 공간의 수가 K개라면, 단어가 들어갈 수 있는 자리의 수 +1

- 【코드】

  ```python
  cnt = 0	# 자리의 수
  
  # 좌에서 우로
  for i in range(N):
      empty = 0	# 빈 공간의 수
      for j in range(N):
          if lst[i][j] == 0:
              empty += 1
          
          if lst[i][j] == 1:
              if empty == K:
                  cnt += 1
              empty = 0
              
      # 하나의 행을 다 탐색하고 나서,
      # 빈 공간의 수가 K개라면, 단어가 들어갈 수 있는 자리의 수 +1
      # (끝을 검사하는 조건문이 필요가 없었네..)
      if empty == K:
          cnt += 1
  ```



# 2. 이차원 리스트

## (1) 회전

> 180도, 270도는 이걸 2번, 3번 하면 OK

1. 왼쪽으로 90도 회전

   ```python
   for i in range(N):
       for j in range(N):
           rotated[i][j] = matrix[j][N - i - 1]
   ```

2. 오른쪽으로 90도 회전

   ```python
   for i in range(N):
       for j in range(N):
           rotated[i][j] = matrix[N - j - 1][i]
   ```



# 3. 완전 탐색 (Exhaustive Search)

## (1) 😱무식하게 다 해보기 (Brute-Force)

> 모든 경우의 수를 탐색하여 문제를 해결하는 방식

- 가장 단순한 풀이 기법이며, 단순 조건문과 반복문을 이용해 풀 수 있다.
- 복잡한 알고리즘보다, 아이디어를 어떻게 코드로 구현할 것인지가 중요하다.



- 【블랙잭 문제】

  1. 5장의 카드 `[5, 6, 7, 8, 9]` 중, 세 장의 카드의 합 `max_total`이 21을 넘지 않아야 한다.

     - 수학적 지식 없이, 그냥 3중 for문으로 무식하게 다 뽑는 게 Brute-force

     - 혹은 5장 중 3개를 순서 상관 없이 뽑음 → **조합 (Combination)**
     - 그리디 알고리즘 (Greedy)

  2. 코드

     ```python
     max_total = 0
     
     # 완전 탐색 (Brute-force)
     # n - 3까지 왔으면, 자동으로 n - 2과 n - 1의 카드도 뽑게 됨.
     for i in range(n - 2):
         # i 다음의 카드를 뽑으니까 i + 1
         # n - 2까지 왔으면, 자동으로 n - 1의 카드도 뽑게 된다.
         for j in range(i + 1, n - 1):
             # j 다음의 카드를 뽑으니까 j + 1
             # 끝까지 돈다.
             for k in range(j + 1, n):
                 total = cards[i] + cards[j] + cards[k]
                 
                 # 카드 세 장의 합이 m을 넘지 않으면서 가장 클 때
                 if max_total < total <= m:
                     max_total = total  
                     
                 # 합이 m과 같으면, 더이상 탐색하는 의미가 없으므로 바로 종료
                 if total == m:
                     return total
                 
     return max_total
     ```



## (2) 🚶델타 탐색 (Delta Search)

> 이차원 리스트의 모든 원소를 순회하며 (완전 탐색), 각 지점에서 상하좌우에 위치한 다른 지점을 조회하거나 이동하는 방식

- 이차원 리스트의 인덱스(좌표)의 조작을 통해 상하좌우 탐색을 한다.
- 이때, 행과 열의 변량인 -1, +1을 **델타(delta) 값**이라 한다.
- 델타 설정, 델타 순회, **경계 값**에 주의



- (개인적으로) 행은 y 또는 r로 나타내고, 열은 x 또는 c로 나타낸다.

  ```python
  # 순서대로 좌, 우, 상, 하
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  
  # 혹은, 헷갈리면 이렇게
  delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
  ```

- 상하좌우 + 대각선의 8방향 델타 값

  ```python
  dx = [-1, 1, 0, 0, -1, 1, -1, 1]
  dy = [0, 0, -1, 1, -1, -1, 1, 1]
  ```

  
