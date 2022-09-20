import sys
sys.stdin = open('input.txt', 'r')

for _ in range(1, 11):
    t = int(input())

    graph = [list(map(int, input().split())) for _ in range(100)]
    visited = [[False] * 100 for _ in range(100)]

    # 좌, 우, 상(가장 낮은 우선순위로 선택)
    dx = [-1, 1, 0]
    dy = [0, 0, -1]

    # 도착한 곳의 좌표
    y = 99
    x = 0

    # 도착점(2) 찾기
    for j in range(100):
        if graph[y][j] == 2:
            x = j

    while True:
        if y == 0:
            break

        for d in range(3):
            ny = y + dy[d]
            nx = x + dx[d]

            # 범위를 벗어나면 건너뛰기
            if not (0 <= ny < 100 and 0 <= nx < 100):
                continue
            
            # 길이 아니면 건너뛰기
            if graph[ny][nx] != 1:
                continue

            if not visited[ny][nx]:
                visited[ny][nx] = True
                y = ny
                x = nx

    print(f'#{t} {x}')

'''
1
1 0 0 0 1 0 1 0 0 1
1 0 0 0 1 0 1 1 1 1
1 0 0 0 1 0 1 0 0 1
1 0 0 0 1 1 1 0 0 1
1 0 0 0 1 0 1 0 0 1
1 1 1 1 1 0 1 1 1 1
1 0 0 0 1 0 1 0 0 1
1 1 1 1 1 0 1 0 0 1
1 0 0 0 1 1 1 0 0 1
1 0 0 0 1 0 1 0 0 1
'''

# for _ in range(1, 11):
#     t = int(input())

#     graph = [list(map(int, input().split())) for _ in range(10)]
#     visited = [[False] * 10 for _ in range(10)]

#     # 좌, 우, 상(가장 낮은 우선순위로 선택)
#     dx = [-1, 1, 0]
#     dy = [0, 0, -1]

#     y = 9
#     x = 9   # 도착점에서 출발

#     while True:
#         if y == 0:
#             break

#         for d in range(3):
#             ny = y + dy[d]
#             nx = x + dx[d]

#             # 범위를 벗어나면 건너뛰기
#             if not (0 <= ny < 10 and 0 <= nx < 10):
#                 continue
            
#             # 길이 아니면 건너뛰기
#             if graph[ny][nx] != 1:
#                 continue
            
#             if not visited[ny][nx]:
#                 visited[ny][nx] = True
#                 y = ny
#                 x = nx

#     print(f'#{t} {x}')