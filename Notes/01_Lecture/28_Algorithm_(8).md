# 1. 코드 리뷰

## (1) 그림

- https://www.acmicpc.net/problem/1926

- 연결 요소의 개수와 동일한 문제 → 모든 점에서 DFS를 돌려

- 4방향의 델타 탐색

- 입력

  ```python
  # 행, 열의 수 입력
  n, m = list(map(int, input().split()))
  
  # n개의 1차원 리스트를 가진 2차원 리스트 입력
  graph = [list(map, int(input().split())) for _ in range(n)]
  ```



- DFS 조건

  1. 방문 처리

     ```python
     # 방문 처리를 위한 2차원 리스트
     graph = [[False] * m for _ in range(n)]
     ```

  2. 값이 1이고, 방문하지 않은 모든 점에서 DFS를 호출

     ```python
     for sy in range(n):
         for sx in range(m):
             if not visited[sy][sx] and graph[sy][sx] == 1:
                 '''
                 DFS 알고리즘
                 '''
     ```



- 【코드】

  ```python
  painting_cnt = 0	# while문이 시작하기 전에 +1
  painting_size_list = list()
  
  # 모든 좌표에서 DFS 로직 실행
  # 이차원 리스트를 순회할 이중 반복문
  for i in range(n):
      for j in range(m):
          # [i][j] 값이 1이고, 방문하지 않았다면 → DFS 실행
          if not visited[i][j] and graph[i][j] == 1:
              # DFS
              stack = list()
              
              stack.append([i, j])
              visited[i][j] = True
              
              painting_cnt += 1	# 그림의 개수 +1
              painting_size = 0	# pop을 한 횟수
              
              while stack:
                  # y, x 값 갱신
                  y, x = stack.pop()
                  
                  # 그림의 넓이 +1
                  painting_size += 1
                  
                  # 델타 탐색
                  for d in range(4):
                      ny = y + dy[d]
                      nx = x + dx[d]
                      
                      # 조건 1. 범위
                      if not (-1 < ny < n and -1 < nx < m):
                          continue
                      
                      # 조건2. 방문 확인
                      if visited[ny][nx]:
                          continue
                      
                      # 조건 3. 좌표의 값이 1 (그림이어야 함)
                      if graph[ny][nx] != 1:
                          continue
                          
                      # 조건을 다 확인하면, 스택에 넣고 방문처리
                      stack.append([ny, nx])
                      visited[ny][nx] = True
                      
              painting_size_list.append(painting_size)
  
  if painting_size_list:
      print(painting_cnt)
  	print(max(painting_size_list))
  else:
      print(0)
      print(0)
  ```



# 2. 기타

- https://techblog.woowahan.com/2608/
- https://techblog.woowahan.com/2717/