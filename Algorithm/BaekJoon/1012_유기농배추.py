import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(y, x):
    visited[y][x] = 1

    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]

        if -1 < ny < N and -1 < nx < M:
            if graph[ny][nx] and not visited[ny][nx]:
                dfs(ny, nx)


'''main'''
for _ in range(int(input())):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    cabbage = list()
    for _ in range(K):
        tx, ty = map(int, input().split())
        graph[ty][tx] = 1
        cabbage.append([ty, tx])

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    cnt = 0
    for coord in cabbage:
        ty, tx = coord

        if graph[ty][tx] and not visited[ty][tx]:
            dfs(ty, tx)
            cnt += 1

    print(cnt)