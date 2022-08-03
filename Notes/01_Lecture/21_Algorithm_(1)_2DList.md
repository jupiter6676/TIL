# 1. 코드 리뷰

## (1) 절댓값 힙

- https://www.acmicpc.net/problem/11286

- 힙의 가장 작은 요소는 항상 루트인 `heap[0]`이다.

- heappush 시 리스트 속 리스트를 넣는다면?

  - [[1, 3], [1, 1], [2, -1], [3, -2]]
  - 처음에 [1, 3]이 들어가고, 후에 [1, 1]이 들어온다.
  - 그러면 둘의 0번째 인덱스를 비교하고, 1로 같으니 그 뒤의 1번째 인덱스를 비교한다.
  - [1, 1]이 더 작으므로 맨 앞으로 온다.
  - [2, -1]이 들어오면, 둘의 0번째 인덱스를 비교한다.
  - 1 < 2 이므로, [1, 1]이 그대로 앞에 위치해 있다.

- 그래서 이 문제에서는 **[절댓값 x, 실제 x]** 쌍을 heappush해주면 된다.

- 출력은 실제 값으로 해야 하니, pop한 거의 1번째 인덱스를 출력한다.

  ```python
  heappush(heap, [abs(x), x])
  
  root = heappop(heap)
  print(root[1])
  ```

- 【코드】

  ```python
  # heappop 값을 뺄 때
  root = heappop(heap)
  print(root[1])
  
  # heappush 값을 넣을 때
  heappush(heap, [abs(x), x])
  ```



## (2) 인사성 밝은 곰곰이

- https://www.acmicpc.net/problem/25192
- ENTER 이후에 새로운 닉네임이 들어오는지 판단
- 즉, 중복된 닉네임이 들어오는지 판단
  - 딕셔너리, 세트를 사용하면, **중복을 탐색할 때 1 만큼의 시간**이 필요하다.
  - 리스트도 가능하지만, 중복을 탐색할 때 N 만큼의 시간이 필요하다.

- 해당 닉네임이 세트에 없을 때만 닉네임 추가, 곰 +1

  ```python
  if 닉네임 not in set:
      set.add(닉네임)
  	곰 += 1
  ```

- ENTER가 들어오면, 세트 초기화

  ```python
  if 닉네임 == 'ENTER':
      set.clear()
  ```

- 【코드】

  ```python
  set_ = set()
  
  for log in log_list:
      if log == 'ENTER':
          set_.clear()
          
      # 닉네임 = log
      if log not in set_:
          set_.add(log)
          gom += 1
          
  print(gom)
  ```



# 2. 이차원 리스트

> 이차원 리스트(행렬)는 세상을 표현하는 방식이다.
>
> 벡터, 암호 등...



## (1) 개념

- 이차원 리스트는 리스트를 원소로 가지는 리스트일 뿐이다.

  ```python
  matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  ```

- 첫 번째 행에 접근 → `matrix[0]` (= [1, 2, 3])

- 첫 번째 행의 첫 번째 열에 접근 → `matrix[0][1]` (= 1)



## (2) 이차원 리스트 만들기

> 특정 값으로 초기화 된 4 × 3 이차원 리스트 만들기

1. ~~직접 작성~~

   ```python
   matrix = [
       [0, 0, 0],
       [0, 0, 0],
       [0, 0, 0],
       [0, 0, 0],
   ]
   ```



2. 반복문으로 작성 

   ```python
   row, col = 4, 3
   matrix = []
   
   for _ in range(row):
       matrix.append([0] * col)
   ```



3. 리스트 컴프리헨션으로 작성

   ```python
   row, col = 4, 3
   
   # row × col 행렬
   # 넣는 식(열)을 앞에, 조건·반복문(행)을 뒤에
   matrix = [[0] * col for _ in range(row)]
   ```

   

4. 리스트 컴프리헨션 vs 리스트 곱셈 연산

   ```python
   row, col = 2, 3
   
   # 리스트 컴프리헨션
   matrix1 = [[0] * col for _ in range(row)]
   
   # 리스트 곱셈 연산
   matrix2 = [[0] * col] * row
   ```

   - 그러면 matrix1과 matrix2는 똑같을까?
   - 프린트 해보면 같아 보이지만, 정답은 X
   - **matrix1**은, 각 행을 가리키는 포인터가 담긴 리스트가 생성된다.
     - ex) [철수, 민수, 영희] → 각 요소는 각각 철수 리스트, 민수 리스트, 영희 리스트를 가리킨다.
     - 그래서 만약 `matrix1[0][0] = 1`을 하면, `[[1, 0, 0], [0, 0, 0]]`이 될 것이다.
   - matrix2은, 포인터 배열이 생성되긴 하지만, 모든 포인터가 같은 리스트를 가리킨다.
     - ex) [영희, 영희, 영희] → 모든 요소는 영희 리스트만 가리킨다.
     - 그래서 만약 `matrix2[0][0] = 1`을 하면, `[[1, 0, 0], [1, 0, 0]]`이 될 것이다.
     - 쓰지 말자!



## (3) 입력 받기

1. **행렬의 크기가 미리 주어지는 경우**

   1. BOJ 1100 하얀 칸

      - https://www.acmicpc.net/problem/1100

      - 체스판은 8 × 8 크기

      - 문제 접근 방법: 인덱스 i + j 가 짝수면 하얀 칸...

      - **리스트 컴프리헨션**을 통해, 입력을 간단히 받을 수 있다.

        ```python
        matrix = [list(input()) for _ in range(8)]
        ```

      - 혹은 반복문

        ```python
        for _ in range(8):
            line = list(input())
            matrix.append(line)
        ```

   2. 3 × 3 크기의 입력을 받아보기

      ```python
      '''
      1 2 3
      4 5 6
      7 8 9
      '''
      matrix = []
      ```

      ```python
      # 1. 반복문
      for _ in range(3):
          # 정수형 데이터는 split()을 해주어 이어주자
          line = list(map(int, input().split()))
          matrix.append(line)
      ```

      ```python
      # 2. 리스트 컴프리헨션
      matrix = [list(map(int, input().split())) for _ in range(3)]
      ```



2. 행렬의 크기가 입력으로 주어지는 경우

   1. BOJ 1245 농장 관리

      - https://www.acmicpc.net/problem/1245

      - 농장은 N × M 격자

      - 리스트 컴프리헨션

        ```python
        N, M = map(int, input().split())
        matrix = [list(map(int, input().split())) for _ in range(N)]
        ```



# 3. 기타

- 3Blue1Brown: https://youtu.be/S9JGmA5_unY