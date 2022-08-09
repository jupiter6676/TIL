R, C = map(int, input().split())
lst = [list(input()) for _ in range(R)]

# 최대 차를 4대까지 부수고 주차할 수 있는 공간 저장
space = [0] * 5

# 아래, 오른쪽, 오른쪽 대각선 아래
dy = [1, 0, 1]
dx = [0, 1, 1]

# 부서진 차의 수
broken_cars = 0

for y in range(R):
    for x in range(C):
        if lst[y][x] == '.':
            tmp = 1
            broken_cars = 0

            for d in range(3):
                ny = y + dy[d]
                nx = x + dx[d]

                if not(0 <= ny < R and 0 <= nx < C):
                    break
                
                # 빌딩 마주치면 주차 X
                if lst[ny][nx] == '#':
                    break
                
                if lst[ny][nx] == 'X':
                    tmp += 1
                    broken_cars += 1
                
                if lst[ny][nx] == '.':
                    tmp += 1

                if tmp == 4:
                    space[broken_cars] += 1

        if lst[y][x] == 'X':
            tmp = 1
            broken_cars = 1

            for d in range(3):
                ny = y + dy[d]
                nx = x + dx[d]

                if not(0 <= ny < R and 0 <= nx < C):
                    break
                
                # 빌딩 마주치면 주차 X
                if lst[ny][nx] == '#':
                    break
                
                if lst[ny][nx] == 'X':
                    tmp += 1
                    broken_cars += 1

                if lst[ny][nx] == '.':
                    tmp += 1

                if tmp == 4:
                    space[broken_cars] += 1

for s in space:
    print(s)