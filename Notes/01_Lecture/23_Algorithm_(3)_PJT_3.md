# 1. 코드 리뷰

## (1) 박스

- https://www.acmicpc.net/problem/9455

- 어떤 조건에서 박스를 아래로 내릴 수 있을까?

  1. 현재 박스 아래에 박스가 없어야 한다.

     ```python
     박스 = 1
     빈공간 = 0
     
     # 좌표
     y, x = 2, 0
     
     if 박스_리스트[y + 1][x] != 박스:
     ```

  2. 박스는 바닥을 벗어나면 안 된다. (= 리스트의 범위를 벗어나면 안 된다.)

     ```python
     # 리스트의 크기 N * M
     N, M = 5, 4
     
     # 현재 박스는 바닥을 벗어나면 X
     if y + 1 != N:
     ```

- 박스 이동 → 현재 위치는 0 저장, 아래 위치는 1 저장

  ```python
  # 조건은 위의 조건 2개
  while 조건:
  	박스_리스트[y + 1][x] = 박스
  	박스_리스트[y][x] = 빈공간
      
      y += 1
  ```

  ```python
  while 박스_리스트[y + 1][x] != 박스 and y + 1 != N:
  	박스_리스트[y + 1][x] = 박스
  	박스_리스트[y][x] = 빈공간
      
      y += 1
      이동거리 += 1
  ```

- 【코드】

  ```python
  row, col = 5, 4
  
  box_list = [
      [1, 0, 0, 0],
      [0, 0, 1, 0],
      [1, 0, 0, 1],
      [0, 1, 0, 0],
      [1, 0, 1, 0]
  ]
  
  dist = 0	# 이동 거리
  
  # 열부터 순회
  for x in range(col):
      # 행 순회. 아래에서 위로 탐색을 한다.
      # 거꾸로 가지 않으면, 제일 첫 번째 상자가 내려가다가
      # 아래에 아직 움직이지 않은 상자를 만나 탐색이 종료될 수 O.
      for y in range(row - 1, -1, -1):
          # 만약 현재 탐색중인 좌표에 박스가 있으면
          if box_list[y][x] == 1:
              while y + 1 != row and box_list[y + 1][x] != 1:
                  box_list[y][x] = 0
                  box_list[y + 1][x] = 1
                  
                  y += 1
                  dist += 1
  ```



## (2) 델타 이동 & 델타 탐색

> 어떤 좌표를 기준으로, 4방위(상하좌우), 혹은 8방위를 탐색

1. 4방위

   ```python
   dy = [0, 0, 1, -1]
   dx = [1, -1, 0, 0]
   
   y, x = 1, 1
   
   for d in range(4):
       next_y = y + dy[d]
       next_x = x + dx[d]
   ```

2. 8

   ```python
   dy = [-1, -1, -1, 0, 0, 1, 1, 1]
   dx = [-1, 0, 1, -1, 1, -1, 0, 1]
   ```



## (3) 지뢰 찾기

- https://www.acmicpc.net/problem/4396

- 각 x를 기준으로, 8방위에 있는 지뢰의 수를 카운트

  ```python
  dy = [-1, -1, -1, 0, 0, 1, 1, 1]
  dx = [-1, 0, 1, -1, 1, -1, 0, 1]
  
  for d in range(8):
      next_y = y + dy[d]
      next_x = x + dx[d]
      
      if 게임보드[next_y][next_x] == 지뢰:
          지뢰수 += 1
          
  결과보드[y][x] = 지뢰수
  ```

- 지뢰를 발견하면, 결과 보드에 모든 지뢰를 표시

  ```python
  if 게임보드[y][x] == 지뢰:
      지뢰_발견 = True
      
  if 지뢰_발견 == True:
      결과보드에서 모든 지뢰 위치에 * 저장
  ```

- 【코드】

  ```python
  # 8방위 델타 리스트
  dy = [-1, -1, -1, 0, 0, 1, 1, 1]
  dx = [-1, 0, 1, -1, 1, -1, 0, 1]
  
  N = 8
  game_board = [list(input()) for _ in range(N)]
  open_board = [list(input()) for _ in range(N)]
  res_board = [['.' * N] for _ in range(N)]
  
  is_mine = False
  
  for y in range(N):
      for x in range(N):
          # 현재 위치가 오픈한 위치
          if open_board[y][x] == 'x':
              mine_cnt = 0
  
              for d in range(8):
                  next_y = y + dy[d]
                  next_x = x + dx[d]
  
                  # next_y와 next_x가 리스트의 범위를 벗어나면 X
                  if 0 <= next_y < N and 0 <= next_x < N:
                      # 게임 보드를 탐색한 곳에 지뢰가 있으면
                      if game_board[next_y][next_x] == '*':
                          mine_cnt += 1
                          
              # 현재 위치에, 주변에 있는 지뢰의 수 표시
  			res_board[y][x] = str(mine_cnt)
                          
  			# 현재 오픈한 위치에 지뢰가 있는지 확인
              if game_board[y][x] == '*':
                  is_mine = True
  
  # 지뢰를 밟으면, 결과 보드에 모든 지뢰의 위치 표시 
  if is_mine == True:
      for y in range(N):
      	for x in range(N):
              if game_board[y][x] == '*':
                  res_board[y][x] = '*'
                  
  # 결과 보드 출력
  for row in game_board:
      print(''.join(row))
  ```



# 2. 기타

- 심화 알고리즘을 빨리 배우고 싶다!

  - SWEA에 알고리즘 강의 + 문제 셋도 있다.

    https://swexpertacademy.com/main/learn/course/subjectList.do?courseId=AVuPDYSqAAbw5UW6

  - 프로그래머스 코테 연습 문제도 싹 풀어보자.

    https://school.programmers.co.kr/learn/challenges?tab=algorithm_practice_kit