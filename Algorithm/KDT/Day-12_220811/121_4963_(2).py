# 121_4963_(1).py는 22.08.10

import sys
input = sys.stdin.readline


# 좌상, 상, 우상, 우, 우하, 하, 좌하, 좌
dy = [-1, -1, -1, 0, 1, 1, 1, 0]
dx = [-1, 0, 1, 1, 1, 0, -1, -1]

stack = list()

def dfs(y, x):
    stack.append((y, x))
    visited[y][x] = True

    while stack:
        pop = stack.pop()

        for d in range(8):
            ny = pop[0] + dy[d]
            nx = pop[1] + dx[d]

            if not (-1 < ny < h and -1 < nx < w):
                continue

            if graph[ny][nx] == 1 and not visited[ny][nx]:
                stack.append((ny, nx))
                visited[ny][nx] = True


while True:
    w, h = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range (h)]
    
    if w == 0 and h == 0:
        break

    visited = [[False] * w for _ in range(h)]
    island_cnt = 0

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                island_cnt += 1
                dfs(i, j)

    print(island_cnt)