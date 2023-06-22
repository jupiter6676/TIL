# 1. 코드 리뷰

## (1) 촌수 계산

- 일단 입력 X

  ```python
  V = 9
  start, end = 7, 3
  E = 7
  
  graph = [[] for _ in range(V + 1)]
  visited = [False] * (V + 1)
  ```

- 그래프 정보 입력

  ```python
  for _ in range(m):
      x, y = map(int, input().split())
      graph[x].append(y)
      graph[y].append(x)
  ```



- 【DFS 코드】

  ```python
  start = 7	# 3에서 시작해도 O
  visited[start] = True
  stack = [start]
  
  while len(stack) != 0:
      pop = stack.pop()
      
      if pop == end:
          break
      
      for adj in graph[pop]:
          if not visited[adj]:
              visited[adj] = True
              stack.append(adj)
  ```



- 촌수 계산

  - 처음 7에서 시작할 때, 스택에 (7, 0)을 넣어.
  - 그 후 2로 갈 때, 스택에 (2, 1)을 넣어야 해.
    - 이 1은 7의 촌수 0에서 +1을 한 것과 같다.

- 【촌수 계산 코드】

  ```python
  start = 7	# 3에서 시작해도 O
  visited[start] = True
  stack.append((start, 0))	# 0은 촌수
  
  answer = -1
  
  while len(stack) != 0:
      num, cnt = stack.pop()
      
      if num == end:
          answer = cnt
          break
      
      for adj in graph[num]:
          if not visited[adj]:
              # (인접 번호, 촌수 +1) 값을 append
              stack.append((adj, cnt + 1)
              visited[adj] = True
                           
  print(answer)
  ```



## (2) 연결 요소의 개수

- 연결 요소 (Connected Component)

  - 그래프가 있을 때, 나뉘어져 있는 그래프(Component)가 몇 개 있는지
  - 덩어리의 개수

- 방문 표시 리스트 `visited`

- 1번부터 시작해서 연결된 요소들을 모두 돌면서 방문 처리

- 그럼 정점들 돌면서, 방문 처리 되지 않은 부분을 새로운 start로

- start한 횟수를 세면 된다.

- 【코드】

  ```python
  answer = 0
  for num in range(1, V + 1):
      if not visited[num]:
          '''
          DFS 로직
          answer는 언제 증가해야 할까?
          '''
  ```



# 2. 코딩 테스트 준비 Ⅰ

## (1) 기본 코딩 테스트

- 기본 코딩 테스트는 주로 **문제의 내용을 코드로 구현 가능한지** 테스트한다.
  - 문제 풀이에 **시간 제한이 없는 경우**가 많기 때문에, 시간 복잡도를 생각하지 않고 풀어보는 것이 좋다.
  - 완전 탐색 중에서도 2차원 배열의 탐색, 델타 탐색 등 선형 탐색이 주를 이룬다.
  - 삼성 SW 역량 테스트 **IM** 시험이 대표적 예시이다.



## (2) 단순 구현 (Implementation)

- 단순 구현은 문제에 제시된 풀이 과정을 그대로 구현하는 유형이다.
  - 시뮬레이션의 경우 **완전 탐색** 유형 중 하나로, 모든 경우의 수를 탐색하여 풀이한다.
  - 아이디어나 알고리즘을 요구하기보다, 문제에 제시된 과정을 그대로 구현할 수 있는지가 핵심이다.
  - 삼성 SW 역량 테스트 **IM**과 **A형**에서도 주로 출제된다.



- 【BOJ 1063번 킹】
  - https://www.acmicpc.net/problem/1063
  - 델타 탐색과 아스키 코드를 사용한다.
  - 단순 구현 유형이므로, 문제에 제시된 동작을 그대로 구현하면 된다.
  - 제한시간 40분 이상



- DFS를 이용해 이차원 격자를 탐색하는 문제가 자주 출제된다.
  - ex) 미로