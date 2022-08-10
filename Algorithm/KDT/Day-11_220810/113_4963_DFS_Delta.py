import sys
input = sys.stdin.readline

# RecursionError를 방지
# 파이썬의 기본 재귀 깊이 제한은 약 1000인데, 
# 이 문제에서는 그보다 깊이 들어갈 수 있다..고 한다.
# https://www.acmicpc.net/board/view/34170
sys.setrecursionlimit(100000)

# 좌상, 상, 우상, 우, 우하, 하, 좌하, 좌
dy = [-1, -1, -1, 0, 1, 1, 1, 0]
dx = [-1, 0, 1, 1, 1, 0, -1, -1]

def dfs(y, x):
    visited[y][x] = True

    for d in range(8):
        ny = y + dy[d]
        nx = x + dx[d]

        if not (-1 < ny < h and -1 < nx < w):
            continue

        if graph[ny][nx] == 1 and not visited[ny][nx]:
            visited[ny][nx] = True

            dfs(ny, nx)


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