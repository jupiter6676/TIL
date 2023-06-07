import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def pprint(mat):
    for row in mat:
        for elem in row:
            print(elem, end=' ')
        print()

def dfs(y, x):
    global size, res

    visited[y][x] = size

    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]

        if -1 < ny < R and -1 < nx < C:
            if graph[ny][nx] and not visited[ny][nx]:
                size += 1
                dfs(ny, nx)

    res = max(res, size)


'''main'''
R, C, K = map(int, input().split())
graph = [[0] * C for _ in range(R)]
visited = [[0] * C for _ in range(R)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for _ in range(K):
    y, x = map(int, input().split())
    graph[y - 1][x - 1] = 1

res = 0
for i in range(R):
    for j in range(C):
        if graph[i][j] and not visited[i][j]:
            size = 1
            dfs(i, j)

# pprint(visited)
print(res)