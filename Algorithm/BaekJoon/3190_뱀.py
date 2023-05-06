import sys
from collections import deque
input = sys.stdin.readline

def pprint(mat):
    print('==================')
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            print(mat[i][j], end=' ')
        print()


'''main'''
N = int(input())
graph = [[0] * (N + 1) for _ in range(N + 1)]
graph[1][1] = 2

for _ in range(int(input())):
    y, x = map(int, input().split())
    graph[y][x] = 1

moves = deque()
for _ in range(int(input())):
    num, _dir = input().split()
    moves.append([int(num), _dir])

RIGHT = 1; DOWN = 2; LEFT = 3; UP = 4

q = deque([[1, 1]])
curr_dir = RIGHT

sec = 0
while q:
    sec += 1

    y, x = q[len(q) - 1]    # 머리의 좌표
    ny = y
    nx = x

    if curr_dir == LEFT:
        nx = x - 1
    elif curr_dir == RIGHT:
        nx = x + 1
    elif curr_dir == UP:
        ny = y - 1
    else:
        ny = y + 1

    # 벽이나 몸에 닿으면 종료
    if not (0 < ny < N + 1 and 0 < nx < N + 1) or graph[ny][nx] == 2:
        break
    
    # 방향 전환
    if moves and sec == moves[0][0]:
        if moves[0][1] == 'D':  # 우회전
            curr_dir = (curr_dir + 1) % 4

        else:   # 좌회전
            curr_dir = (curr_dir - 1) % 4
        
        if curr_dir == 0:
            curr_dir = 4

        moves.popleft()

    # 사과를 먹은 경우
    if graph[ny][nx] == 1:
        graph[ny][nx] = 2
        q.append([ny, nx])  # 길이 늘리기 (머리를 앞으로)

    # 사과를 먹지 않은 경우
    if graph[ny][nx] == 0:
        graph[ny][nx] = 2

        ty, tx = q.popleft()
        graph[ty][tx] = 0   # 꼬리 자르기
        
        q.append([ny, nx])  # 머리를 앞으로

    # pprint(graph)
    # print(curr_dir)
    # print('q:', q)
    # print('moves:', moves)

print(sec)