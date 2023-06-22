# 1. 코드 리뷰

## (1) 유니크

- https://www.acmicpc.net/problem/5533

- 중복은 set을 사용? → 이 문제에선 X

- 행이 참가자들, 열이 자신이 낸 점수라 탐색 시 세로로 먼저 봐야 함.

- 그게 좀 익숙치 않으니까 행을 전치시켜줄 수 있다.

  ```python
  열_리스트 = []
  for x in range(3):
      열 = []
      for y in range(5):
          열.append(리스트[y][x])
          
      열_리스트.append(열)
  ```

- 한 행 (한 게임 당 참가자들이 낸 점수들)

  ```python
  for x in range(3):
      열 = 열_리스트[x]
      for y in range(5):
          점수 = 열[y]
          
          if 열.count(점수) == 1:
              점수_리스트[y] += 점수
  ```

- 【코드】

  ```python
  lst = [[100, 99, 98],
         [100, 97, 92],
         [63, 89, 63],
         [99, 99, 99],
         [89, 97, 98]]
  
  col_list = list()
  
  # 리스트를 90도 회전
  for x in range(3):
      col = []
      for y in range(5):
          col.append(lst[y][x])
          
      col_list.append(col)
      
  # 친구들의 점수 리스트
  score_list = [0] * 5
  
  for y in range(3):
      col = col_list[y]
      for x in range(5):
          # 친구의 점수
          score = col[x]
          # 친구의 점수가 리스트에서 1개일 때
          if col.count(score) == 1:
              score_list[x] += score
              
  print(score_list)
  ```



## (2) 2차원 배열의 합

- https://www.acmicpc.net/problem/2167

- 【코드】

  ```python
  for r in range(i - 1, x):
      for c in range(j - 1, y):
          sum_ += list_[r][c]
  ```

- python3: 메모리 사용이 적고, 속도가 느리다.

- **pypy3**: 메모리 사용이 많고, 속도가 빠르다.

- 누적합을 이용하는 더 빠른 코드도 있지만, 브론즈 1 급은 아니라고...

  - 만약 4 ×4 크기의 2차원 배열에서 누적합 (2, 1)은
  - (1, 1) + (1, 2) + (1, 3) + (1, 4) + (2, 1)이 아니라
  - (1, 1) + (2, 1)이다. 늘 사각형 모양.
  - [부분합 구하기 : 누적합만 들고 있으면 된다.](https://codingdog.tistory.com/entry/부분합-구하기-누적합만-들고-있으면-된다)



# 2. 이차원 리스트

## (1) 순회

1. 이차원 리스트 단순 출력

      ```python
      matrix = [
          [1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 0, 1, 2]
      ]
      
      print(matrix)	# 단순 출력
      ```



2. 이차원 리스트의 모든 요소를 행렬처럼 출력

    - 이중 for문을 이용한 **행 우선 순회**

      ```python
      # N × M
      N = len(matrix)
      M = len(matrix[0])

      # 방법 1
      for i in range(N):
          for j in range(M):
              print(matrix[i][j], end=' ')
          print()

      # 방법 2
      for row in matrix:
          for elem in row:
              print(elem, end=' ')
          print()
      ```

    - 이중 for문을 이용한 **열 우선 순회**

      ```python
      for j in range(M):
          for i in range(N):
              print(matrix[i][j], end=' ')
          print()
      ```



3. 이차원 리스트의 총합 구하기

    - 순회를 이용

      ```python
      total = 0

      # 방법 1 → O(NM)
      for i in range(N):
          for j in range(M):
              total += matrix[i][j]

      # 방법 2 → O(NM)
      for row in matrix:
          total += sum(row)
      ```

    - Pythonic한 방법

      ```python
      # map(sum, matrix)
      # 각 행의 합이 담긴 맵 객체 → matrix = [10, 26, 12]
      # 방법 3 → O(NM)
      total = sum(map(sum, matrix))
      ```



4. 이차원 리스트의 최댓값, 최솟값 구하기

   - 행 우선 순회를 이용

     ```python
     max_val = 0
     # min_val = 99999999
     
     for i in range(N):
         for j in range(M):
             # if matrix[i][j] < min_val
             #	min_val = matrix[i][j]
             if matrix[i][j] > max_val:
                 max_val = matrix[i][j]
     ```

   - Pythonic한 방법

     ```python
     # 방법 2 → O(NM)
     max_value = max(map(max, matrix))
     min_value = min(map(min, matrix))
     ```



## (2) 전치 (Transpose)

> 행과 열을 서로 맞바꾸는 것

```python
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]
]

# 행과 열 맞바꾸기
# 즉, 열 우선 순회 = 전치 행렬
matrix_t = [
    [1, 5, 9],
    [2, 6, 0],
    [3, 7, 1],
    [4, 8, 2]
]
```



## (3) 회전 (Rotate)

> 행렬을 돌리는 것

- 문제에서 이차원 리스트를 왼쪽, 오른쪽으로 N도 회전하는 경우가 존재한다.
- 고개를 돌린다...
